"""aospy.Run objects for simulations from the GFDL HiRAM model."""
import datetime

from aospy import Run
from aospy.data_loader import GFDLDataLoader


hiram_cont = Run(
    name='cont',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs '
        'and sea ice repeated annually, with PD atmospheric composition.'
    ),
    data_loader=GFDLDataLoader(
        data_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim/'
                    'gfdl.ncrc2-default-prod/pp'),
        data_start_date=datetime.datetime(1979, 1, 1),
        data_end_date=datetime.datetime(1995, 12, 31),
    ),
)
hiram_aero = Run(
    name='aero',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and '
        'sea ice repeated annually, overlaid with annual cycle of '
        'equilibrium SST anomalies from a PI-to-PD aerosols '
        'simulation of AM2.1 with a mixed layer ocean.  '
        'PD atmospheric composition.'
    ),
    data_loader=GFDLDataLoader(
        template=hiram_cont.data_loader,
        data_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim_aero/'
                    'gfdl.ncrc2-default-prod/pp'),
    ),
)
hiram_atm = Run(
    name='aero_tm',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid with annual tropical mean equilibrium '
        'SST anomaly from a PI-to-PD aerosols simulation of AM2.1 with a '
        'mixed layer ocean.  PD atmospheric composition.'
    ),
    data_loader=GFDLDataLoader(
        template=hiram_cont.data_loader,
        data_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim_aero_'
                    'trop_mean/gfdl.ncrc2-default-prod/pp'),
    ),
)
hiram_amtm = Run(
    name='aero_mtm',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, subtracting annual tropical mean equilibrium SST '
        'anomaly from a PI-to-PD aerosols simulation of AM2.1 with a mixed '
        'layer ocean.  PD atmospheric composition.'
    ),
    data_loader=GFDLDataLoader(
        template=hiram_cont.data_loader,
        data_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim_aero_m_'
                    'trop_mean/gfdl.ncrc2-default-prod/pp'),
    ),
)
hiram_apac = Run(
    name='aero_pac',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid in Pacific Ocean only with annual cycle '
        'of equilibrium SST anomalies from a PI-to-PD aerosols simulation of '
        'AM2.1 with a mixed layer ocean.  PD atmospheric composition.'
    ),
    data_loader=GFDLDataLoader(
        template=hiram_cont.data_loader,
        data_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim_aero_pac/'
                    'gfdl.ncrc2-default-prod/pp'),
    ),
)
hiram_aatl = Run(
    name='aero_atl',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid in Atlantic Ocean only with annual cycle '
        'of equilibrium SST anomalies from a PI-to-PD aerosols simulation of '
        'AM2.1 with a mixed layer ocean.  PD atmospheric composition.'
    ),
    data_loader=GFDLDataLoader(
        template=hiram_cont.data_loader,
        data_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim_aero_atl/'
                    'gfdl.ncrc2-default-prod/pp'),
    ),
)
hiram_aind = Run(
    name='aero_ind',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid in Indian Ocean only with annual cycle '
        'of equilibrium SST anomalies from a PI-to-PD aerosols simulation of '
        'M2.1 with a mixed layer ocean. PD atmospheric composition.'
    ),
    data_loader=GFDLDataLoader(
        template=hiram_cont.data_loader,
        data_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim_aero_ind/'
                    'gfdl.ncrc2-default-prod/pp'),
    ),
)
hiram_gas = Run(
    name='gas',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and '
        'sea ice repeated annually, overlaid with annual cycle of '
        'equilibrium SST anomalies from a PI-to-PD WMGG and ozone '
        'simulation of AM2.1 with a mixed layer ocean.  '
        'PD atmospheric composition.'
    ),
    data_loader=GFDLDataLoader(
        template=hiram_cont.data_loader,
        data_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim_gas_rerun2/'
                    'gfdl.ncrc2-default-prod/pp'),
    ),
)
hiram_gtm = Run(
    name='gas_tm',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea '
        'ice repeated annually, overlaid with annual tropical mean '
        'equilibrium SST anomaly from a PI-to-PD WMGG and ozone simulation '
        'of AM2.1 with a mixed layer ocean. PD atmospheric composition.'
        ),
    data_loader=GFDLDataLoader(
        template=hiram_cont.data_loader,
        data_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim_gas_'
                    'trop_mean/gfdl.ncrc2-default-prod/pp'),
    ),
)
hiram_gmtm = Run(
    name='gas_mtm',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice'
        'repeated annually, overlaid with annual cycle of equilibrium SST'
        'anomalies minus their annual tropical mean from a PI-to-PD WMGG &'
        'ozone simulation of AM2.1 with a mixed layer ocean. PD atmos'
        'composition.'
    ),
    data_loader=GFDLDataLoader(
        template=hiram_cont.data_loader,
        data_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim_gas_m_'
                    'trop_mean/gfdl.ncrc2-default-prod/pp'),
    ),
)
# hiram_amip = Run(
#     name='amip',
#     ens_mem_prefix='/archive/hrao/ornl/cmip5/c180_hiram_',
#     ens_mem_ext=['H1', 'H3'],
#     ens_mem_suffix='/pp',
#     data_dur=5,
#     data_start_date=datetime.datetime(1979, 1, 1),
#     data_end_date=datetime.datetime(2008, 12, 31),
#     data_dir_struc='gfdl'
# )
