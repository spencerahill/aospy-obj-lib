"""Functions for computing tracer transports."""
from aospy.utils import (int_dp_g, to_pfull_from_phalf, d_deta_from_phalf,
                         dp_from_ps)
from infinite_diff.advec import SphereUpwind
import numpy as np

from .. import PFULL_STR
from .numerics import d_dx_from_latlon, d_dy_from_lat, d_dp_from_p
from .advection import horiz_advec, vert_advec, horiz_advec_spharm
from .mass import (horiz_divg, horiz_divg_mass_adj, horiz_advec_mass_adj,
                   horiz_divg_spharm)


def field_horiz_flux_divg(arr, u, v, radius):
    """Horizontal flux divergence of given scalar field."""
    dfu_dx = d_dx_from_latlon(u*arr, radius)
    dfv_dy = d_dy_from_lat(v*arr, radius, vec_field=True)
    return dfu_dx + dfv_dy


def field_vert_flux_divg(arr, omega, p):
    """Vertical flux divergence of a scalar field."""
    return d_dp_from_p(omega*arr, p)


def field_total_advec(arr, u, v, omega, p, radius):
    return (horiz_advec(arr, u, v, radius) + vert_advec(arr, omega, p))


def field_times_horiz_divg(arr, u, v, radius):
    """Scalar field times horizontal divergence."""
    return arr*horiz_divg(u, v, radius)


def field_vert_int_bal(arr, dp):
    """Impose vertical balance to the field, i.e. column integral = 0.

    Most frequently used for mass flux divergence to impose mass balance.
    """
    pos = np.ma.where(arr > 0, arr, 0)
    neg = np.ma.where(arr < 0, arr, 0)
    pos_int = int_dp_g(pos, dp)[:, np.newaxis, :, :]
    neg_int = int_dp_g(neg, dp)[:, np.newaxis, :, :]
    arr.values = pos - (pos_int/neg_int)*neg
    return arr


def field_times_horiz_divg_mass_adj(arr, u, v, q, ps, radius, dp, p):
    return arr*horiz_divg_mass_adj(u, v, q, ps, radius, dp, p)


def field_horiz_flux_divg_mass_adj(arr, u, v, q, ps, radius, dp, p,
                                   vec_field=False):
    return (field_times_horiz_divg_mass_adj(arr, u, v, q, ps, radius, dp, p) +
            horiz_advec_mass_adj(arr, u, v, q, ps, radius, dp, p,
                                 vec_field=vec_field))


def field_horiz_advec_divg_sum(arr, u, v, radius, dp):
    return (field_times_horiz_divg(arr, u, v, radius) +
            horiz_advec(arr, u, v, radius))


def omega_from_divg_eta(u, v, ps, radius, bk, pk):
    """Omega computed from the horizontal flow on model-native coordinates."""
    ps_advec = horiz_advec_spharm(ps, u, v, radius)
    divg = horiz_divg_spharm(u, v, radius)
    term2 = u.copy()
    pfull_coord = u[PFULL_STR]

    del u, v

    term1 = to_pfull_from_phalf(bk, pfull_coord) * ps_advec

    db = d_deta_from_phalf(bk, pfull_coord)
    term2.values = np.cumsum(ps_advec*db, axis=1)

    del ps_advec

    dp = dp_from_ps(bk, pk, ps, pfull_coord)
    divg_dp = divg*dp

    del dp

    p_axis_num = divg_dp.get_axis_num(PFULL_STR)
    divg_int = np.cumsum(divg_dp, axis=p_axis_num)

    del divg_dp

    return term1 - term2 - divg_int
