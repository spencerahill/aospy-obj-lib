"""MSE budget functions, with height computed using hypsometric equation."""
from indiff.advec import Upwind
from indiff.deriv import LatCenDeriv, LonCenDeriv

from .. import LAT_STR, LON_STR, PLEVEL_STR
from .advection import (zonal_advec_upwind, merid_advec_upwind,
                        horiz_advec_upwind)
from .thermo import cpt_lvq, mse_from_hypso


def mse_from_hypso_merid_deriv(ps, temp, sphum):
    """Meridional derivative of frozen MSE on pressure coordinates."""
    deriv_obj = LatCenDeriv(mse_from_hypso(ps, temp, sphum), LAT_STR)
    return deriv_obj.deriv()


def mse_from_hypso_zonal_deriv(ps, temp, sphum):
    """Zonal derivative of frozen MSE on pressure coordinates."""
    deriv_obj = LonCenDeriv(mse_from_hypso(ps, temp, sphum), LON_STR)
    return deriv_obj.deriv()


def mse_from_hypso_zonal_advec_upwind(ps, temp, sphum, u, radius, order=2):
    """Zonal advection of moist static energy using upwind scheme."""
    return zonal_advec_upwind(mse_from_hypso(ps, temp, sphum), u, radius,
                              order=order)


def mse_from_hypso_merid_advec_upwind(ps, temp, sphum, v, radius, order=2):
    """Meridional advection of moist static energy using upwind scheme."""
    return merid_advec_upwind(mse_from_hypso(ps, temp, sphum), v, radius,
                              order=order)


def mse_from_hypso_horiz_advec_upwind(ps, temp, sphum, u, v, radius, order=2):
    """Horizontal moist static energy advection using upwind scheme."""
    return horiz_advec_upwind(mse_from_hypso(ps, temp, sphum), u, v, radius,
                              order=order)


def mse_from_hypso_vert_advec_upwind(ps, temp, sphum, omega, p, order=2):
    """Upwind vertical advection of moist static energy."""
    return Upwind(omega, mse_from_hypso(ps, temp, sphum), PLEVEL_STR,
                  coord=p, order=order, fill_edge=True).advec()


def cpt_lvq_merid_deriv(temp, sphum):
    """Meridional derivative of c_p*T + L_v*q on pressure coordinates."""
    deriv_obj = LatCenDeriv(cpt_lvq(temp, sphum), LAT_STR)
    return deriv_obj.deriv()


def cpt_lvq_zonal_deriv(temp, sphum):
    """Zonal derivative of c_p*T + L_v*q on pressure coordinates."""
    deriv_obj = LonCenDeriv(cpt_lvq(temp, sphum), LON_STR)
    return deriv_obj.deriv()


def cpt_lvq_zonal_advec_upwind(temp, sphum, u, radius, order=2):
    """Zonal advection of moist static energy using upwind scheme."""
    return zonal_advec_upwind(cpt_lvq(temp, sphum), u, radius,
                              order=order)


def cpt_lvq_merid_advec_upwind(temp, sphum, v, radius, order=2):
    """Meridional advection of moist static energy using upwind scheme."""
    return merid_advec_upwind(cpt_lvq(temp, sphum), v, radius,
                              order=order)


def cpt_lvq_horiz_advec_upwind(temp, sphum, u, v, radius, order=2):
    """Horizontal moist static energy advection using upwind scheme."""
    return horiz_advec_upwind(cpt_lvq(temp, sphum), u, v, radius,
                              order=order)
