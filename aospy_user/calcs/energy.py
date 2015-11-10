"""Energy budget-related fields"""
from aospy.constants import grav
from aospy.utils import int_dp_g, vert_coord_name

from .tendencies import (time_tendency_first_to_last,
                         time_tendency_each_timestep)
from .advection import (horiz_advec, vert_advec, horiz_advec_upwind,
                        vert_advec_upwind, total_advec_upwind,
                        horiz_advec_const_p_from_eta, d_dp_from_eta,
                        d_dp_from_p)
from .mass import (column_flux_divg, budget_residual, uv_mass_adjusted,
                   uv_column_budget_adjustment, horiz_divg_from_eta)
from .transport import (field_horiz_flux_divg, field_vert_flux_divg,
                        field_total_advec, field_horiz_advec_divg_sum,
                        field_times_horiz_divg)
from .thermo import dse, mse, fmse
from .toa_sfc_fluxes import column_energy


def kinetic_energy(u, v):
    """Kinetic energy per unit mass, neglecting vertical motion."""
    return 0.5*(u*u + v*v)


def energy(temp, z, q, q_ice, u, v):
    return fmse(temp, z, q, q_ice) + kinetic_energy(u, v)


def energy_column(temp, z, q, q_ice, u, v, dp):
    return int_dp_g(energy(temp, z, q, q_ice, u, v), dp)


def energy_column_tendency(temp, z, q, q_ice, u, v, dp, freq='1M'):
    return time_tendency_first_to_last(energy_column(temp, z, q, q_ice,
                                                     u, v, dp), freq=freq)


energy_column_source = column_energy


def energy_column_divg(temp, z, q, q_ice, u, v, dp, radius):
    return column_flux_divg(energy(temp, z, q, q_ice, u, v), u, v, radius, dp)


def energy_column_budget_lhs(temp, z, q, q_ice, u, v, ps, dp, radius,
                             freq='1M'):
    tendency = energy_column_tendency(temp, z, q, q_ice, u, v, dp, freq=freq)
    transport = energy_column_divg(temp, z, q, q_ice, u, v, dp, radius)
    return budget_residual(tendency, transport, freq=freq)


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
                              evap, precip, ps, dp, radius, freq='1M'):
    """Horiz wind adjustments to impose column mass and energy balance."""
    u_mass_adj, v_mass_adj = uv_mass_adjusted(ps, u, v, evap, precip, radius,
                                              dp, freq=freq)
    u_en_adj, v_en_adj = uv_energy_adjustment(
        temp, z, q, q_ice, u_mass_adj, v_mass_adj, swdn_toa, swup_toa, olr,
        swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp, radius
    )
    return u_en_adj, v_en_adj


def u_mass_energy_adjustment(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                             swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx,
                             evap, precip, ps, dp, radius, freq='1M'):
    """Zonal wind adjustment to impose column mass and energy balance."""
    u_adj, _ = uv_mass_energy_adjustment(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius, freq=freq
    )
    return u_adj


def v_mass_energy_adjustment(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                             swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx,
                             evap, precip, ps, dp, radius, freq='1M'):
    """Meridional wind adjustment to impose column mass and energy balance."""
    _, v_adj = uv_mass_energy_adjustment(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius, freq=freq
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
                           precip, ps, dp, radius, freq='1M'):
    u_mass_adj, v_mass_adj = uv_mass_adjusted(ps, u, v, evap, precip, radius,
                                              dp)
    u_en_adj, v_en_adj = uv_energy_adjusted(
        temp, z, q, q_ice, u_mass_adj, v_mass_adj, swdn_toa, swup_toa, olr,
        swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp, radius
    )
    return energy_column_divg(temp, z, q, q_ice, u_en_adj,
                              v_en_adj, dp, radius)


def energy_column_budget_adj_residual(temp, z, q, q_ice, u, v, swdn_toa,
                                      swup_toa, olr, swup_sfc, swdn_sfc,
                                      lwup_sfc, lwdn_sfc, shflx, evap, precip,
                                      ps, dp, radius, freq='1M'):
    en = energy(temp, z, q, q_ice, u, v)
    tendency = time_tendency_each_timestep(int_dp_g(en, dp))
    transport = energy_column_divg_adj(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius, freq=freq
    )
    source = energy_column_source(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
                                  lwup_sfc, lwdn_sfc, shflx, evap)

    return tendency + transport - source


def energy_horiz_advec_from_eta(temp, z, q, q_ice, u, v, swdn_toa, swup_toa,
                                olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc,
                                shflx, evap, precip, ps, dp, radius, bk, pk,
                                freq='1M'):
    """Horizontal advection of energy at constant pressure."""
    u_adj, v_adj = uv_mass_energy_adjusted(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius
    )
    en = energy(temp, z, q, q_ice, u_adj, v_adj)
    return horiz_advec_const_p_from_eta(en, u_adj, v_adj, ps, radius, bk, pk)


def energy_horiz_advec(temp, z, q, q_ice, u, v, swdn_toa, swup_toa,
                       olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc,
                       shflx, evap, precip, ps, dp, radius, freq='1M'):
    """Horizontal advection of energy at constant pressure."""
    u_adj, v_adj = uv_mass_energy_adjusted(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius
    )
    en = energy(temp, z, q, q_ice, u_adj, v_adj)
    return horiz_advec(en, u_adj, v_adj, radius)


def energy_vert_advec(temp, z, q, q_ice, u, v, omega):
    """Vertical advection of energy."""
    return omega*d_dp_from_p(energy(temp, z, q, q_ice, u, v))


def energy_vert_advec_from_eta(temp, z, q, q_ice, u, v, omega, ps, bk, pk):
    """Vertical advection of energy."""
    return omega*d_dp_from_eta(energy(temp, z, q, q_ice, u, v), ps, bk, pk)


def energy_horiz_divg_from_eta(temp, z, q, q_ice, u, v, evap, precip, ps, dp,
                               radius, bk, pk, freq='1M'):
    """Horizontal advection of energy at constant pressure."""
    u_adj, v_adj = uv_mass_adjusted(ps, u, v, evap, precip, radius, dp,
                                    freq=freq)
    return (energy(temp, z, q, q_ice, u_adj, v_adj) *
            horiz_divg_from_eta(u_adj, v_adj, ps, radius, bk, pk))


def energy_column_vert_advec_as_resid_from_eta(temp, z, q, q_ice, u, v,
                                               swdn_toa, swup_toa, olr,
                                               swup_sfc, swdn_sfc, lwup_sfc,
                                               lwdn_sfc, shflx, evap, precip,
                                               ps, dp, radius, bk, pk,
                                               freq='1M'):
    """Divergent component of column energy flux divergence."""
    return energy_column_divg_adj(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius, freq=freq
    ) - int_dp_g(energy_horiz_advec_from_eta(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius, bk, pk,
        freq=freq
    ), dp)


def energy_column_vert_advec_as_resid(temp, z, q, q_ice, u, v, swdn_toa,
                                      swup_toa, olr, swup_sfc, swdn_sfc,
                                      lwup_sfc, lwdn_sfc, shflx, evap, precip,
                                      ps, dp, radius, freq='1M'):
    """Divergent component of column energy flux divergence."""
    return energy_column_divg_adj(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius, freq=freq
    ) - int_dp_g(energy_horiz_advec(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius, freq=freq
    ), dp)


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
        sfc_sel = {p_str: en[p_str].max()}
        return arr.sel(**sfc_sel).drop(p_str)

    en = sel(en)
    u_adj = sel(u_adj)
    v_adj = sel(v_adj)
    return horiz_advec(ps, u_adj*en, v_adj*en, radius) / grav.value


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
