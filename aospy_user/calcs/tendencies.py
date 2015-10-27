"""Calculations involved in mass and energy budgets."""
import numpy as np
from aospy.constants import grav
from aospy.utils import coord_to_new_dataarray, int_dp_g

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
    first = arr.resample(freq, TIME_STR, how='first')
    last = arr.resample(freq, TIME_STR, how='last')
    return (last - first) / first_to_last_vals_dur(arr, freq)


def wvp_time_tendency(q, dp, freq='1M'):
    """Time tendency of water vapor path."""
    return time_tendency(int_dp_g(q, dp), freq=freq)


def mass_budget_tendency_term(ps, q, dp, freq='1M'):
    """Combined time-tendency term in column mass budget equation.

    See e.g. Trenberth 1991, Eq. 9.
    """
    return (time_tendency(ps, freq=freq) -
            grav.value * wvp_time_tendency(q, dp, freq=freq))
