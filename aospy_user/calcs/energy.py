"""Energy budget-related fields"""
from aospy.utils import int_dp_g
import numpy as np

from ..sphere_harm import SpharmInterface
from .tendencies import (time_tendency_first_to_last,
                         time_tendency_each_timestep)
from .advection import (horiz_advec, vert_advec, horiz_advec_upwind,
                        vert_advec_upwind, total_advec_upwind)
from .mass import (column_flux_divg, column_flux_divg_with_adj,
                   budget_residual, mass_column_divg_with_adj,
                   mass_adjusted)
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


def energy_column_divg_with_adj(temp, z, q, q_ice, ps, u, v, evap,
                                precip, radius, dp):
    return column_flux_divg_with_adj(energy(temp, z, q, q_ice, u, v), ps, u, v,
                                     evap, precip, radius, dp)


def energy_column_divg_with_adj2(temp, z, q, q_ice, ps, u, v, evap, precip,
                                 radius, dp, freq='1M'):
    """Column flux divergence, with the field defined per unit mass of air."""
    en = energy(temp, z, q, q_ice, u, v)
    col_energy_divg = column_flux_divg_with_adj(en, ps, u, v, evap, precip,
                                                radius, dp)
    col_mass_divg = mass_column_divg_with_adj(ps, u, v, evap, precip, radius,
                                              dp, freq=freq)
    return col_energy_divg - col_mass_divg * int_dp_g(en, dp) / ps


def energy_column_divg_with_adj3(temp, z, q, q_ice, ps, u, v, evap, precip,
                                 radius, dp, freq='1M'):
    """Column flux divergence, with the field defined per unit mass of air."""
    en = energy(temp, z, q, q_ice, u, v)
    col_energy_divg = column_flux_divg(en, u, v, radius, dp)
    col_mass_divg = mass_column_divg_with_adj(ps, u, v, evap, precip, radius,
                                              dp, freq=freq)
    return col_energy_divg - col_mass_divg * int_dp_g(en, dp) / ps


def energy_column_budget_residual(temp, z, q, q_ice, u, v, swdn_toa, swup_toa,
                                  olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc,
                                  shflx, evap, dp, radius):
    en = energy(temp, z, q, q_ice, u, v)
    tendency = time_tendency_each_timestep(int_dp_g(en, dp))
    transport = column_flux_divg(en, u, v, radius, dp)
    source = energy_column_source(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
                                  lwup_sfc, lwdn_sfc, shflx, evap)
    return tendency + transport - source


def energy_adj(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc,
               swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp, radius):
    """Adjustment to subtract off of u, v to impose column energy balance."""
    residual = energy_column_budget_residual(
        temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc,
        swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp, radius
    )
    # Get the residual in terms of its spectral coefficients.
    # Grab only one level of u, v since residual not defined vertically.
    sph_int = SpharmInterface(u[:,0], v[:,0], rsphere=radius,
                              make_spharmt=True)
    resid_spectral = SpharmInterface.prep_for_spharm(residual)
    resid_spectral = sph_int.spharmt.grdtospec(resid_spectral)

    # Assume residual stems entirely from divergent flow.
    vort_spectral = np.zeros_like(resid_spectral)
    u_adj, v_adj = sph_int.spharmt.getuv(vort_spectral, resid_spectral)

    u_arr = sph_int.to_xray(u_adj)
    v_arr = sph_int.to_xray(v_adj)

    col_energy = int_dp_g(energy(temp, z, q, q_ice, u, v), dp)
    return u_arr / col_energy, v_arr / col_energy


def energy_adjusted(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr, swup_sfc,
                    swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp, radius):
    """Horizontal wind components with column energy balance-adjustment."""
    u_adj, v_adj = energy_adj(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                              swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx,
                              evap, dp, radius)
    return u - u_adj, v - v_adj


def energy_column_divg_adj(temp, z, q, q_ice, u, v, swdn_toa, swup_toa, olr,
                           swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
                           precip, ps, dp, radius, freq='1M'):
    u_mass_adj, v_mass_adj = mass_adjusted(ps, u, v, evap, precip, radius,
                                           dp, freq=freq)
    u_en_adj, v_en_adj = energy_adjusted(
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
        lwup_sfc, lwdn_sfc, shflx, evap, precip, ps, dp, radius, freq='1M'
    )
    source = energy_column_source(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
                                  lwup_sfc, lwdn_sfc, shflx, evap)

    return tendency + transport - source


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
