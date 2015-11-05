"""Advection-related quantities."""
from aospy.constants import grav
from aospy.utils import to_radians, to_pascal
from infinite_diff import FiniteDiff
import numpy as np

from .. import LAT_STR, PFULL_STR
from .numerics import (fwd_diff1, latlon_deriv_prefactor, upwind_scheme,
                       wraparound_lon, d_dx_from_latlon, d_dy_from_lat,
                       d_dp_from_p, d_dx_at_const_p_from_eta,
                       d_dy_at_const_p_from_eta, d_dp_from_eta)


def zonal_advec(arr, u, radius):
    """Zonal advection of the given field."""
    return u*d_dx_from_latlon(arr, radius)


def merid_advec(arr, v, radius, vec_field=False):
    """Meridional advection of the given field."""
    return v*d_dy_from_lat(arr, radius, vec_field=vec_field)


def horiz_advec(arr, u, v, radius, vec_field=False):
    """Horizontal advection of the given field."""
    return (zonal_advec(arr, u, radius) +
            merid_advec(arr, v, radius, vec_field=vec_field))


def vert_advec(arr, omega, p):
    """Vertical advection of the given field."""
    return omega*d_dp_from_p(arr, p)


def total_advec(arr, u, v, omega, p, radius, vec_field=False):
    """Total advection of the given field."""
    return (horiz_advec(arr, u, v, radius, vec_field=vec_field) +
            vert_advec(arr, omega, p))


def zonal_advec_upwind(arr, u, radius):
    """Advection in the zonal direction using upwind differencing."""
    prefactor = latlon_deriv_prefactor(to_radians(arr.coords[LAT_STR]),
                                       radius, d_dy_of_scalar_field=False)
    arr_ext = wraparound_lon(arr)
    df_fwd = FiniteDiff.fwd_diff1(arr_ext)
    df_bwd = FiniteDiff.bwd_diff1(arr_ext)
    # Transpose again to regain original axis order.
    return prefactor*upwind_scheme(df_fwd, df_bwd, u)


def merid_advec_upwind(arr, v, radius, vec_field=False):
    """Advection in the meridional direction using upwind differencing."""
    lat = to_radians(arr[LAT_STR])
    prefactor = 1. / radius
    # Del operator differs in spherical coords for scalar v. vector fields.
    if vec_field:
        arr *= np.cos(lat)
        prefactor /= np.cos(lat)
        prefactor = prefactor.T
    # Create arrays holding positive and negative values, each with forward
    # differencing at south pole and backward differencing at north pole.
    # df_fwd_except_np = fwd_diff2(f, lat)
    # df_bwd_except_sp = fwd_diff2(f[::-1], lat[::-1])[::-1]
    # df_fwd_adj_np = fwd_diff1(f[-2:], lat[-2:])
    # df_bwd_adj_sp = fwd_diff1(f[1::-1], lat[1::-1])[::-1]
    # df_fwd = np.ma.concatenate((df_fwd_except_np, df_fwd_adj_np,
                                # df_bwd_except_sp[-1:]), axis=0)
    # df_bwd = np.ma.concatenate((df_fwd_except_np[:1], df_bwd_adj_sp,
                                # df_bwd_except_sp), axis=0)
    df_fwd_except_np = fwd_diff1(arr, lat)
    df_bwd_except_sp = fwd_diff1(arr[::-1], lat[::-1])[::-1]
    df_fwd = np.ma.concatenate((df_fwd_except_np,
                                df_bwd_except_sp[-1:]), axis=0)
    df_bwd = np.ma.concatenate((df_fwd_except_np[:1],
                                df_bwd_except_sp), axis=0)
    # Roll axis and transpose again to regain original axis order.
    df_fwd = np.rollaxis(df_fwd, 0, 2).T
    df_bwd = np.rollaxis(df_bwd, 0, 2).T
    return prefactor*upwind_scheme(df_fwd, df_bwd, v)


def horiz_advec_upwind(arr, u, v, radius, vec_field=False):
    return (zonal_advec_upwind(arr, u, radius) +
            merid_advec_upwind(arr, v, radius, vec_field=vec_field))


def vert_advec_upwind(arr, omega, p):
    """Advection in pressure using upwind differencing."""
    p = to_pascal(p)
    # Create arrays holding positive and negative values, each with forward
    # differencing at south pole and backward differencing at north pole.
    df_fwd_partial = fwd_diff1(arr, p)
    df_bwd_partial = fwd_diff1(arr[::-1], p[::-1])[::-1]
    df_fwd = np.ma.concatenate((df_fwd_partial, df_bwd_partial[-1:]), axis=0)
    df_bwd = np.ma.concatenate((df_fwd_partial[:1], df_bwd_partial), axis=0)
    # 2015-10-26 S. Hill: does omega having the opposite sign convention as
    # normal mean that the forward v. backward differencing should be switched?
    return upwind_scheme(df_fwd, df_bwd, omega)


def total_advec_upwind(arr, u, v, omega, p, radius,
                       vec_field=False):
    return (horiz_advec_upwind(arr, u, v, radius, vec_field) +
            vert_advec_upwind(arr, omega, p))


def zonal_advec_const_p_from_eta(arr, u, ps, radius, bk, pk):
    """Zonal advection at constant pressure of the given scalar field."""
    return u*d_dx_at_const_p_from_eta(arr, ps, radius, bk, pk)


def merid_advec_const_p_from_eta(arr, v, ps, radius, bk, pk, vec_field=False):
    """Meridional advection at constant pressure of the given scalar field."""
    return v*d_dy_at_const_p_from_eta(arr, ps, radius, bk, pk,
                                      vec_field=vec_field)


def horiz_advec_const_p_from_eta(arr, u, v, ps, radius, bk, pk,
                                 vec_field=False):
    """Horizontal advection at constant pressure of the given scalar field."""
    return (zonal_advec_const_p_from_eta(arr, u, ps, radius, bk, pk) +
            merid_advec_const_p_from_eta(arr, v, ps, radius, bk, pk,
                                         vec_field=vec_field))


def vert_advec_from_eta(arr, omega, ps, bk, pk):
    """Vertical advection of the given field."""
    return omega*d_dp_from_eta(arr, ps, bk, pk)


def total_advec_from_eta(arr, u, v, omega, p, ps, radius, bk, pk,
                         vec_field=False):
    """Total advection of the given scalar field."""
    return (horiz_advec_const_p_from_eta(arr, u, v, ps, radius, bk, pk,
                                         vec_field=vec_field) +
            vert_advec(arr, omega, p))


def horiz_advec_sfc_pressure(ps, u, v, radius):
    """Horizontal advection of surface pressure."""
    # Pressure data indexing is surface to TOA; sigma data is opposite.
    u_sfc = u.isel(**{PFULL_STR: 0})
    v_sfc = v.isel(**{PFULL_STR: 0})
    return horiz_advec(ps, u_sfc, v_sfc, radius) / grav.value
