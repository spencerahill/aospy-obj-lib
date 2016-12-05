"""Functions relating to the moist static energy budget."""
from aospy.utils.vertcoord import int_dp_g
from indiff.advec import Upwind
from indiff.deriv import LatCenDeriv, LonCenDeriv

from .. import LAT_STR, LON_STR, PLEVEL_STR
from .advection import (horiz_advec, vert_advec, horiz_advec_upwind,
                        zonal_advec_upwind, merid_advec_upwind,
                        total_advec_upwind)
from .transport import (field_horiz_flux_divg, field_vert_flux_divg,
                        field_total_advec, field_horiz_advec_divg_sum,
                        field_times_horiz_divg)
from .thermo import mse
from .toa_sfc_fluxes import column_energy


def mse_merid_deriv_eta(temp, hght, sphum):
    """Meridional derivative of MSE on pressure coordinates."""
    return LatCenDeriv(mse(temp, hght, sphum), LAT_STR).deriv()


def mse_zonal_deriv_eta(temp, hght, sphum):
    """Zonal derivative of MSE on pressure coordinates."""
    return LonCenDeriv(mse(temp, hght, sphum), LON_STR).deriv()


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


def mse_zonal_advec_upwind(temp, z, q, u, radius, order=2):
    """Zonal advection of moist static energy using upwind scheme."""
    return zonal_advec_upwind(mse(temp, z, q), u, radius, order=order)


def mse_merid_advec_upwind(temp, z, q, v, radius, order=2):
    """Meridional advection of moist static energy using upwind scheme."""
    return merid_advec_upwind(mse(temp, z, q), v, radius, order=order)


def mse_horiz_advec_upwind(temp, hght, sphum, u, v, radius, order=2):
    """Horizontal moist static energy advection using upwind scheme."""
    return horiz_advec_upwind(mse(temp, hght, sphum), u, v, radius,
                              order=order)


def mse_vert_advec_upwind(temp, hght, sphum, omega, p, order=2):
    """Upwind vertical advection of moist static energy."""
    # p_names = ['plev', PLEVEL_STR]
    # p_str = get_dim_name(p, p_names)
    # p = p.rename({p_str: PLEVEL_STR})
    return Upwind(omega, mse(temp, hght, sphum), PLEVEL_STR, coord=p,
                  order=order, fill_edge=True).advec()


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
