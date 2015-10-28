"""Finite differencing and other numerical methods."""
from aospy import FiniteDiff
from aospy.utils import pfull_from_ps, to_radians
import numpy as np
import xray

from .. import LAT_STR, LON_STR, PFULL_STR, PLEVEL_STR


def fwd_diff1(arr, dim):
    """1st order accurate forward differencing approximation of derivative.

    :param arr: Field to take derivative of.
    :param dim: Values of dimension over which derivative is taken.  If a
              singleton, assumed to be the uniform spacing.  If an array,
              assumed to be the values themselves, not the spacing, and must
              be the same length as `arr`.
    :out: Array containing the df/dx approximation, with length in the 0th
          axis one less than that of the input array.
    """
    return FiniteDiff.fwd_diff_deriv(arr, dim)


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


def cen_diff2(arr, dim):
    return FiniteDiff.cen_diff_deriv(arr, dim, order=2,
                                     do_edges_one_sided=True)


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
def latlon_deriv_prefactor(lat, radius, d_dy_of_scalar_field=False):
    """Factor that multiplies del operations in spherical coordinates."""
    if d_dy_of_scalar_field:
        return 1. / radius
    else:
        return 1. / (radius*np.cos(to_radians(lat)))


def wraparound_lon(arr, num=1):
    """Append wrap-around points in longitude to the DataArray or Dataset.

    The longitude arraymust span from 0 to 360.  While this will usually be the
    case, it's not guaranteed.  Some pre-processing step should be implemented
    in the future that forces this to be the case.
    """
    edge_left = arr.isel(**{LON_STR: 0})
    edge_left[LON_STR] += 360.
    edge_right = arr.isel(**{LON_STR: -1})
    edge_right[LON_STR] -= 360.
    return xray.concat([edge_right, arr, edge_left], dim=LON_STR)


def d_dx_from_latlon(arr, radius):
    """Compute \partial arr/\partial x using centered differencing."""
    prefactor = latlon_deriv_prefactor(to_radians(arr.coords[LAT_STR]),
                                       radius, d_dy_of_scalar_field=False)
    arr_ext = wraparound_lon(arr)
    darr_dx = FiniteDiff.cen_diff_deriv(arr_ext, LON_STR,
                                        do_edges_one_sided=False)
    return prefactor*darr_dx


def d_dy_from_lat(arr, radius, vec_field=False):
    """Compute \partial(field)/\partial y using centered differencing."""
    lat = to_radians(arr.coords[LAT_STR])
    prefactor = latlon_deriv_prefactor(lat, radius,
                                       d_dy_of_scalar_field=(not vec_field))
    if vec_field:
        arr *= np.cos(lat)
    darr_dy = FiniteDiff.cen_diff_deriv(arr, LAT_STR, do_edges_one_sided=True)
    return prefactor*darr_dy


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
