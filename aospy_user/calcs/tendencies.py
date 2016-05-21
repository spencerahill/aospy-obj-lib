"""Calculations involved in mass and energy budgets."""
from infinite_diff import CenDeriv
import numpy as np

from .. import TIME_STR


def first_to_last_vals_dur(arr, freq='1M'):
    """Time elapsed between 1st and last values in each given time period."""
    time = arr[TIME_STR]
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


def cen_diff_time(arr):
    """Time centered differencing"""
    time = arr[TIME_STR].copy()
    # Force time units to be seconds.
    time = (time - np.datetime64(0, 's')) / np.timedelta64(1, 's')
    return CenDeriv(arr, TIME_STR, coord=time, fill_edge=True).deriv()


def time_tendency_each_timestep(arr):
    """Time tendency of the given field at each timestep.

    Compute via centered differencing at interior timesteps, one-sided
    differencing at endpoints.
    """
    return arr.groupby('time.year').apply(cen_diff_time)
