"""Advection-related quantities."""
from aospy.utils import to_radians
from indiff import Upwind

from .. import LAT_STR, LON_STR, PFULL_STR
from .numerics import (latlon_deriv_prefactor, wraparound,
                       d_dx_from_latlon, d_dy_from_lat, d_dp_from_p,
                       d_dx_at_const_p_from_eta, d_dy_at_const_p_from_eta,
                       d_dp_from_eta, horiz_gradient_spharm,
                       horiz_gradient_from_eta_spharm)


def zonal_advec(arr, u, radius):
    """Zonal advection of the given field."""
    return u*d_dx_from_latlon(arr, radius)


def merid_advec(arr, v, radius):
    """Meridional advection of the given field."""
    return v*d_dy_from_lat(arr, radius)


def horiz_advec(arr, u, v, radius):
    """Horizontal advection of the given field."""
    return zonal_advec(arr, u, radius) + merid_advec(arr, v, radius)


def vert_advec(arr, omega, p):
    """Vertical advection of the given field."""
    return omega*d_dp_from_p(arr, p)


def total_advec(arr, u, v, omega, p, radius):
    """Total advection of the given field."""
    return horiz_advec(arr, u, v, radius) + vert_advec(arr, omega, p)


def zonal_advec_upwind(arr, u, radius, order=2):
    """Advection in the zonal direction using upwind differencing."""
    prefactor = latlon_deriv_prefactor(to_radians(arr.coords[LAT_STR]),
                                       radius, d_dy_of_scalar_field=False)
    arr_ext = wraparound(arr, LON_STR, left=order, right=order, circumf=360.)
    lon_rad_ext = to_radians(arr_ext[LON_STR])
    return prefactor*Upwind(u, arr_ext, LON_STR, coord=lon_rad_ext,
                            order=order, fill_edge=False).advec()


def merid_advec_upwind(arr, v, radius, order=2):
    """Advection in the meridional direction using upwind differencing."""
    lat_rad = to_radians(arr.coords[LAT_STR])
    prefactor = 1. / radius
    return prefactor*Upwind(v, arr, LAT_STR, coord=lat_rad, order=order,
                            fill_edge=True).advec()


def horiz_advec_upwind(arr, u, v, radius, order=2):
    """Horizontal (meridional plus zonal) upwind advection."""
    return (zonal_advec_upwind(arr, u, radius, order=order) +
            merid_advec_upwind(arr, v, radius, order=order))


def total_advec_upwind(arr, u, v, omega, p, radius,
                       p_str=PFULL_STR, order=1):
    """Total (horizontal plus vertical) upwind advection."""
    return (horiz_advec_upwind(arr, u, v, radius, order=order) +
            Upwind(omega, p_str, arr, coord=p, order=order,
                   fill_edge=True).advec())


def zonal_advec_const_p_from_eta(arr, u, ps, radius, bk, pk):
    """Zonal advection at constant pressure of the given scalar field."""
    return u*d_dx_at_const_p_from_eta(arr, ps, radius, bk, pk)


def merid_advec_const_p_from_eta(arr, v, ps, radius, bk, pk):
    """Meridional advection at constant pressure of the given scalar field."""
    return v*d_dy_at_const_p_from_eta(arr, ps, radius, bk, pk)


def horiz_advec_const_p_from_eta(arr, u, v, ps, radius, bk, pk):
    """Horizontal advection at constant pressure of the given scalar field."""
    return (zonal_advec_const_p_from_eta(arr, u, ps, radius, bk, pk) +
            merid_advec_const_p_from_eta(arr, v, ps, radius, bk, pk))


def vert_advec_from_eta(arr, omega, ps, bk, pk):
    """Vertical advection of the given field."""
    return omega*d_dp_from_eta(arr, ps, bk, pk)


def total_advec_from_eta(arr, u, v, omega, p, ps, radius, bk, pk):
    """Total advection of the given scalar field."""
    return (horiz_advec_const_p_from_eta(arr, u, v, ps, radius, bk, pk) +
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
