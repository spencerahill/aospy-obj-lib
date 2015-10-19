"""Finite differencing and other numerical methods."""
import numpy as np

from aospy import FiniteDiff


def fwd_diff1(fx, x):
    """1st order accurate forward differencing approximation of derivative.

    :param fx: Field to take derivative of.
    :param x: Values of dimension over which derivative is taken.  If a
              singleton, assumed to be the uniform spacing.  If an array,
              assumed to be the values themselves, not the spacing, and must
              be the same length as `fx`.
    :out: Array containing the df/dx approximation, with length in the 0th
          axis one less than that of the input array.
    """
    if isinstance(x, (float, int)):
        dx = x
    else:
        dx = x[1:] - x[:-1]
    if not np.all(dx):
        raise ValueError("`dx` has >=1 zero value")
    return (fx[1:] - fx[:-1]) / dx


def fwd_diff2(fx, x):
    """2nd order accurate forward differencing approximation of derivative.

    :param fx: Field to take derivative of.
    :param x: Values of dimension over which derivative is taken.  If a
              singleton, assumed to be the uniform spacing.  If an array,
              assumed to be the values themselves, not the spacing, and must
              be the same length as `fx`.
    :out: Array containing the df/dx approximation, with length in the 0th
          axis two less than that of the input array.
    """
    if isinstance(x, (float, int)):
        dx = x
        return (-fx[2:] +4*fx[1:-1] -3*fx[:-2]) / (2.*dx)
    else:
        df_dx1 = (fx[1:-1] - fx[:-2]) / (x[1:-1] - x[:-2])
        df_dx2 = (fx[2:]   - fx[:-2]) / (x[2:]   - x[:-2])
        return 2.*df_dx1 - df_dx2


def cen_diff2(fx, x):
    fd = FiniteDiff(fx, positions=x)
    return fd.cen_diff_deriv(order=2)


def cen_diff4(fx, x):
    """4th order accurate centered differencing."""
    if isinstance(x, (float, int)):
        dx = x
        return (8*(fx[3:-1] - fx[1:-3]) - (fx[4:] - fx[:-4])) / (12.*dx)
    else:
        df_dx1 = (fx[3:-1] - fx[1:-3]) / (x[3:-1] - x[1:-3])
        df_dx2 = (fx[4:] - fx[:-4]) / (x[4:] - x[:-4])
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
