"""aospy.Run objects library for simulations in GFDL AM3 model."""
import datetime

from aospy import Run

am3_cont = Run(
    name='cont',
    description=('1981-2000 Hurrell climatological annual cycle of SSTs and '
                 'sea ice, with PD atmospheric composition.'),
    data_direc=('/archive/Yi.Ming/fms/siena_201211/c48L48_am3p10/'
                   'gfdl.ncrc2-intel-prod/pp'),
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2000, 12, 31),
    data_dur=20,
)
am3_aero = Run(
    name='aero',
    description=(
        '1981-2000 Hurrell climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid with annual cycle of equilibrium SST '
        'anomalies from a PI-to-PD aerosols simulation of AM2.1 with a mixed '
        'layer ocean.  PD atmospheric composition.'
    ),
    data_direc=('/archive/Yi.Ming/fms/siena_201211/c48L48_am3p10_aero/'
                   'gfdl.ncrc2-intel-prod/pp'),
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2000, 12, 31),
    data_dur=20,
)
am3_atm = Run(
    name='aero_tm',
    description=(
        '1981-2000 Hurrell climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid with annual tropical mean equilibrium '
        'SST anomaly from a PI-to-PD aerosols simulation of AM2.1 with a '
        'mixed layer ocean. PD atmospheric composition.'
    ),
    data_direc=('/archive/Yi.Ming/fms/siena_201211/'
                   'c48L48_am3p10_aero_trop_mean/gfdl.ncrc2-intel-prod/pp'),
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2000, 12, 31),
    data_dur=20,
)
am3_amtm = Run(
    name='aero_mtm',
    description=(
        '1981-2000 Hurrell climatological annual cycle of SSTs and sea ice '
        'repeated annually, subtracting annual tropical mean equilibrium SST '
        'anomaly from a PI-to-PD aerosols simulation of AM2.1 with a mixed '
        'layer ocean. PD atmospheric composition.'
    ),
    data_direc=('/archive/Yi.Ming/fms/siena_201211/c48L48_am3p10_aero_m_'
                   'trop_mean_fixed/gfdl.ncrc2-intel-prod-openmp/pp'),
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2000, 12, 31),
    data_dur=20,
)
am3_apac = Run(
    name='aero_pac',
    description=(
        """1981-2000 Hurrell climatological annual cycle of SSTs and sea ice
        repeated annually, overlaid in Pacific Ocean only with annual cycle of
        equilibrium SST anomalies from a PI-to-PD aerosols simulation of AM2.1
        with a mixed layer ocean. PD atmospheric composition."""
    ),
    data_direc=('/archive/Yi.Ming/fms/siena_201211/c48L48_am3p10_aero_pac/'
                   'gfdl.ncrc2-intel-prod/pp'),
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2000, 12, 31),
    data_dur=20,
)
am3_aatl = Run(
    name='aero_atl',
    description=(
        """1981-2000 Hurrell climatological annual cycle of SSTs and sea ice
        repeated annually, overlaid in Atlantic Ocean only with annual cycle of
        equilibrium SST anomalies from a PI-to-PD aerosols simulation of AM2.1
        with a mixed layer ocean. PD atmospheric composition."""
    ),
    data_direc=('/archive/Yi.Ming/fms/siena_201211/c48L48_am3p10_aero_atl/'
                   'gfdl.ncrc2-intel-prod/pp'),
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2000, 12, 31),
    data_dur=20,
)
am3_aind = Run(
    name='aero_ind',
    description=(
        """1981-2000 Hurrell climatological annual cycle of SSTs and sea ice
        repeated annually, overlaid in Indian Ocean only with annual cycle of
        equilibrium SST anomalies from a PI-to-PD aerosols simulation of AM2.1
        with a mixed layer ocean. PD atmospheric composition."""
    ),
    data_direc=('/archive/Yi.Ming/fms/siena_201211/c48L48_am3p10_aero_ind/'
                   'gfdl.ncrc2-intel-prod/pp'),
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2000, 12, 31),
    data_dur=20,
)
am3_gas = Run(
    name='gas',
    description=(
        """1981-2000 Hurrell climatological annual cycle of SSTs and sea ice
        repeated annually, overlaid with annual cycle of equilibrium SST
        anomalies from a PI-to-PD WMGG and ozone simulation of AM2.1 with a
        mixed layer ocean. PD atmospheric composition."""
    ),
    data_direc=('/archive/Yi.Ming/fms/siena_201211/c48L48_am3p10_gas/'
                   'gfdl.ncrc2-intel-prod/pp'),
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2000, 12, 31),
    data_dur=20,
)
am3_gtm = Run(
    name='gas_tm',
    description=(
        """1981-2000 Hurrell climatological annual cycle of SSTs and sea ice
        repeated annually, overlaid with annual tropical mean equilibrium SST
        anomaly from a PI-to-PD WMGG and ozone simulation of AM2.1 with a mixed
        layer ocean. PD atmospheric composition."""
    ),
    data_direc=('/archive/Yi.Ming/fms/siena_201211/c48L48_am3p10_gas_trop'
                   '_mean/gfdl.ncrc2-intel-prod/pp'),
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2000, 12, 31),
    data_dur=20,
)
am3_gmtm = Run(
    name='gas_mtm',
    description=(
        '1981-2000 Hurrell climatological annual cycle of SSTs and '
        'sea ice repeated annually, overlaid with annual cycle of '
        'equilibrium SST anomalies minus their annual tropical mean '
        'from a PI-to-PD WMGG and ozone simulation of AM2.1 with a '
        'mixed layer ocean.  PD atmospheric composition.'
    ),
    data_direc=('/archive/Yi.Ming/fms/siena_201211/c48L48_am3p10_gas_m_'
                   'trop_mean/gfdl.ncrc2-intel-prod/pp'),
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2000, 12, 31),
    data_dur=20,
)
am3_amip = Run(
    name='amip',
    description='',
    ens_mem_prefix='/archive/lwh/fms/riga_201104/c48L48_am3p9_',
    ens_mem_ext=['ext', 'ext2', 'ext3'],
    ens_mem_suffix='/gfdl.intel-prod/pp',
    data_dur=136,
    data_start_date=datetime.datetime(1870, 1, 1),
    data_end_date=datetime.datetime(2005, 12, 31),
    default_end_date=datetime.datetime(2004, 12, 31),
)
am3_hc = Run(
    name='hurrell_cont',
    description='',
    data_direc=('/archive/Spencer.Hill/am3/am3clim_hurrell/'
                   'gfdl.ncrc3-intel-prod-openmp/pp'),
    data_dur=30,
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2010, 12, 31),
)
am3_hp1k = Run(
    name='hurrell+1K',
    description='',
    data_direc=('/archive/Spencer.Hill/am3/am3clim_hurrell+1K/'
                   'gfdl.ncrc2-intel-prod-openmp/pp'),
    data_dur=30,
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2010, 12, 31),
)
am3_hp2k = Run(
    name='hurrell+2K',
    description='',
    data_direc=('/archive/Spencer.Hill/am3/am3clim_hurrell+2K/'
                   'gfdl.ncrc3-intel-prod-openmp/pp'),
    data_dur=30,
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2010, 12, 31),
)
am3_hp4k = Run(
    name='hurrell+4K',
    description='',
    data_direc=('/archive/Spencer.Hill/am3/am3clim_hurrell+4K/'
                   'gfdl.ncrc3-intel-prod-openmp/pp'),
    data_dur=30,
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2010, 12, 31),
)
am3_hp6k = Run(
    name='hurrell+6K',
    description='',
    data_direc=('/archive/Spencer.Hill/am3/am3clim_hurrell+6K/'
                   'gfdl.ncrc2-intel-prod-openmp/pp'),
    data_dur=30,
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2010, 12, 31),
)
am3_hp8k = Run(
    name='hurrell+8K',
    description='',
    data_direc=('/archive/Spencer.Hill/am3/am3clim_hurrell+8K/'
                   'gfdl.ncrc2-intel-prod-openmp/pp'),
    data_dur=30,
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2010, 12, 31),
)
am3_hp10k = Run(
    name='hurrell+10K',
    description='',
    data_direc=('/archive/Spencer.Hill/am3/am3clim_hurrell+10K/'
                   'gfdl.ncrc2-intel-prod-openmp/pp'),
    data_dur=30,
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2010, 12, 31),
)
am3_hm1k = Run(
    name='hurrell-1K',
    description='',
    data_direc=('/archive/Spencer.Hill/am3/am3clim_hurrell-1K/'
                   'gfdl.ncrc2-intel-prod-openmp/pp'),
    data_dur=30,
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2010, 12, 31),
)
am3_hm2k = Run(
    name='hurrell-2K',
    description='',
    data_direc=('/archive/Spencer.Hill/am3/am3clim_hurrell-2K/'
                   'gfdl.ncrc2-intel-prod-openmp/pp'),
    data_dur=30,
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2010, 12, 31),
)
am3_hm4k = Run(
    name='hurrell-4K',
    description='',
    data_direc=('/archive/Spencer.Hill/am3/am3clim_hurrell-4K/'
                   'gfdl.ncrc2-intel-prod-openmp/pp'),
    data_dur=30,
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2010, 12, 31),
)
am3_hm6k = Run(
    name='hurrell-6K',
    description='',
    data_direc=('/archive/Spencer.Hill/am3/am3clim_hurrell-6K/'
                   'gfdl.ncrc2-intel-prod-openmp/pp'),
    data_dur=30,
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2010, 12, 31),
)
am3_hm8k = Run(
    name='hurrell-8K',
    description='',
    data_direc=('/archive/Spencer.Hill/am3/am3clim_hurrell-8K/'
                   'gfdl.ncrc2-intel-prod-openmp/pp'),
    data_dur=30,
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2010, 12, 31),
)
am3_hm10k = Run(
    name='hurrell-10K',
    description='',
    data_direc=('/archive/Spencer.Hill/am3/am3clim_hurrell-10K/'
                   'gfdl.ncrc2-intel-prod-openmp/pp'),
    data_dur=30,
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2010, 12, 31),
)
am3_hm15k = Run(
    name='hurrell-15K',
    description='',
    data_direc=('/archive/Spencer.Hill/am3/am3clim_hurrell-15K/'
                   'gfdl.ncrc2-intel-prod-openmp/pp'),
    data_dur=30,
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2010, 12, 31),
)
am3_hwpwp_p2k = Run(
    name='hurrell_wpwp+2K',
    description='',
    data_direc=('/archive/Spencer.Hill/am3/am3clim_hurrell_wpwp+2K/'
                   'gfdl.ncrc2-intel-prod-openmp/pp'),
    data_dur=1,
    data_start_date=datetime.datetime(1980, 1, 1),
    data_end_date=datetime.datetime(2010, 12, 31),
)
am3_hc_static_veg = Run(
    name='hurrell_static_veg_cont',
    description=('Climatological SST annual cycle from Hurrell dataset '
                 'repeated annually, with static year 2000 vegetation'),
    data_direc=('/archive/Spencer.Hill/am3/am3clim_hurrell_static_veg/'
                   'gfdl.ncrc2-intel-prod-openmp/pp'),
    data_dur=30,
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2010, 12, 31),
)
am3_hc_static_veg_p4k = Run(
    name='hurrell_static_veg+4K',
    description='Hurrell climatological SSTs w/ uniform +4K and static veg',
    data_direc=('/archive/Spencer.Hill/am3/am3clim_hurrell_static_veg+4K/'
                   'gfdl.ncrc2-intel-prod-openmp/pp'),
    data_dur=30,
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2010, 12, 31),
)
am3_hc_static_veg_10kyr = Run(
    name='hurrell_static_veg_10kyr',
    description=('Hurrell climatological SSTs w/ 10 ka obliquity and '
                 'precession and static year 2000 vegetation'),
    data_direc=(
        '/archive/Spencer.Hill/am3/am3clim_hurrell_static_veg_10kyr_obliq'
        '_prec/gfdl.ncrc2-intel-prod-openmp/pp'
    ),
    data_dur=30,
    data_start_date=datetime.datetime(1981, 1, 1),
    data_end_date=datetime.datetime(2010, 12, 31),
)
