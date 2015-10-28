"""Mass budget-related quantities."""
from aospy.constants import grav
from aospy.utils import int_dp_g, integrate

from .. import PFULL_STR
from .numerics import d_dx_from_latlon, d_dy_from_lat, d_dp_from_p
from .advection import horiz_advec
from .tendencies import time_tendency


def horiz_divg(u, v, radius):
    """Mass horizontal divergence."""
    du_dx = d_dx_from_latlon(u, radius)
    dv_dy = d_dy_from_lat(v, radius, vec_field=True)
    return du_dx + dv_dy


def vert_divg(omega, p):
    """Mass vertical divergence."""
    return d_dp_from_p(omega, p)


def divg_3d(u, v, omega, radius, p):
    """Total (3-D) divergence.  Should nearly equal 0 by continuity."""
    return horiz_divg(u, v, radius) + vert_divg(omega, p)


def divg_of_vert_int_horiz_flow(u, v, radius, dp):
    """Horizontal divergence of vertically integrated flow."""
    u_int = integrate(u, dp, PFULL_STR)
    v_int = integrate(v, dp, PFULL_STR)
    return horiz_divg(u_int, v_int, radius)


def column_flux_divg(arr, u, v, radius, dp):
    """Column flux divergence of the field."""
    u_int = int_dp_g(arr*u, dp)
    v_int = int_dp_g(arr*v, dp)
    return horiz_divg(u_int, v_int, radius)


def divg_of_vert_int_mass_adj_horiz_flow(u, v, q, ps, radius, dp):
    """Divergence of vertically integrated, mass-adjusted horizontal wind."""
    return divg_of_vert_int_horiz_flow(uv_mass_adjusted(u, q, ps, dp),
                                       uv_mass_adjusted(v, q, ps, dp),
                                       radius, dp)


# Mass balance & energy budget quantities
def column_mass(ps):
    """Total mass per square meter of atmospheric column."""
    return ps / grav.value


def column_mass_integral(arr, dp):
    """
    Total mass per square meter of atmospheric column.

    Explicitly computed by integrating over pressure, rather than implicitly
    using surface pressure.  Useful for checking if model data conserves mass.

    :param dp: Pressure thickness of the model levels.
    """
    # 2015-10-27 S. Hill: This is almost definitely incorrect.
    mass = arr.copy()
    mass.values = int_dp_g(mass, dp)
    return mass


def column_dry_air_mass(ps, wvp):
    """Total mass of dry air in an atmospheric column (from Trenberth 1991)"""
    return ps / grav - wvp


def uv_mass_adjustment(uv, q, ps, dp):
    """Correction to subtract from outputted u or v to balance mass budget.

    C.f. Trenberth 1991, J. Climate, equations 9 and 10.
    """
    wvp = int_dp_g(q, dp)
    numer = integrate((1. - q)*uv, dp, PFULL_STR)
    denom = (ps - grav.value * wvp)
    return numer / denom


def uv_mass_adjusted(uv, q, ps, dp):
    """Corrected u or v in order to balance mass budget."""
    return uv - uv_mass_adjustment(uv, q, ps, dp)


def horiz_divg_mass_adj(u, v, q, ps, radius, dp):
    return horiz_divg(uv_mass_adjusted(u, q, ps, dp),
                      uv_mass_adjusted(v, q, ps, dp), radius)


def horiz_advec_mass_adj(arr, u, v, q, ps, radius, dp, p, vec_field=False):
    u_cor = uv_mass_adjusted(u, q, ps, dp, p)
    v_cor = uv_mass_adjusted(v, q, ps, dp, p)
    return horiz_advec(arr, u_cor, v_cor, radius, vec_field=vec_field)


# def horiz_divg_mass_bal(u, v, radius, dp):
#     """Horizontal divergence with column mass-balance correction applied."""
#     div = horiz_divg(u, v, radius)
#     return field_vert_int_bal(div, dp)


# def vert_divg_mass_bal(omega, p, dp):
#     """Vertical divergence with column mass-balance correction applied."""
#     div = vert_divg(omega, p)
#     return field_vert_int_bal(div, dp)


def mass_budget_tendency_term(ps, q, dp, freq='1M'):
    """Combined time-tendency term in column mass budget equation.

    See e.g. Trenberth 1991, Eq. 9.
    """
    return (time_tendency(ps, freq=freq) -
            grav.value * time_tendency(int_dp_g(q, dp), dp, freq=freq))


def mass_budget_transport_term(u, v, q, radius, dp):
    """Transport term of atmospheric column mass budget.

    E.g. Trenberth 1991, Eq. 9
    """
    u_int = integrate((1 - q)*u, dp, PFULL_STR)
    v_int = integrate((1 - q)*v, dp, PFULL_STR)
    return horiz_divg(u_int, v_int, radius)


def mass_budget_residual(ps, u, v, q, radius, dp):
    """Residual in the mass budget.

    Theoretically the sum of the tendency and transport terms is exactly zero,
    however artifacts introduced by numerics and other things yield a
    residual.
    """
    return (mass_budget_tendency_term(ps, q, dp) +
            mass_budget_transport_term(u, v, q, radius, dp))


def mass_budget_with_adj_transport_term(u, v, q, ps, radius, dp):
    """Transport term of atmospheric column mass budget with adjustment.

    Based on Trenberth 1991 J. Climate, but in the limit that the mass
    transport term is much larger magnitude than the tendency term.
    """
    u_int = integrate((1 - q)*uv_mass_adjusted(u, q, ps, dp), dp, PFULL_STR)
    v_int = integrate((1 - q)*uv_mass_adjusted(v, q, ps, dp), dp, PFULL_STR)
    return horiz_divg(u_int, v_int, radius)


def mass_budget_with_adj_residual(ps, u, v, q, radius, dp):
    """Residual in column mass budget when flow is adjusted for balance."""
    return (mass_budget_tendency_term(ps, q, dp) +
            mass_budget_with_adj_transport_term(u, v, q, ps, radius, dp))
