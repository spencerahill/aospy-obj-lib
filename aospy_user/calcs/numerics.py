"""Finite differencing and other numerical methods."""
from animal_spharm import SpharmInterface
from aospy.utils import (d_deta_from_pfull, d_deta_from_phalf, pfull_from_ps,
                         to_pfull_from_phalf, to_radians)
from infinite_diff import FiniteDiff
import numpy as np
import xray

from .. import LAT_STR, LON_STR, PFULL_STR, PLEVEL_STR


def fwd_diff2(arr, dim):
    """2nd order accurate forward differencing approximation of derivative.

    :param arr: Field to take derivative of.
    :param dim: Values of dimension over which derivative is taken.  If a
              singleton, assumed to be the uniform spacing.  If an array,
              assumed to be the values themselves, not the spacing, and must
              be the same length as `arr`.
    :out: Array containing the df/dx approximation, with length in the 0th
          axis two less than that of the input array.
    """
    if isinstance(dim, (float, int)):
        dx = dim
        return (-arr[2:] + 4*arr[1:-1] - 3*arr[:-2]) / (2.*dx)
    else:
        df_dx1 = (arr[1:-1] - arr[:-2]) / (dim[1:-1] - dim[:-2])
        df_dx2 = (arr[2:]   - arr[:-2]) / (dim[2:]   - dim[:-2])
        return 2.*df_dx1 - df_dx2


def cen_diff4(arr, dim):
    """4th order accurate centered differencing."""
    if isinstance(dim, (float, int)):
        dx = dim
        return (8*(arr[3:-1] - arr[1:-3]) - (arr[4:] - arr[:-4])) / (12.*dx)
    else:
        df_dx1 = (arr[3:-1] - arr[1:-3]) / (dim[3:-1] - dim[1:-3])
        df_dx2 = (arr[4:] - arr[:-4]) / (dim[4:] - dim[:-4])
        return (8.*df_dx1 - df_dx2) / 12.


def upwind_scheme(df_fwd, df_bwd, a):
    """Upwind differencing scheme for advection.

    :param df_fwd: Forward difference of the field.
    :param df_bwd: Backard difference of the field.
    :param a: Flow that is advecting the field `f`.
    """
    a_pos = np.ma.where(a >= 0., a, 0)
    a_neg = np.ma.where(a < 0., a, 0)
    return a_pos*df_bwd + a_neg*df_fwd


# Functions for derivatives in x, y, and p.
def latlon_deriv_prefactor(lat, radius, radians=True,
                           d_dy_of_scalar_field=False):
    """Factor that multiplies del operations in spherical coordinates."""
    if d_dy_of_scalar_field:
        return 1. / radius
    else:
        lat_rad = lat if radians else np.deg2rad(lat)
        return 1. / (radius*np.cos(lat_rad))


def wraparound_lon(arr, n=1, radians=True):
    """Append wrap-around points in longitude to the DataArray or Dataset.

    The longitude arraymust span from 0 to 360.  While this will usually be the
    case, it's not guaranteed.  Some pre-processing step should be implemented
    in the future that forces this to be the case.
    """
    circumf = 2*np.pi if radians else 360.
    edge_left = arr.isel(**{LON_STR: 0})
    edge_left[LON_STR] += circumf
    edge_right = arr.isel(**{LON_STR: -1})
    edge_right[LON_STR] -= circumf
    return xray.concat([edge_right, arr, edge_left], dim=LON_STR)


def d_dx_from_latlon(arr, radius):
    """Compute \partial arr/\partial x using centered differencing."""
    lon_rad = to_radians(arr[LON_STR])
    prefactor = latlon_deriv_prefactor(arr[LAT_STR], radius, radians=False)
    arr_ext = wraparound_lon(arr, n=1, radians=False)
    lon_rad = to_radians(arr_ext[LON_STR])
    darr_dx = (FiniteDiff.cen_diff(arr_ext, LON_STR, is_coord=False) /
               FiniteDiff.cen_diff(lon_rad, LON_STR, is_coord=False))
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
        FiniteDiff.cen_diff(lat_rad, LAT_STR, do_edges_one_sided=True,
                            is_coord=False)
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
    d_dy_ps = d_dy_from_lat(ps, radius, vec_field=False)

    return d_dy_const_eta + (darr_deta*bk_at_pfull * d_dy_ps /
                             (da_deta + db_deta*ps))


def d_dp_from_p(arr, p):
    """Derivative in pressure of array defined on fixed pressure levels."""
    return FiniteDiff.cen_diff_deriv(arr, PLEVEL_STR, do_edges_one_sided=True)


def d_dp_from_eta(arr, ps, bk, pk):
    """Derivative in pressure of array defined on hybrid sigma-p coords.

    The array is assumed to be on full (as opposed to half) levels.
    """
    pfull = pfull_from_ps(bk, pk, ps, arr[PFULL_STR])
    return (FiniteDiff.cen_diff(arr, PFULL_STR, do_edges_one_sided=True) /
            FiniteDiff.cen_diff(pfull, PFULL_STR, do_edges_one_sided=True))


def horiz_gradient_spharm(arr, radius):
    """Horizontal gradient computed spectrally using spherical harmonics."""
    n_lat, n_lon = arr[LAT_STR].size, arr[LON_STR].size
    sph = SpharmInterface(n_lat=n_lat, n_lon=n_lon, rsphere=radius,
                          make_spharmt=True)
    d_dx, d_dy = (sph.spharmt.getgrad(sph.spharmt.grdtospec(
        sph.prep_for_spharm(arr)
    )))
    return sph.to_xray(d_dx, arr_orig=arr), sph.to_xray(d_dy, arr_orig=arr)


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
