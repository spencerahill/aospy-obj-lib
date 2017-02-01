"""aospy.Run objects for the CMIP5 Project."""
import datetime

from aospy import Run

onepctCO2 = Run(
    name='1pctCO2',
    description='Coupled; 1% increase in CO2 per year from PI',
)
abrupt4xCO2 = Run(
    name='abrupt4xCO2',
    description='Coupled; Instantaneous 4X CO2 increase',
)
amip = Run(
    name='amip',
    description='Atmosphere only',
    # data_direc='mon/atmos/Amon/r1i1p1',
    # data_dir_struc='gfdl_repo',
    default_start_date=datetime.datetime(1979, 1, 1),
    default_end_date=datetime.datetime(2008, 12, 31),
)
amip4K = Run(
    name='amip4K',
    description='Atmosphere only',
    # data_direc='mon/atmos/Amon/r1i1p1',
    # data_dir_struc='gfdl_repo',
    default_start_date=datetime.datetime(1979, 1, 1),
    default_end_date=datetime.datetime(2008, 12, 31),
)
amip4xCO2 = Run(
    name='amip4xCO2',
    description='Atmosphere only',
    default_start_date=datetime.datetime(1979, 1, 1),
    default_end_date=datetime.datetime(2008, 12, 31),
)
amipFuture = Run(
    name='amipFuture',
    description='Atmosphere only',
    default_start_date=datetime.datetime(1979, 1, 1),
    default_end_date=datetime.datetime(2008, 12, 31),
)
historical = Run(
    name='historical',
    description='Coupled',
)
rcp26 = Run(
    name='rcp26',
    description='Coupled',
)
rcp45 = Run(
    name='rcp45',
    description='Coupled',
)
rcp60 = Run(
    name='rcp60',
    description='Coupled',
)
rcp86 = Run(
    name='rcp86',
    description='Coupled',
)
sstClim = Run(
    name='sstClim',
    description='Atmosphere only',
)
sstClim4xCO2 = Run(
    name='sstClim4xCO2',
    description='Atmosphere only',
)
aquaControl = Run(
    name='aquaControl',
    description='Atmosphere only',
)
aqua4K = Run(
    name='aqua4K',
    description='Atmosphere only',
)
aqua4xCO2 = Run(
    name='aqua4xCO2',
    description='Atmosphere only',
)
