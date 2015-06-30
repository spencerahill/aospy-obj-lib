from aospy.model import Model
from aospy.utils import load_user_data

runs = load_user_data('runs')

am2 = Model(
    name='am2',
    nc_grid_paths=(
        ('/archive/s1h/am2/am2clim_reyoi/gfdl.ncrc2-default-prod/'
         'pp/atmos/atmos.static.nc'),
        # ['/archive/s1h/am2/am2clim_reyoi/gfdl.ncrc2-default-prod/pp/'
         # 'atmos/ts/monthly/1yr/atmos.' + str(n) + '01-' + str(n) +
         # '12.ucomp.nc' for n in range(1982, 2013)],
        ('/archive/yim/siena_201203/m45_am2p14_1990/gfdl.ncrc2-intel-prod/'
         'pp/atmos/ts/monthly/16yr/atmos.198301-199812.temp.nc'),
        ('/archive/s1h/am2/am2clim_reyoi/gfdl.ncrc2-default-prod/'
         'pp/atmos_level/atmos_level.static.nc'),
        ('/archive/s1h/am2/am2clim_reyoi/gfdl.ncrc2-default-prod/'
         'pp/atmos_level/ts/monthly/1yr/atmos_level.198201-198212.temp.nc'),
        ('/archive/s1h/am2/am2clim_reyoi/gfdl.ncrc2-default-prod/'
         'pp/atmos_level/ts/monthly/1yr/atmos_level.198201-198212.hght.nc')
    ),
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012),
    runs=[
        runs.am2_cont, runs.am2_aero, runs.am2_atm, runs.am2_amtm,
        runs.am2_gas, runs.am2_gtm, runs.am2_gmtm, runs.am2_aatl,
        runs.am2_aind, runs.am2_apac, runs.am2_noT, runs.am2_noT_p2K,
        runs.am2_amip, runs.am2_reyoi_cont, runs.am2_reyoi_m0p25,
        runs.am2_reyoi_m0p5, runs.am2_reyoi_m1, runs.am2_reyoi_m1p5,
        runs.am2_reyoi_m2, runs.am2_reyoi_m3, runs.am2_reyoi_m4,
        runs.am2_reyoi_p0p25, runs.am2_reyoi_p0p5, runs.am2_reyoi_p1,
        runs.am2_reyoi_p1p5, runs.am2_reyoi_p2, runs.am2_reyoi_p3,
        runs.am2_reyoi_p4, runs.am2_reyoi_p6, runs.am2_reyoi_p8,
        runs.am2_reyoi_m6, runs.am2_reyoi_m8, runs.am2_reyoi_m10,
        runs.am2_reyoi_p10, runs.am2_reyoi_wpwp_p2, runs.am2_reyoi_wpwp_m2,
        runs.am2_cld_lock_cont, runs.am2_cld_lock_p2,
        runs.am2_cld_lock_sst, runs.am2_cld_lock_cld, runs.am2_amip1,
        runs.am2_amip1_p2, runs.am2_reynolds, runs.am2_reynolds_p2,
        runs.am2_hurrell_cont, runs.am2_hurrell_p2,
        runs.am2_cld_seed_all_p2, runs.am2_cld_seed_np_p2,
        runs.am2_cld_seed_sp_p2, runs.am2_cld_seed_sa_p2
    ],
    default_runs=[runs.am2_reyoi_cont, runs.am2_reyoi_p2]
)
am3 = Model(
    name='am3',
    nc_grid_paths=(
        '/archive/s1h/am3/am3clim_hurrell/gfdl.ncrc2-intel-prod-openmp/'
        'pp/atmos/atmos.static.nc',
        ['/archive/s1h/am3/am3clim_hurrell/gfdl.ncrc2-intel-prod-openmp/pp/'
         'atmos/ts/monthly/1yr/atmos.' + str(n) + '01-' + str(n) +
         '12.ucomp.nc' for n in range(1980, 2011)]
    ),
    nc_dur=1,
    nc_start_yr=1980,
    nc_end_yr=2010,
    default_yr_range=(1981, 2010),
    runs=[
        runs.am3_cont, runs.am3_aero, runs.am3_atm, runs.am3_amtm,
        runs.am3_gas, runs.am3_gtm, runs.am3_gmtm, runs.am3_aatl,
        runs.am3_aind, runs.am3_apac, runs.am3_hc, runs.am3_hp1k,
        runs.am3_hp2k, runs.am3_hp4k, runs.am3_hp6k, runs.am3_hp8k,
        runs.am3_hp10k, runs.am3_hm1k, runs.am3_hm2k, runs.am3_hm4k,
        runs.am3_hm6k, runs.am3_hm8k, runs.am3_hm10k, runs.am3_hm15k,
        runs.am3_amip, runs.am3_hwpwp_p2k
    ],
    default_runs=[runs.am3_hc, runs.am3_hp2k]
)
hiram = Model(
    name='hiram',
    nc_grid_paths=(
        '/archive/yim/siena_201211/c180_hiram_clim/gfdl.ncrc2-default-prod/'
        'pp/atmos/atmos.static.nc',
        '/archive/yim/siena_201211/c180_hiram_clim/gfdl.ncrc2-default-prod/'
        'pp/atmos/ts/monthly/17yr/atmos.197901-199512.ucomp.nc'
    ),
    nc_dur=17,
    nc_start_yr=1979,
    nc_end_yr=1995,
    default_yr_range=(1979, 1995),
    runs=[
        runs.hiram_amip, runs.hiram_cont, runs.hiram_aero, runs.hiram_atm,
        runs.hiram_amtm, runs.hiram_gas, runs.hiram_gtm, runs.hiram_gmtm,
        runs.hiram_aatl, runs.hiram_aind, runs.hiram_apac
    ],
    default_runs=[runs.hiram_cont, runs.hiram_gtm]
)
sm2 = Model(
    name='sm2',
    description='AM2.1 atmosphere coupled to mixed-layer ocean.',
    nc_grid_paths=(
        '/archive/yim/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie_rerun6.YIM/pp/'
        'atmos/ts/monthly/100yr/atmos.000101-010012.vcomp.nc',
        '/archive/yim/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie_rerun6.YIM/pp/'
        'atmos/atmos.static.nc'
    ),
    nc_dur=20,
    nc_start_yr=1,
    default_yr_range=(61, 80),
    runs=[runs.sm2_cont, runs.sm2_aero, runs.sm2_gas, runs.sm2_both],
)
hiram_c48 = Model(
    name='hiram_mz',
    description=('Low resolution version of HiRAM used by Zhao 2014,'
                 ' J. Climate.'),
    nc_grid_paths=(
        '/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0/'
        'gfdl.ncrc2-intel-prod/pp/atmos/atmos.static.nc',
        '/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0/'
        'gfdl.ncrc2-intel-prod/pp/atmos/ts/monthly/15yr/'
        'atmos.198101-199512.ucomp.nc'
    ),
    nc_dur=15,
    nc_start_yr=1981,
    nc_end_yr=1995,
    default_yr_range=(1981, 1995),
    runs=[
        runs.hiram_c48_0, runs.hiram_c48_0_p2K, runs.hiram_c48_1,
        runs.hiram_c48_1_p2K, runs.hiram_c48_2, runs.hiram_c48_2_p2K,
        runs.hiram_c48_3, runs.hiram_c48_3_p2K, runs.hiram_c48_4,
        runs.hiram_c48_4_p2K, runs.hiram_c48_5, runs.hiram_c48_5_p2K,
        runs.hiram_c48_6, runs.hiram_c48_6_p2K, runs.hiram_c48_7,
        runs.hiram_c48_7_p2K, runs.hiram_c48_8, runs.hiram_c48_8_p2K
    ],
    default_runs=[runs.hiram_c48_0, runs.hiram_c48_0_p2K]
)
am3c90 = Model(
    name='am3c90',
    nc_grid_paths=(
        '/archive/h1g/FMS/siena_201203/c90L48_am3p10_v6_clim/gfdl.ncrc2-intel'
        '-prod-openmp/pp/atmos/atmos.static.nc',
        '/archive/h1g/FMS/siena_201203/c90L48_am3p10_v6_clim/gfdl.ncrc2-intel'
        '-prod-openmp/pp/atmos/ts/monthly/10yr/atmos.198101-199012.ucomp.nc'
    ),
    nc_dur=10,
    nc_start_yr=1981,
    nc_end_yr=1990,
    default_yr_range=(1981, 1990),
    runs=[runs.am3c90_cont, runs.am3c90_p2K]
)
am2p5 = Model(
    name='am2p5',
    nc_grid_paths=(
        '/archive/miz/hiramdp/siena_201204/c180l32_am2_C0/gfdl.ncrc2-intel-'
        'prod/pp/atmos/atmos.static.nc',
        ['/archive/miz/hiramdp/siena_201204/c180l32_am2_C0/gfdl.ncrc2-intel-'
         'prod/pp/atmos/ts/monthly/10yr/atmos.%04d01-%04d12.ucomp.nc'
         % (y1, y2) for (y1, y2) in zip((1981, 1991), (1990, 2000))]
    ),
    nc_dur=10,
    nc_start_yr=1981,
    nc_end_yr=2000,
    default_yr_range=(1981, 2000),
    runs=[runs.am2p5_cont, runs.am2p5_p2K]
)
am4a1 = Model(
    name='am4a1',
    nc_grid_paths=(
        '/archive/Ming.Zhao/awg/tikal_201403/c96L48_am4a1_'
        '2000climo_highsen1/gfdl.ncrc2-intel-prod-openmp/pp/atmos/'
        'atmos.static.nc',
        ['/archive/Ming.Zhao/awg/tikal_201403/c96L48_am4a1_'
         '2000climo_highsen1/gfdl.ncrc2-intel-prod-openmp/pp/atmos/'
         'ts/monthly/1yr/atmos.00%02d01-00%02d12.temp.nc' % (n, n)
         for n in range(2, 12)]
    ),
    nc_dur=1,
    nc_start_yr=2,
    nc_end_yr=11,
    default_yr_range=(2, 11),
    runs=[runs.am4_a1c, runs.am4_a1p2k]
)
am4a2 = Model(
    name='am4a2',
    nc_grid_paths=(
        '/archive/cjg/awg/tikal_201403/c96L48_am4a2r1_2000climo/gfdl.ncrc2-'
        'intel-prod-openmp/pp/atmos/atmos.static.nc',
        ['/archive/cjg/awg/tikal_201403/c96L48_am4a2r1_2000climo/gfdl.ncrc2-'
         'intel-prod-openmp/pp/atmos/ts/monthly/5yr/atmos.00%02d01-00%02d12.'
         'ucomp.nc' % (y1, y2) for (y1, y2) in zip((2, 7), (6, 11))]
    ),
    nc_dur=5,
    nc_start_yr=2,
    nc_end_yr=11,
    default_yr_range=(2, 11),
    runs=[runs.am4_a2c, runs.am4_a2p2k]
)
am4c1 = Model(
    name='am4c1',
    nc_grid_paths=(
        '/archive/miz/tikal_201409_awgUpdates_mom6_2014.08.29/'
        'c96L48_am4c1r2_2000climo/gfdl.ncrc2-intel-prod-openmp/pp/'
        'atmos/atmos.static.nc',
        '/archive/miz/tikal_201409_awgUpdates_mom6_2014.08.29/'
        'c96L48_am4c1r2_2000climo/gfdl.ncrc2-intel-prod-openmp/pp/'
        'atmos/ts/monthly/10yr/atmos.000101-001012.temp.nc'
    ),
    nc_dur=10,
    nc_start_yr=1,
    nc_end_yr=10,
    default_yr_range=(1, 10),
    runs=[runs.am4_c1c, runs.am4_c1p2k]
)
