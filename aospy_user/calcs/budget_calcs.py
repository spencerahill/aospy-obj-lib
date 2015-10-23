"""Calculations involved in mass and energy budgets."""
import numpy as np

from aospy.utils import (apply_time_offset, coord_to_new_dataarray,
                         to_pfull_from_phalf, d_deta_from_pfull,
                         d_deta_from_phalf)

PFULL_STR = 'pfull'
TIME_STR = 'time'


def first_to_last_vals_dur(arr, freq='1M'):
    """Time elapsed between 1st and last values in each given time period."""
    time = coord_to_new_dataarray(arr, TIME_STR)
    first = time.resample(freq, TIME_STR, how='first')
    last = time.resample(freq, TIME_STR, how='last')
    delta_time = last - first
    # Divide by a 1 sec timedelta to convert to seconds.
    delta_time.values = delta_time.values / np.timedelta64(1, 's')
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
