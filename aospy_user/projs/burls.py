"""Spencer Hill's aospy.Proj object for collaboration w/ Natalie Burls."""
import datetime
import os

from aospy.proj import Proj
from aospy.model import Model
from aospy.run import Run
from aospy_user import regions

_ROOT = os.path.join(os.environ['HOME'], 'Dropbox/projects/gms_natalie_burls')

cam_2xco2 = Run(
    name='2xco2',
    description='Coupled model w/ doubled CO2',
    data_in_direc=os.path.join(_ROOT,' cam_output'),
    data_in_dir_struc='one_dir',
    data_in_dur=1,
    data_in_start_date=datetime.datetime(701, 1, 1),
    data_in_end_date=datetime.datetime(800, 12, 31),
    data_in_files={
        'precip': 'abrupt2xCO2_T31_gx3v7.cam2.h0.0700-01.nc'
        # '*': 'abrupt2xCO2_T31_gx3v7_ANN_climo.701.800.nc'
    }
)


cam = Model(
    name='cam',
    description='NCAR CAM',
    grid_file_paths=os.path.join(
        _ROOT,
        'cam_output/abrupt2xCO2_T31_gx3v7.cam2.h0.0700-01.nc'
        # 'cam_output/abrupt2xCO2_T31_gx3v7_ANN_climo.701.800.nc
    ),
    data_in_dur=1,
    data_in_start_date=datetime.datetime(701, 1, 1),
    data_in_end_date=datetime.datetime(800, 12, 31),
    runs=[cam_2xco2],
)


burls = Proj(
    'burls',
    direc_out=os.path.join(_ROOT, 'aospy_output'),
    nc_dir_struc='one_dir',
    models=[cam],
    regions=(
        regions.globe,
        regions.nh,
        regions.sh,
        regions.tropics,
        regions.wpwp,
        regions.epac,
        regions.sahel,
        regions.sahel2,
        regions.sahel3,
        regions.sahara,
        regions.ind_monsoon,
        regions.land,
        regions.ocean,
        regions.trop_land,
        regions.trop_ocean,
        regions.sahel_south,
        regions.sahel_north,
        regions.sahel_east,
        regions.sahel_west,
        regions.east_asia_monsoon,
        regions.china_east,
        regions.china_west,
    )
)
