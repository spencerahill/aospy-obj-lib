"""Functions relating to precipitation, moisture budget, etc."""
from aospy.constants import grav
from aospy.utils import int_dp_g
import numpy as np

from .mass import column_flux_divg, mass_budget_residual
from .transport import field_horiz_flux_divg, field_total_advec
from .tendencies import time_tendency


def moisture_budget_lhs(u, v, q, radius, dp):
    return (time_tendency(int_dp_g(q, dp), dp) +
            column_flux_divg(q, u, v, radius, dp))


def moisture_budget_with_adj_lhs(ps, u, v, q, radius, dp):
    moist_lhs = moisture_budget_lhs(u, v, q, radius, dp)
    mass_resid = mass_budget_residual(ps, u, v, q, radius, dp)
    wvp = int_dp_g(q, dp)
    return moist_lhs - mass_resid * grav.value * wvp / ps


def p_minus_e(precip, evap):
    """Precipitation minus evaporation."""
    return precip - evap


def prec_conv_frac(prec_conv, precip, prec_ls=False):
    """Fraction of precipitation coming from convection scheme."""
    # Mask where precip is zero to avoid dividing by zero.
    prec_conv = np.ma.masked_where(precip == 0., prec_conv)
    precip = np.ma.masked_where(precip == 0., precip)
    if prec_ls:
        return prec_conv/(precip + prec_conv)
    else:
        return prec_conv/precip


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


def qu(sphum, u):
    """"Zonal moisture flux."""
    return sphum*u


def qv(sphum, v):
    """Meridional moisture flux."""
    return sphum*v
