from aospy.run import Run

am2_cont = Run(
    name='cont',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea '
        'ice repeated annually, with PD atmospheric composition.'
    ),
    direc_nc=('/archive/yim/siena_201203/m45_am2p14_1990/'
              'gfdl.ncrc2-intel-prod/pp'),
    nc_dur=16,
    nc_start_yr=1983,
    nc_end_yr=1998,
    default_yr_range=(1983, 1998)
)
am2_aero = Run(
    name='aero',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid with annual cycle of equilibrium SST anomalies from a PI-to-PD aerosols simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    direc_nc='/archive/yim/siena_201203/m45_am2p14_1990_clim_aero/gfdl.ncrc2-intel-prod/pp',
    nc_dur=16,
    nc_start_yr=1983,
    nc_end_yr=1998,
    default_yr_range=(1983, 1998)
)
am2_atm = Run(
    name='aero_tm',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid with annual tropical mean equilibrium SST anomaly from a PI-to-PD aerosols simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    direc_nc='/archive/yim/siena_201203/m45_am2p14_1990_clim_aero_trop_mean/gfdl.ncrc2-intel-prod/pp',
    nc_dur=16,
    nc_start_yr=1983,
    nc_end_yr=1998,
    default_yr_range=(1983, 1998)
)
am2_amtm = Run(
    name='aero_mtm',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, subtracting annual tropical mean equilibrium SST anomaly from a PI-to-PD aerosols simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    direc_nc='/archive/yim/siena_201203/m45_am2p14_1990_clim_aero_m_trop_mean_fixed2/gfdl.ncrc2-intel-prod/pp',
    nc_dur=16,
    nc_start_yr=1983,
    nc_end_yr=1998,
    default_yr_range=(1983, 1998)
)
am2_apac = Run(
    name='aero_pac',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid in Pacific Ocean only with annual cycle of equilibrium SST anomalies from a PI-to-PD aerosols simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    direc_nc='/archive/yim/siena_201203/m45_am2p14_1990_clim_aero_pac/gfdl.ncrc2-intel-prod/pp',
    nc_dur=16,
    nc_start_yr=1983,
    nc_end_yr=1998,
    default_yr_range=(1983, 1998)
)
am2_aatl = Run(
    name='aero_atl',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid in Atlantic Ocean only with annual cycle of equilibrium SST anomalies from a PI-to-PD aerosols simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    direc_nc='/archive/yim/siena_201203/m45_am2p14_1990_clim_aero_atl/gfdl.ncrc2-intel-prod/pp',
    nc_dur=16,
    nc_start_yr=1983,
    nc_end_yr=1998,
    default_yr_range=(1983, 1998)
)
am2_aind = Run(
    name='aero_ind',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid in Indian Ocean only with annual cycle of equilibrium SST anomalies from a PI-to-PD aerosols simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    direc_nc='/archive/yim/siena_201203/m45_am2p14_1990_clim_aero_ind/gfdl.ncrc2-intel-prod/pp',
    nc_dur=16,
    nc_start_yr=1983,
    nc_end_yr=1998,
    default_yr_range=(1983, 1998)
)
am2_gas = Run(
    name='gas',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid with annual cycle of equilibrium SST anomalies from a PI-to-PD WMGG and ozone simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    direc_nc='/archive/yim/siena_201203/m45_am2p14_1990_clim_gas/gfdl.ncrc2-intel-prod/pp',
    nc_dur=16,
    nc_start_yr=1983,
    nc_end_yr=1998,
    default_yr_range=(1983, 1998)
)
am2_gtm = Run(
    name='gas_tm',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid with annual tropical mean equilibrium SST anomaly from a PI-to-PD WMGG and ozone simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    direc_nc='/archive/yim/siena_201203/m45_am2p14_1990_clim_gas_trop_mean/gfdl.ncrc2-intel-prod/pp',
    nc_dur=16,
    nc_start_yr=1983,
    nc_end_yr=1998,
    default_yr_range=(1983, 1998)
)
am2_gmtm = Run(
    name='gas_mtm',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid with annual cycle of equilibrium SST anomalies minus their annual tropical mean from a PI-to-PD WMGG and ozone simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    direc_nc='/archive/yim/siena_201203/m45_am2p14_1990_clim_gas_m_trop_mean/gfdl.ncrc2-intel-prod/pp',
    nc_dur=16,
    nc_start_yr=1983,
    nc_end_yr=1998,
    default_yr_range=(1983, 1998)
)
am2_noT = Run(
    name='noTok',
    description='',
    direc_nc='/archive/miz/GCM/miz_cess_noT/cess/am2_cess/pp/',
    nc_dur=5,
    nc_start_yr=1983,
    nc_end_yr=1987,
    default_yr_range=(1983, 1987)
)
am2_noT_p2K = Run(
    name='noTok_p2K',
    description='',
    direc_nc='/archive/miz/GCM/miz_cess_noT/cess+2/am2_cess+2/pp/',
    nc_dur=5,
    nc_start_yr=1983,
    nc_end_yr=1987,
    default_yr_range=(1983, 1987)
)
am2_amip = Run(
    name='amip',
    description='',
    direc_nc='/archive/fjz/AM2.1_1870-2004/AM2.1_1870-2004-HGlob-SST' + \
             '-ICE-AllForc_B1-_B10_ens/pp/',
    nc_dur=130,
    nc_start_yr=1870,
    nc_end_yr=1999,
    default_yr_range=(1870, 1999)
)
am2_reyoi_cont = Run(
    name='reyoi_cont',
    tags=['reyoi', 'cont'],
    description='PI atmos and Reynolds OI climatological SSTs',
    direc_nc='/archive/s1h/am2/am2clim_reyoi/gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_m0p25 = Run(
    name='reyoi-0.25K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi-0p25K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_m0p5 = Run(
    name='reyoi-0.5K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi-0p5K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=15,
    nc_start_yr=1983,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_m1 = Run(
    name='reyoi-1K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi-1K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=15,
    nc_start_yr=1983,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_m1p5 = Run(
    name='reyoi-1.5K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi-1p5K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_m2 = Run(
    name='reyoi-2K',
    tags=['reyoi', '-2K'],
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi-2K/gfdl.ncrc2-default-prod/pp/',
    nc_dur=15,
    nc_start_yr=1983,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_m3 = Run(
    name='reyoi-3K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi-3K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_m4 = Run(
    name='reyoi-4K',
    description='',
    direc_nc=('/archive/s1h/am2/am2clim_reyoi-4K/'
              'gfdl.ncrc2-default-prod/pp/'),
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_m6 = Run(
    name='reyoi-6K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi-6K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_m8 = Run(
    name='reyoi-8K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi-8K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_m10 = Run(
    name='reyoi-10K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi-10K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_p0p25 = Run(
    name='reyoi+0.25K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi+0p25K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_p0p5 = Run(
    name='reyoi+0.5K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi+0p5K/gfdl.ncrc2-default-prod/pp/',
    nc_dur=15,
    nc_start_yr=1983,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_p1 = Run(
    name='reyoi+1K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi+1K/gfdl.ncrc2-default-prod/pp/',
    nc_dur=15,
    nc_start_yr=1983,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_p1p5 = Run(
    name='reyoi+1.5K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi+1p5K/gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_p2 = Run(
    name='reyoi+2K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi+2K/gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_p3 = Run(
    name='reyoi+3K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi+3K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_p4 = Run(
    name='reyoi+4K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi+4K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_p6 = Run(
    name='reyoi+6K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi+6K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_p8 = Run(
    name='reyoi+8K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi+8K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_p10 = Run(
    name='reyoi+10K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi+10K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_wpwp_p2 = Run(
    name='reyoi_wpwp+2K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi_wpwp+2K/gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_wpwp_m2 = Run(
    name='reyoi_wpwp-2K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi_wpwp-2K/gfdl.ncrc2-default-prod/pp/',
    nc_dur=30,
    nc_start_yr=1983,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reyoi_wpwp_m2 = Run(
    name='reyoi_wpwp-2K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi_wpwp-2K/gfdl.ncrc2-default-prod/pp/',
    nc_dur=30,
    nc_start_yr=1983,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_cld_lock_cont = Run(
    name='cld_lock_cont',
    description='',
    direc_nc=('/archive/yim/quickstart/m45_am2p14_1990_nocre_1995/'
              'gfdl.ncrc2-default-prod/pp/'),
    nc_dur=16,
    nc_start_yr=1983,
    nc_end_yr=1998,
    default_yr_range=(1983, 1998)
)
am2_cld_lock_cld = Run(
    name='cld_lock+2Kcld',
    description='',
    direc_nc=('/archive/yim/quickstart/m45_am2p14_1990_nocre_1995_p2K_fix2/'
              'gfdl.ncrc2-default-prod/pp/'),
    nc_dur=16,
    nc_start_yr=1983,
    nc_end_yr=1998,
    default_yr_range=(1983, 1998)
)
am2_cld_lock_sst = Run(
    name='cld_lock+2Ksst',
    description='',
    direc_nc=('/archive/yim/quickstart/m45_am2p14_1990_nocre_1995_p2K_fix1/'
              'gfdl.ncrc2-default-prod/pp/'),
    nc_dur=16,
    nc_start_yr=1983,
    nc_end_yr=1998,
    default_yr_range=(1983, 1998)
)
am2_cld_lock_p2 = Run(
    name='cld_lock+2K',
    description='',
    direc_nc=('/archive/yim/quickstart/m45_am2p14_1990_nocre_1995_p2K/'
              'gfdl.ncrc2-default-prod/pp/'),
    nc_dur=16,
    nc_start_yr=1983,
    nc_end_yr=1998,
    default_yr_range=(1983, 1998)
)
am2_hurrell_cont = Run(
    name='hurrell_cont',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_hurrell/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1983,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_hurrell_p2 = Run(
    name='hurrell+2K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_hurrell+2K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1983,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reynolds = Run(
    name='reynolds_cont',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reynoldsEOF/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1983,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_reynolds_p2 = Run(
    name='reynolds+2K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reynoldsEOF+2K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1983,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_amip1 = Run(
    name='amip1_cont',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_amip1/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1983,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_amip1_p2 = Run(
    name='amip1+2K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_amip1+2K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1983,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_cld_seed_all_p2 = Run(
    name='cld_seed_all+2K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi_cld_seed_all+2K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1983,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_cld_seed_np_p2 = Run(
    name='cld_seed_np+2K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi_cld_seed_np+2K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1983,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_cld_seed_sp_p2 = Run(
    name='cld_seed_sp+2K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi_cld_seed_sp+2K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1983,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_cld_seed_sa_p2 = Run(
    name='cld_seed_sa+2K',
    description='',
    direc_nc='/archive/s1h/am2/am2clim_reyoi_cld_seed_sa+2K/' + \
             'gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1983,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012)
)
am2_test = Run(
    name='test',
    description='Dummy/testing run',
    direc_nc='/archive/s1h/am2/am2test/gfdl.ncrc2-default-prod/pp/',
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=1984,
    default_yr_range=(1983, 1984)
)

# AM3
am3_cont = Run(
    name='cont',
    description=('1981-2000 Hurrell climatological annual cycle of SSTs and '
                 'sea ice, with PD atmospheric composition.'),
    direc_nc=('/archive/yim/fms/siena_201211/c48L48_am3p10/'
              'gfdl.ncrc2-intel-prod/pp')
)
am3_aero = Run(
    name='aero',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid with annual cycle of equilibrium SST anomalies from a PI-to-PD aerosols simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    direc_nc='/archive/yim/fms/siena_201211/c48L48_am3p10_aero/gfdl.ncrc2-intel-prod/pp'
)
am3_atm = Run(
    name='aero_tm',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid with annual tropical mean equilibrium SST anomaly from a PI-to-PD aerosols simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    direc_nc='/archive/yim/fms/siena_201211/c48L48_am3p10_aero_trop_mean/gfdl.ncrc2-intel-prod/pp'
)
am3_amtm = Run(
    name='aero_mtm',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, subtracting annual tropical mean equilibrium SST anomaly from a PI-to-PD aerosols simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    direc_nc='/archive/yim/fms/siena_201211/c48L48_am3p10_aero_m_trop_mean_fixed/gfdl.ncrc2-intel-prod-openmp/pp'
)
am3_apac = Run(
    name='aero_pac',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid in Pacific Ocean only with annual cycle of equilibrium SST anomalies from a PI-to-PD aerosols simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    direc_nc='/archive/yim/fms/siena_201211/c48L48_am3p10_aero_pac/gfdl.ncrc2-intel-prod/pp'
)
am3_aatl = Run(
    name='aero_atl',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid in Atlantic Ocean only with annual cycle of equilibrium SST anomalies from a PI-to-PD aerosols simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    direc_nc='/archive/yim/fms/siena_201211/c48L48_am3p10_aero_atl/gfdl.ncrc2-intel-prod/pp'
)
am3_aind = Run(
    name='aero_ind',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid in Indian Ocean only with annual cycle of equilibrium SST anomalies from a PI-to-PD aerosols simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    direc_nc='/archive/yim/fms/siena_201211/c48L48_am3p10_aero_ind/gfdl.ncrc2-intel-prod/pp'
)
am3_gas = Run(
    name='gas',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid with annual cycle of equilibrium SST anomalies from a PI-to-PD WMGG and ozone simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    direc_nc='/archive/yim/fms/siena_201211/c48L48_am3p10_gas/gfdl.ncrc2-intel-prod/pp'
)
am3_gtm = Run(
    name='gas_tm',
    description='1981-2000 HadISST climatological annual cycle of SSTs and sea ice repeated annually, overlaid with annual tropical mean equilibrium SST anomaly from a PI-to-PD WMGG and ozone simulation of AM2.1 with a mixed layer ocean. PD atmospheric composition.',
    direc_nc='/archive/yim/fms/siena_201211/c48L48_am3p10_gas_trop_mean/gfdl.ncrc2-intel-prod/pp'
)
am3_gmtm = Run(
    name='gas_mtm',
    description=('1981-2000 HadISST climatological annual cycle of SSTs and '
                 'sea ice repeated annually, overlaid with annual cycle of '
                 'equilibrium SST anomalies minus their annual tropical mean '
                 'from a PI-to-PD WMGG and ozone simulation of AM2.1 with a '
                 'mixed layer ocean.  PD atmospheric composition.'),
    direc_nc=('/archive/yim/fms/siena_201211/c48L48_am3p10_gas_m_trop_mean/'
              'gfdl.ncrc2-intel-prod/pp')
)
am3_amip = Run(
    name='amip',
    description='',
    ens_mem_prefix='/archive/lwh/fms/riga_201104/c48L48_am3p9_',
    ens_mem_ext=['ext', 'ext2', 'ext3'],
    ens_mem_suffix='/gfdl.intel-prod/pp',
    nc_dur=136,
    nc_start_yr=1870,
    nc_end_yr=2005,
    default_yr_range=(1870,2005)
)
am3_hc = Run(
    name='hurrell_cont',
    description='',
    direc_nc='/archive/s1h/am3/am3clim_hurrell/' + \
             'gfdl.ncrc2-intel-prod-openmp/pp',
    nc_dur=1,
    nc_start_yr=1980,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010)
)
am3_hp1k = Run(
    name='hurrell+1K',
    description='',
    direc_nc=('/archive/s1h/am3/am3clim_hurrell+1K/'
              'gfdl.ncrc2-intel-prod-openmp/pp'),
    nc_dur=31,
    nc_start_yr=1980,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010)
)
am3_hp2k = Run(
    name='hurrell+2K',
    description='',
    direc_nc=('/archive/s1h/am3/am3clim_hurrell+2K/'
              'gfdl.ncrc2-intel-prod-openmp/pp'),
    nc_dur=1,
    nc_start_yr=1980,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010)
)
am3_hp4k = Run(
    name='hurrell+4K',
    description='',
    direc_nc=('/archive/s1h/am3/am3clim_hurrell+4K/'
              'gfdl.ncrc2-intel-prod-openmp/pp'),
    nc_dur=1,
    nc_start_yr=1980,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010)
)
am3_hp6k = Run(
    name='hurrell+6K',
    description='',
    direc_nc=('/archive/s1h/am3/am3clim_hurrell+6K/'
              'gfdl.ncrc2-intel-prod-openmp/pp'),
    nc_dur=31,
    nc_start_yr=1980,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010)
)
am3_hp8k = Run(
    name='hurrell+8K',
    description='',
    direc_nc=('/archive/s1h/am3/am3clim_hurrell+8K/'
              'gfdl.ncrc2-intel-prod-openmp/pp'),
    nc_dur=31,
    nc_start_yr=1980,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010)
)
am3_hp10k = Run(
    name='hurrell+10K',
    description='',
    direc_nc=('/archive/s1h/am3/am3clim_hurrell+10K/'
              'gfdl.ncrc2-intel-prod-openmp/pp'),
    nc_dur=31,
    nc_start_yr=1980,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010)
)
am3_hm1k = Run(
    name='hurrell-1K',
    description='',
    direc_nc=('/archive/s1h/am3/am3clim_hurrell-1K/'
              'gfdl.ncrc2-intel-prod-openmp/pp'),
    nc_dur=1,
    nc_start_yr=1980,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010)
)
am3_hm2k = Run(
    name='hurrell-2K',
    description='',
    direc_nc=('/archive/s1h/am3/am3clim_hurrell-2K/'
              'gfdl.ncrc2-intel-prod-openmp/pp'),
    nc_dur=1,
    nc_start_yr=1980,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010)
)
am3_hm4k = Run(
    name='hurrell-4K',
    description='',
    direc_nc=('/archive/s1h/am3/am3clim_hurrell-4K/'
              'gfdl.ncrc2-intel-prod-openmp/pp'),
    nc_dur=31,
    nc_start_yr=1980,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010)
)
am3_hm6k = Run(
    name='hurrell-6K',
    description='',
    direc_nc=('/archive/s1h/am3/am3clim_hurrell-6K/'
              'gfdl.ncrc2-intel-prod-openmp/pp'),
    nc_dur=31,
    nc_start_yr=1980,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010)
)
am3_hm8k = Run(
    name='hurrell-8K',
    description='',
    direc_nc=('/archive/s1h/am3/am3clim_hurrell-8K/'
              'gfdl.ncrc2-intel-prod-openmp/pp'),
    nc_dur=31,
    nc_start_yr=1980,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010)
)
am3_hm10k = Run(
    name='hurrell-10K',
    description='',
    direc_nc=('/archive/s1h/am3/am3clim_hurrell-10K/'
              'gfdl.ncrc2-intel-prod-openmp/pp'),
    nc_dur=31,
    nc_start_yr=1980,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010)
)
am3_hm15k = Run(
    name='hurrell-15K',
    description='',
    direc_nc=('/archive/s1h/am3/am3clim_hurrell-15K/'
              'gfdl.ncrc2-intel-prod-openmp/pp'),
    nc_dur=31,
    nc_start_yr=1980,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010)
)
am3_hwpwp_p2k = Run(
    name='hurrell_wpwp+2K',
    description='',
    direc_nc='/archive/s1h/am3/am3clim_hurrell_wpwp+2K/' + \
             'gfdl.ncrc2-intel-prod-openmp/pp',
    nc_dur=1,
    nc_start_yr=1980,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010)
)
am3_hc_static_veg = Run(
    name='hurrell_static_veg_cont',
    description=('Climatological SST annual cycle from Hurrell dataset '
                 'repeated annually, with static year 2000 vegetation'),
    direc_nc=('/archive/s1h/am3/am3clim_hurrell_static_veg/'
              'gfdl.ncrc2-intel-prod-openmp/pp'),
    nc_dur=30,
    nc_start_yr=1981,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010)
)
am3_hc_static_veg_p4k = Run(
    name='hurrell_static_veg+4K',
    description='Hurrell climatological SSTs w/ uniform +4K and static veg',
    direc_nc=('/archive/s1h/am3/am3clim_hurrell_static_veg+4K/'
              'gfdl.ncrc2-intel-prod-openmp/pp'),
    nc_dur=30,
    nc_start_yr=1981,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010)
)
am3_hc_static_veg_10kyr = Run(
    name='hurrell_static_veg_10kyr',
    description=('Hurrell climatological SSTs w/ 10 ka obliquity and '
                 'precession and static year 2000 vegetation'),
    direc_nc=('/archive/s1h/am3/am3clim_hurrell_static_veg_10kyr_obliq_prec/'
              'gfdl.ncrc2-intel-prod-openmp/pp'),
    nc_dur=30,
    nc_start_yr=1981,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010)
)

# HiRAM
hiram_cont = Run(
    name='cont',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs '
        'and sea ice repeated annually, with PD atmospheric composition.'
    ),
    default_yr_range=(1979, 1995),
    direc_nc=('/archive/yim/siena_201211/c180_hiram_clim/'
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
    default_yr_range=(1979, 1995),
    direc_nc=('/archive/yim/siena_201211/c180_hiram_clim_aero/'
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
    default_yr_range=(1979, 1995),
    direc_nc=('/archive/yim/siena_201211/c180_hiram_clim_aero_trop_mean/'
              'gfdl.ncrc2-default-prod/pp')
)
hiram_amtm = Run(
    name='aero_mtm',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, subtracting annual tropical mean equilibrium SST '
        'anomaly from a PI-to-PD aerosols simulation of AM2.1 with a mixed '
        'layer ocean.  PD atmospheric composition.'
    ),
    default_yr_range=(1979, 1995),
    direc_nc=('/archive/yim/siena_201211/c180_hiram_clim_aero_m_trop_mean/'
              'gfdl.ncrc2-default-prod/pp')
)
hiram_apac = Run(
    name='aero_pac',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea ice '
        'repeated annually, overlaid in Pacific Ocean only with annual cycle '
        'of equilibrium SST anomalies from a PI-to-PD aerosols simulation of '
        'AM2.1 with a mixed layer ocean.  PD atmospheric composition.'
    ),
    default_yr_range=(1979, 1995),
    direc_nc=('/archive/yim/siena_201211/c180_hiram_clim_aero_pac/'
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
    default_yr_range=(1979, 1995),
    direc_nc=('/archive/yim/siena_201211/c180_hiram_clim_aero_atl/'
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
    default_yr_range=(1979, 1995),
    direc_nc=('/archive/yim/siena_201211/c180_hiram_clim_aero_ind/'
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
    default_yr_range=(1979, 1995),
    direc_nc=('/archive/yim/siena_201211/c180_hiram_clim_gas_rerun2/'
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
    default_yr_range=(1979, 1995),
    direc_nc=('/archive/yim/siena_201211/c180_hiram_clim_gas_trop_mean/'
              'gfdl.ncrc2-default-prod/pp')
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
    default_yr_range=(1979, 1995),
    direc_nc=('/archive/yim/siena_201211/c180_hiram_clim_gas_m_trop_mean'
              '/gfdl.ncrc2-default-prod/pp')
)
hiram_amip = Run(
    name='amip',
    description='',
    ens_mem_prefix='/archive/hrao/ornl/cmip5/c180_hiram_',
    ens_mem_ext=['H1', 'H3'],
    ens_mem_suffix='/pp',
    nc_dur=5,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    nc_dir_struc='gfdl'
)

# SM2.1
sm2_cont = Run(
    name='cont',
    description='',
    direc_nc=('/archive/yim/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie'
              '_rerun6.YIM/pp'),
    nc_dur=20,
    nc_start_yr=1,
    nc_end_yr=120
)
sm2_aero = Run(
    name='aero',
    description='',
    direc_nc=('/archive/yim/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie2'
              '_rerun6.YIM/pp'),
    nc_dur=100,
    nc_start_yr=1,
    nc_end_yr=100
)
sm2_gas = Run(
    name='gas',
    description='',
    direc_nc=('/archive/yim/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie3'
              '_rerun8.YIM/pp'),
    nc_dur=5,
    nc_start_yr=1,
    nc_end_yr=80
)
sm2_both = Run(
    name='both',
    description='',
    direc_nc=('/archive/yim/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie4'
              '_rerun6.YIM/pp'),
    nc_dur=100,
    nc_start_yr=1,
    nc_end_yr=100
)

## c48-HiRAM
hiram_c48_0 = Run(
    name='ming0',
    description='',
    default_yr_range=(1981, 1995),
    direc_nc=('/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0/'
              'gfdl.ncrc2-intel-prod/pp')
)
hiram_c48_0_p2K = Run(
    name='ming0_p2K',
    description='',
    default_yr_range=(1981, 1995),
    direc_nc=('/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0_p2K/'
              'gfdl.ncrc2-intel-prod/pp')
)
hiram_c48_1 = Run(
    name='ming1',
    description='',
    default_yr_range=(1981, 1995),
    direc_nc='/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0b/' + \
             'gfdl.ncrc2-intel-prod/pp'
)
hiram_c48_1_p2K = Run(
    name='ming1_p2K',
    description='',
    direc_nc='/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0b_p2K/'+\
             'gfdl.ncrc2-intel-prod/pp'
)
hiram_c48_2 = Run(
    name='ming2',
    description='',
    default_yr_range=(1981, 1995),
    direc_nc='/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0e/' + \
             'gfdl.ncrc2-intel-prod/pp'
)
hiram_c48_2_p2K = Run(
    name='ming2_p2K',
    description='',
    default_yr_range=(1981, 1995),
    direc_nc='/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0e_p2K/'+\
             'gfdl.ncrc2-intel-prod/pp'
)
hiram_c48_3 = Run(
    name='ming3',
    description='',
    default_yr_range=(1981, 1995),
    direc_nc='/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0f/' + \
             'gfdl.ncrc2-intel-prod/pp'
)
hiram_c48_3_p2K = Run(
    name='ming3_p2K',
    description='',
    default_yr_range=(1981, 1995),
    direc_nc='/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0f_p2K/'+\
             'gfdl.ncrc2-intel-prod/pp'
)
hiram_c48_4 = Run(
    name='ming4',
    description='',
    default_yr_range=(1981, 1995),
    direc_nc='/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0c/' + \
             'gfdl.ncrc2-intel-prod/pp'
)
hiram_c48_4_p2K = Run(
    name='ming4_p2K',
    description='',
    default_yr_range=(1981, 1995),
    direc_nc='/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0c_p2K/'+\
             'gfdl.ncrc2-intel-prod/pp'
)
hiram_c48_5 = Run(
    name='ming5',
    description='',
    default_yr_range=(1981, 1995),
    direc_nc='/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X01/' + \
             'gfdl.ncrc2-intel-prod/pp'
)
hiram_c48_5_p2K = Run(
    name='ming5_p2K',
    description='',
    default_yr_range=(1981, 1995),
    direc_nc='/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X01_p2K/'+\
             'gfdl.ncrc2-intel-prod/pp'
)
hiram_c48_6 = Run(
    name='ming6',
    description='',
    default_yr_range=(1981, 1995),
    direc_nc='/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X02/' + \
             'gfdl.ncrc2-intel-prod/pp'
)
hiram_c48_6_p2K = Run(
    name='ming6_p2K',
    description='',
    default_yr_range=(1981, 1995),
    direc_nc='/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X02_p2K/'+\
             'gfdl.ncrc2-intel-prod/pp'
)
hiram_c48_7 = Run(
    name='ming7',
    description='',
    default_yr_range=(1981, 1995),
    direc_nc='/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X03/' + \
             'gfdl.ncrc2-intel-prod/pp'
)
hiram_c48_7_p2K = Run(
    name='ming7_p2K',
    description='',
    default_yr_range=(1981, 1995),
    direc_nc='/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X03_p2K/'+\
             'gfdl.ncrc2-intel-prod/pp'
)
hiram_c48_8 = Run(
    name='ming8',
    description='',
    default_yr_range=(1981, 1995),
    direc_nc='/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X04/' + \
             'gfdl.ncrc2-intel-prod/pp'
)
hiram_c48_8_p2K = Run(
    name='ming8_p2K',
    description='',
    default_yr_range=(1981, 1995),
    direc_nc='/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X04_p2K/'+\
             'gfdl.ncrc2-intel-prod/pp'
)

# AM3_c90
am3c90_cont = Run(
    name='cont',
    description='',
    direc_nc='/archive/h1g/FMS/siena_201203/c90L48_am3p10_v6_clim/' + \
             'gfdl.ncrc2-intel-prod-openmp/pp'
)
am3c90_p2K = Run(
    name='p2K',
    description='',
    direc_nc='/archive/h1g/FMS/siena_201203/c90L48_am3p10_v6_clim_p2k/' + \
             'gfdl.ncrc2-intel-prod-openmp/pp'
)

# AM2.5
am2p5_cont = Run(
    name='cont',
    description='',
    direc_nc='/archive/miz/hiramdp/siena_201204/c180l32_am2_C0/' + \
             'gfdl.ncrc2-intel-prod/pp'
)
am2p5_p2K = Run(
    name='p2K',
    description='',
    direc_nc='/archive/miz/hiramdp/siena_201204/c180l32_am2_C0_p2K/gfdl.ncrc2-intel-prod/pp'
)

# AM4 prototypes
am4_a1c = Run(
    name='cont',
    description='',
    direc_nc='/archive/Ming.Zhao/awg/tikal_201403/c96L48_am4a1_' + \
             '2000climo_highsen1/gfdl.ncrc2-intel-prod-openmp/pp'
)
am4_a1p2k = Run(
    name='+2K',
    description='',
    direc_nc='/archive/Ming.Zhao/awg/tikal_201403/c96L48_am4a1_' + \
             '2000climo_highsen1_p2K/gfdl.ncrc2-intel-prod-openmp/pp'
)
am4_a2c = Run(
    name='cont',
    description='',
    direc_nc='/archive/cjg/awg/tikal_201403/c96L48_am4a2r1_' + \
             '2000climo/gfdl.ncrc2-intel-prod-openmp/pp'
)
am4_a2p2k = Run(
    name='+2K',
    description='',
    direc_nc='/archive/cjg/awg/tikal_201403/c96L48_am4a2r1_' + \
             '2000climo_p2K/gfdl.ncrc2-intel-prod-openmp/pp'
)
am4_c1c = Run(
    name='cont',
    description='',
    direc_nc='/archive/miz/tikal_201409_awgUpdates_mom6_2014.08.29/' + \
             'c96L48_am4c1r2_2000climo/gfdl.ncrc2-intel-prod-openmp/pp'
)
am4_c1p2k = Run(
    name='+2K',
    description='',
    direc_nc='/archive/miz/tikal_201409_awgUpdates_mom6_2014.08.29/' + \
             'c96L48_am4c1r2_2000climo_p2K/gfdl.ncrc2-intel-prod-openmp/pp'
)
