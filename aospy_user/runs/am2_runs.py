"""aospy.Run objects library for simulations in GFDL AM2.1 model."""
from aospy import Run

am2_cont = Run(
    name='cont',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea '
        'ice repeated annually, with PD atmospheric composition.'
    ),
    data_in_direc=('/archive/yim/siena_201203/m45_am2p14_1990/'
                   'gfdl.ncrc2-intel-prod/pp'),
    data_in_dur=16,
    data_in_start_date=1983,
    data_in_end_date=1998,
    default_date_range=(1983, 1998)
)
am2_aero = Run(
    name='aero',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid with annual cycle of equilibrium SST '
        'anomalies from a PI-to-PD aerosols simulation of AM2.1 with a mixed '
        'layer ocean.  PD atmospheric composition.'
    ),
    data_in_direc=('/archive/Yi.Ming/siena_201203/m45_am2p14_1990_clim_aero/'
                   'gfdl.ncrc2-intel-prod/pp'),
    data_in_dur=16,
    data_in_start_date=1983,
    data_in_end_date=1998,
    default_date_range=(1983, 1998)
)
am2_atm = Run(
    name='aero_tm',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid with annual tropical mean equilibrium SST anomaly from a PI-to-PD aerosols simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    data_in_direc=('/archive/Yi.Ming/siena_201203/''m45_am2p14_1990_clim'
                   '_aero_trop_mean/gfdl.ncrc2-intel-prod/pp'),
    data_in_dur=16,
    data_in_start_date=1983,
    data_in_end_date=1998,
    default_date_range=(1983, 1998)
)
am2_amtm = Run(
    name='aero_mtm',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, subtracting annual tropical mean equilibrium SST anomaly from a PI-to-PD aerosols simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    data_in_direc='/archive/Yi.Ming/siena_201203/m45_am2p14_1990_clim_aero_m_trop_mean_fixed2/gfdl.ncrc2-intel-prod/pp',
    data_in_dur=16,
    data_in_start_date=1983,
    data_in_end_date=1998,
    default_date_range=(1983, 1998)
)
am2_apac = Run(
    name='aero_pac',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid in Pacific Ocean only with annual cycle of equilibrium SST anomalies from a PI-to-PD aerosols simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    data_in_direc='/archive/Yi.Ming/siena_201203/m45_am2p14_1990_clim_aero_pac/gfdl.ncrc2-intel-prod/pp',
    data_in_dur=16,
    data_in_start_date=1983,
    data_in_end_date=1998,
    default_date_range=(1983, 1998)
)
am2_aatl = Run(
    name='aero_atl',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid in Atlantic Ocean only with annual cycle of equilibrium SST anomalies from a PI-to-PD aerosols simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    data_in_direc='/archive/Yi.Ming/siena_201203/m45_am2p14_1990_clim_aero_atl/gfdl.ncrc2-intel-prod/pp',
    data_in_dur=16,
    data_in_start_date=1983,
    data_in_end_date=1998,
    default_date_range=(1983, 1998)
)
am2_aind = Run(
    name='aero_ind',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid in Indian Ocean only with annual cycle of equilibrium SST anomalies from a PI-to-PD aerosols simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    data_in_direc='/archive/Yi.Ming/siena_201203/m45_am2p14_1990_clim_aero_ind/gfdl.ncrc2-intel-prod/pp',
    data_in_dur=16,
    data_in_start_date=1983,
    data_in_end_date=1998,
    default_date_range=(1983, 1998)
)
am2_gas = Run(
    name='gas',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid with annual cycle of equilibrium SST anomalies from a PI-to-PD WMGG and ozone simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    data_in_direc='/archive/Yi.Ming/siena_201203/m45_am2p14_1990_clim_gas/gfdl.ncrc2-intel-prod/pp',
    data_in_dur=16,
    data_in_start_date=1983,
    data_in_end_date=1998,
    default_date_range=(1983, 1998)
)
am2_gtm = Run(
    name='gas_tm',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid with annual tropical mean equilibrium SST anomaly from a PI-to-PD WMGG and ozone simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    data_in_direc='/archive/Yi.Ming/siena_201203/m45_am2p14_1990_clim_gas_trop_mean/gfdl.ncrc2-intel-prod/pp',
    data_in_dur=16,
    data_in_start_date=1983,
    data_in_end_date=1998,
    default_date_range=(1983, 1998)
)
am2_gmtm = Run(
    name='gas_mtm',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid with annual cycle of equilibrium SST anomalies minus their annual tropical mean from a PI-to-PD WMGG and ozone simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    data_in_direc='/archive/Yi.Ming/siena_201203/m45_am2p14_1990_clim_gas_m_trop_mean/gfdl.ncrc2-intel-prod/pp',
    data_in_dur=16,
    data_in_start_date=1983,
    data_in_end_date=1998,
    default_date_range=(1983, 1998)
)
am2_noT = Run(
    name='noTok',
    description='',
    data_in_direc='/archive/miz/GCM/miz_cess_noT/cess/am2_cess/pp/',
    data_in_dur=5,
    data_in_start_date=1983,
    data_in_end_date=1987,
    default_date_range=(1983, 1987)
)
am2_noT_p2K = Run(
    name='noTok_p2K',
    description='',
    data_in_direc='/archive/miz/GCM/miz_cess_noT/cess+2/am2_cess+2/pp/',
    data_in_dur=5,
    data_in_start_date=1983,
    data_in_end_date=1987,
    default_date_range=(1983, 1987)
)
am2_amip = Run(
    name='amip',
    description='',
    data_in_direc=(
        '/archive/fjz/AM2.1_1870-2004/AM2.1_1870-2004-HGlob-SST-ICE-AllForc_B1'
        '-_B10_ens/pp/'
    ),
    data_in_dur=130,
    data_in_start_date=1870,
    data_in_end_date=1999,
    default_date_range=(1870, 1999)
)
am2_reyoi_cont = Run(
    name='reyoi_cont',
    tags=['reyoi', 'cont'],
    description='PI atmos and Reynolds OI climatological SSTs',
    data_in_direc=(
        '/archive/Spencer.Hill/am2/am2clim_reyoi/gfdl.ncrc2-default-prod/pp/'
    ),
    data_in_dur=1,
    # data_in_dur=30,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_m0p25 = Run(
    name='reyoi-0.25K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi-0p25K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_m0p5 = Run(
    name='reyoi-0.5K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi-0p5K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=15,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_m1 = Run(
    name='reyoi-1K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi-1K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=15,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_m1p5 = Run(
    name='reyoi-1.5K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi-1p5K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_m2 = Run(
    name='reyoi-2K',
    tags=['reyoi', '-2K'],
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi-2K/gfdl.ncrc2-default-prod/pp/',
    data_in_dur=15,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_m3 = Run(
    name='reyoi-3K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi-3K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_m4 = Run(
    name='reyoi-4K',
    description='',
    data_in_direc=('/archive/Spencer.Hill/am2/am2clim_reyoi-4K/'
              'gfdl.ncrc2-default-prod/pp/'),
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_m6 = Run(
    name='reyoi-6K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi-6K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_m8 = Run(
    name='reyoi-8K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi-8K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_m10 = Run(
    name='reyoi-10K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi-10K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_p0p25 = Run(
    name='reyoi+0.25K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi+0p25K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_p0p5 = Run(
    name='reyoi+0.5K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi+0p5K/gfdl.ncrc2-default-prod/pp/',
    data_in_dur=15,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_p1 = Run(
    name='reyoi+1K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi+1K/gfdl.ncrc2-default-prod/pp/',
    data_in_dur=15,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_p1p5 = Run(
    name='reyoi+1.5K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi+1p5K/gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_p2 = Run(
    name='reyoi+2K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi+2K/gfdl.ncrc2-default-prod/pp/',
    data_in_dur=30,
    # data_in_dur=1,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_p3 = Run(
    name='reyoi+3K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi+3K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_p4 = Run(
    name='reyoi+4K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi+4K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_p6 = Run(
    name='reyoi+6K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi+6K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_p8 = Run(
    name='reyoi+8K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi+8K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_p10 = Run(
    name='reyoi+10K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi+10K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_wpwp_p2 = Run(
    name='reyoi_wpwp+2K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi_wpwp+2K/gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_wpwp_m2 = Run(
    name='reyoi_wpwp-2K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi_wpwp-2K/gfdl.ncrc2-default-prod/pp/',
    data_in_dur=30,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_wpwp_m2 = Run(
    name='reyoi_wpwp-2K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi_wpwp-2K/gfdl.ncrc2-default-prod/pp/',
    data_in_dur=30,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_uw = Run(
    name='reyoi_uw_conv',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS',
    ),
    data_in_direc=(
        '/archive/Spencer.Hill/am2/am2clim_reyoi_uw_conv/'
        'gfdl.ncrc2-default-prod/pp/'
    ),
    data_in_dur=1,
    # data_in_dur=30,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_uw_p2 = Run(
    name='reyoi_uw_conv+2K',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS and +2K SST',
    ),
    data_in_direc=(
        '/archive/Spencer.Hill/am2/am2clim_reyoi_uw_conv+2K/'
        'gfdl.ncrc2-default-prod/pp/'
    ),
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_uw_p5 = Run(
    name='reyoi_uw_conv+5K',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS and +5K SST',
    ),
    data_in_direc=(
        '/archive/Spencer.Hill/am2/am2clim_reyoi_uw_conv+5K/'
        'gfdl.ncrc2-default-prod/pp/'
    ),
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_uw_p10 = Run(
    name='reyoi_uw_conv+10K',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS and +10K SST',
    ),
    data_in_direc=(
        '/archive/Spencer.Hill/am2/am2clim_reyoi_uw_conv+10K/'
        'gfdl.ncrc2-default-prod/pp/'
    ),
    data_in_dur=1,
    # data_in_dur=30,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_uw_m2 = Run(
    name='reyoi_uw_conv-2K',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS and -2K SST',
    ),
    data_in_direc=(
        '/archive/Spencer.Hill/am2/am2clim_reyoi_uw_conv-2K/'
        'gfdl.ncrc2-default-prod/pp/'
    ),
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_uw_m5 = Run(
    name='reyoi_uw_conv-5K',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS and -5K SST',
    ),
    data_in_direc=(
        '/archive/Spencer.Hill/am2/am2clim_reyoi_uw_conv-5K/'
        'gfdl.ncrc2-default-prod/pp/'
    ),
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_uw_m10 = Run(
    name='reyoi_uw_conv-10K',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS and -10K SST',
    ),
    data_in_direc=(
        '/archive/Spencer.Hill/am2/am2clim_reyoi_uw_conv-10K/'
        'gfdl.ncrc2-default-prod/pp/'
    ),
    data_in_dur=1,
    # data_in_dur=30,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_uw_lo_0p5 = Run(
    name='reyoi_uw_landocean0.5',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS, and with the '
        'land-ocean entrainment rate ratio set to 0.5',
    ),
    data_in_direc=(
        '/archive/Spencer.Hill/am2/am2clim_reyoi_uw_lofactor0.5/'
        'gfdl.ncrc2-default-prod/pp/'
    ),
    # data_in_dur=1,
    data_in_dur=30,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_uw_lo_0p5_p2k = Run(
    name='reyoi_uw_landocean0.5+2K',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS, and with the '
        'land-ocean entrainment rate ratio set to 0.5 and +2K SSTs',
    ),
    data_in_direc=(
        '/archive/Spencer.Hill/am2/am2clim_reyoi_uw_lofactor0.5+2K/'
        'gfdl.ncrc2-default-prod/pp/'
    ),
    # data_in_dur=1,
    data_in_dur=30,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_uw_lo_0p25 = Run(
    name='reyoi_uw_landocean0.25',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS, and with the '
        'land-ocean entrainment rate ratio set to 0.25',
    ),
    data_in_direc=(
        '/archive/Spencer.Hill/am2/am2clim_reyoi_uw_lofactor0.25/'
        'gfdl.ncrc2-default-prod/pp/'
    ),
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_uw_lo_0p25_p2k = Run(
    name='reyoi_uw_landocean0.25+2K',
    description=(
        'Same NOAA OI SST dataset climatology used in other `am2_reyoi` runs, '
        'but using UW shallow convection scheme rather than RAS, and with the '
        'land-ocean entrainment rate ratio set to 0.25 and +2K SSTs',
    ),
    data_in_direc=(
        '/archive/Spencer.Hill/am2/am2clim_reyoi_uw_lofactor0.25+2K/'
        'gfdl.ncrc2-default-prod/pp/'
    ),
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_cld_lock_cont = Run(
    name='cld_lock_cont',
    description='',
    data_in_direc=('/archive/Yi.Ming/quickstart/m45_am2p14_1990_nocre_1995/'
              'gfdl.ncrc2-default-prod/pp/'),
    data_in_dur=16,
    data_in_start_date=1983,
    data_in_end_date=1998,
    default_date_range=(1983, 1998)
)
am2_cld_lock_cld = Run(
    name='cld_lock+2Kcld',
    description='',
    data_in_direc=('/archive/Yi.Ming/quickstart/m45_am2p14_1990_nocre_1995_p2K_fix2/'
              'gfdl.ncrc2-default-prod/pp/'),
    data_in_dur=16,
    data_in_start_date=1983,
    data_in_end_date=1998,
    default_date_range=(1983, 1998)
)
am2_cld_lock_sst = Run(
    name='cld_lock+2Ksst',
    description='',
    data_in_direc=('/archive/Yi.Ming/quickstart/m45_am2p14_1990_nocre_1995_p2K_fix1/'
              'gfdl.ncrc2-default-prod/pp/'),
    data_in_dur=16,
    data_in_start_date=1983,
    data_in_end_date=1998,
    default_date_range=(1983, 1998)
)
am2_cld_lock_p2 = Run(
    name='cld_lock+2K',
    description='',
    data_in_direc=('/archive/Yi.Ming/quickstart/m45_am2p14_1990_nocre_1995_p2K/'
              'gfdl.ncrc2-default-prod/pp/'),
    data_in_dur=16,
    data_in_start_date=1983,
    data_in_end_date=1998,
    default_date_range=(1983, 1998)
)
am2_hurrell_cont = Run(
    name='hurrell_cont',
    description='',
    data_in_direc=(
        '/archive/Spencer.Hill/am2/am2clim_hurrell/gfdl.ncrc2-default-prod/pp/'
    ),
    data_in_dur=30,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_hurrell_p2 = Run(
    name='hurrell+2K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_hurrell+2K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=30,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reynolds = Run(
    name='reynolds_cont',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reynoldsEOF/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reynolds_p2 = Run(
    name='reynolds+2K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reynoldsEOF+2K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_amip1 = Run(
    name='amip1_cont',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_amip1/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_amip1_p2 = Run(
    name='amip1+2K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_amip1+2K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_cld_seed_all_p2 = Run(
    name='cld_seed_all+2K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi_cld_seed_all+2K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_cld_seed_np_p2 = Run(
    name='cld_seed_np+2K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi_cld_seed_np+2K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_cld_seed_sp_p2 = Run(
    name='cld_seed_sp+2K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi_cld_seed_sp+2K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_cld_seed_sa_p2 = Run(
    name='cld_seed_sa+2K',
    description='',
    data_in_direc='/archive/Spencer.Hill/am2/am2clim_reyoi_cld_seed_sa+2K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    data_in_dur=1,
    data_in_start_date=1983,
    data_in_end_date=2012,
    default_date_range=(1983, 2012)
)
am2_reyoi_w_ice = Run(
    name='reyoi_w_ice_file',
    description='Standard climatological OI SSTs run but including ice file',
    data_in_direc=(
        '/archive/Spencer.Hill/am2/am2clim_reyoi_with_ice_file/'
        'gfdl.ncrc2-default-prod/pp/',
        ),
    data_in_dur=1,
    data_in_start_date=1982,
    data_in_end_date=2012,
    default_date_range=(1982, 1985)
)
am2_test = Run(
    name='test',
    description='Dummy/testing run',
    data_in_direc='/archive/Spencer.Hill/am2/am2test/gfdl.ncrc2-default-prod/pp/',
    data_in_dur=2,
    data_in_start_date=1983,
    data_in_end_date=1984,
    default_date_range=(1983, 1984)
)
