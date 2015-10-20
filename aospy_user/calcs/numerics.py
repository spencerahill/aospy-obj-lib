"""Finite differencing and other numerical methods."""
import numpy as np

from aospy import FiniteDiff


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
# def fwd_diff1(arr, dim):
#     """1st order accurate forward differencing approximation of derivative.

#     :param arr: Field to take derivative of.
#     :param dim: Values of dimension over which derivative is taken.  If a
#               singleton, assumed to be the uniform spacing.  If an array,
#               assumed to be the values themselves, not the spacing, and must
#               be the same length as `arr`.
#     :out: Array containing the df/dx approximation, with length in the 0th
#           axis one less than that of the input array.
#     """
#     if isinstance(dim, (float, int)):
#         dx = dim
#     else:
#         dx = dim[1:] - dim[:-1]
#     if not np.all(dx):
#         raise ValueError("`dx` has >=1 zero value")
#     return (arr[1:] - arr[:-1]) / dx


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
        return (-arr[2:] +4*arr[1:-1] -3*arr[:-2]) / (2.*dx)
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
