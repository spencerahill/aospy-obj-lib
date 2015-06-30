#!/usr/bin/env python
"""Create netCDF files for use as GCM input data."""
import datetime
import os

import netCDF4
import numpy as np
import scipy.interpolate

from aospy.region import regions
from aospy.var import variables

def pivot_index(longitudes):
    """Get index where longitudes change sign."""
    return np.where(np.diff(np.sign(longitudes)))[0][0] + 1


def pivot_data(data, pivot_ind, axis=None):
    """
    Pivot data so that its longitude ranges from 0 to 360.
    Designed to mimic the 'lonPivot' function of NCL.
    """
    return np.roll(data, -pivot_ind, axis=axis)


    coarsened = scipy.interpolate.RectBivariateSpline(
        lat, lon, data_in, kx=1, ky=1
    )


def create_anom(gcminputs, function):
    """Combine data from two netCDF files using the supplied function."""
    arrays = []
    for (path, var) in zip(paths, vars_):
        with netCDF4.Dataset(path, 'r') as nc:
            arrays.append(nc.variables[var])

    if operator:
         operator(*arrays)
    else:
        return arrays


def to_am2_input_time_format(sst, start_month=11, num_months=207):
    """Convert a 12 month climatology file into AM2 SST input format."""
    if start_month == 0:
        offset = 0
    else:
        offset = 13 - start_month
    num_mon_offset = int(num_months - offset)
    num_full_years = num_mon_offset / 12
    num_extra_months = num_mon_offset % 12
    sst_ts1 = sst[(start_month - 1):]
    sst_ts2 = np.tile(sst, (num_full_years, 1, 1))
    sst_ts3 = sst[:num_extra_months]
    return np.vstack((sst_ts1, sst_ts2, sst_ts3, sst,
                      sst.mean(axis=0)[np.newaxis,:]))


def copy_ncattr(new_nc_obj, old_nc_obj, attr_name):
    """Copy a netCDF attribute from an old to a new object."""
    try:
        attr_val = getattr(old_nc_obj, attr_name)
    except AttributeError:
        pass
    else:
        setattr(new_nc_obj, attr_name, attr_val)

def main():

    return

# "Pivot" the longitudes to span 0 to 360 degrees.
pivot_index = get_pivot_index(lon_cont)
lon_cont_pivoted = pivot_data(lon_cont, pivot_index)
lon_cont_pivoted[(360 - pivot_index):] += 360.
sst_anom_pivoted = pivot_data(sst_anom_in, pivot_index, axis=-1)

# Take monthly averages.
num_yr = 20
sst_anom_monthly = sst_anom_pivoted.reshape((num_yr, 12, lat_cont.size,
                                             lon_cont.size)).mean(axis=0)

# Load the climatological SST field, lat, lon, etc.
sst_clim = nc_clim.variables[sst_clim_name]

# Interpolate from the native SST grid to the desired one.
sst_anom_interp = np.empty((12, sst_clim.shape[-2], sst_clim.shape[-1]))
for t in range(12):
    sst_anom_spline = scipy.interpolate.RectBivariateSpline(
        lat_cont, lon_cont_pivoted, sst_anom_monthly[t], kx=1, ky=1
    )
    sst_anom_interp[t] = sst_anom_spline(lat_clim[:], lon_clim[:])

# Apply desired regional mask to the reinterpolated data.
    region = getattr(regions, region_name)
    region_mask = \
        np.tile(region.make_mask_from_lat_lon(lat_clim[:], lon_clim[:]),
                (12, 1, 1))
    if invert_mask:
        region_mask = 1. - region_mask
    sst_anom_masked = np.where(region_mask, 0., sst_anom_interp)
else:
    sst_anom_masked = sst_anom_interp

# Add the anomalies to the climatology.  For AM2, add the anomalies to
# the full monthly time series, the monthly means, and the annual
# mean, and then combine those three into one array.
am2_format_start_month = 11
am2_format_num_month = 207

if time_format_in == 'am2' and time_format_out == 'am2':
    sst_anom_month_ts = sst_clim[:-13]
    for t in range(12):
        sst_anom_month_ts[t::12] += sst_anom_masked[t]
    sst_anom_month_av = sst_clim[-13:-1] + sst_anom_masked
    sst_anom_ann_av = sst_clim[-1] + sst_anom_masked.mean(axis=0)
    sst_full = np.vstack((sst_anom_month_ts, sst_anom_month_av,
                          sst_anom_ann_av[np.newaxis,:]))

elif time_format_out == 'am2':
    sst_clim_am2format = to_am2_input_time_format(
        sst_clim[:], start_month=am2_format_start_month,
        num_months=am2_format_num_month
    )
    sst_anom_am2format = to_am2_input_time_format(
        sst_anom_masked, start_month=am2_format_start_month,
        num_months=am2_format_num_month
    )
    sst_full = sst_clim_am2format + sst_anom_am2format - 273.15

else:
    sst_full = sst_clim[:] + sst_anom_masked

# Store the new SST field in a new netCDF file.
name_out_tag = ''
if do_mask:
    name_out_tag += region_name
if anom != 0:
    plus_sign = '+' if anom > 0 else ''
    if anom % 1 == 0:
        anom_tag = str(int(anom))
    else:
        anom_tag = str(anom)
    name_out_tag += plus_sign + anom_tag + "K"
if do_am2_format:
    name_out_tag += '.am2format'

nc_out_dir = '/'.join([nc_out_base_dir, dir_out_name,
                       '']).replace('//', '/')
if not os.path.isdir(nc_out_dir):
    os.mkdir(nc_out_dir)
nc_out_path = nc_out_dir + '.'.join([name_out_prefix, name_out_tag,
                                     'nc']).replace('..', '.')
print "New SST data saved to:", nc_out_path
nc_out = netCDF4.Dataset(nc_out_path, 'w', format=nc_clim.file_format)
nc_out.createDimension(time_dim_clim_name, None)
nc_out.createDimension(lat_dim_clim_name, lat_clim.size)
nc_out.createDimension(lon_dim_clim_name, lon_clim.size)
nc_out.createDimension(idim_clim_name, time_clim.size)
time_out = nc_out.createVariable(time_clim_name, time_clim[:].dtype,
                                 (time_dim_clim_name,))
lat_out = nc_out.createVariable(lat_clim_name, lat_clim[:].dtype,
                                (lat_dim_clim_name,))
lon_out = nc_out.createVariable(lon_clim_name, lon_clim[:].dtype,
                                (lon_dim_clim_name,))
if model == 'am2':
    sst_out = nc_out.createVariable(
        sst_clim_name, sst_clim[:].dtype,
        (time_dim_clim_name, lat_dim_clim_name, lon_dim_clim_name))
elif model == 'am3':
    sst_out = nc_out.createVariable(
        sst_clim_name, sst_clim[:].dtype,
        (time_dim_clim_name, lat_dim_clim_name, lon_dim_clim_name),
        fill_value=fill_value
        )
num_records_out = nc_out.createVariable(num_records_clim_name,
                                        num_records_clim[:].dtype)
year_out = nc_out.createVariable(year_clim_name, year_clim[:].dtype,
                                 (idim_clim_name,))
month_out = nc_out.createVariable(month_clim_name, month_clim[:].dtype,
                                  (idim_clim_name,))
day_out = nc_out.createVariable(day_clim_name, day_clim[:].dtype,
                                (idim_clim_name,))

try:
    T1_out = nc_out.createVariable(T1_clim_name, T1_clim[:].dtype,
                                   (time_clim_name,))
    T2_out = nc_out.createVariable(T2_clim_name, T2_clim[:].dtype,
                                   (time_clim_name,))
    DT_out = nc_out.createVariable(DT_clim_name, DT_clim[:].dtype,
                                   (time_clim_name,))
except:
    pass
nc_out.description = ("Spencer Hill " +
                      datetime.date.today().strftime("%Y-%m-%d"))

# Copy attributes from climatology netCDF file to the new netCDF file.
for pair in (
        (time_out, time_clim), (lat_out, lat_clim), (lon_out, lon_clim),
        (sst_out, sst_clim), (year_out, year_clim),
        (month_out, month_clim), (day_out, day_clim)
        # (T1_out, T1_clim), (T2_out, T2_clim), (DT_out, DT_clim)
):
    for attr_name in ('units', 'long_name', 'calendar', 'missing_value',
                      'time_origin', 'axis', 'modulo',
                      'point_spacing', 'history', 'time_avg_info'):
        copy_ncattr(pair[0], pair[1], attr_name)

# Copy data values into new netCDF variables.
time_out[:] = time_clim[:]
lat_out[:] = lat_clim[:]
lon_out[:] = lon_clim[:]
sst_out[:] = sst_full
num_records_out[:] = num_records_clim[:]
year_out[:] = year_clim[:]
month_out[:] = month_clim[:]
day_out[:] = day_clim[:]
try:
    T1_out[:] = T1_clim[:]
    T2_out[:] = T2_clim[:]
    DT_out[:] = DT_clim[:]
except:
    pass

# Close the netCDF file.
nc_out.close()
nc_clim.close()


class GCMInput(object):
    """Container for creating input netCDF files for GCM simulations."""
    def __init__(self, path, var_name):
        self.path = path
        self.var_name = var_name

        try:
            self.Var = aospy.var.var_inst(var_name)
        except AttributeError:
            raise AttributeError

        with netCDF4.Dataset(self.path, 'r') as nc:


if __name__ == '__main__':
    path_anom = ('/archive/yim/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie2_rerun6'
                 '.YIM/pp/ocean/ts/monthly/20yr/ocean.006101-008012.SST.nc')
    path_cont = ('/archive/yim/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie_rerun6'
                 '.YIM/pp/ocean/ts/monthly/20yr/ocean.006101-008012.SST.nc')
    var_anom = 'sst'
    var_cont = 'sst'

    anom = GCMInput(path_anom, var_anom)
    cont = GCMInput(path_cont, var_cont)
    nc_base_path = '/net/yim/sst/reyoi_sst.data.nc' # AM2.1
    # nc_base_path = '/net/yim/sst/sst.climo.1981-2000.data.nc' # AM3
    # nc_base_path = '/net/yim/sst/HadISST_sst.nc' # HiRAM

    time_format_in = 'am2'
    time_format_out = 'am2'
    mask_regional = False
    mask_invert = False

    outdir = "/home/s1h/sst/"

    main()
