"""aospy Model objects corresponding to observational & renalayses data."""
from aospy.model import Model
from aospy_user import runs

# Precipitation
cru = Model(
    name='cru',
    description='Univ. East Anglia Climate Research Unit obs',
    grid_file_paths=('/archive/Spencer.Hill/obs/HadCRU/3.22/'
                   'cru_ts3.22.1901.2013.pre.dat.nc',),
    data_in_dur=113,
    data_in_start_date=1901,
    data_in_end_date=2013,
    default_date_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)
prec_l = Model(
    name='prec_l',
    description='NOAA PRECipitation REConstruction over Land (PREC/L)',
    grid_file_paths=('/archive/Spencer.Hill/obs/PREC_L/20150212/'
                   'precip.mon.mean.1x1.nc',),
    data_in_dur=64,
    data_in_start_date='1948-01',
    data_in_end_date=2012,
    default_date_range=(1948, 2012),
    # runs=[runs.prec_l_0p5deg, runs.prec_l_1deg, runs.prec_l_2p5deg]
    runs=[runs.prec_l_1deg],
    default_runs=[runs.prec_l_1deg]
)
gpcp = Model(
    name='gpcp',
    description=('Global Precipitation Climatology Project: '
                 'http://www.gewex.org/gpcp.html'),
    grid_file_paths=([
        '/archive/pcmdi/repo/obs4MIPs/NASA-GSFC/GPCP/atmos/'
        'mon/v20130401/pr_GPCP-SG_L3_v2.2_' + yrs + '.nc' for yrs in
        ('197901-197912', '198001-198912', '199001-199912',
         '200001-200912', '201001-201312')
    ],),
    data_in_dur=10,
    data_in_start_date=1979,
    data_in_end_date=2013,
    default_date_range=(1979, 2013),
    runs=[runs.gpcp_v2p2],
    default_runs=[runs.gpcp_v2p2]
)
cmap = Model(
    name='cmap',
    description='CPC Merged Analysis of Precipitation',
    grid_file_paths=('/archive/Spencer.Hill/obs/CMAP/standard/'
                   'precip.mon.mean.nc',),
    data_in_dur=36,
    data_in_start_date=1979,
    data_in_end_date=2014,
    default_date_range=(1979, 2014),
    runs=[runs.cmap_standard, runs.cmap_enhanced],
    default_runs=[runs.cmap_standard]
)
trmm = Model(
    name='trmm',
    description=('Tropical Rainfall Measuring Mission: '
                 'http://trmm.gsfc.nasa.gov/'),
    grid_file_paths=(['/archive/pcmdi/repo/obs4MIPs/NASA-GSFC/TRMM/atmos/'
                    'mon/v20130204/pr_TRMM-L3_v7A_' + yrs + '.nc' for yrs
                    in ('200001-200912', '201001-201009')],),
    data_in_dur=10,
    data_in_start_date=2000,
    data_in_end_date='2010-09',
    runs=[runs.trmm_v7a],
    default_runs=[runs.trmm_v7a]
)
udel = Model(
    name='udel',
    description='U. Delaware gridded land data from station obs',
    grid_file_paths=('/archive/Spencer.Hill/obs/U_Del/precip.mon.total.v301.nc',),
    data_in_dur=111,
    data_in_start_date=1900,
    runs=[runs.udel_v201, runs.udel_v301],
    default_runs=[runs.udel_v301]
)

# Radiation
ceres = Model(
    name='ceres',
    grid_file_paths=(
        '/archive/pcmdi/repo/obs4MIPs/NASA-LaRC/'
        'CERES-EBAF/atmos/mon/v20140402/CERES-EBAF/'
        'rsut_CERES-EBAF_L3B_Ed2-8_200003-201310.nc',
    ),
    data_in_dur=14,
    data_in_start_date=2000,
    data_in_end_date='2013-03',
    default_date_range=(2000, 2013),
    runs=[runs.ceres_ebaf, runs.ceres_ebaf_sfc],
    default_runs=[runs.ceres_ebaf]
)

# Reanalyses
era = Model(
    name='era',
    description='ERA reanalyses',
    grid_file_paths=('/archive/pcmdi/repo/ana4MIPs/ECMWF/ERA-Interim/atmos/'
                   'mon/v20140416/wap_*.nc'),
    data_in_dur=1,
    data_in_start_date=1979,
    data_in_end_date=2013,
    default_date_range=(1981, 2000),
    runs=[runs.era_i],
    default_runs=[runs.era_i]
)
merra = Model(
    name='merra',
    description='MERRA reanalyses',
    grid_file_paths=(
        # ['/archive/pcmdi/repo/ana4MIPs/NASA-GMAO/MERRA/atmos/'
         # 'mon/v20140624/hfss_Amon_reanalysis_MERRA_' + yrs +
         # '.nc' for yrs in [str(yr) + '01-' + str(yr) + '12'
                           # for yr in range(1979, 2012)]],
        ['/archive/pcmdi/repo/ana4MIPs/NASA-GMAO/MERRA/atmos/'
         'mon/v20140624/wap_Amon_reanalysis_MERRA_' + yrs +
         '.nc' for yrs in [str(yr) + '01-' + str(yr) + '12'
                           for yr in range(1979, 2012)]],
    ),
    data_in_dur=1,
    data_in_start_date=1979,
    data_in_end_date=2011,
    default_date_range=(1981, 2000),
    runs=[runs.merra],
    default_runs=[runs.merra]
)
cfsr = Model(
    name='cfsr',
    description='NCEP CFSR reanalyses',
    grid_file_paths=(
        ['/archive/pcmdi/repo/ana4MIPs/NOAA-NCEP/CFSR/atmos/'
         'mon/v20140822/zg_Amon_reanalysis_CFSR_' + yrs +
         '.nc' for yrs in [str(yr) + '01-' + str(yr) + '12'
                           for yr in range(1979, 2014)]],
        # ('/archive/pcmdi/repo/ana4MIPs/NOAA-NCEP/CFSR/atmos/'
         # 'mon/v20140822/rlut_Amon_reanalysis_CFSR_201201-201212.nc'),
    ),
    data_in_dur=1,
    data_in_start_date=1979,
    data_in_end_date=2013,
    default_date_range=(1981, 2000),
    runs=[runs.cfsr],
    default_runs=[runs.cfsr]
)
jra = Model(
    name='jra',
    description='JRA-25 reanalyses',
    grid_file_paths=('/archive/pcmdi/repo/ana4MIPs/JMA/JRA-25/atmos/mon/'
                   'v20140408/va_Amon_reanalysis_JRA-25_197901-201312.nc',),
    data_in_dur=1,
    data_in_start_date=1979,
    data_in_end_date=2013,
    default_date_range=(1979, 2013),
    runs=[runs.jra25]
)

# Evapotranspiration
landflux = Model(
    name='landflux-eval',
    description='LandFlux-EVAL evapotranspiration data, 1989-2005',
    grid_file_paths=('/archive/Spencer.Hill/obs/LandFlux-EVAL/'
                   'LandFluxEVAL.merged.89-05.monthly.all.nc',),
    data_in_dur=17,
    data_in_start_date=1989,
    data_in_end_date=2005,
    default_date_range=(1989, 2005),
    runs=[runs.lfe_all, runs.lfe_diag, runs.lfe_lsm, runs.lfe_rean],
    default_runs=[runs.lfe_all]
)
landflux95 = Model(
    name='landflux-eval95',
    description='LandFlux-EVAL evapotranspiration data, 1989-1995',
    grid_file_paths=('/archive/Spencer.Hill/obs/LandFlux-EVAL/'
                   'LandFluxEVAL.merged.89-95.monthly.all.nc',),
    data_in_dur=17,
    data_in_start_date=1989,
    data_in_end_date=1995,
    default_date_range=(1989, 1995),
    runs=[runs.lfe95_all, runs.lfe95_diag, runs.lfe95_lsm, runs.lfe95_rean],
    default_runs=[runs.lfe95_all]
)

# SST
hadisst = Model(
    name='hadisst',
    description='HadISST: Hadley Centre SST and sea ice obs datasets',
    grid_file_paths=('/archive/Spencer.Hill/obs/HadISST/HadISST_sst.nc',),
    data_in_dur=1,
    data_in_start_date=2005,
    data_in_end_date=2005,
    default_date_range=(2005, 2005),
    runs=[runs.hadisst1],
    default_runs=[runs.hadisst1]
)
hurrell = Model(
    name='hurrell',
    description='Hurrell SST observational dataset',
    grid_file_paths=('/archive/Spencer.Hill/obs/Hurrell/sst.climo.1981-2000.data.nc',),
    data_in_dur=1,
    data_in_start_date=2000,
    data_in_end_date=2000,
    default_date_range=(2000, 2000),
    runs=[runs.hurrell],
    default_runs=[runs.hurrell]
)
reynolds_oi = Model(
    name='reynolds_oi',
    description='Reynolds OI SST observational dataset',
    grid_file_paths=('/archive/Spencer.Hill/obs/ReynoldsOI/reyoi_sst.data.nc',),
    data_in_dur=19,
    data_in_start_date='1981-11',
    data_in_end_date='1999-01',
    default_date_range=(1982, 1998),
    runs=[runs.reynolds_oi],
    default_runs=[runs.reynolds_oi]
)
