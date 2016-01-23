"""Advection-related quantities."""
from aospy.utils import (to_radians, to_pascal, to_pfull_from_phalf,
                         d_deta_from_phalf)
from infinite_diff import FiniteDiff
import numpy as np

from .. import LAT_STR, LON_STR, PFULL_STR
from .numerics import (latlon_deriv_prefactor, upwind_scheme,
                       wraparound_lon, d_dx_from_latlon, d_dy_from_lat,
                       d_dp_from_p, d_dx_at_const_p_from_eta,
                       d_dy_at_const_p_from_eta, d_dp_from_eta,
                       horiz_gradient_spharm, horiz_gradient_from_eta_spharm)


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
    df_fwd = FiniteDiff.fwd_diff_deriv(arr_ext, LON_STR)
    df_bwd = FiniteDiff.bwd_diff_deriv(arr_ext, LON_STR)
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
    df_fwd_except_np = FiniteDiff.fwd_diff1(arr, lat)
    df_bwd_except_sp = FiniteDiff.fwd_diff1(arr[::-1], lat[::-1])[::-1]
    df_fwd = np.ma.concatenate((df_fwd_except_np,
                                df_bwd_except_sp[-1:]), axis=0)
    df_bwd = np.ma.concatenate((df_fwd_except_np[:1],
                                df_bwd_except_sp), axis=0)
    return prefactor*upwind_scheme(df_fwd, df_bwd, v)


def horiz_advec_upwind(arr, u, v, radius, vec_field=False):
    return (zonal_advec_upwind(arr, u, radius) +
            merid_advec_upwind(arr, v, radius, vec_field=vec_field))


def vert_advec_upwind(arr, omega, p):
    """Advection in pressure using upwind differencing."""
    p = to_pascal(p)
    # Create arrays holding positive and negative values, each with forward
    # differencing at south pole and backward differencing at north pole.
    df_fwd_partial = FiniteDiff.fwd_diff1(arr, p)
    df_bwd_partial = FiniteDiff.fwd_diff1(arr[::-1], p[::-1])[::-1]
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


def horiz_advec_spharm(arr, u, v, radius):
    """Horizontal advection using spherical harmonics."""
    d_dx, d_dy = horiz_gradient_spharm(arr, radius)
    return u * d_dx + v * d_dy


def zonal_advec_spharm(arr, u, radius):
    """Zonal advection using spherical harmonics."""
    d_dx, _ = horiz_gradient_spharm(arr, radius)
    return u * d_dx


def merid_advec_spharm(arr, v, radius):
    """Meridional advection using spherical harmonics."""
    _, d_dy = horiz_gradient_spharm(arr, radius)
    return v * d_dy


def horiz_advec_from_eta_spharm(arr, u, v, ps, radius, bk, pk):
    """Horizontal advection using spherical harmonics from model coords."""
    d_dx, d_dy = horiz_gradient_from_eta_spharm(arr, ps, radius, bk, pk)
    return u * d_dx + v * d_dy


def zonal_advec_from_eta_spharm(arr, u, ps, radius, bk, pk):
    """Zonal advection using spherical harmonics from model coords."""
    d_dx, _ = horiz_gradient_from_eta_spharm(arr, ps, radius, bk, pk)
    return u * d_dx


def merid_advec_from_eta_spharm(arr, v, ps, radius, bk, pk):
    """Meridional advection using spherical harmonics from model coords."""
    _, d_dy = horiz_gradient_from_eta_spharm(arr, ps, radius, bk, pk)
    return v * d_dy
