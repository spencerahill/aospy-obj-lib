"""Calculations involved in mass and energy budgets."""
from aospy.utils import coord_to_new_dataarray
from infinite_diff import FiniteDiff
import numpy as np

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


def time_tendency_first_to_last(arr, freq='1M'):
    """Time tendency of the given field over given time interval."""
    first = arr.resample(freq, TIME_STR, how='first').dropna(TIME_STR)
    last = arr.resample(freq, TIME_STR, how='last').dropna(TIME_STR)
    return (last - first) / first_to_last_vals_dur(arr, freq)


def time_tendency_each_timestep(arr):
    """Time tendency of the given field at each timestep.

    Compute via centered differencing at interior timesteps, one-sided
    differencing at endpoints.
    """
    time = arr[TIME_STR].copy()
    # Force time units to be seconds.
    time = (time - np.datetime64(0, 's')) / np.timedelta64(1, 's')
    return (FiniteDiff.cen_diff(arr, TIME_STR, do_edges_one_sided=True) /
            FiniteDiff.cen_diff(time, TIME_STR, do_edges_one_sided=True))
