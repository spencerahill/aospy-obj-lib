"""Functions relating to precipitation, moisture budget, etc."""
from aospy.constants import grav
from aospy.utils import int_dp_g
import numpy as np

from .tendencies import time_tendency_first_to_last
from .mass import (column_flux_divg, column_flux_divg_adj,
                   budget_residual, dry_mass_column_budget_residual,
                   mass_column_divg_adj)


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


def moisture_column_source(precip, evap):
    return evap - precip


def moisture_column_tendency(q, dp, freq='1M'):
    """Time tendency of column-integrated water vapor."""
    return time_tendency_first_to_last(int_dp_g(q, dp), freq=freq)


def moisture_column_budget_lhs(u, v, q, radius, dp, freq='1M'):
    """Transport plus tendency terms of column-integrated water vapor.

    Equivalently, the left-hand-side of the budget, where the right-hand-side
    is the source term, namely evaporation minus precipitation.
    """
    tendency = moisture_column_tendency(q, dp)
    transport = column_flux_divg(q, u, v, radius, dp)
    return budget_residual(tendency, transport, freq=freq)


def moisture_column_budget_residual(q, u, v, dp, radius, evap, precip,
                                    freq='1M'):
    """Residual in vertically integrated MSE budget."""
    tendency = moisture_column_tendency(q, dp)
    transport = column_flux_divg(q, u, v, radius, dp)
    source = -1*p_minus_e(precip, evap)
    return budget_residual(tendency, transport, source=source, freq=freq)


def moisture_column_divg_with_adj2(q, ps, u, v, evap, precip, radius, dp,
                                   freq='1M'):
    """Column flux divergence, with the field defined per unit mass of air."""
    col_moist_divg = column_flux_divg_adj(q, ps, u, v, evap, precip,
                                          radius, dp)
    col_mass_divg = mass_column_divg_adj(ps, u, v, evap, precip, radius,
                                         dp, freq=freq)
    return col_moist_divg - col_mass_divg * int_dp_g(q, dp) / ps


def moisture_column_budget_with_adj_lhs(ps, u, v, q, radius, dp, freq='1M'):
    """Column moisture budget LHS, with mass-balance adjustment applied.

    The mass adjustment: subtract off the column mass residual (deduced from
    the column dry mass budget) times the column average specific humidity.
    """
    moist_lhs = moisture_column_budget_lhs(u, v, q, radius, dp, freq=freq)
    dry_mass_resid = dry_mass_column_budget_residual(ps, u, v, q, radius, dp)
    wvp = int_dp_g(q, dp)
    return moist_lhs - dry_mass_resid * grav.value * wvp / ps


def moisture_column_budget_with_adj2_lhs(ps, u, v, q, radius, dp, freq='1M'):
    """Column moisture budget LHS, with mass-balance adjustment applied.

    In this case the mass-adjusted wind at each level is inserted into the
    column flux divergence computation.
    """
    return (moisture_column_tendency(q, dp, freq=freq) +
            column_flux_divg_adj(q, u, v, q, ps, radius, dp))
