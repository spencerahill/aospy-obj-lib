"""Gross moist stability-related quantities."""
from aospy.constants import c_p, grav, L_v
from aospy.utils import to_pascal
from infinite_diff.deriv import EtaCenDeriv
import numpy as np

from . import horiz_divg, vert_divg
from .thermo import dse, mse, fmse


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
    return field_vert_int_max(horiz_divg(u, v, radius, dp), dp)


def vert_divg_vert_int_max(omega, p, dp):
    """Maximum magnitude of integral from surface up of vertical divergence."""
    return field_vert_int_max(vert_divg(omega, p, dp), dp)


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


def gms_up_low(temp, hght, sphum, level, lev_up=400., lev_dn=925.):
    """Gross moist stability. Upper minus lower level MSE."""
    m = mse(temp, hght, sphum)
    return (np.squeeze(m[np.where(level == lev_up)] -
                       m[np.where(level == lev_dn)])/c_p)


def gms_each_level(temp, hght, sphum, level, lev_dn=925.):
    m = mse(temp, hght, sphum)
    return (m - m[np.where(level == lev_dn)])/c_p


def dry_static_stab(temp, hght, level, lev_dn=925.):
    """Dry static stability, in terms of dry static energy."""
    d = dse(temp, hght)
    return (d - d[np.where(level == lev_dn)])/c_p


def moist_static_stab(temp, hght, sphum, q_ice, ps, bk, pk):
    """Moist static stability, in terms of frozen moist static energy."""
    return EtaCenDeriv(fmse(temp, hght, sphum, q_ice), pk, bk, ps, order=2,
                       fill_edge=True).deriv()
