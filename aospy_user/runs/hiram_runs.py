"""aospy.Run objects for simulations from the GFDL HiRAM model."""
from aospy import Run

hiram_cont = Run(
    name='cont',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs '
        'and sea ice repeated annually, with PD atmospheric composition.'
    ),
    data_in_start_date=1979,
    data_in_end_date=1995,
    default_date_range=(1979, 1995),
    data_in_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim/'
                   'gfdl.ncrc2-default-prod/pp')
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
    data_in_start_date=1979,
    data_in_end_date=1995,
    default_date_range=(1979, 1995),
    data_in_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim_aero/'
                   'gfdl.ncrc2-default-prod/pp')
)
hiram_atm = Run(
    name='aero_tm',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid with annual tropical mean equilibrium '
        'SST anomaly from a PI-to-PD aerosols simulation of AM2.1 with a '
        'mixed layer ocean.  PD atmospheric composition.'
    ),
    data_in_start_date=1979,
    data_in_end_date=1995,
    default_date_range=(1979, 1995),
    data_in_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim_aero_'
                   'trop_mean/gfdl.ncrc2-default-prod/pp')
)
hiram_amtm = Run(
    name='aero_mtm',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, subtracting annual tropical mean equilibrium SST '
        'anomaly from a PI-to-PD aerosols simulation of AM2.1 with a mixed '
        'layer ocean.  PD atmospheric composition.'
    ),
    data_in_start_date=1979,
    data_in_end_date=1995,
    default_date_range=(1979, 1995),
    data_in_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim_aero_m_'
                   'trop_mean/gfdl.ncrc2-default-prod/pp')
)
hiram_apac = Run(
    name='aero_pac',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid in Pacific Ocean only with annual cycle '
        'of equilibrium SST anomalies from a PI-to-PD aerosols simulation of '
        'AM2.1 with a mixed layer ocean.  PD atmospheric composition.'
    ),
    data_in_start_date=1979,
    data_in_end_date=1995,
    default_date_range=(1979, 1995),
    data_in_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim_aero_pac/'
                   'gfdl.ncrc2-default-prod/pp')
)
hiram_aatl = Run(
    name='aero_atl',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid in Atlantic Ocean only with annual cycle '
        'of equilibrium SST anomalies from a PI-to-PD aerosols simulation of '
        'AM2.1 with a mixed layer ocean.  PD atmospheric composition.'
    ),
    data_in_start_date=1979,
    data_in_end_date=1995,
    default_date_range=(1979, 1995),
    data_in_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim_aero_atl/'
                   'gfdl.ncrc2-default-prod/pp')
)
hiram_aind = Run(
    name='aero_ind',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid in Indian Ocean only with annual cycle '
        'of equilibrium SST anomalies from a PI-to-PD aerosols simulation of '
        'M2.1 with a mixed layer ocean. PD atmospheric composition.'
    ),
    data_in_start_date=1979,
    data_in_end_date=1995,
    default_date_range=(1979, 1995),
    data_in_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim_aero_ind/'
                   'gfdl.ncrc2-default-prod/pp')
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
    data_in_start_date=1979,
    data_in_end_date=1995,
    default_date_range=(1979, 1995),
    data_in_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim_gas_rerun2/'
                   'gfdl.ncrc2-default-prod/pp')
)
hiram_gtm = Run(
    name='gas_tm',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea '
        'ice repeated annually, overlaid with annual tropical mean '
        'equilibrium SST anomaly from a PI-to-PD WMGG and ozone simulation '
        'of AM2.1 with a mixed layer ocean. PD atmospheric composition.'
        ),
    data_in_start_date=1979,
    data_in_end_date=1995,
    default_date_range=(1979, 1995),
    data_in_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim_gas_'
                   'trop_mean/gfdl.ncrc2-default-prod/pp')
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
    data_in_start_date=1979,
    data_in_end_date=1995,
    default_date_range=(1979, 1995),
    data_in_direc=('/archive/Yi.Ming/siena_201211/c180_hiram_clim_gas_m_'
                   'trop_mean/gfdl.ncrc2-default-prod/pp')
)
hiram_amip = Run(
    name='amip',
    description='',
    ens_mem_prefix='/archive/hrao/ornl/cmip5/c180_hiram_',
    ens_mem_ext=['H1', 'H3'],
    ens_mem_suffix='/pp',
    data_in_dur=5,
    data_in_start_date=1979,
    data_in_end_date=2008,
    default_date_range=(1979, 2008),
    data_in_dir_struc='gfdl'
)
