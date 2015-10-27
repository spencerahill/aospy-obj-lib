"""Functions related to statistical methods."""
import numpy as np
import scipy

from .toa_sfc_fluxes import cre_sw, cre_lw, cre_net, toa_rad_clr


def flatten_spatial_dims(data):
    """Flatten all spatial dimensions of an input array.

    Assumes input array has shape (time, vert, lat, lon).
    """
    n_lon, n_lat, n_lev = data.shape[-1], data.shape[-2], data.shape[-3]
    n_pt = n_lon*n_lat*n_lev
    return data.reshape((-1, n_pt))


def pointwise_corr(x, y):
    """Pointwise Pearson correlation coefficient in time of two arrays.

    Assumes input arrays have shape (time, vert, lat, lon).
    """
    if not np.all(np.shape(x) == np.shape(y)):
        raise ValueError("x and y must have same shapes")
    # pearsonr only accepts 1d arrays.  Must flatten, compute, then reshape.
    orig_shape = np.shape(x)
    x, y = [flatten_spatial_dims(z) for z in (x, y)]
    n_pt = x.shape[-1]
    # pearsonr returns (corr, p_value).  Retain only corr via '[0]'.
    corr = [scipy.stats.pearsonr(x[:, i], y[:, i])[0] for i in range(n_pt)]
    # Reshape to original shape, but dropping the time dimension.
    return np.reshape(corr, orig_shape[1:])


def pointwise_lin_regr(x, y):
    """Pointwise least squares linear regression in time of two arrays.

    Assumes input arrays have shape (time, vert, lat, lon).  The regression is
    of x against y, i.e. the slope returned is m, where y=mx+b.
    """
    if not np.all(np.shape(x) == np.shape(y)):
        raise ValueError("x and y must have same shapes")
    # linregress only accepts 1d arrays.  Must flatten, compute, then reshape.
    orig_shape = np.shape(x)
    x, y = [flatten_spatial_dims(x_) for x_ in (x, y)]
    n_pt = x.shape[-1]
    # linregress returns (slope, ...).  Retain only slope via '[0]'.
    slope = [scipy.stats.linregress(x[:, i], y[:, i])[0] for i in range(n_pt)]
    # Reshape to original shape, but dropping the time dimension.
    return np.reshape(slope, orig_shape[1:])


def corr_cre_sw(swup_toa, swup_toa_clr, var2):
    return pointwise_corr(cre_sw(swup_toa, swup_toa_clr), var2)


def corr_cre_lw(olr, olr_clr, var2):
    return pointwise_corr(cre_lw(olr, olr_clr), var2)


def corr_cre_net(swup_toa, olr, swup_toa_clr, olr_clr, var2):
    return pointwise_corr(cre_net(swup_toa, olr, swup_toa_clr, olr_clr), var2)


def corr_toa_rad_clr(swdn_toa_clr, swup_toa_clr, olr_clr, var2):
    return pointwise_corr(
        toa_rad_clr(swdn_toa_clr, swup_toa_clr, olr_clr), var2
    )


def lin_regr_cre_net(swup_toa, olr, swup_toa_clr, olr_clr, var2):
    return pointwise_lin_regr(
        var2, cre_net(swup_toa, olr, swup_toa_clr, olr_clr)
    )


def lin_regr_toa_rad_clr(swdn_toa_clr, swup_toa_clr, olr_clr, var2):
    return pointwise_lin_regr(
        var2, toa_rad_clr(swdn_toa_clr, swup_toa_clr, olr_clr)
    )
