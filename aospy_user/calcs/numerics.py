"""Finite differencing and other numerical methods."""
from animal_spharm import SpharmInterface
from aospy.utils import (d_deta_from_pfull, d_deta_from_phalf, pfull_from_ps,
                         to_pfull_from_phalf, to_radians, to_pascal)
from infinite_diff import FiniteDiff
import numpy as np
import xarray as xr

from .. import LAT_STR, LON_STR, PFULL_STR, PLEVEL_STR


def latlon_deriv_prefactor(lat, radius, radians=True,
                           d_dy_of_scalar_field=False):
    """Factor that multiplies del operations in spherical coordinates."""
    lat_rad = to_radians(lat)
    if d_dy_of_scalar_field:
        return 1. / radius
    else:
        return 1. / (radius*np.cos(lat_rad))


def wraparound(arr, dim, left=1, right=1, circumf=360., spacing=1):
    """Append wrap-around point(s) to the DataArray or Dataset coord."""
    if left:
        edge_left = arr.isel(**{dim: slice(0, left, spacing)})
        edge_left[dim] += circumf
        arr = xr.concat([arr, edge_left], dim=dim)
    if right:
        edge_right = arr.isel(**{dim: slice(-right, None, spacing)})
        edge_right[dim] -= circumf
        xr.concat([edge_right, arr], dim=dim)
    return arr


def d_dx_from_latlon(arr, radius):
    """Compute \partial arr/\partial x using centered differencing."""
    prefactor = latlon_deriv_prefactor(arr[LAT_STR], radius, radians=False)
    arr_ext = wraparound(arr, LON_STR, left=True, right=True, circumf=360.)
    lon_rad_ext = to_radians(arr_ext[LON_STR])
    darr_dx = (FiniteDiff.cen_diff(arr_ext, LON_STR) /
               FiniteDiff.cen_diff(lon_rad_ext, LON_STR))
    return prefactor*darr_dx


def d_dy_from_lat(arr, radius, vec_field=False):
    """Compute \partial(field)/\partial y using centered differencing."""
    lat_rad = to_radians(arr[LAT_STR])
    prefactor = latlon_deriv_prefactor(lat_rad, radius, radians=True,
                                       d_dy_of_scalar_field=False)
    if vec_field:
        arr = arr * np.cos(lat_rad)
    darr_dy = (
        FiniteDiff.cen_diff(arr, LAT_STR, do_edges_one_sided=True) /
        FiniteDiff.cen_diff(lat_rad, LAT_STR, do_edges_one_sided=True)
    )
    return prefactor*darr_dy


def d_dx_at_const_p_from_eta(arr, ps, radius, bk, pk):
    """d/dx at constant pressure of `arr`.

    `arr` must be defined on full levels in hybrid sigma-pressure coordinates.
    """
    pfull_coord = arr[PFULL_STR]
    d_dx_const_eta = d_dx_from_latlon(arr, radius)
    darr_deta = d_deta_from_pfull(arr)
    bk_at_pfull = to_pfull_from_phalf(bk, pfull_coord)
    da_deta = d_deta_from_phalf(pk, pfull_coord)
    db_deta = d_deta_from_phalf(bk, pfull_coord)
    d_dx_ps = d_dx_from_latlon(ps, radius)

    return d_dx_const_eta + (darr_deta * bk_at_pfull * d_dx_ps /
                             (da_deta + db_deta*ps))


def d_dy_at_const_p_from_eta(arr, ps, radius, bk, pk, vec_field=False):
    """d/dy at constant pressure of `arr`.

    `arr` must be defined on full levels in hybrid sigma-pressure coordinates.
    """
    pfull_coord = arr[PFULL_STR]
    d_dy_const_eta = d_dy_from_lat(arr, radius, vec_field=vec_field)
    darr_deta = d_deta_from_pfull(arr)
    bk_at_pfull = to_pfull_from_phalf(bk, pfull_coord)
    da_deta = d_deta_from_phalf(pk, pfull_coord)
    db_deta = d_deta_from_phalf(bk, pfull_coord)
    d_dy_ps = d_dy_from_lat(ps, radius, vec_field=vec_field)

    return d_dy_const_eta + (darr_deta*bk_at_pfull * d_dy_ps /
                             (da_deta + db_deta*ps))


def d_dp_from_p(arr, order=2):
    """Derivative in pressure of array defined on fixed pressure levels."""
    p = to_pascal(arr[PLEVEL_STR])
    return FiniteDiff.cen_diff_deriv(arr, PLEVEL_STR, coord=p, order=order,
                                     do_edges_one_sided=True)


def d_dp_from_eta(arr, ps, bk, pk, order=2):
    """Derivative in pressure of array defined on hybrid sigma-p coords.

    The array is assumed to be on full (as opposed to half) levels.
    """
    pfull = pfull_from_ps(bk, pk, ps, arr[PFULL_STR])
    return FiniteDiff.cen_diff_deriv(arr, PFULL_STR, coord=pfull, order=order,
                                     do_edges_one_sided=True)


def horiz_gradient_spharm(arr, radius):
    """Horizontal gradient computed spectrally using spherical harmonics."""
    n_lat, n_lon = arr[LAT_STR].size, arr[LON_STR].size
    sph = SpharmInterface(n_lat=n_lat, n_lon=n_lon, rsphere=radius,
                          make_spharmt=True)
    d_dx, d_dy = (sph.spharmt.getgrad(sph.spharmt.grdtospec(
        sph.prep_for_spharm(arr)
    )))
    return sph.to_xarray(d_dx, arr_orig=arr), sph.to_xarray(d_dy, arr_orig=arr)


def horiz_gradient_from_eta_spharm(arr, ps, radius, bk, pk, vec_field=False):
    """Horizontal gradient at constant pressure of `arr`.

    `arr` must be defined on full levels in hybrid sigma-pressure coordinates.
    """
    pfull_coord = arr[PFULL_STR]
    d_dx_const_eta, d_dy_const_eta = horiz_gradient_spharm(arr, radius)
    darr_deta = d_deta_from_pfull(arr)
    bk_at_pfull = to_pfull_from_phalf(bk, pfull_coord)
    da_deta = d_deta_from_phalf(pk, pfull_coord)
    db_deta = d_deta_from_phalf(bk, pfull_coord)
    d_dx_ps, d_dy_ps = horiz_gradient_spharm(ps, radius)
    return (d_dx_const_eta + (darr_deta * bk_at_pfull * d_dx_ps /
                              (da_deta + db_deta*ps)),
            d_dy_const_eta + (darr_deta * bk_at_pfull * d_dy_ps /
                              (da_deta + db_deta*ps)))


def d_dx_from_eta_spharm(arr, ps, radius, bk, pk, vec_field=False):
    """d/dx at constant pressure of `arr`.

    `arr` must be defined on full levels in hybrid sigma-pressure coordinates.
    """
    d_dx, _ = horiz_gradient_from_eta_spharm(arr, ps, radius, bk, pk,
                                             vec_field=vec_field)
    return d_dx


def d_dy_from_eta_spharm(arr, ps, radius, bk, pk, vec_field=False):
    """d/dy at constant pressure of `arr`.

    `arr` must be defined on full levels in hybrid sigma-pressure coordinates.
    """
    _, d_dy = horiz_gradient_from_eta_spharm(arr, ps, radius, bk, pk,
                                             vec_field=vec_field)
    return d_dy
