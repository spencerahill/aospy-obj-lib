"""Mass budget-related quantities."""
from aospy.constants import grav
from aospy.utils import dp_from_ps, int_dp_g, integrate


from .. import PFULL_STR, TIME_STR
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


def mass_column(ps):
    """Total mass per square meter of atmospheric column."""
    return ps / grav.value


def mass_column_integral(bk, pk, ps):
    """
    Total mass per square meter of atmospheric column.

    Explicitly computed by integrating over pressure, rather than implicitly
    using surface pressure.  Useful for checking if model data conserves mass.

    :param dp: Pressure thickness of the model levels.
    """
    dp = dp_from_ps(bk, pk, ps)
    return dp.sum(dim=PFULL_STR)


def mass_column_source(evap, precip):
    """Source term of column mass budget."""
    return grav.value * (evap - precip)


def mass_column_divg(u, v, radius, dp):
    """Horizontal divergence of vertically integrated flow."""
    u_int = integrate(u, dp, PFULL_STR)
    v_int = integrate(v, dp, PFULL_STR)
    return horiz_divg(u_int, v_int, radius)


def mass_column_divg_with_adj(u, v, q, ps, radius, dp):
    """Divergence of vertically integrated, mass-adjusted horizontal wind."""
    return mass_column_divg(uv_mass_adjusted(u, q, ps, dp),
                            uv_mass_adjusted(v, q, ps, dp), radius, dp)


def mass_column_budget_lhs(ps, u, v, radius, dp, freq='1M'):
    """Tendency plus flux terms in the column-integrated mass budget.

    Theoretically the sum of the tendency and transport terms exactly equals
    the source term, however artifacts introduced by numerics and other things
    yield a residual.
    """
    tendency = time_tendency(ps)
    transport = mass_column_divg(u, v, radius, dp)
    return budget_residual(tendency, transport, freq=freq)


def mass_column_budget_with_adj_lhs(ps, u, v, q, radius, dp, freq='1M'):
    """Tendency plus flux terms in the column-integrated mass budget.

    Theoretically the sum of the tendency and transport terms exactly equals
    the source term, however artifacts introduced by numerics and other things
    yield a residual.
    """
    tendency = time_tendency(ps, freq=freq)
    transport = mass_column_divg_with_adj(u, v, q, ps, radius, dp)
    return budget_residual(tendency, transport, freq=freq)


def mass_column_budget_residual(ps, u, v, evap, precip, radius, dp, freq='1M'):
    """Residual in the mass budget.

    Theoretically the sum of the tendency and transport terms exactly equals
    the source term, however artifacts introduced by numerics and other things
    yield a residual.
    """
    tendency = time_tendency(ps, freq=freq)
    transport = mass_column_divg(u, v, radius, dp)
    source = mass_column_source(evap, precip)
    return budget_residual(tendency, transport, source, freq=freq)


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


def column_dry_air_mass(ps, wvp):
    """Total mass of dry air in an atmospheric column (from Trenberth 1991)"""
    return ps / grav - wvp


def dry_mass_column_tendency(ps, q, dp, freq='1M'):
    """Combined time-tendency term in column mass budget equation.

    See e.g. Trenberth 1991, Eq. 9.
    """
    return (time_tendency(ps, freq=freq) -
            grav.value * time_tendency(int_dp_g(q, dp), freq=freq))


def dry_mass_column_divg(u, v, q, radius, dp):
    """Transport term of atmospheric column mass budget.

    E.g. Trenberth 1991, Eq. 9
    """
    u_int = integrate((1. - q)*u, dp, PFULL_STR)
    v_int = integrate((1. - q)*v, dp, PFULL_STR)
    return horiz_divg(u_int, v_int, radius)


def budget_residual(tendency, transport, source=None, freq='1M'):
    """Compute residual between tendency and transport terms.

    Resamples transport and source terms to specified frequency, since often
    tendencies are computed at monthly intervals while the transport is much
    higher frequencies (e.g. 3- or 6-hourly).
    """
    resid = tendency + transport.resample(freq, TIME_STR,
                                          how='mean').dropna(TIME_STR)
    if source is not None:
        resid -= source.resample(freq, TIME_STR, how='mean').dropna(TIME_STR)
    return resid


def dry_mass_column_budget_residual(ps, u, v, q, radius, dp, freq='1M'):
    """Residual in the dry mass budget.

    Theoretically the sum of the tendency and transport terms is exactly zero,
    however artifacts introduced by numerics and other things yield a
    residual.
    """
    tendency = dry_mass_column_tendency(ps, q, dp, freq=freq)
    transport = dry_mass_column_divg(u, v, q, radius, dp)
    return budget_residual(tendency, transport, freq=freq)


def dry_mass_column_divg_with_adj(u, v, q, ps, radius, dp):
    """Transport term of atmospheric column mass budget with adjustment.

    Based on Trenberth 1991 J. Climate, but in the limit that the mass
    transport term is much larger magnitude than the tendency term.
    """
    u_int = integrate((1 - q)*uv_mass_adjusted(u, q, ps, dp), dp, PFULL_STR)
    v_int = integrate((1 - q)*uv_mass_adjusted(v, q, ps, dp), dp, PFULL_STR)
    return horiz_divg(u_int, v_int, radius)


def dry_mass_column_budget_with_adj_residual(ps, u, v, q, radius, dp,
                                             freq='1M'):
    """Residual in column mass budget when flow is adjusted for balance."""
    tendency = dry_mass_column_tendency(ps, q, dp, freq=freq)
    transport = dry_mass_column_divg_with_adj(u, v, q, ps, radius, dp)
    return budget_residual(tendency, transport, freq=freq)
