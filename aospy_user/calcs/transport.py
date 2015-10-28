"""Functions for computing tracer transports."""
from aospy.utils import int_dp_g
import numpy as np

from .numerics import d_dx_from_latlon, d_dy_from_lat, d_dp_from_p
from .advection import horiz_advec, vert_advec
from .mass import horiz_divg, horiz_divg_mass_adj, horiz_advec_mass_adj


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
