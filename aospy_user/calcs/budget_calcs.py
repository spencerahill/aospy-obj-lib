"""Calculations involved in mass and energy budgets."""
import numpy as np
import pandas as pd
import xray

TIME_STR = 'time'


def apply_time_offset(time, hours):
    """Apply the given offset to the given time array.

    This is useful for GFDL model output of instantaneous values.  For example,
    3 hourly data postprocessed to netCDF files spanning 1 year each will
    actually have time values that are offset by 3 hours, such that the first
    value is for 1 Jan 03:00 and the last value is 1 Jan 00:00 of the
    subsequent year.  This causes problems in xray, e.g. when trying to group
    by month.  It is resolved by manually subtracting off those three hours,
    such that the dates span from 1 Jan 00:00 to 31 Dec 21:00 as desired.
    """
    return (pd.to_datetime(time.values) +
            pd.tseries.offsets.DateOffset(hours=hours))


def monthly_mean_ts(arr):
    """Convert a sub-monthly time-series into one of monthly means."""
    return arr.resample('1M', TIME_STR, how='mean')


def first_to_last_vals_dur(arr, freq='1M'):
    """Time elapsed between 1st and last values in each given time period."""
    time = xray.DataArray(arr[TIME_STR].values,
                          coords=[arr[TIME_STR].values],
                          dims=[TIME_STR])
    first = time.resample(freq, TIME_STR, how='first')
    last = time.resample(freq, TIME_STR, how='last')
    delta_time = last - first
    # Divide by a 1 sec timedelta to convert to seconds.
    delta_time.values = delta_time.values / np.timedelta64
    return delta_time


def time_tendency(arr, freq='1M'):
    """Monthly time tendency of the given field."""
    first = arr.resample(freq, TIME_STR, how='first')
    last = arr.resample(freq, TIME_STR, how='last')
    return (last - first) / first_to_last_vals_dur(arr, freq)


def time_tendency_gfdl(arr, hours=3):
    """Compute the time tendency of GFDL output, which requires time offset.

    See `apply_time_offset` docstring for more info re: GFDL data.
    """
    arr[TIME_STR] = apply_time_offset(arr[TIME_STR], hours)
    return time_tendency(arr)


def horiz_grad(field):
    raise NotImplementedError


def dfield_deta(field):
    raise NotImplementedError


def phalf_to_pfull(field):
    raise NotImplementedError


def horiz_grad_at_const_p_from_eta(field, bk, pk, ps):
    """Horizontal gradient at constant pressure of scalar field.

    Field is presumably defined in some other coordinates, typically
    model-native (e.g. sigma or hybrid sigma-pressure) coordinates.
    """
    horiz_grad_eta = horiz_grad(field)
    df_deta = dfield_deta(field)
    bk_at_pfull = phalf_to_pfull(bk)
    da_deta = dfield_deta(pk)
    db_deta = dfield_deta(bk)
    horiz_grad_ps = horiz_grad(ps)

    return horiz_grad_eta + (df_deta*bk_at_pfull * horiz_grad_ps /
                             (da_deta + db_deta*ps))
