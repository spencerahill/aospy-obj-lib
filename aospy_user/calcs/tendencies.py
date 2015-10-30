"""Calculations involved in mass and energy budgets."""
from __future__ import print_function
import numpy as np
from aospy.utils import coord_to_new_dataarray

from .. import TIME_STR


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
    first = arr.resample(freq, TIME_STR, how='first').dropna(TIME_STR)
    last = arr.resample(freq, TIME_STR, how='last').dropna(TIME_STR)
    return (last - first) / first_to_last_vals_dur(arr, freq)
