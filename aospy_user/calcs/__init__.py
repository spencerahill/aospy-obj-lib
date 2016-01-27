"""My library of functions for use in aospy.

Historically, these assumed input variables in the form of numpy arrays or
masked numpy arrays.  As of October 2015, I have switched to assuming
xray.DataArrays, to coincide with the same switch within aospy.  However, not
all of the functions in this module have been converted to support this new
datatype.
"""
from .tendencies import (
    first_to_last_vals_dur,
    time_tendency_first_to_last,
    time_tendency_each_timestep,
)
from .numerics import (
    fwd_diff2,
    latlon_deriv_prefactor,
    wraparound,
    d_dx_from_latlon,
    d_dy_from_lat,
    d_dx_at_const_p_from_eta,
    d_dy_at_const_p_from_eta,
    d_dp_from_p,
    d_dp_from_eta
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
    specific_entropy_water_vapor,
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
    column_lw,
    column_sw,
    bowen_ratio,
    evap_frac,
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
    horiz_advec_spharm,
)
from .mass import (
    horiz_divg,
    horiz_divg_spharm,
    vert_divg,
    divg_3d,
    dp,
    uv_mass_adjustment,
    uv_mass_adjusted,
    u_mass_adjustment,
    u_mass_adjusted,
    v_mass_adjustment,
    v_mass_adjusted,
    column_flux_divg,
    column_flux_divg_adj,
    mass_column,
    mass_column_divg,
    mass_column_divg_spharm,
    mass_column_divg_adj,
    mass_column_integral,
    mass_column_source,
    mass_column_budget_lhs,
    mass_column_budget_with_adj_lhs,
    mass_column_budget_residual,
    mass_column_budget_adj_residual,
    horiz_divg_mass_adj,
    horiz_divg_mass_adj_spharm,
    horiz_divg_mass_adj_from_eta,
    ps_horiz_advec,
    uv_dry_mass_adjusted,
    dry_mass_column_tendency,
    dry_mass_column_divg,
    dry_mass_column_divg_adj,
    dry_mass_column_budget_residual,
    dry_mass_column_budget_adj_residual,
    uv_mass_adjustment,
    uv_mass_adjusted,
    horiz_divg_mass_adj,
    horiz_advec_mass_adj,
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
    omega_from_divg_eta,
)
from .energy import (
    kinetic_energy,
    energy,
    energy_column,
    energy_column_tendency,
    energy_column_tendency_each_timestep,
    energy_column_source,
    energy_column_divg,
    energy_column_budget_residual,
    uv_energy_adjustment,
    uv_energy_adjusted,
    uv_mass_energy_adjustment,
    uv_mass_energy_adjusted,
    u_energy_adjustment,
    u_energy_adjusted,
    u_mass_energy_adjustment,
    u_mass_energy_adjusted,
    v_energy_adjustment,
    v_energy_adjusted,
    v_mass_energy_adjustment,
    v_mass_energy_adjusted,
    energy_column_divg_adj,
    energy_column_divg_adj_time_mean,
    energy_column_divg_adj_eddy,
    energy_column_budget_adj_residual,
    energy_column_budget_energy_adj_residual,
    energy_column_budget_mass_adj_residual,
    energy_column_budget_dry_mass_adj_residual,
    energy_column_divg_mass_adj,
    energy_sfc_ps_advec,
    energy_sfc_ps_advec_as_resid,
    energy_horiz_advec_from_eta,
    energy_horiz_advec_from_eta_upwind,
    energy_horiz_advec_from_eta_time_mean,
    energy_horiz_advec,
    energy_horiz_divg_from_eta,
    energy_column_vert_advec_as_resid_from_eta_time_mean,
    energy_column_vert_advec_as_resid,
    energy_vert_advec,
    energy_vert_advec_from_eta,
    energy_vert_advec_from_eta_upwind,
    energy_vert_advec_eta_omega_adj,
    energy_vert_advec_eta_omega_adj_time_mean,
    energy_vert_advec_adj_from_eta,
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
    tdt_sw_cld,
    tdt_moist_diabatic,
    mse_tendency
    )
from .stats import (
    pointwise_corr,
    pointwise_lin_regr,
    corr_cre_sw,
    corr_cre_lw,
    corr_cre_net,
    corr_toa_rad_clr,
    lin_regr_cre_net,
    lin_regr_toa_rad_clr,
    vert_centroid,
    )
from .water import (
    p_minus_e,
    prec_conv_frac,
    moisture_column_source,
    moisture_column_tendency,
    moisture_column_divg_with_adj2,
    moisture_column_budget_lhs,
    moisture_column_budget_with_adj_lhs,
    moisture_column_budget_with_adj2_lhs,
    moisture_column_budget_residual,
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
    moist_static_stab,
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
    precip_centroid,
    trop_height,
)
