"""Mass budget-related quantities."""
from aospy.constants import grav
from aospy.utils import dp_from_ps, int_dp_g, integrate


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


def dp(ps, bk, pk, arr):
    """Pressure thickness of hybrid coordinate levels from surface pressure."""
    return dp_from_ps(bk, pk, ps, arr[PFULL_STR])


def column_mass_divg(u, v, radius, dp):
    """Horizontal divergence of vertically integrated flow."""
    u_int = integrate(u, dp, PFULL_STR)
    v_int = integrate(v, dp, PFULL_STR)
    return horiz_divg(u_int, v_int, radius)


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


def column_mass_divg_with_adj(u, v, q, ps, radius, dp):
    """Divergence of vertically integrated, mass-adjusted horizontal wind."""
    return column_mass_divg(uv_mass_adjusted(u, q, ps, dp),
                            uv_mass_adjusted(v, q, ps, dp), radius, dp)


def column_flux_divg(arr, u, v, radius, dp):
    """Column flux divergence, with the field defined per unit mass of air."""
    return horiz_divg(int_dp_g(arr*u, dp), int_dp_g(arr*v, dp), radius)


def column_flux_divg_with_adj(arr, u, v, q, ps, radius, dp):
    """Column flux divergence, with the field defined per unit mass of air."""
    u_adj = uv_mass_adjusted(u, q, ps, dp)
    v_adj = uv_mass_adjusted(v, q, ps, dp)
    return horiz_divg(int_dp_g(arr*u_adj, dp), int_dp_g(arr*v_adj, dp), radius)


def horiz_divg_mass_adj(u, v, q, ps, radius, dp):
    return horiz_divg(uv_mass_adjusted(u, q, ps, dp),
                      uv_mass_adjusted(v, q, ps, dp), radius)


def horiz_advec_mass_adj(arr, u, v, q, ps, radius, dp, p, vec_field=False):
    u_cor = uv_mass_adjusted(u, q, ps, dp, p)
    v_cor = uv_mass_adjusted(v, q, ps, dp, p)
    return horiz_advec(arr, u_cor, v_cor, radius, vec_field=vec_field)


def column_mass(ps):
    """Total mass per square meter of atmospheric column."""
    return ps / grav.value


def column_mass_integral(bk, pk, ps):
    """
    Total mass per square meter of atmospheric column.

    Explicitly computed by integrating over pressure, rather than implicitly
    using surface pressure.  Useful for checking if model data conserves mass.

    :param dp: Pressure thickness of the model levels.
    """
    dp = dp_from_ps(bk, pk, ps)
    return dp.sum(dim=PFULL_STR)


def column_dry_air_mass(ps, wvp):
    """Total mass of dry air in an atmospheric column (from Trenberth 1991)"""
    return ps / grav - wvp


def dry_mass_budget_tendency_term(ps, q, dp, freq='1M'):
    """Combined time-tendency term in column mass budget equation.

    See e.g. Trenberth 1991, Eq. 9.
    """
    return (time_tendency(ps, freq=freq) -
            grav.value * time_tendency(int_dp_g(q, dp), freq=freq))


def dry_mass_budget_transport_term(u, v, q, radius, dp):
    """Transport term of atmospheric column mass budget.

    E.g. Trenberth 1991, Eq. 9
    """
    u_int = integrate((1. - q)*u, dp, PFULL_STR)
    v_int = integrate((1. - q)*v, dp, PFULL_STR)
    return horiz_divg(u_int, v_int, radius)


def dry_mass_budget_residual(ps, u, v, q, radius, dp):
    """Residual in the mass budget.

    Theoretically the sum of the tendency and transport terms is exactly zero,
    however artifacts introduced by numerics and other things yield a
    residual.
    """
    return (dry_mass_budget_tendency_term(ps, q, dp) +
            dry_mass_budget_transport_term(u, v, q, radius, dp))


def dry_mass_budget_with_adj_transport_term(u, v, q, ps, radius, dp):
    """Transport term of atmospheric column mass budget with adjustment.

    Based on Trenberth 1991 J. Climate, but in the limit that the mass
    transport term is much larger magnitude than the tendency term.
    """
    u_int = integrate((1 - q)*uv_mass_adjusted(u, q, ps, dp), dp, PFULL_STR)
    v_int = integrate((1 - q)*uv_mass_adjusted(v, q, ps, dp), dp, PFULL_STR)
    return horiz_divg(u_int, v_int, radius)


def dry_mass_budget_with_adj_residual(ps, u, v, q, radius, dp):
    """Residual in column mass budget when flow is adjusted for balance."""
    return (dry_mass_budget_tendency_term(ps, q, dp) +
            dry_mass_budget_with_adj_transport_term(u, v, q, ps, radius, dp))


def column_mass_source(evap, precip):
    """Source term of column mass budget."""
    return grav.value * (evap - precip)
