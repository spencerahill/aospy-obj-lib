"""aospy.Run objects for observational data."""
from aospy.run import Run

# CRU
cru_v322 = Run(
    name='v3.22',
    description='CRU v3.22',
    direc_nc='/archive/s1h/obs/HadCRU/3.22',
    nc_dir_struc='one_dir',
    nc_dur=113,
    nc_start_yr=1901,
    nc_start_month=1,
    nc_end_yr=2013,
    nc_end_month=12,
    default_yr_range=(1901, 2013),
    nc_files={'precip': 'cru_ts3.22.1901.2013.pre.dat.nc',
              'cld_amt': 'cru_ts3.22.1901.2013.cld.dat.nc',
              'diurnal_temp_range': 'cru_ts3.22.1901.2013.dtr.dat.nc',
              'ground_frost_freq': 'cru_ts3.22.1901.2013.frs.dat.nc',
              'pet': 'cru_ts3.22.1901.2013.pet.dat.nc',
              't_surf_min': 'cru_ts3.22.1901.2013.tmn.dat.nc',
              't_surf_max': 'cru_ts3.22.1901.2013.tmx.dat.nc',
              't_surf': 'cru_ts3.22.1901.2013.tmp.dat.nc',
              'vap_pres': 'cru_ts3.22.1901.2013.vap.dat.nc',
              'wet_day_freq': 'cru_ts3.22.1901.2013.wet.dat.nc'}
)

# PREC/L
prec_l_0p5deg = Run(
    name='0.5deg',
    description='PREC/L 0.5x0.5 degree resolution',
    direc_nc='/archive/s1h/obs/PREC_L/20150212',
    nc_dir_struc='one_dir',
    nc_dur=64,
    nc_start_yr=1948,
    nc_start_month=1,
    nc_end_yr=2011,
    nc_end_month=12,
    default_yr_range=(1948, 2011),
    nc_files={'precip': 'precip.mon.mean.0.5x0.5.nc'}
)
prec_l_1deg = Run(
    name='1deg',
    description='PREC/L 1x1 degree resolution',
    direc_nc='/archive/s1h/obs/PREC_L/20150212',
    nc_dir_struc='one_dir',
    nc_dur=67,
    nc_start_yr=1948,
    nc_start_month=1,
    nc_end_yr=2014,
    nc_end_month=12,
    default_yr_range=(1948, 2014),
    nc_files={'precip': 'precip.mon.mean.1x1.nc'}
)
prec_l_2p5deg = Run(
    name='2.5deg',
    description='PREC/L 2.5x2.5 degree resolution',
    direc_nc='/archive/s1h/obs/PREC_L/20150212',
    nc_dir_struc='one_dir',
    nc_dur=67,
    nc_start_yr=1948,
    nc_start_month=1,
    nc_end_yr=2014,
    nc_end_month=12,
    default_yr_range=(1948, 2014),
    nc_files={'precip': 'precip.mon.mean.2.5x2.5.nc'}
)

# CERES
ceres_ebaf = Run(
    name='ebaf',
    description='CERES EBAF',
    direc_nc=('/archive/pcmdi/repo/obs4MIPs/NASA-LaRC/CERES-EBAF/'
              'atmos/mon/v20140402'),
    nc_dir_struc='one_dir',
    nc_dur=14,
    nc_start_yr=2000,
    nc_start_month=3,
    nc_end_yr=2013,
    nc_end_month=10,
    default_yr_range=(2000, 2013),
    nc_suffix='_CERES-EBAF_L3B_Ed2-8_200003-201310.nc',
    nc_files={
        'swdn_toa': 'rsdt_CERES-EBAF_L3B_Ed2-8_200003-201310.nc',
        'swup_toa': 'rsut_CERES-EBAF_L3B_Ed2-8_200003-201310.nc',
        'swup_toa_clr': 'rsutcs_CERES-EBAF_L3B_Ed2-8_200003-201310.nc',
        'olr': 'rlut_CERES-EBAF_L3B_Ed2-8_200003-201310.nc',
        'olr_clr': 'rlutcs_CERES-EBAF_L3B_Ed2-8_200003-201310.nc'
    }
)
ceres_ebaf_sfc = Run(
    name='ebaf-sfc',
    description='CERES EBAF-surface',
    direc_nc=('/archive/pcmdi/repo/obs4MIPs/NASA-LaRC/CERES-EBAF_Surface/'
              'atmos/mon/v20140402'),
    nc_dir_struc='one_dir',
    nc_dur=14,
    nc_start_yr=2000,
    nc_start_month=3,
    nc_end_yr=2013,
    nc_end_month=3,
    default_yr_range=(2000, 2012),
    nc_suffix='_CERES-EBAF_L3B_Ed2-7_200003-201303.nc',
    nc_files={
        'swdn_sfc': 'rsds_CERES-EBAF_L3B_Ed2-7_200003-201303.nc',
        'swdn_sfc_clr': 'rsdscs_CERES-EBAF_L3B_Ed2-7_200003-201303.nc',
        'swup_sfc': 'rsus_CERES-EBAF_L3B_Ed2-7_200003-201303.nc',
        'swup_sfc_clr': 'rsuscs_CERES-EBAF_L3B_Ed2-7_200003-201303.nc',
        'lwdn_sfc': 'rlds_CERES-EBAF_L3B_Ed2-7_200003-201303.nc',
        'lwdn_sfc_clr': 'rldscs_CERES-EBAF_L3B_Ed2-7_200003-201303.nc',
        'lwup_sfc': 'rlus_CERES-EBAF_L3B_Ed2-7_200003-201303.nc',
    }
)

# GPCP
gpcp_v2p2 = Run(
    name='v2p2',
    description=('GPCP v2.2 gridded precipitation, from blend of '
                 'satellite and station gauge data.'),
    direc_nc='/archive/pcmdi/repo/obs4MIPs/NASA-GSFC/GPCP/atmos/',
    nc_dur=10,
    nc_start_yr=1979,
    nc_end_yr=2013,
    default_yr_range=(1979, 2013),
    nc_dir_struc='one_dir',
    nc_files={'monthly':
              ['mon/v20130401/pr_GPCP-SG_L3_v2.2_' + yrs + '.nc' for yrs in
               ('197901-197912', '198001-198912', '199001-199912',
                '200001-200912', '201001-201312')],
              'pentad': 'day/v20121003/'}
)

# TRMM
trmm_v7a = Run(
    name='v7a',
    description='TRMM v7 gridded precipitation, from satellite data',
    direc_nc='/archive/pcmdi/repo/obs4MIPs/NASA-GSFC/TRMM/atmos/',
    nc_dur=2,
    nc_start_yr=2000,
    nc_start_month=1,
    nc_end_yr=2010,
    nc_end_month=9,
    default_yr_range=(2000, 2009),
    nc_dir_struc='one_dir',
    nc_files={'monthly': ['mon/v20130204/pr_TRMM-L3_v7A_' + yrs + '.nc'
                          for yrs in ('200001-200912', '201001-201009')]}

)

# CMAP
cmap_standard = Run(
    name='standard',
    description=('CMAP standard version, which does not include NCEP '
                 'reanalysis data to fill in gaps.'),
    direc_nc='/archive/s1h/obs/CMAP/standard',
    nc_dir_struc='one_dir',
    nc_dur=36,
    nc_start_yr=1979,
    nc_start_month=1,
    nc_end_yr=2014,
    nc_end_month=12,
    default_yr_range=(1979, 2014),
    nc_files={'monthly': 'precip.mon.mean.nc',
              'pentad': 'precip.pentad.mean.nc'}
)
cmap_enhanced = Run(
    name='enhanced',
    description=('CMAP enhanced version, which includes NCEP reanalysis '
                 'data to fill in gaps.'),
    direc_nc='/archive/s1h/obs/CMAP/enhanced',
    nc_dur=36,
    nc_start_yr=1979,
    nc_end_yr=2014,
    default_yr_range=(1979, 2014),
    nc_dir_struc='one_dir',
    nc_files={'monthly': 'precip.mon.mean.nc',
              'pentad': 'precip.pentad.mean.nc'}
)

# U. Delaware
udel_v201 = Run(
    name='v201',
    description='U. Delaware version 2.01',
    direc_nc='/archive/s1h/obs/U_Del',
    nc_dur=109,
    nc_start_yr=1900,
    nc_end_yr=2008,
    default_yr_range=(1900, 2008),
    nc_dir_struc='one_dir',
    nc_files={'precip': 'precip.mon.total.v201.nc',
              't_surf': 'air.mon.total.v201.nc'}
    )
udel_v301 = Run(
    name='v301',
    description='U. Delaware version 3.01',
    direc_nc='/archive/s1h/obs/U_Del',
    nc_dur=111,
    nc_start_yr=1900,
    nc_end_yr=2010,
    default_yr_range=(1900, 2010),
    nc_dir_struc='one_dir',
    nc_files={'precip': 'precip.mon.total.v301.nc',
              't_surf': 'air.mon.total.v301.nc'}
    )

# ERA-Interim
era_i = Run(
    name='interim',
    description='',
    direc_nc=('/archive/pcmdi/repo/ana4MIPs/ECMWF/ERA-Interim/atmos/'
              'mon/v20140416'),
    nc_dur=1,
    nc_start_yr=1979,
    nc_start_month=1,
    nc_end_yr=2013,
    nc_end_month=12,
    default_yr_range=(1979, 2013),
    nc_dir_struc='one_dir',
    nc_files={
              'cld_amt': ['cl_Amon_reanalysis_IFS-Cy31r2_' + yrs + '.nc'
                          for yrs in [str(yr) + '01-' + str(yr) + '12'
                                      for yr in range(1979, 2014)]],
              'evap': ['evspsbl_Amon_reanalysis_IFS-Cy31r2_' + yrs + '.nc'
                       for yrs in [str(yr) + '01-' + str(yr) + '12'
                                   for yr in range(1979, 2014)]],
              'hght': ['zg_Amon_reanalysis_IFS-Cy31r2_' + yrs + '.nc'
                       for yrs in [str(yr) + '01-' + str(yr) + '12'
                                   for yr in range(1979, 2014)]],
              'omega': ['wap_Amon_reanalysis_IFS-Cy31r2_' + yrs + '.nc'
                        for yrs in [str(yr) + '01-' + str(yr) + '12'
                                    for yr in range(1979, 2014)]],
              'precip': ['pr_Amon_reanalysis_IFS-Cy31r2_' + yrs + '.nc'
                         for yrs in [str(yr) + '01-' + str(yr) + '12'
                                     for yr in range(1979, 2014)]],
              'ps': ['ps_Amon_reanalysis_IFS-Cy31r2_' + yrs + '.nc'
                     for yrs in [str(yr) + '01-' + str(yr) + '12'
                                 for yr in range(1979, 2014)]],
              'rh': ['hur_Amon_reanalysis_IFS-Cy31r2_' + yrs + '.nc'
                     for yrs in [str(yr) + '01-' + str(yr) + '12'
                                 for yr in range(1979, 2014)]],
              'shflx': ['hfss_Amon_reanalysis_IFS-Cy31r2_' + yrs + '.nc'
                        for yrs in [str(yr) + '01-' + str(yr) + '12'
                                    for yr in range(1979, 2014)]],
              'slp': ['psl_Amon_reanalysis_IFS-Cy31r2_' + yrs + '.nc'
                      for yrs in [str(yr) + '01-' + str(yr) + '12'
                                  for yr in range(1979, 2014)]],
              'sphum': ['hus_Amon_reanalysis_IFS-Cy31r2_' + yrs + '.nc'
                        for yrs in [str(yr) + '01-' + str(yr) + '12'
                                    for yr in range(1979, 2014)]],
              'temp': ['ta_Amon_reanalysis_IFS-Cy31r2_' + yrs + '.nc'
                       for yrs in [str(yr) + '01-' + str(yr) + '12'
                                   for yr in range(1979, 2014)]],
              'ucomp': ['ua_Amon_reanalysis_IFS-Cy31r2_' + yrs + '.nc'
                        for yrs in [str(yr) + '01-' + str(yr) + '12'
                                    for yr in range(1979, 2014)]],
              'vcomp': ['va_Amon_reanalysis_IFS-Cy31r2_' + yrs + '.nc'
                        for yrs in [str(yr) + '01-' + str(yr) + '12'
                                    for yr in range(1979, 2014)]],
              'wvp': ['prw_Amon_reanalysis_IFS-Cy31r2_' + yrs + '.nc'
                      for yrs in [str(yr) + '01-' + str(yr) + '12'
                                  for yr in range(1979, 2014)]]
              }
    )

# MERRA
merra = Run(
    name='merra',
    description='',
    direc_nc=('/archive/pcmdi/repo/ana4MIPs/NASA-GMAO/MERRA/atmos/mon/'
              'v20140624'),
    nc_dur=1,
    nc_start_yr=1979,
    nc_start_month=1,
    nc_end_yr=2011,
    nc_end_month=12,
    default_yr_range=(1979, 2011),
    nc_dir_struc='one_dir',
    nc_files={'cld_amt': ['cl_Amon_reanalysis_MERRA_' + yrs + '.nc'
                          for yrs in [str(yr) + '01-' + str(yr) + '12'
                                      for yr in range(1979, 2012)]],
              'evap': ['evspsbl_Amon_reanalysis_MERRA_' + yrs + '.nc'
                       for yrs in [str(yr) + '01-' + str(yr) + '12'
                                   for yr in range(1979, 2012)]],
              'hght': ['zg_Amon_reanalysis_MERRA_' + yrs + '.nc'
                       for yrs in [str(yr) + '01-' + str(yr) + '12'
                                   for yr in range(1979, 2012)]],
              'omega': ['wap_Amon_reanalysis_MERRA_' + yrs + '.nc'
                        for yrs in [str(yr) + '01-' + str(yr) + '12'
                                    for yr in range(1979, 2012)]],
              'precip': ['pr_Amon_reanalysis_MERRA_' + yrs + '.nc'
                         for yrs in [str(yr) + '01-' + str(yr) + '12'
                                     for yr in range(1979, 2012)]],
              'ps': ['ps_Amon_reanalysis_MERRA_' + yrs + '.nc'
                     for yrs in [str(yr) + '01-' + str(yr) + '12'
                                 for yr in range(1979, 2012)]],
              'rh': ['hur_Amon_reanalysis_MERRA_' + yrs + '.nc'
                     for yrs in [str(yr) + '01-' + str(yr) + '12'
                                 for yr in range(1979, 2012)]],
              'shflx': ['hfss_Amon_reanalysis_MERRA_' + yrs + '.nc'
                        for yrs in [str(yr) + '01-' + str(yr) + '12'
                                    for yr in range(1979, 2012)]],
              'slp': ['psl_Amon_reanalysis_MERRA_' + yrs + '.nc'
                      for yrs in [str(yr) + '01-' + str(yr) + '12'
                                  for yr in range(1979, 2012)]],
              'sphum': ['hus_Amon_reanalysis_MERRA_' + yrs + '.nc'
                        for yrs in [str(yr) + '01-' + str(yr) + '12'
                                    for yr in range(1979, 2012)]],
              'temp': ['ta_Amon_reanalysis_MERRA_' + yrs + '.nc'
                       for yrs in [str(yr) + '01-' + str(yr) + '12'
                                   for yr in range(1979, 2012)]],
              'ucomp': ['ua_Amon_reanalysis_MERRA_' + yrs + '.nc'
                        for yrs in [str(yr) + '01-' + str(yr) + '12'
                                    for yr in range(1979, 2012)]],
              'vcomp': ['va_Amon_reanalysis_MERRA_' + yrs + '.nc'
                        for yrs in [str(yr) + '01-' + str(yr) + '12'
                                    for yr in range(1979, 2012)]],
              'wvp': ['prw_Amon_reanalysis_MERRA_' + yrs + '.nc'
                      for yrs in [str(yr) + '01-' + str(yr) + '12'
                                  for yr in range(1979, 2012)]]
              }
    )

# NCEP CFSR
cfsr = Run(
    name='cfsr',
    description='',
    direc_nc=('/archive/pcmdi/repo/ana4MIPs/NOAA-NCEP/CFSR/atmos/'
              'mon/v20140822'),
    nc_dur=1,
    nc_start_yr=1979,
    nc_start_month=1,
    nc_end_yr=2013,
    nc_end_month=12,
    default_yr_range=(1979, 2013),
    nc_dir_struc='one_dir',
    nc_files={'cld_amt': ['cl_Amon_reanalysis_CFSR_' + yrs + '.nc'
                          for yrs in [str(yr) + '01-' + str(yr) + '12'
                                      for yr in range(1979, 2014)]],
              'evap': ['evspsbl_Amon_reanalysis_CFSR_' + yrs + '.nc'
                       for yrs in [str(yr) + '01-' + str(yr) + '12'
                                   for yr in range(1979, 2014)]],
              'hght': ['zg_Amon_reanalysis_CFSR_' + yrs + '.nc'
                       for yrs in [str(yr) + '01-' + str(yr) + '12'
                                   for yr in range(1979, 2014)]],
              'omega': ['wap_Amon_reanalysis_CFSR_' + yrs + '.nc'
                        for yrs in [str(yr) + '01-' + str(yr) + '12'
                                    for yr in range(1979, 2014)]],
              'precip': ['pr_Amon_reanalysis_CFSR_' + yrs + '.nc'
                         for yrs in [str(yr) + '01-' + str(yr) + '12'
                                     for yr in range(1979, 2014)]],
              'ps': ['ps_Amon_reanalysis_CFSR_' + yrs + '.nc'
                     for yrs in [str(yr) + '01-' + str(yr) + '12'
                                 for yr in range(1979, 2014)]],
              'rh': ['hur_Amon_reanalysis_CFSR_' + yrs + '.nc'
                     for yrs in [str(yr) + '01-' + str(yr) + '12'
                                 for yr in range(1979, 2014)]],
              'shflx': ['hfss_Amon_reanalysis_CFSR_' + yrs + '.nc'
                        for yrs in [str(yr) + '01-' + str(yr) + '12'
                                    for yr in range(1979, 2014)]],
              'slp': ['psl_Amon_reanalysis_CFSR_' + yrs + '.nc'
                      for yrs in [str(yr) + '01-' + str(yr) + '12'
                                  for yr in range(1979, 2014)]],
              'sphum': ['hus_Amon_reanalysis_CFSR_' + yrs + '.nc'
                        for yrs in [str(yr) + '01-' + str(yr) + '12'
                                    for yr in range(1979, 2014)]],
              'temp': ['ta_Amon_reanalysis_CFSR_' + yrs + '.nc'
                       for yrs in [str(yr) + '01-' + str(yr) + '12'
                                   for yr in range(1979, 2014)]],
              'ucomp': ['ua_Amon_reanalysis_CFSR_' + yrs + '.nc'
                        for yrs in [str(yr) + '01-' + str(yr) + '12'
                                    for yr in range(1979, 2014)]],
              'vcomp': ['va_Amon_reanalysis_CFSR_' + yrs + '.nc'
                        for yrs in [str(yr) + '01-' + str(yr) + '12'
                                    for yr in range(1979, 2014)]],
              'wvp': ['prw_Amon_reanalysis_CFSR_' + yrs + '.nc'
                      for yrs in [str(yr) + '01-' + str(yr) + '12'
                                  for yr in range(1979, 2014)]]
              }
)

# JMA JRA-25
jra25 = Run(
    name='jra-25',
    description='Japanase Meteorological Agency reanalyses',
    direc_nc='/archive/pcmdi/repo/ana4MIPs/JMA/JRA-25/atmos/mon/v20140408',
    nc_dur=1,
    nc_start_yr=1979,
    nc_start_month=1,
    nc_end_yr=2013,
    nc_end_month=12,
    default_yr_range=(1979, 2013),
    nc_dir_struc='one_dir',
    nc_files={'monthly': ['va_Amon_reanalysis_JRA-25_' + yrs + '.nc'
                          for yrs in [str(yr) + '01-' + str(yr) + '12'
                                      for yr in range(1979, 2014)]]}
)

# LandFlux-EVAL 1989-2005
lfe_all = Run(
    name='all',
    description='LandFlux-EVAL 1989-2005 using all products',
    direc_nc='/archive/s1h/obs/LandFlux-EVAL',
    nc_dur=17,
    nc_start_yr=1989,
    nc_start_month=1,
    nc_end_yr=2005,
    nc_end_month=12,
    default_yr_range=(1989, 2005),
    nc_dir_struc='one_dir',
    nc_files={'monthly': 'LandFluxEVAL.merged.89-05.monthly.all.nc',
              'annual': 'LandFluxEVAL.merged.89-05.yearly.all.nc'}
)
lfe_diag = Run(
    name='diagnostic',
    description='LandFlux-EVAL 1989-2005 using only diagnostic products',
    direc_nc='/archive/s1h/obs/LandFlux-EVAL',
    nc_dur=17,
    nc_start_yr=1989,
    nc_start_month=1,
    nc_end_yr=2005,
    nc_end_month=12,
    default_yr_range=(1989, 2005),
    nc_dir_struc='one_dir',
    nc_files={'monthly': 'LandFluxEVAL.merged.89-05.monthly.diagnostic.nc',
              'annual': 'LandFluxEVAL.merged.89-05.yearly.diagnostic.nc'}
)
lfe_lsm = Run(
    name='lsm',
    description='LandFlux-EVAL 1989-2005 using land surface models only',
    direc_nc='/archive/s1h/obs/LandFlux-EVAL',
    nc_dur=17,
    nc_start_yr=1989,
    nc_start_month=1,
    nc_end_yr=2005,
    nc_end_month=12,
    default_yr_range=(1989, 2005),
    nc_dir_struc='one_dir',
    nc_files={'monthly': 'LandFluxEVAL.merged.89-05.monthly.lsm.nc',
              'annual': 'LandFluxEVAL.merged.89-05.yearly.lsm.nc'}
)
lfe_rean = Run(
    name='reanalyses',
    description='LandFlux-EVAL 1989-2005 using reanalyses only',
    direc_nc='/archive/s1h/obs/LandFlux-EVAL',
    nc_dur=17,
    nc_start_yr=1989,
    nc_start_month=1,
    nc_end_yr=2005,
    nc_end_month=12,
    default_yr_range=(1989, 2005),
    nc_dir_struc='one_dir',
    nc_files={'monthly': 'LandFluxEVAL.merged.89-05.monthly.reanalyses.nc',
              'annual': 'LandFluxEVAL.merged.89-05.yearly.reanlayses.nc'}
)

# LandFlux-EVAL 1989-1995
lfe95_all = Run(
    name='all',
    description='LandFlux-EVAL 1989-1995 using all products',
    direc_nc='/archive/s1h/obs/LandFlux-EVAL',
    nc_dur=17,
    nc_start_yr=1989,
    nc_start_month=1,
    nc_end_yr=1995,
    nc_end_month=12,
    default_yr_range=(1989, 1995),
    nc_dir_struc='one_dir',
    nc_files={'monthly': 'LandFluxEVAL.merged.89-95.monthly.all.nc',
              'annual': 'LandFluxEVAL.merged.89-95.yearly.all.nc'}
)
lfe95_diag = Run(
    name='diagnostic',
    description='LandFlux-EVAL 1989-1995 using diagnostic products only',
    direc_nc='/archive/s1h/obs/LandFlux-EVAL',
    nc_dur=17,
    nc_start_yr=1989,
    nc_start_month=1,
    nc_end_yr=1995,
    nc_end_month=12,
    default_yr_range=(1989, 1995),
    nc_dir_struc='one_dir',
    nc_files={'monthly': 'LandFluxEVAL.merged.89-95.monthly.diagnostic.nc',
              'annual': 'LandFluxEVAL.merged.89-95.yearly.diagnostic.nc'}
)
lfe95_lsm = Run(
    name='lsm',
    description='LandFlux-EVAL 1989-1995 using land surface models only',
    direc_nc='/archive/s1h/obs/LandFlux-EVAL',
    nc_dur=17,
    nc_start_yr=1989,
    nc_start_month=1,
    nc_end_yr=1995,
    nc_end_month=12,
    default_yr_range=(1989, 1995),
    nc_dir_struc='one_dir',
    nc_files={'monthly': 'LandFluxEVAL.merged.89-95.monthly.lsm.nc',
              'annual': 'LandFluxEVAL.merged.89-95.yearly.lsm.nc'}
)
lfe95_rean = Run(
    name='reanalyses',
    description='LandFlux-EVAL 1989-1995 using reanalyses only',
    direc_nc='/archive/s1h/obs/LandFlux-EVAL',
    nc_dur=17,
    nc_start_yr=1989,
    nc_start_month=1,
    nc_end_yr=1995,
    nc_end_month=12,
    default_yr_range=(1989, 1995),
    nc_dir_struc='one_dir',
    nc_files={'monthly': 'LandFluxEVAL.merged.89-95.monthly.reanalyses.nc',
              'annual': 'LandFluxEVAL.merged.89-95.yearly.reanlayses.nc'}
)

# SST datasets
hadisst1 = Run(
    name='hadisst1',
    description='HadISST1 product; SST data only',
    direc_nc='/archive/s1h/obs/HadISST',
    nc_dur=1,
    nc_start_yr=2005,
    nc_start_month=1,
    nc_end_yr=2005,
    nc_end_month=12,
    default_yr_range=(2005, 2005),
    nc_dir_struc='one_dir',
    nc_files={'monthly': '/archive/s1h/obs/HadISST/HadISST_sst.nc'}
)
hurrell = Run(
    name='hurrell',
    description='Hurrell SST product',
    direc_nc='/archive/s1h/obs/Hurrell',
    nc_dur=1,
    nc_start_yr=2000,
    nc_start_month=1,
    nc_end_yr=2000,
    nc_end_month=12,
    default_yr_range=(2000, 2000),
    nc_dir_struc='one_dir',
    nc_files={
        'monthly': '/archive/s1h/obs/Hurrell/sst.climo.1981-2000.data.nc'
    }
)
reynolds_oi = Run(
    name='reynolds_oi',
    description='Reynolds OI SST observational dataset',
    direc_nc='/archive/s1h/obs/ReynoldsOI',
    nc_dur=19,
    nc_start_yr=1981,
    nc_start_month=11,
    nc_end_yr=1999,
    nc_end_month=1,
    default_yr_range=(1982, 1998),
    nc_dir_struc='one_dir',
    nc_files={'monthly': '/archive/s1h/obs/ReynoldsOI/reyoi_sst.data.nc'}
)