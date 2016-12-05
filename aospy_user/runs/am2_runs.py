"""aospy.Run objects library for simulations in GFDL AM2.1 model."""
import datetime

from aospy import Run

am2_cont = Run(
    name='cont',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea '
        'ice repeated annually, with PD atmospheric composition.'
    ),
    data_direc=('/archive/yim/siena_201203/m45_am2p14_1990/'
                   'gfdl.ncrc2-intel-prod/pp'),
    data_dur=16,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1998, 12, 31),
)
am2_aero = Run(
    name='aero',
    description=(
        """1981-2000 HadISST climatological annual cycle of SSTs and sea ice
        repeated annually, overlaid with annual cycle of equilibrium SST
        anomalies from a PI-to-PD aerosols simulation of AM2.1 with a mixed
        layer ocean.  PD atmospheric composition."""
    ),
    data_direc=('/archive/Yi.Ming/siena_201203/m45_am2p14_1990_clim_aero/'
                   'gfdl.ncrc2-intel-prod/pp'),
    data_dur=16,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1998, 12, 31),
)
am2_atm = Run(
    name='aero_tm',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid with annual tropical mean equilibrium '
        'SST anomaly from a PI-to-PD aerosols simulation of AM2.1 with a '
        'mixed layer ocean.  PD atmospheric composition.'
    ),
    data_direc=('/archive/Yi.Ming/siena_201203/''m45_am2p14_1990_clim'
                   '_aero_trop_mean/gfdl.ncrc2-intel-prod/pp'),
    data_dur=16,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1998, 12, 31),
)
am2_amtm = Run(
    name='aero_mtm',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, subtracting annual tropical mean equilibrium SST '
        'anomaly from a PI-to-PD aerosols simulation of AM2.1 with a mixed '
        'layer ocean.  PD atmospheric composition.'
    ),
    data_direc=('/archive/Yi.Ming/siena_201203/m45_am2p14_1990_clim_aero_m'
                   '_trop_mean_fixed2/gfdl.ncrc2-intel-prod/pp'),
    data_dur=16,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1998, 12, 31),
)
am2_apac = Run(
    name='aero_pac',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid in Pacific Ocean only with annual cycle '
        'of equilibrium SST anomalies from a PI-to-PD aerosols simulation of '
        'AM2.1 with a mixed layer ocean.  PD atmospheric composition.'
    ),
    data_direc=('/archive/Yi.Ming/siena_201203/m45_am2p14_1990_clim_aero_'
                   'pac/gfdl.ncrc2-intel-prod/pp'),
    data_dur=16,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1998, 12, 31),
)
am2_aatl = Run(
    name='aero_atl',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid in Atlantic Ocean only with annual '
        'cycle of equilibrium SST anomalies from a PI-to-PD aerosols '
        'simulation of AM2.1 with a mixed layer ocean.  '
        'PD atmospheric composition.'
    ),
    data_direc=('/archive/Yi.Ming/siena_201203/m45_am2p14_1990_clim_aero_'
                   'atl/gfdl.ncrc2-intel-prod/pp'),
    data_dur=16,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1998, 12, 31),
)
am2_aind = Run(
    name='aero_ind',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid in Indian Ocean only with annual cycle '
        'of equilibrium SST anomalies from a PI-to-PD aerosols simulation of '
        'AM2.1 with a mixed layer ocean.  PD atmospheric composition.'
    ),
    data_direc=('/archive/Yi.Ming/siena_201203/m45_am2p14_1990_clim_aero_'
                   'ind/gfdl.ncrc2-intel-prod/pp'),
    data_dur=16,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1998, 12, 31),
)
am2_gas = Run(
    name='gas',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid with annual cycle of equilibrium SST '
        'anomalies from a PI-to-PD WMGG and ozone simulation of AM2.1 with '
        'a mixed layer ocean. PD atmospheric composition.'
    ),
    data_direc=('/archive/Yi.Ming/siena_201203/m45_am2p14_1990_clim_gas/'
                   'gfdl.ncrc2-intel-prod/pp'),
    data_dur=16,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1998, 12, 31),
)
am2_gtm = Run(
    name='gas_tm',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid with annual tropical mean equilibrium '
        'SST anomaly from a PI-to-PD WMGG and ozone simulation of AM2.1 with '
        'a mixed layer ocean. PD atmospheric composition.'
    ),
    data_direc=('/archive/Yi.Ming/siena_201203/m45_am2p14_1990_clim_gas_'
                   'trop_mean/gfdl.ncrc2-intel-prod/pp'),
    data_dur=16,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1998, 12, 31),
)
am2_gmtm = Run(
    name='gas_mtm',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid with annual cycle of equilibrium SST '
        'anomalies minus their annual tropical mean from a PI-to-PD WMGG and '
        'ozone simulation of AM2.1 with a mixed layer ocean.  '
        'PD atmospheric composition.'
    ),
    data_direc=('/archive/Yi.Ming/siena_201203/m45_am2p14_1990_clim_gas_'
                   'm_trop_mean/gfdl.ncrc2-intel-prod/pp'),
    data_dur=16,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1998, 12, 31),
)
am2_noT = Run(
    name='noTok',
    description='',
    data_direc='/archive/miz/GCM/miz_cess_noT/cess/am2_cess/pp/',
    data_dur=5,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1987, 12, 31),
)
am2_noT_p2K = Run(
    name='noTok_p2K',
    description='',
    data_direc='/archive/miz/GCM/miz_cess_noT/cess+2/am2_cess+2/pp/',
    data_dur=5,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1987, 12, 31),
)
am2_amip = Run(
    name='amip',
    description='',
    data_direc=('/archive/Spencer.Hill/AM2.1_1870-2004/AM2.1_1870-2004-'
                   'HGlob-SST-ICE-AllForc_B1-_B10_ens/pp/'),
    data_dur=5,
    data_start_date=datetime.datetime(1870, 1, 1),
    data_end_date=datetime.datetime(1999, 12, 31),
)
am2_reyoi_cont = Run(
    name='reyoi_cont',
    tags=['reyoi', 'cont'],
    description='PI atmos and Reynolds OI climatological SSTs',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi/'
                   'gfdl.ncrc3-intel-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_m0p25 = Run(
    name='reyoi-0.25K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi-0p25K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_m0p5 = Run(
    name='reyoi-0.5K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi-0p5K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_m1 = Run(
    name='reyoi-1K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi-1K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_m1p5 = Run(
    name='reyoi-1.5K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi-1p5K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_m2 = Run(
    name='reyoi-2K',
    tags=['reyoi', '-2K'],
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi-2K/'
                   'gfdl.ncrc3-intel-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_m3 = Run(
    name='reyoi-3K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi-3K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_m4 = Run(
    name='reyoi-4K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi-4K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_m6 = Run(
    name='reyoi-6K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi-6K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_m8 = Run(
    name='reyoi-8K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi-8K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_m10 = Run(
    name='reyoi-10K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi-10K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_m15 = Run(
    name='reyoi-15K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi-15K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_p0p25 = Run(
    name='reyoi+0.25K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi+0p25K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_p0p5 = Run(
    name='reyoi+0.5K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi+0p5K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_p1 = Run(
    name='reyoi+1K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi+1K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_p1p5 = Run(
    name='reyoi+1.5K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi+1p5K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_p2 = Run(
    name='reyoi+2K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi+2K/'
                   'gfdl.ncrc3-intel-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_p3 = Run(
    name='reyoi+3K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi+3K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_p4 = Run(
    name='reyoi+4K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi+4K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_p6 = Run(
    name='reyoi+6K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi+6K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_p8 = Run(
    name='reyoi+8K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi+8K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_p10 = Run(
    name='reyoi+10K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi+10K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_wpwp_p2 = Run(
    name='reyoi_wpwp+2K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_wpwp+2K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_wpwp_m2 = Run(
    name='reyoi_wpwp-2K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_wpwp-2K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_uw = Run(
    name='reyoi_uw_lo_0p75',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw_conv/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_uw_p2 = Run(
    name='reyoi_uw_lo_0p75_p2k',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS and +2K SST',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw_conv+2K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1982, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
    default_start_date=datetime.datetime(1983, 1, 1),
)
am2_reyoi_uw_p5 = Run(
    name='reyoi_uw_lo_0p75_p5k',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS and +5K SST',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw_conv+5K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1982, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
    default_start_date=datetime.datetime(1983, 1, 1),
)
am2_reyoi_uw_p10 = Run(
    name='reyoi_uw_lo_0p75_p10k',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS and +10K SST',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw_conv+10K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_uw_m2 = Run(
    name='reyoi_uw_lo_0p75_m2k',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS and -2K SST',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw_conv-2K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1982, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
    default_start_date=datetime.datetime(1983, 1, 1),
)
am2_reyoi_uw_m5 = Run(
    name='reyoi_uw_lo_0p75_m5k',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS and -5K SST',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw_conv-5K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1982, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
    default_start_date=datetime.datetime(1983, 1, 1),
)
am2_reyoi_uw_m10 = Run(
    name='reyoi_uw_lo_0p75_m10k',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS and -10K SST',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw_conv-10K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_uw_lo_0p5 = Run(
    name='reyoi_uw_landocean0.5',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS, and with the '
        'land-ocean entrainment rate ratio set to 0.5',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw_lofactor0.5/'
                   'gfdl.ncrc3-intel-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_uw_lo_0p5_p2k = Run(
    name='reyoi_uw_landocean0.5+2K',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS, and with the '
        'land-ocean entrainment rate ratio set to 0.5 and +2K SSTs',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw_lofactor0.5+2K/'
                   'gfdl.ncrc3-intel-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_uw_lo_0p5_p4k = Run(
    name='reyoi_uw_lo_0p5_p4k',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS, and with the '
        'land-ocean entrainment rate ratio set to 0.5 and +4K SSTs',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw+4K/'
                   'gfdl.ncrc3-intel-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_uw_lo_0p5_p6k = Run(
    name='reyoi_uw_lo_0p5_p6k',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS, and with the '
        'land-ocean entrainment rate ratio set to 0.5 and +6K SSTs',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw+6K/'
                   'gfdl.ncrc3-intel-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_uw_lo_0p5_p8k = Run(
    name='reyoi_uw_lo_0p5_p8k',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS, and with the '
        'land-ocean entrainment rate ratio set to 0.5 and +8K SSTs',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw+8K/'
                   'gfdl.ncrc3-intel-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_uw_lo_0p5_p10k = Run(
    name='reyoi_uw_lo_0p5_p10k',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS, and with the '
        'land-ocean entrainment rate ratio set to 0.5 and +10K SSTs',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw+10K/'
                   'gfdl.ncrc3-intel-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_uw_lo_0p5_m2k = Run(
    name='reyoi_uw_lo_0p5_m2k',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS, and with the '
        'land-ocean entrainment rate ratio set to 0.5 and -2K SSTs',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw-2K/'
                   'gfdl.ncrc3-intel-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_uw_lo_0p5_m4k = Run(
    name='reyoi_uw_lo_0p5_m4k',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS, and with the '
        'land-ocean entrainment rate ratio set to 0.5 and -4K SSTs',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw-4K/'
                   'gfdl.ncrc3-intel-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_uw_lo_0p5_m6k = Run(
    name='reyoi_uw_lo_0p5_m6k',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS, and with the '
        'land-ocean entrainment rate ratio set to 0.5 and -6K SSTs',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw-6K/'
                   'gfdl.ncrc3-intel-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_uw_lo_0p5_m8k = Run(
    name='reyoi_uw_lo_0p5_m8k',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS, and with the '
        'land-ocean entrainment rate ratio set to 0.5 and -8K SSTs',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw-8K/'
                   'gfdl.ncrc3-intel-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_uw_lo_0p5_m10k = Run(
    name='reyoi_uw_lo_0p5_m10k',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS, and with the '
        'land-ocean entrainment rate ratio set to 0.5 and -10K SSTs',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw-10K/'
                   'gfdl.ncrc3-intel-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reyoi_uw_lo_0p25 = Run(
    name='reyoi_uw_lo_0p25',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS, and with the '
        'land-ocean entrainment rate ratio set to 0.25',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw_lofactor0.25/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1982, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
    default_start_date=datetime.datetime(1983, 1, 1),
)
am2_reyoi_uw_lo_0p25_p2k = Run(
    name='reyoi_uw_lo_0p25_p2k',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS, and with the '
        'land-ocean entrainment rate ratio set to 0.25 and +2K SSTs',
    ),
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_uw_lofactor0.25'
                   '+2K/gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1982, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
    default_start_date=datetime.datetime(1983, 1, 1),
)
am2_cld_lock_cont = Run(
    name='cld_lock_cont',
    description='',
    data_direc=('/archive/Yi.Ming/quickstart/m45_am2p14_1990_nocre_1995/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=16,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1998, 12, 31),
)
am2_cld_lock_cld = Run(
    name='cld_lock+2Kcld',
    description='',
    data_direc=('/archive/Yi.Ming/quickstart/m45_am2p14_1990_nocre_1995_'
                   'p2K_fix2/gfdl.ncrc2-default-prod/pp/'),
    data_dur=16,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1998, 12, 31),
)
am2_cld_lock_sst = Run(
    name='cld_lock+2Ksst',
    description='',
    data_direc=('/archive/Yi.Ming/quickstart/m45_am2p14_1990_nocre_1995_'
                   'p2K_fix1/gfdl.ncrc2-default-prod/pp/'),
    data_dur=16,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1998, 12, 31),
)
am2_cld_lock_p2 = Run(
    name='cld_lock+2K',
    description='',
    data_direc=('/archive/Yi.Ming/quickstart/m45_am2p14_1990_nocre_1995'
                   '_p2K/gfdl.ncrc2-default-prod/pp/'),
    data_dur=16,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1998, 12, 31),
)
am2_hurrell_cont = Run(
    name='hurrell_cont',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_hurrell/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_hurrell_p2 = Run(
    name='hurrell+2K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_hurrell+2K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=30,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reynolds = Run(
    name='reynolds_cont',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reynoldsEOF/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=1,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_reynolds_p2 = Run(
    name='reynolds+2K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reynoldsEOF+2K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=1,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_amip1 = Run(
    name='amip1_cont',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_amip1/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=1,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_amip1_p2 = Run(
    name='amip1+2K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_amip1+2K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=1,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_cld_seed_all_p2 = Run(
    name='cld_seed_all+2K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_cld_seed_all+2K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=1,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_cld_seed_np_p2 = Run(
    name='cld_seed_np+2K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_cld_seed_np+2K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=1,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_cld_seed_sp_p2 = Run(
    name='cld_seed_sp+2K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_cld_seed_sp+2K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=1,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_cld_seed_sa_p2 = Run(
    name='cld_seed_sa+2K',
    description='',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_cld_seed_sa+2K/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=1,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
)
am2_zshen_cont = Run(
    name='zshen_cont',
    description="Control run for Zhaoyi Shen's simulations",
    data_direc=('/archive/Zhaoyi.Shen/quickstart/m45_am2p14_1990_base/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=16,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1998, 12, 31),
)
am2_atmos_heat_wpwp = Run(
    name='atmos_heat_wpwp',
    description=(
        "Created by Zhaoyi Shen.  Prescribed PD SSTs (standard AM2 control "
        "simulation) but with a prescribed heating in the upper troposphere "
        "above the Indo-Pacific Warm Pool, defined as 10S-10N,90E-150E."
    ),
    data_direc=('/archive/Zhaoyi.Shen/quickstart/m45_am2p14_1990_bc_l8_'
                   'WPWP/gfdl.ncrc2-default-prod-openmp/pp/'),
    data_dur=16,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1998, 12, 31),
)
am2_atmos_heat_wpwp_small = Run(
    name='atmos_heat_wpwp_small',
    description=(
        "Created by Zhaoyi Shen.  Prescribed PD SSTs (standard AM2 control "
        "simulation) but with a prescribed heating in the upper troposphere "
        "above the Indo-Pacific Warm Pool, defined as 5S-5N, 105E-125E."
    ),
    data_direc=('/archive/Zhaoyi.Shen/quickstart/m45_am2p14_1990_bc_l8_'
                   'WPWPs/gfdl.ncrc2-default-prod/pp/'),
    data_dur=16,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1998, 12, 31),
)
am2_reyoi_w_ice = Run(
    name='reyoi_w_ice_file',
    description='Standard climatological OI SSTs run but including ice file',
    data_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi_with_ice_file/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=1,
    data_start_date=datetime.datetime(1982, 1, 1),
    data_end_date=datetime.datetime(2012, 12, 31),
    default_start_date=datetime.datetime(1983, 1, 1),
)
am2_test = Run(
    name='test',
    description='Dummy/testing run',
    data_direc=('/archive/Spencer.Hill/am2/am2test/'
                   'gfdl.ncrc2-default-prod/pp/'),
    data_dur=2,
    data_start_date=datetime.datetime(1983, 1, 1),
    data_end_date=datetime.datetime(1984, 12, 31),
)
