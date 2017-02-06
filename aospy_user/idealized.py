"""Dry and moist idealized GCM simulations run on Caltech's Fram cluster."""
import os

from aospy import Proj, Model, Run
from aospy.data_loader import DictDataLoader

from . import regions


_ROOT = os.path.join(os.environ['HOME'], 'fms_output')


forcing_max90 = Run(
    name='forcing_max90',
    description='Thermal forcing maximum latitude fixed at 90N',
    data_loader=DictDataLoader(
        data_direc=os.path.join(_ROOT, 'therm_forcing_max_lat_wide_range',
                                'dry_forcing_max_lat_90', 'history'),
        file_map={'monthly': 'day0200h00.nc'},
    )
)


dry_model = Model(
    name='idealized_dry',
    description='Dry dynamical core',
    grid_file_paths=os.path.join(_ROOT, 'therm_forcing_max_lat_wide_range',
                                 'dry_forcing_max_lat_90', 'history',
                                 'day0200h00.nc'),
    runs=[forcing_max90],
)


idealized = Proj(
    'fram',
    direc_out=os.path.join(os.environ['HOME'], 'aospy_output'),
    models=[dry_model],
    regions=(
        regions.globe,
        regions.nh,
        regions.sh,
        regions.tropics,
    )
)
