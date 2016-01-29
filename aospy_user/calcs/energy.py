"""Energy budget-related fields"""
from aospy.constants import grav, c_p, L_v
from aospy.utils import (d_deta_from_pfull, d_deta_from_phalf,
                         to_pfull_from_phalf, int_dp_g, vert_coord_name,
                         monthly_mean_ts, monthly_mean_at_each_ind,
                         pfull_from_ps)

from .. import PFULL_STR
from .numerics import d_dp_from_eta, d_dp_from_p
from .tendencies import (time_tendency_first_to_last,
                         time_tendency_each_timestep)
from .advection import (horiz_advec, vert_advec, horiz_advec_upwind,
                        vert_advec_upwind, total_advec_upwind,
                        horiz_advec_const_p_from_eta, horiz_advec_spharm)
from .mass import (column_flux_divg, budget_residual, uv_mass_adjusted,
                   uv_dry_mass_adjusted, uv_column_budget_adjustment,
                   horiz_divg_spharm, horiz_divg_from_eta)
from .transport import (field_horiz_flux_divg, field_vert_flux_divg,
                        field_total_advec, field_horiz_advec_divg_sum,
                        field_times_horiz_divg, omega_from_divg_eta)
from .thermo import dse, mse, fmse
from .toa_sfc_fluxes import column_energy


def kinetic_energy(u, v):
    """Kinetic energy per unit mass, neglecting vertical motion."""
    return 0.5*(u*u + v*v)


def energy(temp, z, q, q_ice, u, v):
    return fmse(temp, z, q, q_ice) + kinetic_energy(u, v)


def energy_column(temp, z, q, q_ice, u, v, dp):
    return int_dp_g(energy(temp, z, q, q_ice, u, v), dp)


def energy_column_tendency(temp, z, q, q_ice, u, v, dp):
    return time_tendency_first_to_last(energy_column(temp, z, q, q_ice,
                                                     u, v, dp))


def energy_column_tendency_each_timestep(temp, z, q, q_ice, u, v, dp):
    return time_tendency_each_timestep(energy_column(temp, z, q, q_ice, u, v,
                                                     dp))


energy_column_source = column_energy


def energy_column_divg(temp, z, q, q_ice, u, v, dp, radius):
    return column_flux_divg(energy(temp, z, q, q_ice, u, v), u, v, radius, dp)


def energy_column_budget_lhs(temp, z, q, q_ice, u, v, ps, dp, radius):
    tendency = energy_column_tendency(temp, z, q, q_ice, u, v, dp)
    transport = energy_column_divg(temp, z, q, q_ice, u, v, dp, radius)
    return budget_residual(tendency, transport)


def energy_column_budget_residual(temp, z, q, q_ice, u, v, swdn_toa, swup_toa,
                                  olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc,
                                  shflx, evap, dp, radius):
    en = energy(temp, z, q, q_ice, u, v)
    tendency = time_tendency_each_timestep(int_dp_g(en, dp))
    transport = column_flux_divg(en, u, v, radius, dp)
    source = energy_column_source(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
                                  lwup_sfc, lwdn_sfc, shflx, evap)
    return tendency + transport - source


def uv_energy_adjustment(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                         swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
                         dp, radius):
    """Adjustment to subtract off of u, v to impose column energy balance."""
    residual = energy_column_budget_residual(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc,
        swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp, radius
    )
    col_energy = energy_column(temp, z, q, q_ice, u, v, dp)
    return uv_column_budget_adjustment(u, v, residual, col_energy, radius)


def u_energy_adjustment(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                        swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
                        dp, radius):
    """Adjustment applied to zonal wind to close column energy budget."""
    u_adj, _ = uv_energy_adjustment(temp, z, q, q_ice, u, v, swdn_toa,
                                    swup_toa, olr, swup_sfc, swdn_sfc,
                                    lwup_sfc, lwdn_sfc, shflx, evap, dp,
                                    radius)
    return u_adj


def v_energy_adjustment(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                        swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
                        dp, radius):
    """Adjustment applied to meridional wind to close column energy budget."""
    _, v_adj = uv_energy_adjustment(temp, z, q, q_ice, u, v, swdn_toa,
                                    swup_toa, olr, swup_sfc, swdn_sfc,
                                    lwup_sfc, lwdn_sfc, shflx, evap, dp,
                                    radius)
    return v_adj


def uv_energy_adjusted(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                       swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp,
                       radius):
    """Horizontal wind components with column energy balance-adjustment."""
    u_adj, v_adj = uv_energy_adjustment(temp, z, q, q_ice, u, v, swdn_toa,
                                        swup_toa, olr, swup_sfc, swdn_sfc,
                                        lwup_sfc, lwdn_sfc, shflx, evap, dp,
                                        radius)
    return u - u_adj, v - v_adj


def u_energy_adjusted(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                      swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp,
                      radius):
    """Zonal wind with column energy balance-adjustment applied."""
    u_adj, _ = uv_energy_adjusted(temp, z, q, q_ice, u, v, swdn_toa, swup_toa,
                                  olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc,
                                  shflx, evap, dp, radius)
    return u_adj


def v_energy_adjusted(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                      swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp,
                      radius):
    """Meridional wind with column energy balance-adjustment applied."""
    _, v_adj = uv_energy_adjusted(temp, z, q, q_ice, u, v, swdn_toa, swup_toa,
                                  olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc,
                                  shflx, evap, dp, radius)
    return v_adj


def uv_mass_energy_adjustment(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                              swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx,
                              evap, precip, ps, dp, radius):
    """Horiz wind adjustments to impose column mass and energy balance."""
    u_mass_adj, v_mass_adj = uv_mass_adjusted(ps, u, v, evap, precip, radius,
                                              dp)
    u_en_adj, v_en_adj = uv_energy_adjustment(
        temp, z, q, q_ice, u_mass_adj, v_mass_adj, swdn_toa, swup_toa, olr,
        swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp, radius
    )
    return u_en_adj, v_en_adj


def u_mass_energy_adjustment(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                             swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx,
                             evap, precip, ps, dp, radius):
    """Zonal wind adjustment to impose column mass and energy balance."""
    u_adj, _ = uv_mass_energy_adjustment(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius,
    )
    return u_adj


def v_mass_energy_adjustment(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                             swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx,
                             evap, precip, ps, dp, radius):
    """Meridional wind adjustment to impose column mass and energy balance."""
    _, v_adj = uv_mass_energy_adjustment(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius,
        )
    return v_adj


def uv_mass_energy_adjusted(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                            swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx,
                            evap, precip, ps, dp, radius):
    """Horizontal wind components with column energy balance-adjustment."""
    u_mass_adj, v_mass_adj = uv_mass_adjusted(ps, u, v, evap, precip, radius,
                                              dp)
    u_en_adj, v_en_adj = uv_energy_adjusted(
        temp, z, q, q_ice, u_mass_adj, v_mass_adj, swdn_toa, swup_toa, olr,
        swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp, radius
    )
    return u_en_adj, v_en_adj


def u_mass_energy_adjusted(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                           swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
                           precip, ps, dp, radius):
    """Zonal wind with column energy balance-adjustment applied."""
    u_adj, _ = uv_mass_energy_adjusted(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius
    )
    return u_adj


def v_mass_energy_adjusted(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                           swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
                           precip, ps, dp, radius):
    """Meridional wind with column energy balance-adjustment applied."""
    _, v_adj = uv_mass_energy_adjusted(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius
    )
    return v_adj


def energy_column_divg_adj(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                           swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
                           precip, ps, dp, radius):
    """Column energy divergence with mass and energy adjustments."""
    u_mass_adj, v_mass_adj = uv_mass_adjusted(ps, u, v, evap, precip, radius,
                                              dp)
    u_en_adj, v_en_adj = uv_energy_adjusted(
        temp, z, q, q_ice, u_mass_adj, v_mass_adj, swdn_toa, swup_toa, olr,
        swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp, radius
    )
    return energy_column_divg(temp, z, q, q_ice, u_en_adj,
                              v_en_adj, dp, radius)


def energy_column_divg_adj_time_mean(temp, z, q, q_ice, u, v, swdn_toa,
                                     swup_toa, olr, swup_sfc, swdn_sfc,
                                     lwup_sfc, lwdn_sfc, shflx, evap, precip,
                                     ps, dp, radius):
    """Column energy divergence with energy adjustments by time mean flow."""
    u_mass_adj, v_mass_adj = uv_mass_adjusted(ps, u, v, evap, precip, radius,
                                              dp)
    u_en_adj, v_en_adj = uv_energy_adjusted(
        temp, z, q, q_ice, u_mass_adj, v_mass_adj, swdn_toa, swup_toa, olr,
        swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp, radius
    )
    monthly_terms = [monthly_mean_ts(d) for d in (temp, z, q, q_ice, u_en_adj,
                                                  v_en_adj, dp, radius)]
    return energy_column_divg(*monthly_terms)


def energy_column_divg_adj_eddy(temp, z, q, q_ice, u, v, swdn_toa, swup_toa,
                                olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc,
                                shflx, evap, precip, ps, dp, radius):
    """Column energy divergence with energy adjustments by transient eddies."""
    full = energy_column_divg_adj(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius
    )
    time_mean = energy_column_divg_adj_time_mean(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius
    )
    return full - monthly_mean_at_each_ind(time_mean, full)


def energy_column_divg_dry_mass_adj(temp, z, q, q_ice, u, v, ps, dp, radius):
    """Column energy divergence with adjustment for dry mass."""
    u_adj, v_adj = uv_dry_mass_adjusted(ps, u, v, q, radius, dp)
    return energy_column_divg(temp, z, q, q_ice, u_adj, v_adj, dp, radius)


def energy_column_divg_mass_adj(temp, z, q, q_ice, u, v, evap, precip, ps, dp,
                                radius):
    """Column energy divergence with adjustment for mass but not energy."""
    u_adj, v_adj = uv_mass_adjusted(ps, u, v, evap, precip, radius, dp)
    return energy_column_divg(temp, z, q, q_ice, u_adj, v_adj, dp, radius)


def energy_column_divg_energy_adj(temp, z, q, q_ice, u, v, swdn_toa,
                                  swup_toa, olr, swup_sfc, swdn_sfc,
                                  lwup_sfc, lwdn_sfc, shflx, evap,
                                  ps, dp, radius):
    """Column energy divergence with adjustment for energy but not mass."""
    u_adj, v_adj = uv_energy_adjusted(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
        swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp, radius
    )
    return energy_column_divg(temp, z, q, q_ice, u_adj, v_adj, dp, radius)


def energy_column_budget_adj_residual(temp, z, q, q_ice, u, v, swdn_toa,
                                      swup_toa, olr, swup_sfc, swdn_sfc,
                                      lwup_sfc, lwdn_sfc, shflx, evap, precip,
                                      ps, dp, radius):
    """Column energy budget residual when mass and energy adjustments used."""
    en = energy(temp, z, q, q_ice, u, v)
    tendency = time_tendency_each_timestep(int_dp_g(en, dp))
    transport = energy_column_divg_adj(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius,
    )
    source = energy_column_source(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
                                  lwup_sfc, lwdn_sfc, shflx, evap)

    return tendency + transport - source


def energy_column_budget_dry_mass_adj_residual(temp, z, q, q_ice, u, v,
                                               swdn_toa, swup_toa, olr,
                                               swup_sfc, swdn_sfc, lwup_sfc,
                                               lwdn_sfc, shflx, evap, ps, dp,
                                               radius):
    """Column energy budget residual when column dry mass is corrected."""
    en = energy(temp, z, q, q_ice, u, v)
    tendency = time_tendency_each_timestep(int_dp_g(en, dp))
    transport = energy_column_divg_dry_mass_adj(
        temp, z, q, q_ice, u, v, ps, dp, radius
    )
    source = energy_column_source(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
                                  lwup_sfc, lwdn_sfc, shflx, evap)
    return tendency + transport - source


def energy_column_budget_mass_adj_residual(temp, z, q, q_ice, u, v, swdn_toa,
                                           swup_toa, olr, swup_sfc, swdn_sfc,
                                           lwup_sfc, lwdn_sfc, shflx, evap,
                                           precip, ps, dp, radius):
    """Column energy budget residual when column mass is corrected."""
    en = energy(temp, z, q, q_ice, u, v)
    tendency = time_tendency_each_timestep(int_dp_g(en, dp))
    transport = energy_column_divg_mass_adj(
        temp, z, q, q_ice, u, v, evap, precip, ps, dp, radius
    )
    source = energy_column_source(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
                                  lwup_sfc, lwdn_sfc, shflx, evap)
    return tendency + transport - source


def energy_column_budget_energy_adj_residual(temp, z, q, q_ice, u, v, swdn_toa,
                                             swup_toa, olr, swup_sfc, swdn_sfc,
                                             lwup_sfc, lwdn_sfc, shflx, evap,
                                             ps, dp, radius):
    """Column energy budget residual when column energy is corrected."""
    en = energy(temp, z, q, q_ice, u, v)
    tendency = time_tendency_each_timestep(int_dp_g(en, dp))
    transport = energy_column_divg_energy_adj(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc,
        swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, ps, dp, radius
    )
    source = energy_column_source(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
                                  lwup_sfc, lwdn_sfc, shflx, evap)
    return tendency + transport - source


def energy_horiz_advec_eta(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                           swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
                           precip, ps, dp, radius, bk, pk):
    """Horizontal advection of energy at constant pressure."""
    u_adj, v_adj = uv_mass_energy_adjusted(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius
    )
    en = energy(temp, z, q, q_ice, u_adj, v_adj)
    # return horiz_advec_from_eta_spharm(en, u_adj, v_adj, ps, radius, bk, pk)
    return horiz_advec_const_p_from_eta(en, u_adj, v_adj, ps, radius, bk, pk)


def energy_horiz_advec_eta_time_mean(temp, z, q, q_ice, u, v, swdn_toa,
                                     swup_toa, olr, swup_sfc, swdn_sfc,
                                     lwup_sfc, lwdn_sfc, shflx, evap, precip,
                                     ps, dp, radius, bk, pk):
    """Horizontal energy advection at constant pressure by time-mean flow."""
    u_adj, v_adj = uv_mass_energy_adjusted(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius
    )
    en = energy(temp, z, q, q_ice, u_adj, v_adj)
    monthly_terms = [monthly_mean_ts(d) for d in (en, u_adj, v_adj, ps)]
    monthly_terms += [radius, bk, pk]
    return horiz_advec_const_p_from_eta(*monthly_terms)


def energy_horiz_advec(temp, z, q, q_ice, u, v, swdn_toa, swup_toa,
                       olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc,
                       shflx, evap, precip, ps, dp, radius):
    """Horizontal advection of energy at constant pressure."""
    u_adj, v_adj = uv_mass_energy_adjusted(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius
    )
    en = energy(temp, z, q, q_ice, u_adj, v_adj)
    return horiz_advec(en, u_adj, v_adj, radius)


def energy_horiz_advec_eta_upwind(temp, z, q, q_ice, u, v, radius, ps, bk, pk,
                                  order=1):
    """Vertical advection of energy using upwind scheme."""
    return horiz_advec_upwind(energy(temp, z, q, q_ice, u, v), u, v, radius,
                              order=order)


def energy_vert_advec(temp, z, q, q_ice, u, v, omega):
    """Vertical advection of energy."""
    return omega*d_dp_from_p(energy(temp, z, q, q_ice, u, v))


def energy_vert_advec_eta(temp, z, q, q_ice, u, v, omega, ps, bk, pk):
    """Vertical advection of energy."""
    return omega*d_dp_from_eta(energy(temp, z, q, q_ice, u, v), ps, bk, pk)


def energy_vert_advec_eta_upwind(temp, z, q, q_ice, u, v, omega, ps, bk, pk,
                                 order=1):
    """Vertical advection of energy using upwind scheme."""
    pfull_coord = u[PFULL_STR]
    pfull = pfull_from_ps(bk, pk, ps, pfull_coord)
    return vert_advec_upwind(energy(temp, z, q, q_ice, u, v), omega,
                             dim=PFULL_STR, coord=pfull, order=order)


def energy_vert_advec_eta_adj(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                              swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx,
                              evap, precip, ps, dp, radius, bk, pk):
    """Vertical advection of energy using column energy-adjusted omega."""
    u_adj, v_adj = uv_mass_energy_adjusted(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius
    )
    omega_adj = omega_from_divg_eta(u_adj, v_adj, ps, radius, bk, pk)
    return omega_adj*d_dp_from_eta(energy(temp, z, q, q_ice, u, v), ps, bk, pk)


def energy_vert_advec_eta_time_mean(temp, z, q, q_ice, u, v,
                                    omega, ps, bk, pk):
    """Time-mean vertical energy advection from model coordinates."""
    monthly_terms = [monthly_mean_ts(d) for d in (temp, z, q, q_ice, u, v)]
    ps_mon = monthly_mean_ts(ps)
    return omega*d_dp_from_eta(energy(*monthly_terms), ps_mon, bk, pk)


def energy_vert_advec_eta_adj_time_mean(temp, z, q, q_ice, u, v, swdn_toa,
                                        swup_toa, olr, swup_sfc, swdn_sfc,
                                        lwup_sfc, lwdn_sfc, shflx, evap,
                                        precip, ps, dp, radius, bk, pk):
    """Time-mean vertical energy advection w/ column energy-adjusted omega."""
    u_adj, v_adj = uv_mass_energy_adjusted(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius
    )
    omega_adj = omega_from_divg_eta(u_adj, v_adj, ps, radius, bk, pk)
    monthly_terms = [monthly_mean_ts(d) for d in (temp, z, q, q_ice,
                                                  u_adj, v_adj)]
    ps_mon = monthly_mean_ts(ps)
    return omega_adj*d_dp_from_eta(energy(*monthly_terms), ps_mon, bk, pk)


def energy_vert_advec_eta_upwind_time_mean(temp, z, q, q_ice, u, v, omega,
                                           ps, radius, bk, pk, order=1):
    """Time-mean vertical energy advection w/ column energy-adjusted omega."""
    monthly_terms = [monthly_mean_ts(d) for d in (temp, z, q, q_ice, u, v)]
    pfull_coord = u[PFULL_STR]
    ps_mon = monthly_mean_ts(ps)
    pfull = pfull_from_ps(bk, pk, ps_mon, pfull_coord)
    return vert_advec_upwind(energy(*monthly_terms), omega,
                             dim=PFULL_STR, coord=pfull, order=order)


def energy_vert_advec_eta_upwind_adj_time_mean(temp, z, q, q_ice, u, v,
                                               swdn_toa, swup_toa, olr,
                                               swup_sfc, swdn_sfc, lwup_sfc,
                                               lwdn_sfc, shflx, evap, precip,
                                               ps, dp, radius, bk, pk,
                                               order=1):
    """Time-mean vertical energy advection w/ column energy-adjusted omega."""
    u_adj, v_adj = uv_mass_energy_adjusted(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius
    )
    omega_adj = omega_from_divg_eta(u_adj, v_adj, ps, radius, bk, pk)
    monthly_terms = [monthly_mean_ts(d) for d in (temp, z, q, q_ice,
                                                  u_adj, v_adj)]
    omega_mon = monthly_mean_ts(omega_adj)
    pfull_coord = u[PFULL_STR]
    pfull = pfull_from_ps(bk, pk, monthly_mean_ts(ps), pfull_coord)
    return vert_advec_upwind(energy(*monthly_terms), omega_mon,
                             dim=PFULL_STR, coord=pfull, order=order)


def horiz_divg_energy_adj_eta(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                              swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx,
                              evap, precip, ps, dp, radius, bk, pk):
    """Mass-balance adjusted horizontal divergence from model coordinates."""
    u_adj, v_adj = uv_mass_energy_adjusted(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius
    )
    divg_eta = horiz_divg_spharm(u_adj, v_adj, radius)
    du_deta, dv_deta = d_deta_from_pfull(u_adj), d_deta_from_pfull(v_adj)
    pfull_coord = u[PFULL_STR]
    bk_at_pfull = to_pfull_from_phalf(bk, pfull_coord)
    da_deta = d_deta_from_phalf(pk, pfull_coord)
    db_deta = d_deta_from_phalf(bk, pfull_coord)
    return (divg_eta - (bk_at_pfull / (da_deta + db_deta*ps)) *
            horiz_advec_spharm(ps, du_deta, dv_deta, radius))


def energy_horiz_divg_eta(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                          swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
                          precip, ps, dp, radius, bk, pk):
    """Energy times adjusted horizontal divergence at constant pressure."""
    return (energy(temp, z, q, q_ice, u, v) *
            horiz_divg_energy_adj_eta(
                temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc,
                swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp,
                radius, bk, pk,
            ))


def energy_column_vert_advec_as_resid(temp, z, q, q_ice, u, v, swdn_toa,
                                      swup_toa, olr, swup_sfc, swdn_sfc,
                                      lwup_sfc, lwdn_sfc, shflx, evap, precip,
                                      ps, dp, radius):
    """Divergent component of column energy flux divergence."""
    return energy_column_divg_adj(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius,
    ) - int_dp_g(energy_horiz_advec(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius,
    ), dp)


def energy_column_vert_advec_as_resid_eta_time_mean(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius, bk, pk
):
    """Vertical advection energy by time-mean flow."""
    return energy_column_divg_adj_time_mean(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius
    ) - int_dp_g(energy_horiz_advec_eta_time_mean(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius, bk, pk
    ), dp)


def energy_vert_advec_adj_eta(temp, z, q, q_ice, u, v, omega, swdn_toa,
                              swup_toa, olr, swup_sfc, swdn_sfc, lwup_sfc,
                              lwdn_sfc, shflx, evap, precip, ps, dp, radius,
                              bk, pk):
    """Vertical advection of energy with column balance adjustment."""
    column_advec_as_resid = energy_column_vert_advec_as_resid_eta(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius, bk, pk,

    )
    en = energy(temp, z, q, q_ice, u, v)
    # monthly_terms = [monthly_mean_ts(d) for d in (en, ps)]
    # monthly_terms += [bk, pk]
    advec = omega*d_dp_from_eta(en, ps, bk, pk)
    column_advec = int_dp_g(advec, dp)
    residual = column_advec_as_resid - column_advec
    return advec - (residual * grav.value / ps)


def energy_sfc_ps_advec(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                        swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
                        precip, ps, dp, radius):
    """Advection of energy times surface pressure."""
    u_adj, v_adj = uv_mass_energy_adjusted(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius
    )
    en = energy(temp, z, q, q_ice, u_adj, v_adj)
    p_str = vert_coord_name(temp)

    def sel(arr):
        sfc_sel = {p_str: temp[p_str].max()}
        return arr.sel(**sfc_sel).drop(p_str)

    en = sel(en)
    u_adj = sel(u_adj)
    v_adj = sel(v_adj)
    return horiz_advec_spharm(ps, u_adj*en, v_adj*en, radius) / grav.value


def energy_sfc_ps_advec_as_resid(temp, z, q, q_ice, u, v, swdn_toa, swup_toa,
                                 olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc,
                                 shflx, evap, precip, ps, dp, radius, bk, pk):
    """Advection of energy times surface pressure."""
    u_adj, v_adj = uv_mass_energy_adjusted(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius
    )
    col_divg = energy_column_divg_adj(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius
    )
    en = energy(temp, z, q, q_ice, u_adj, v_adj)
    # 2015-11-16 S. Hill: This should have eta correction applied.
    divg_col_int = int_dp_g(horiz_divg_from_eta(en*u_adj, en*v_adj, ps,
                                                radius, bk, pk), dp)
    return col_divg - divg_col_int


def mse_horiz_flux_divg(temp, hght, sphum, u, v, radius):
    """Horizontal flux convergence of moist static energy."""
    return field_horiz_flux_divg(mse(temp, hght, sphum), u, v, radius)


def mse_horiz_advec(temp, hght, sphum, u, v, radius):
    """Horizontal advection of moist static energy."""
    return horiz_advec(mse(temp, hght, sphum), u, v, radius)


def mse_times_horiz_divg(temp, hght, sphum, u, v, radius, dp):
    """Horizontal divergence of moist static energy."""
    return field_times_horiz_divg(mse(temp, hght, sphum), u, v, radius, dp)


def mse_horiz_advec_divg_sum(T, z, q, u, v, rad, dp):
    return field_horiz_advec_divg_sum(mse(T, z, q), u, v, rad, dp)


def mse_vert_flux_divg(T, z, q, omega, p):
    """Vertical divergence times moist static energy."""
    return field_vert_flux_divg(mse(T, z, q), omega, p)


def mse_vert_advec(temp, hght, sphum, omega, p):
    """Vertical advection of moist static energy."""
    return vert_advec(mse(temp, hght, sphum), omega, p)


def mse_total_advec(temp, hght, sphum, u, v, omega, p, radius):
    mse_ = mse(temp, hght, sphum)
    return field_total_advec(mse_, u, v, omega, p, radius)


def mse_horiz_advec_upwind(temp, hght, sphum, u, v, radius):
    return horiz_advec_upwind(mse(temp, hght, sphum), u, v, radius)


def mse_vert_advec_upwind(temp, hght, sphum, omega, p):
    return vert_advec_upwind(mse(temp, hght, sphum), omega, p)


def mse_total_advec_upwind(temp, hght, sphum, u, v, omega, p, radius):
    return total_advec_upwind(mse(temp, hght, sphum), u, v, omega, p, radius)


def mse_budget_advec_residual(temp, hght, sphum, ucomp, vcomp, omega,
                              p, dp, radius, swdn_toa, swup_toa, olr, swup_sfc,
                              swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap):
    """Residual in vertically integrated MSE budget."""
    mse_ = mse(temp, hght, sphum)
    transport = field_total_advec(mse_, ucomp, vcomp, omega, p, radius)
    trans_vert_int = int_dp_g(transport, dp)
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
    trans_vert_int = int_dp_g(transport, dp)
    f_net = column_energy(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
                          lwup_sfc, lwdn_sfc, shflx, evap)
    return f_net - trans_vert_int


def dse_horiz_flux_divg(temp, hght, u, v, radius):
    """Horizontal flux convergence of moist static energy."""
    return field_horiz_flux_divg(dse(temp, hght), u, v, radius)


def dse_horiz_advec(temp, hght, u, v, radius):
    """Horizontal advection of moist static energy."""
    return horiz_advec(dse(temp, hght), u, v, radius)


def dse_times_horiz_divg(temp, hght, u, v, radius, dp):
    """Horizontal divergence of moist static energy."""
    return field_times_horiz_divg(dse(temp, hght), u, v, radius, dp)


def dse_horiz_advec_divg_sum(T, z, u, v, rad, dp):
    return field_horiz_advec_divg_sum(dse(T, z), u, v, rad, dp)


def dse_vert_advec(temp, hght, omega, p):
    """Vertical advection of moist static energy."""
    return vert_advec(dse(temp, hght), omega, p)


def tdt_diab(tdt_lw, tdt_sw, tdt_conv, tdt_ls):
    """Net diabatic heating rate."""
    return tdt_lw + tdt_sw + tdt_conv + tdt_ls


def tdt_lw_cld(tdt_lw, tdt_lw_clr):
    """Cloudy-sky temperature tendency from longwave radiation."""
    return tdt_lw - tdt_lw_clr


def tdt_sw_cld(tdt_sw, tdt_sw_clr):
    """Cloudy-sky temperature tendency from shortwave radiation."""
    return tdt_sw - tdt_sw_clr


def tdt_moist_diabatic(tdt_lw, tdt_sw, tdt_vdif):
    """Net moist diabatic heating rate, i.e. neglecting condensation."""
    return tdt_lw + tdt_sw + tdt_vdif


def mse_tendency(tdt_lw, tdt_sw, tdt_vdif, qdt_vdif):
    """Net moist energetic forcing, i.e. neglecting condensation."""
    return (c_p.value*tdt_moist_diabatic(tdt_lw, tdt_sw, tdt_vdif) +
            L_v.value*qdt_vdif)
