import numpy as np
import pytest
import xray

from aospy_user import calcs


@pytest.fixture
def tend_first_to_last(arr, freq='1M'):
    return calcs.time_tendency_first_to_last(arr, freq=freq)


@pytest.fixture
def tend_each_timestep(arr):
    return calcs.time_tendency_each_timestep(arr)


def load(var_name):
    path = ('/archive/Spencer.Hill/am2/am2clim_reyoi/gfdl.ncrc2-default-prod/'
            'pp/atmos_level/ts/monthly/1yr/atmos_level.198301-198312.')

    ds = xray.open_dataset(path + var_name + '.nc',
                           drop_variables=['nv', 'time_bounds'])
    return ds[var_name]


def test_tend_each_timestep():
    arr = load('ucomp')
    darr_dt = tend_each_timestep(arr)
    assert darr_dt.shape == arr.shape
    np.testing.assert_array_equal(arr.time.values, darr_dt.time.values)

    # Dummy case: zeros everywhere
    arr_zeros = xray.DataArray(np.zeros_like(arr.values), dims=arr.dims,
                               coords=arr.coords)
    darr_dt = tend_each_timestep(arr_zeros)
    assert not darr_dt.any()
