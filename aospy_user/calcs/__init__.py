"""My library of functions for use in aospy.

Historically, these assumed input variables in the form of numpy arrays or
masked numpy arrays.  As of October 2015, I have switched to assuming
xray.DataArrays, to coincide with the same switch within aospy.  However, not
all of the functions in this module have been converted to support this new
datatype.
"""
from aospy.constants import c_p, grav, R_d
from aospy.utils import level_thickness, int_dp_g
import numpy as np


from .tendencies import (
    first_to_last_vals_dur,
    time_tendency
)
from .numerics import (
    fwd_diff1,
    fwd_diff2,
    cen_diff2,
    cen_diff4,
    upwind_scheme,
    latlon_deriv_prefactor,
    wraparound_lon,
    d_dx_from_latlon,
    d_dy_from_lat,
    d_dx_at_const_p_from_eta,
    d_dy_at_const_p_from_eta,
    d_dx_of_vert_int,
    d_dy_of_vert_int,
    d_dp_from_p,
    d_dp_from_eta
)

from .advection import (
    zonal_advec,
    merid_advec,
    vert_advec,
    horiz_advec,
    total_advec,
    zonal_advec_upwind,
    merid_advec_upwind,
    vert_advec_upwind,
    horiz_advec_upwind,
    total_advec_upwind,
    zonal_advec_const_p_from_eta,
    merid_advec_const_p_from_eta,
    horiz_advec_const_p_from_eta,
    vert_advec_from_eta,
    total_advec_from_eta,
    horiz_advec_sfc_pressure
)
from .mass import (
    horiz_divg,
    vert_divg,
    divg_3d,
    divg_of_vert_int_horiz_flow,
    column_flux_divg,
    divg_of_vert_int_mass_adj_horiz_flow,
    column_mass,
    column_mass_integral,
    column_dry_air_mass,
    uv_mass_adjustment,
    uv_mass_adjusted,
    horiz_divg_mass_adj,
    horiz_advec_mass_adj,
    mass_budget_tendency_term,
    mass_budget_transport_term,
    mass_budget_residual,
    mass_budget_with_adj_transport_term,
    mass_budget_with_adj_residual
)
from .transport import (
    field_horiz_flux_divg,
    field_vert_flux_divg,
    field_times_horiz_divg,
    field_horiz_advec_divg_sum,
    field_total_advec,
    field_vert_int_bal,
    field_times_horiz_divg_mass_adj,
    field_horiz_flux_divg_mass_adj,
)
from .thermo import (
    dse,
    mse,
    fmse,
    pot_temp,
    virt_pot_temp,
    equiv_pot_temp,
    mixing_ratio_from_specific_mass,
    specific_mass_dry_air,
    specific_gas_constant_moist_air,
    heat_capacity_moist_air_constant_volume,
    specific_entropy_dry_air,
    specific_entropy_water_vapor
)
from .toa_sfc_fluxes import (
    albedo,
    sfc_albedo,
    cre_sw,
    cre_lw,
    cre_net,
    toa_rad,
    toa_rad_clr,
    toa_sw,
    sfc_rad,
    sfc_rad_cld,
    sfc_lw,
    sfc_lw_cld,
    sfc_sw,
    sfc_sw_cld,
    sfc_energy,
    column_energy,
    bowen_ratio,
    evap_frac
)
from .energy import (
    mse_horiz_flux_divg,
    mse_horiz_advec,
    mse_times_horiz_divg,
    mse_horiz_advec_divg_sum,
    mse_vert_flux_divg,
    mse_vert_advec,
    mse_total_advec,
    mse_horiz_advec_upwind,
    mse_vert_advec_upwind,
    mse_total_advec_upwind,
    mse_budget_advec_residual,
    fmse_budget_advec_residual,
    dse_horiz_flux_divg,
    dse_horiz_advec,
    dse_times_horiz_divg,
    dse_horiz_advec_divg_sum,
    dse_vert_advec,
    tdt_diab,
    tdt_lw_cld,
    tdt_sw_cld
    )
from .stats import (
    pointwise_corr,
    pointwise_lin_regr,
    corr_cre_sw,
    corr_cre_lw,
    corr_cre_net,
    corr_toa_rad_clr,
    lin_regr_cre_net,
    lin_regr_toa_rad_clr
    )
from .water import (
    moisture_budget_lhs,
    moisture_budget_with_adj_lhs,
    p_minus_e,
    prec_conv_frac,
    q_budget_advec_residual,
    q_budget_horiz_flux_divg_residual,
    qu,
    qv,
)
from .gms import (
    field_vert_int_max,
    horiz_divg_vert_int_max,
    vert_divg_vert_int_max,
    gms_like_ratio,
    gross_moist_strat,
    gross_dry_stab,
    gross_moist_stab,
    gms_up_low,
    gms_each_level,
    dry_static_stab,
    moist_static_stab
)
from .zonal_mean_circ import (
    msf,
    msf_max,
    aht,
    aht_no_snow,
    oht,
    tht,
    gms_change_est,
    gms_change_est2,
    gms_h01,
    gms_h01est,
    gms_h01est2,
    gms_moc,
    gms_msf,
    total_gms,
    ang_mom,
    hadley_bounds,
    had_bounds,
    had_bounds500,
    thermal_equator,
    itcz_pos,
    itcz_loc,
    prec_centroid,
    precip_centroid
)


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
