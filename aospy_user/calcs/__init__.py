"""My library of functions for use in aospy.

Historically, these assumed input variables in the form of numpy arrays or
masked numpy arrays.  However, as of October 2015, I have switched to assuming
xray.DataArrays, to coincide with the same switch within aospy.  However, not
all of the functions in this module have been converted to support this new
datatype.
"""
from __future__ import division

from aospy.constants import c_p, grav, L_f, L_v, r_e, R_d
from aospy.numerics import FiniteDiff
from aospy.utils import (level_thickness, to_pascal, to_radians, int_dp_g,
                         integrate, d_deta_from_pfull, d_deta_from_phalf,
                         pfull_from_ps, to_pfull_from_phalf)
import numpy as np
import scipy.stats
import xray

from .. import (
    LAT_STR, LON_STR, PFULL_STR, PLEVEL_STR
)
from .tendencies import (
    mass_budget_tendency_term, time_tendency, wvp_time_tendency
)
from .numerics import (
    fwd_diff1, fwd_diff2, cen_diff2, cen_diff4, upwind_scheme
)
from .thermo import (
    dse, mse, fmse, pot_temp, virt_pot_temp, equiv_pot_temp,
    mixing_ratio_from_specific_mass, specific_mass_dry_air,
    specific_gas_constant_moist_air, heat_capacity_moist_air_constant_volume,
    specific_entropy_dry_air, specific_entropy_water_vapor
)
from .toa_sfc_fluxes import (
    albedo, sfc_albedo, cre_sw, cre_lw, cre_net, toa_rad, toa_rad_clr, toa_sw,
    sfc_rad, sfc_rad_cld, sfc_lw, sfc_lw_cld, sfc_sw, sfc_sw_cld, sfc_energy,
    column_energy, bowen_ratio, evap_frac
)
from .stats import (
    pointwise_corr, pointwise_lin_regr, corr_cre_sw, corr_cre_lw, corr_cre_net,
    corr_toa_rad_clr, lin_regr_cre_net, lin_regr_toa_rad_clr
    )
from .zonal_mean_circ import (
    msf, msf_max, aht, aht_no_snow, oht, tht, gms_change_est, gms_change_est2,
    gms_h01, gms_h01est, gms_h01est2, gms_moc, gms_msf, total_gms, ang_mom,
    hadley_bounds, had_bounds, had_bounds500, thermal_equator, itcz_pos,
    itcz_loc, prec_centroid, precip_centroid
)


# Functions for derivatives in x, y, and p.
def latlon_deriv_prefactor(lat, radius, d_dy_of_scalar_field=False):
    """Factor that multiplies del operations in spherical coordinates."""
    if d_dy_of_scalar_field:
        return 1. / radius
    else:
        return 1. / (radius*np.cos(to_radians(lat)))


def wraparound_lon(arr, num=1):
    """Append wrap-around points in longitude to the DataArray or Dataset.

    The longitude arraymust span from 0 to 360.  While this will usually be the
    case, it's not guaranteed.  Some pre-processing step should be implemented
    in the future that forces this to be the case.
    """
    edge_left = arr.isel(**{LON_STR: 0})
    edge_left[LON_STR] += 360.
    edge_right = arr.isel(**{LON_STR: -1})
    edge_right[LON_STR] -= 360.
    return xray.concat([edge_right, arr, edge_left], dim=LON_STR)


def d_dx_from_latlon(arr, radius):
    """Compute \partial arr/\partial x using centered differencing."""
    prefactor = latlon_deriv_prefactor(to_radians(arr.coords[LAT_STR]),
                                       radius, d_dy_of_scalar_field=False)
    arr_ext = wraparound_lon(arr)
    darr_dx = FiniteDiff.cen_diff_deriv(arr_ext, LON_STR,
                                        do_edges_one_sided=False)
    return prefactor*darr_dx


def d_dy_from_lat(arr, radius, vec_field=False):
    """Compute \partial(field)/\partial y using centered differencing."""
    lat = to_radians(arr.coords[LAT_STR])
    prefactor = latlon_deriv_prefactor(lat, radius,
                                       d_dy_of_scalar_field=(not vec_field))
    if vec_field:
        arr *= np.cos(lat)
    darr_dy = FiniteDiff.cen_diff_deriv(arr, LAT_STR, do_edges_one_sided=True)
    return prefactor*darr_dy


def d_dp_from_p(arr, p):
    """Derivative in pressure of array defined on fixed pressure levels."""
    return FiniteDiff.cen_diff_deriv(arr, PLEVEL_STR, do_edges_one_sided=True)


def d_dp_from_eta(arr, ps, bk, pk):
    """Derivative in pressure of array defined on hybrid sigma-p coords.

    The array is assumed to be on full (as opposed to half) levels.
    """
    pfull = pfull_from_ps(bk, pk, ps, arr[PFULL_STR])
    return (FiniteDiff.cen_diff(arr, PFULL_STR, do_edges_one_sided=True) /
            FiniteDiff.cen_diff(pfull, PFULL_STR, do_edges_one_sided=True))


def zonal_advec_upwind(arr, u, radius):
    """Advection in the zonal direction using upwind differencing."""
    prefactor = latlon_deriv_prefactor(to_radians(arr.coords[LAT_STR]),
                                       radius, d_dy_of_scalar_field=False)
    arr_ext = wraparound_lon(arr)
    df_fwd = FiniteDiff.fwd_diff1(arr_ext)
    df_bwd = FiniteDiff.bwd_diff1(arr_ext)
    # Transpose again to regain original axis order.
    return prefactor*upwind_scheme(df_fwd, df_bwd, u)


def merid_advec_upwind(arr, v, radius, vec_field=False):
    """Advection in the meridional direction using upwind differencing."""
    lat = to_radians(arr[LAT_STR])
    prefactor = 1. / radius
    # Del operator differs in spherical coords for scalar v. vector fields.
    if vec_field:
        arr *= np.cos(lat)
        prefactor /= np.cos(lat)
        prefactor = prefactor.T
    # Create arrays holding positive and negative values, each with forward
    # differencing at south pole and backward differencing at north pole.
    # df_fwd_except_np = fwd_diff2(f, lat)
    # df_bwd_except_sp = fwd_diff2(f[::-1], lat[::-1])[::-1]
    # df_fwd_adj_np = fwd_diff1(f[-2:], lat[-2:])
    # df_bwd_adj_sp = fwd_diff1(f[1::-1], lat[1::-1])[::-1]
    # df_fwd = np.ma.concatenate((df_fwd_except_np, df_fwd_adj_np,
                                # df_bwd_except_sp[-1:]), axis=0)
    # df_bwd = np.ma.concatenate((df_fwd_except_np[:1], df_bwd_adj_sp,
                                # df_bwd_except_sp), axis=0)
    df_fwd_except_np = fwd_diff1(f, lat)
    df_bwd_except_sp = fwd_diff1(f[::-1], lat[::-1])[::-1]
    df_fwd = np.ma.concatenate((df_fwd_except_np,
                                df_bwd_except_sp[-1:]), axis=0)
    df_bwd = np.ma.concatenate((df_fwd_except_np[:1],
                                df_bwd_except_sp), axis=0)
    # Roll axis and transpose again to regain original axis order.
    df_fwd = np.rollaxis(df_fwd, 0, 2).T
    df_bwd = np.rollaxis(df_bwd, 0, 2).T
    return prefactor*upwind_scheme(df_fwd, df_bwd, v)


def horiz_advec_upwind(arr, u, v, radius, vec_field=False):
    return (zonal_advec_upwind(arr, u, radius) +
            merid_advec_upwind(arr, v, radius, vec_field=vec_field))


def vert_advec_upwind(arr, omega, p):
    """Advection in pressure using upwind differencing."""
    # Assume pressure is 3rd to last axis: ([time,] p, lat, lon)
    f = arr.T
    p = to_pascal(p)
    # Create arrays holding positive and negative values, each with forward
    # differencing at south pole and backward differencing at north pole.
    df_fwd_partial = fwd_diff1(f, p)
    df_bwd_partial = fwd_diff1(f[::-1], p[::-1])[::-1]
    df_fwd = np.ma.concatenate((df_fwd_partial, df_bwd_partial[-1:]), axis=0)
    df_bwd = np.ma.concatenate((df_fwd_partial[:1], df_bwd_partial), axis=0)
    # 2015-10-26 S. Hill: does omega having the opposite sign convention as
    # normal mean that the forward v. backward differencing should be switched?
    return upwind_scheme(df_fwd, df_bwd, omega)


def total_advec_upwind(arr, u, v, omega, p, radius,
                       vec_field=False):
    return (horiz_advec_upwind(arr, u, v, radius, vec_field) +
            vert_advec_upwind(arr, omega, p))


def d_dx_at_const_p_from_eta(arr, ps, radius, bk, pk):
    """d/dx at constant pressure of `arr`.

    `arr` must be defined on full levels in hybrid sigma-pressure coordinates.
    """
    pfull_coord = arr[PFULL_STR]
    d_dx_const_eta = d_dx_from_latlon(arr, radius)
    darr_deta = d_deta_from_pfull(arr)
    bk_at_pfull = to_pfull_from_phalf(bk, pfull_coord)
    da_deta = d_deta_from_phalf(pk, pfull_coord)
    db_deta = d_deta_from_phalf(bk, pfull_coord)
    d_dx_ps = d_dx_from_latlon(ps, radius)

    return d_dx_const_eta + (darr_deta * bk_at_pfull * d_dx_ps /
                             (da_deta + db_deta*ps))


def d_dy_at_const_p_from_eta(arr, ps, radius, bk, pk, vec_field=False):
    """d/dy at constant pressure of `arr`.

    `arr` must be defined on full levels in hybrid sigma-pressure coordinates.
    """
    pfull_coord = arr[PFULL_STR]
    d_dy_const_eta = d_dy_from_lat(arr, radius, vec_field=vec_field)
    darr_deta = d_deta_from_pfull(arr)
    bk_at_pfull = to_pfull_from_phalf(bk, pfull_coord)
    da_deta = d_deta_from_phalf(pk, pfull_coord)
    db_deta = d_deta_from_phalf(bk, pfull_coord)
    d_dy_ps = d_dy_from_lat(ps, radius, vec_field=False)

    return d_dy_const_eta + (darr_deta*bk_at_pfull * d_dy_ps /
                             (da_deta + db_deta*ps))


# Advection and divergence functions.
def zonal_advec(arr, u, radius):
    """Zonal advection of the given field."""
    return u*d_dx_from_latlon(arr, radius)


def merid_advec(arr, v, radius, vec_field=False):
    """Meridional advection of the given field."""
    return v*d_dy_from_lat(arr, radius, vec_field=vec_field)


def horiz_advec(arr, u, v, radius, vec_field=False):
    """Horizontal advection of the given field."""
    return (zonal_advec(arr, u, radius) +
            merid_advec(arr, v, radius, vec_field=vec_field))


def vert_advec(arr, omega, p):
    """Vertical advection of the given field."""
    return omega*d_dp_from_p(arr, p)


def total_advec(arr, u, v, omega, p, radius, vec_field=False):
    """Total advection of the given field."""
    return (horiz_advec(arr, u, v, radius, vec_field=vec_field) +
            vert_advec(arr, omega, p))


def zonal_advec_const_p_from_eta(arr, u, ps, radius, bk, pk):
    """Zonal advection at constant pressure of the given scalar field."""
    return u*d_dx_at_const_p_from_eta(arr, ps, radius, bk, pk)


def merid_advec_const_p_from_eta(arr, v, ps, radius, bk, pk, vec_field=False):
    """Meridional advection at constant pressure of the given scalar field."""
    return v*d_dy_at_const_p_from_eta(arr, ps, radius, bk, pk,
                                      vec_field=vec_field)


def horiz_advec_const_p_from_eta(arr, u, v, ps, radius, bk, pk,
                                 vec_field=False):
    """Horizontal advection at constant pressure of the given scalar field."""
    return (zonal_advec_const_p_from_eta(arr, u, ps, radius, bk, pk) +
            merid_advec_const_p_from_eta(arr, v, ps, radius, bk, pk,
                                         vec_field=vec_field))


def vert_advec_from_eta(arr, omega, ps, bk, pk):
    """Vertical advection of the given field."""
    return omega*d_dp_from_eta(arr, ps, bk, pk)


def total_advec_from_eta(arr, u, v, omega, p, ps, radius, bk, pk,
                         vec_field=False):
    """Total advection of the given scalar field."""
    return (horiz_advec_const_p_from_eta(arr, u, v, ps, radius, bk, pk,
                                         vec_field=vec_field) +
            vert_advec(arr, omega, p))


def horiz_divg(u, v, radius):
    """Flow horizontal divergence."""
    du_dx = d_dx_from_latlon(u, radius)
    dv_dy = d_dy_from_lat(v, radius, vec_field=True)
    return du_dx + dv_dy


# def divg_spharm(u, v, **kwargs):
    # s = SpharmInterface(u, v, **kwargs)
    # return s.revert_to_raw(s.divergence())


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


def column_dry_air_mass_tendency(q, u, v, radius, dp):
    """Time tendency of column dry air mass.  Trenberth 1991, Eq. (3)"""
    dry_air = 1 - q
    dry_air_flux_divg = field_horiz_flux_divg(dry_air, u, v, radius)
    return -1*int_dp_g(dry_air_flux_divg, dp)


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


def field_times_horiz_divg_mass_adj(arr, u, v, q, ps, radius, dp, p):
    return arr*horiz_divg_mass_adj(u, v, q, ps, radius, dp, p)


def horiz_advec_mass_adj(arr, u, v, q, ps, radius, dp, p, vec_field=False):
    u_cor = uv_mass_adjusted(u, q, ps, dp, p)
    v_cor = uv_mass_adjusted(v, q, ps, dp, p)
    return horiz_advec(arr, u_cor, v_cor, radius, vec_field=vec_field)


def field_horiz_flux_divg_mass_adj(arr, u, v, q, ps, radius, dp, p,
                                   vec_field=False):
    return (field_times_horiz_divg_mass_adj(arr, u, v, q, ps, radius, dp, p) +
            horiz_advec_mass_adj(arr, u, v, q, ps, radius, dp, p,
                                 vec_field=vec_field))


def d_dx_of_vert_int(arr, radius, dp):
    return d_dx_from_latlon(int_dp_g(arr, dp), radius)


def d_dy_of_vert_int(arr, radius, dp):
    return d_dy_from_lat(int_dp_g(arr, dp), radius, vec_field=True)


def divg_of_vert_int_horiz_flow(u, v, radius, dp):
    """Horizontal divergence of vertically integrated flow."""
    u_int = integrate(u, dp, PFULL_STR)
    v_int = integrate(v, dp, PFULL_STR)
    return horiz_divg(u_int, v_int, radius)


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


def divg_of_vert_int_mass_adj_horiz_flow(u, v, q, ps, radius, dp):
    """Divergence of vertically integrated, mass-adjusted horizontal wind."""
    return divg_of_vert_int_horiz_flow(uv_mass_adjusted(u, q, ps, dp),
                                       uv_mass_adjusted(v, q, ps, dp),
                                       radius, dp)


def mass_budget_with_adj_transport_term(u, v, q, ps, radius, dp):
    """Transport term of atmospheric column mass budget with adjustment."""
    u_int = integrate((1 - q)*uv_mass_adjusted(u, q, ps, dp), dp, PFULL_STR)
    v_int = integrate((1 - q)*uv_mass_adjusted(v, q, ps, dp), dp, PFULL_STR)
    return horiz_divg(u_int, v_int, radius)


def mass_budget_with_adj_residual(ps, u, v, q, radius, dp):
    """Residual in column mass budget when flow is adjusted for balance."""
    return (mass_budget_tendency_term(ps, q, dp) +
            mass_budget_with_adj_transport_term(u, v, q, ps, radius, dp))


def horiz_advec_sfc_pressure(ps, u, v, radius):
    """Horizontal advection of surface pressure."""
    # Pressure data indexing is surface to TOA; sigma data is opposite.
    u_sfc = u.isel(**{PFULL_STR: -1})
    v_sfc = v.isel(**{PFULL_STR: -1})
    return horiz_advec(ps, u_sfc, v_sfc, radius) * (1./grav)


def vert_divg(omega, p):
    """Flow vertical divergence."""
    return d_dp_from_p(omega, p)


def field_vert_int_bal(arr, dp):
    """Impose vertical balance to the field, i.e. column integral = 0.

    Most frequently used for mass flux divergence to impose mass balance.
    """
    pos = np.ma.where(arr > 0, arr, 0)
    neg = np.ma.where(arr < 0, arr, 0)
    pos_int = int_dp_g(pos, dp)[:,np.newaxis,:,:]
    neg_int = int_dp_g(neg, dp)[:,np.newaxis,:,:]
    return pos - (pos_int/neg_int)*neg


def horiz_divg_mass_bal(u, v, radius, dp):
    """Horizontal divergence with column mass-balance correction applied."""
    div = horiz_divg(u, v, radius)
    return field_vert_int_bal(div, dp)


def vert_divg_mass_bal(omega, p, dp):
    """Vertical divergence with column mass-balance correction applied."""
    div = vert_divg(omega, p)
    return field_vert_int_bal(div, dp)


def divg_3d(u, v, omega, radius, p):
    """Total (3-D) divergence.  Should nearly equal 0 by continuity."""
    return horiz_divg(u, v, radius) + vert_divg(omega, p)


def field_times_horiz_divg(arr, u, v, radius):
    """Scalar field times horizontal divergence."""
    return arr*horiz_divg(u, v, radius)


def field_times_horiz_divg_mass_bal(arr, u, v, radius, dp):
    """Scalar field times horizontal divergence."""
    return arr*horiz_divg_mass_bal(u, v, radius, dp)


def field_times_vert_divg_mass_bal(arr, omega, p, dp):
    """Scalar field times vertical divergence."""
    return arr*vert_divg_mass_bal(omega, p, dp)


def field_horiz_flux_divg(arr, u, v, radius):
    """Horizontal flux divergence of given scalar field."""
    dfu_dx = d_dx_from_latlon(u*arr, radius)
    dfv_dy = d_dy_from_lat(v*arr, radius, vec_field=True)
    return dfu_dx + dfv_dy


def field_vert_flux_divg(arr, omega, p):
    """Vertical flux divergence of a scalar field."""
    return d_dp_from_p(omega*arr, p)


def field_horiz_advec_divg_sum(arr, u, v, radius, dp):
    return (field_times_horiz_divg(arr, u, v, radius) +
            horiz_advec(arr, u, v, radius))


def field_total_advec(arr, u, v, omega, p, radius):
    return (horiz_advec(arr, u, v, radius) + vert_advec(arr, omega, p))


# Advection, divergence etc. applied to specific fields.
def mse_horiz_flux_divg(temp, hght, sphum, u, v, radius):
    """Horizontal flux convergence of moist static energy."""
    return field_horiz_flux_divg(mse(temp, hght, sphum), u, v, radius)


def mse_horiz_advec(temp, hght, sphum, u, v, radius):
    """Horizontal advection of moist static energy."""
    return horiz_advec(mse(temp, hght, sphum), u, v, radius)


def mse_times_horiz_divg(temp, hght, sphum, u, v, radius, dp):
    """Horizontal divergence of moist static energy."""
    return field_times_horiz_divg_mass_bal(mse(temp, hght, sphum),
                                           u, v, radius, dp)


def mse_horiz_advec_divg_sum(T, gz, q, u, v, rad, dp):
    return field_horiz_advec_divg_sum(mse(T, gz, q), u, v, rad, dp)


def mse_vert_flux_divg(T, gz, q, omega, p):
    """Vertical divergence times moist static energy."""
    return field_vert_flux_divg(mse(T, gz, q), omega, p)


def mse_vert_advec(temp, hght, sphum, omega, p):
    """Vertical advection of moist static energy."""
    return vert_advec(mse(temp, hght, sphum), omega, p)


def mse_times_vert_divg(T, gz, q, omega, p, dp):
    """Vertical divergence times moist static energy."""
    return field_times_vert_divg_mass_bal(mse(T, gz, q), omega, p, dp)


def mse_total_advec(temp, hght, sphum, u, v, omega, p, radius):
    mse_ = mse(temp, hght, sphum)
    return field_total_advec(mse_, u, v, omega, p, radius)



def mse_horiz_advec_upwind(temp, hght, sphum, u, v, radius, vec_field=False):
    return horiz_advec_upwind(mse(temp, hght, sphum), u, v, radius,
                              vec_field=vec_field)


def mse_vert_advec_upwind(temp, hght, sphum, omega, p):
    return vert_advec_upwind(mse(temp, hght, sphum), omega, p)


def mse_total_advec_upwind(temp, hght, sphum, u, v, omega, p, radius,
                           vec_field=False):
    return total_advec_upwind(mse(temp, hght, sphum), u, v, omega, p, radius,
                              vec_field=vec_field)


def mse_budget_advec_residual(temp, hght, sphum, ucomp, vcomp, omega,
                              p, dp, radius, swdn_toa, swup_toa, olr, swup_sfc,
                              swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap):
    """Residual in vertically integrated MSE budget."""
    mse_ = mse(temp, hght, sphum)
    transport = field_total_advec(mse_, ucomp, vcomp, omega, p, radius)
    trans_vert_int = int_dp_g(transport, dp)[:,np.newaxis,:,:]
    f_net = column_energy(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
                          lwup_sfc, lwdn_sfc, shflx, evap)
    return f_net - trans_vert_int


def fmse_budget_advec_residual(temp, hght, sphum, ice_wat, ucomp, vcomp, omega,
                               p, dp, radius, swdn_toa, swup_toa, olr,
                               swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx,
                               evap):
    """Residual in vertically integrated MSE budget."""
    fmse_ = fmse(temp, hght, sphum, ice_wat)
    transport = field_total_advec(fmse_, ucomp, vcomp, omega, p, radius)
    trans_vert_int = int_dp_g(transport, dp)[:,np.newaxis,:,:]
    f_net = column_energy(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
                          lwup_sfc, lwdn_sfc, shflx, evap)
    return f_net - trans_vert_int

def q_budget_advec_residual(sphum, ucomp, vcomp, omega, p, dp, radius, evap,
                            precip):
    """Residual in vertically integrated MSE budget."""
    transport = field_total_advec(sphum, ucomp, vcomp, omega, p, radius)
    trans_vert_int = int_dp_g(transport, dp)[:,np.newaxis,:,:]
    e_minus_p = evap - precip
    return e_minus_p - trans_vert_int

def q_budget_horiz_flux_divg_residual(sphum, ucomp, vcomp, dp, radius, evap,
                                      precip):
    """Residual in vertically integrated MSE budget."""
    transport = field_horiz_flux_divg(sphum, ucomp, vcomp, radius)
    trans_vert_int = int_dp_g(transport, dp)[:,np.newaxis,:,:]
    e_minus_p = evap - precip
    return e_minus_p - trans_vert_int


def dse_horiz_flux_divg(temp, hght, u, v, radius):
    """Horizontal flux convergence of moist static energy."""
    return field_horiz_flux_divg(dse(temp, hght), u, v, radius)


def dse_horiz_advec(temp, hght, u, v, radius):
    """Horizontal advection of moist static energy."""
    return horiz_advec(dse(temp, hght), u, v, radius)


def dse_times_horiz_divg(temp, hght, u, v, radius, dp):
    """Horizontal divergence of moist static energy."""
    return field_times_horiz_divg_mass_bal(dse(temp, hght), u, v, radius, dp)


def dse_horiz_advec_divg_sum(T, gz, u, v, rad, dp):
    return field_horiz_advec_divg_sum(dse(T, gz), u, v, rad, dp)


def dse_vert_advec(temp, hght, omega, p):
    """Vertical advection of moist static energy."""
    return vert_advec(dse(temp, hght), omega, p)


def qu(sphum, u):
    """"Zonal moisture flux."""
    return sphum*u


def qv(sphum, v):
    """Meridional moisture flux."""
    return sphum*v


# Gross moist stability-related quantities
def field_vert_int_max(arr, dp):
    """Maximum magnitude of integral of a field from surface up."""
    dp = to_pascal(dp)
    # 2015-05-15: Problem: Sigma data indexing starts at TOA, while pressure
    #             data indexing starts at 1000 hPa.  So for now only do for
    #             sigma data and flip array direction to start from sfc.
    arr_dp_g = (arr*dp)[::-1] / grav
    # Input array dimensions are assumed ([time dims,] level, lat, lon).
    pos_max = np.amax(np.cumsum(arr_dp_g, axis=0), axis=-3)
    neg_max = np.amin(np.cumsum(arr_dp_g, axis=0), axis=-3)
    # Flip sign because integrating from p_sfc up, i.e. with dp negative.
    return -1*np.where(pos_max > -neg_max, pos_max, neg_max)


def horiz_divg_vert_int_max(u, v, radius, dp):
    """Maximum magnitude of integral upwards of horizontal divergence."""
    return field_vert_int_max(horiz_divg_mass_bal(u, v, radius, dp), dp)


def vert_divg_vert_int_max(omega, p, dp):
    """Maximum magnitude of integral from surface up of vertical divergence."""
    return field_vert_int_max(vert_divg_mass_bal(omega, p, dp), dp)


def gms_like_ratio(weights, tracer, dp):
    """Compute ratio of integrals in the style of gross moist stability."""
    # Integrate weights over lower tropospheric layer
    dp = to_pascal(dp)
    denominator = field_vert_int_max(weights, dp)
    # Integrate tracer*weights over whole column and divide.
    numerator = np.sum(weights*tracer*dp, axis=-3) / grav
    return numerator / denominator


def gross_moist_strat(sphum, u, v, radius, dp):
    """Gross moisture stratification, in horizontal divergence form."""
    divg = horiz_divg(u, v, radius)
    return L_v*gms_like_ratio(divg, sphum, dp)


def gross_dry_stab(temp, hght, u, v, radius, dp):
    """Gross dry stability, in horizontal divergence form."""
    divg = horiz_divg(u, v, radius)
    return -gms_like_ratio(divg, dse(temp, hght), dp)


def gross_moist_stab(temp, hght, sphum, u, v, radius, dp):
    """Gross moist stability, in horizontal divergence form."""
    divg = horiz_divg(u, v, radius)
    return -gms_like_ratio(divg, mse(temp, hght, sphum), dp)


def tdt_diab(tdt_lw, tdt_sw, tdt_conv, tdt_ls):
    """Net diabatic heating rate."""
    return tdt_lw + tdt_sw + tdt_conv + tdt_ls


def tdt_lw_cld(tdt_lw, tdt_lw_clr):
    """Cloudy-sky temperature tendency from longwave radiation."""
    return tdt_lw - tdt_lw_clr


def tdt_sw_cld(tdt_sw, tdt_sw_clr):
    """Cloudy-sky temperature tendency from shortwave radiation."""
    return tdt_sw - tdt_sw_clr


def p_minus_e(precip, evap):
    """Precipitation minus evaporation."""
    return precip - evap


def gms_up_low(temp, hght, sphum, level, lev_up=400., lev_dn=925.):
    """Gross moist stability. Upper minus lower level MSE."""
    m = mse(temp, hght, sphum)
    return (np.squeeze(m[np.where(level == lev_up)] -
                       m[np.where(level == lev_dn)])/c_p)


def gms_each_level(temp, hght, sphum, level, lev_dn=925.):
    m = mse(temp, hght, sphum)
    return (m - m[np.where(level == lev_dn)])/c_p


def dry_static_stab(temp, hght, level, lev_dn=925.):
    d = dse(temp, hght)
    return (d - d[np.where(level == lev_dn)])/c_p


def moist_static_stab(temp, hght, sphum, p):
    mse_ = mse(temp, hght, sphum)
    return d_dp_from_p(mse_, p)


def prec_conv_frac(prec_conv, precip, prec_ls=False):
    """Fraction of precipitation coming from convection scheme."""
    # Mask where precip is zero to avoid dividing by zero.
    prec_conv = np.ma.masked_where(precip == 0., prec_conv)
    precip = np.ma.masked_where(precip == 0., precip)
    if prec_ls:
        return prec_conv/(precip + prec_conv)
    else:
        return prec_conv/precip


def descent_tot(omega, mc):
    """Vertical motion from both convection and large-scale."""
    return omega + grav*mc


def ascent_ls(omega):
    """Large-scale vertically upward motion."""
    # Get positive values and replace negative ones with zero.
    return np.where(omega > 0., omega, 0)


def vert_centroid(arr, level, p_bot=850., p_top=150.):
    """
    Compute the vertical centroid of some vertically defined field.
    """
    desired_levs = np.where((level <= p_bot) & (level >= p_top))
    lev_thick = level_thickness(level)/100.
    # Add axes for later broadcasting and truncate to desired vertical levels.
    level = level[desired_levs]; level = level[:,np.newaxis,np.newaxis]
    lev_thick = lev_thick[desired_levs]
    lev_thick = lev_thick[:,np.newaxis,np.newaxis]
    arr = arr[desired_levs]
    # For 1D arrays, have to move the vertical coordinate to leftmost dim.
    if arr.ndim == 1:
        arr = np.atleast_3d(arr).swapaxes(0,1)
    else:
        arr = np.atleast_3d(arr)
    return (np.sum(arr*level*lev_thick, axis=0) /
            np.sum(arr*lev_thick, axis=0))


def trop_height(level, T):
    """
    Tropopause height of each column, based on Reichler et al 2003 GRL.
    """
    # Get pressure and temperature data.
    p = level[:,np.newaxis,np.newaxis]
    # Compute half levels of pressure^kappa
    kap = R_d / c_p
    pkap_half = 0.5*(p[1:]**kap + p[:-1]**kap)
    # Compute lapse rate at half-levels, assuming T linear in pressure^kappa.
    Gamma = ((T[1:] - T[:-1])*(p[:-1]**kap + p[1:]**kap) /
            ((T[1:] + T[:-1])*(p[:-1]**kap - p[1:]**kap)))*kap*grav/R_d
    # Find levels of continuous Gamma where dT/dz > -2 K/km.
    Gamma_crit = -2e-3
    Gamma_good = np.where(Gamma > Gamma_crit, Gamma, 0)
    # Check that avg dT/dz in 2 km above > -2 K/km.
    Gam_slope = (Gamma[1:] - Gamma[:-1]) / (pkap_half[1:] - pkap_half[:-1])
    # Take lowest level satisfying these criteria.
    tp = 8
    # Linearly interpolate to pressure level of critical Gamma value.
    pkap_tp = (pkap_half[tp-1] + ((pkap_half[tp] - pkap_half[tp-1]) *
               (Gamma_crit - Gamma[tp-1])/(Gamma[tp] - Gamma[tp-1])))
    # Convert from pressure^kappa to pressure.
    return pkap_tp**(1./kap)
