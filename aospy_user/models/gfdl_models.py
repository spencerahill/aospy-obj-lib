"""aospy.Model objects associated w/ GFDL climate models."""
import datetime

from aospy import Model

from .. import runs


am2 = Model(
    name='am2',
    grid_file_paths=(
        ('/archive/Spencer.Hill/am2/am2clim_reyoi/gfdl.ncrc2-default-prod/'
         'pp/atmos/atmos.static.nc'),
        ('/archive/Spencer.Hill/am2/am2clim_reyoi/gfdl.ncrc2-default-prod/'
         'pp/atmos_level/ts/monthly/30yr/atmos_level.198301-201212.temp.nc'),
        ('/archive/Spencer.Hill/am2/am2clim_reyoi/gfdl.ncrc2-default-prod/'
         'pp/atmos/ts/monthly/30yr/atmos.198301-201212.temp.nc'),
    ),
    default_start_date=datetime.datetime(1982, 1, 1),
    default_end_date=datetime.datetime(2012, 12, 31),
    runs={
        runs.am2_cont,
        runs.am2_aero,
        runs.am2_atm,
        runs.am2_amtm,
        runs.am2_gas,
        runs.am2_gtm,
        runs.am2_gmtm,
        runs.am2_aatl,
        runs.am2_aind,
        runs.am2_apac,
        runs.am2_noT,
        runs.am2_noT_p2K,
        runs.am2_amip,
        runs.am2_reyoi_cont,
        runs.am2_reyoi_m0p25,
        runs.am2_reyoi_m0p5,
        runs.am2_reyoi_m1,
        runs.am2_reyoi_m1p5,
        runs.am2_reyoi_m2,
        runs.am2_reyoi_m3,
        runs.am2_reyoi_m4,
        runs.am2_reyoi_p0p25,
        runs.am2_reyoi_p0p5,
        runs.am2_reyoi_p1,
        runs.am2_reyoi_p1p5,
        runs.am2_reyoi_p2,
        runs.am2_reyoi_p3,
        runs.am2_reyoi_p4,
        runs.am2_reyoi_p6,
        runs.am2_reyoi_p8,
        runs.am2_reyoi_m6,
        runs.am2_reyoi_m8,
        runs.am2_reyoi_m10,
        runs.am2_reyoi_m15,
        runs.am2_reyoi_p10,
        runs.am2_reyoi_wpwp_p2,
        runs.am2_reyoi_wpwp_m2,
        runs.am2_reyoi_uw,
        runs.am2_reyoi_uw_p2,
        runs.am2_reyoi_uw_p5,
        runs.am2_reyoi_uw_p10,
        runs.am2_reyoi_uw_m2,
        runs.am2_reyoi_uw_m5,
        runs.am2_reyoi_uw_m10,
        runs.am2_reyoi_uw_lo_0p5,
        runs.am2_reyoi_uw_lo_0p5_p2k,
        runs.am2_reyoi_uw_lo_0p5_p4k,
        runs.am2_reyoi_uw_lo_0p5_p6k,
        runs.am2_reyoi_uw_lo_0p5_p8k,
        runs.am2_reyoi_uw_lo_0p5_p10k,
        runs.am2_reyoi_uw_lo_0p5_m2k,
        runs.am2_reyoi_uw_lo_0p5_m4k,
        runs.am2_reyoi_uw_lo_0p5_m6k,
        runs.am2_reyoi_uw_lo_0p5_m8k,
        runs.am2_reyoi_uw_lo_0p5_m10k,
        runs.am2_reyoi_uw_lo_0p25,
        runs.am2_reyoi_uw_lo_0p25_p2k,
        runs.am2_cld_lock_cont,
        runs.am2_cld_lock_p2,
        runs.am2_cld_lock_sst,
        runs.am2_cld_lock_cld,
        runs.am2_amip1,
        runs.am2_amip1_p2,
        runs.am2_reynolds,
        runs.am2_reynolds_p2,
        runs.am2_hurrell_cont,
        runs.am2_hurrell_p2,
        runs.am2_cld_seed_all_p2,
        runs.am2_cld_seed_np_p2,
        runs.am2_cld_seed_sp_p2,
        runs.am2_cld_seed_sa_p2,
        runs.am2_zshen_cont,
        runs.am2_atmos_heat_wpwp,
        runs.am2_atmos_heat_wpwp_small,
        runs.am2_reyoi_w_ice,
        runs.am2_test,
    },
    default_runs={
        runs.am2_reyoi_cont,
        runs.am2_reyoi_p2
    }
)
am3 = Model(
    name='am3',
    grid_file_paths=(
        ('/archive/Spencer.Hill/am3/am3clim_hurrell/gfdl.ncrc2-intel-prod-'
         'openmp/pp/atmos/atmos.static.nc'),
        ('/archive/Spencer.Hill/am3/am3clim_hurrell/gfdl.ncrc2-intel-prod-'
         'openmp/pp/atmos/ts/monthly/1yr/atmos.198101-198112.ucomp.nc'),
        ('/archive/Spencer.Hill/am3/am3clim_hurrell/gfdl.ncrc2-intel-prod-'
         'openmp/pp/atmos_level/ts/monthly/1yr/'
         'atmos_level.198101-198112.ucomp.nc')
    ),
    default_start_date=datetime.datetime(1981, 1, 1),
    default_end_date=datetime.datetime(2010, 12, 31),
    runs={
        runs.am3_cont,
        runs.am3_aero,
        runs.am3_atm,
        runs.am3_amtm,
        runs.am3_gas,
        runs.am3_gtm,
        runs.am3_gmtm,
        runs.am3_aatl,
        runs.am3_aind,
        runs.am3_apac,
        runs.am3_hc,
        runs.am3_hp1k,
        runs.am3_hp2k,
        runs.am3_hp4k,
        runs.am3_hp6k,
        runs.am3_hp8k,
        runs.am3_hp10k,
        runs.am3_hm1k,
        runs.am3_hm2k,
        runs.am3_hm4k,
        runs.am3_hm6k,
        runs.am3_hm8k,
        runs.am3_hm10k,
        runs.am3_hm15k,
        # runs.am3_amip,
        runs.am3_hwpwp_p2k,
        runs.am3_hc_static_veg,
        runs.am3_hc_static_veg_p4k,
        runs.am3_hc_static_veg_10kyr,
    },
    default_runs={
        runs.am3_hc,
        runs.am3_hp2k,
    }
)
hiram = Model(
    name='hiram',
    grid_file_paths=(
        '/archive/Yi.Ming/siena_201211/c180_hiram_clim/gfdl.ncrc2-default-prod/'
        'pp/atmos/atmos.static.nc',
        '/archive/Yi.Ming/siena_201211/c180_hiram_clim/gfdl.ncrc2-default-prod/'
        'pp/atmos/ts/monthly/17yr/atmos.197901-199512.ucomp.nc'
    ),
    default_start_date=datetime.datetime(1979, 1, 1),
    default_end_date=datetime.datetime(1995, 12, 31),
    runs={
        # runs.hiram_amip,
        runs.hiram_cont,
        runs.hiram_aero,
        runs.hiram_atm,
        runs.hiram_amtm,
        runs.hiram_gas,
        runs.hiram_gtm,
        runs.hiram_gmtm,
        runs.hiram_aatl,
        runs.hiram_aind,
        runs.hiram_apac,
    },
    default_runs={
        runs.hiram_cont,
        runs.hiram_gtm,
    }
)
sm2 = Model(
    name='sm2',
    description='AM2.1 atmosphere coupled to mixed-layer ocean.',
    grid_file_paths=(
        '/archive/Yi.Ming/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie_rerun6.YIM/pp/'
        'atmos/ts/monthly/100yr/atmos.000101-010012.vcomp.nc',
        '/archive/Yi.Ming/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie_rerun6.YIM/pp/'
        'atmos/atmos.static.nc'
    ),
    default_start_date=datetime.datetime(61, 1, 1),
    default_end_date=datetime.datetime(80, 12, 31),
    runs={
        runs.sm2_cont,
        runs.sm2_aero,
        runs.sm2_gas,
        runs.sm2_both,
    },
)
hiram_c48 = Model(
    name='hiram_mz',
    description=('Low resolution version of HiRAM used by Zhao 2014,'
                 ' J. Climate.'),
    grid_file_paths=(
        '/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0/'
        'gfdl.ncrc2-intel-prod/pp/atmos/atmos.static.nc',
        '/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0/'
        'gfdl.ncrc2-intel-prod/pp/atmos/ts/monthly/15yr/'
        'atmos.198101-199512.ucomp.nc'
    ),
    default_start_date=datetime.datetime(1981, 1, 1),
    default_end_date=datetime.datetime(1995, 12, 31),
    runs={
        runs.hiram_c48_0,
        runs.hiram_c48_0_p2K,
        runs.hiram_c48_1,
        runs.hiram_c48_1_p2K,
        runs.hiram_c48_2,
        runs.hiram_c48_2_p2K,
        runs.hiram_c48_3,
        runs.hiram_c48_3_p2K,
        runs.hiram_c48_4,
        runs.hiram_c48_4_p2K,
        runs.hiram_c48_5,
        runs.hiram_c48_5_p2K,
        runs.hiram_c48_6,
        runs.hiram_c48_6_p2K,
        runs.hiram_c48_7,
        runs.hiram_c48_7_p2K,
        runs.hiram_c48_8,
        runs.hiram_c48_8_p2K,
    },
    default_runs={
        runs.hiram_c48_0,
        runs.hiram_c48_0_p2K,
    }
)
am3c90 = Model(
    name='am3c90',
    grid_file_paths=(
        '/archive/h1g/FMS/siena_201203/c90L48_am3p10_v6_clim/gfdl.ncrc2-intel'
        '-prod-openmp/pp/atmos/atmos.static.nc',
        '/archive/h1g/FMS/siena_201203/c90L48_am3p10_v6_clim/gfdl.ncrc2-intel'
        '-prod-openmp/pp/atmos/ts/monthly/10yr/atmos.198101-199012.ucomp.nc'
    ),
    default_start_date=datetime.datetime(1981, 1, 1),
    default_end_date=datetime.datetime(1990, 12, 31),
    runs={
        runs.am3c90_cont,
        runs.am3c90_p2K,
    },
    default_runs={
        runs.am3c90_cont,
        runs.am3c90_p2K,
    }
)
am2p5 = Model(
    name='am2p5',
    # The atmos.static.nc in the actual AM2.5 data directories has the wrong
    # horizontal resolution, so use the one from HiRAM, which matches the
    # actual AM2.5 resolution.
    grid_file_paths=(
        '/archive/Yi.Ming/siena_201211/c180_hiram_clim/'
        'gfdl.ncrc2-default-prod/pp/atmos/atmos.static.nc',
        ['/archive/miz/hiramdp/siena_201204/c180l32_am2_C0/gfdl.ncrc2-intel-'
         'prod/pp/atmos/ts/monthly/10yr/atmos.%04d01-%04d12.ucomp.nc'
         % (y1, y2) for (y1, y2) in zip((1981, 1991), (1990, 2000))]
    ),
    default_start_date=datetime.datetime(1981, 1, 1),
    default_end_date=datetime.datetime(2000, 12, 31),
    runs={
        runs.am2p5_cont,
        runs.am2p5_p2K,
    },
    default_runs={
        runs.am2p5_cont,
        runs.am2p5_p2K,
    }
)
am4a1 = Model(
    name='am4a1',
    grid_file_paths=(
        '/archive/Ming.Zhao/awg/tikal_201403/c96L48_am4a1_'
        '2000climo_highsen1/gfdl.ncrc2-intel-prod-openmp/pp/atmos/'
        'atmos.static.nc',
        ['/archive/Ming.Zhao/awg/tikal_201403/c96L48_am4a1_'
         '2000climo_highsen1/gfdl.ncrc2-intel-prod-openmp/pp/atmos/'
         'ts/monthly/1yr/atmos.00%02d01-00%02d12.temp.nc' % (n, n)
         for n in range(2, 12)]
    ),
    default_start_date=datetime.datetime(2, 1, 1),
    default_end_date=datetime.datetime(11, 12, 31),
    runs={
        runs.am4_a1c,
        runs.am4_a1p2k,
    }
)
am4a2 = Model(
    name='am4a2',
    grid_file_paths=(
        '/archive/cjg/awg/tikal_201403/c96L48_am4a2r1_2000climo/gfdl.ncrc2-'
        'intel-prod-openmp/pp/atmos/atmos.static.nc',
        ['/archive/cjg/awg/tikal_201403/c96L48_am4a2r1_2000climo/gfdl.ncrc2-'
         'intel-prod-openmp/pp/atmos/ts/monthly/5yr/atmos.00%02d01-00%02d12.'
         'ucomp.nc' % (y1, y2) for (y1, y2) in zip((2, 7), (6, 11))]
    ),
    default_start_date=datetime.datetime(2, 1, 1),
    default_end_date=datetime.datetime(11, 12, 31),
    runs={
        runs.am4_a2c,
        runs.am4_a2p2k,
    }
)
am4c1 = Model(
    name='am4c1',
    grid_file_paths=(
        '/archive/miz/tikal_201409_awgUpdates_mom6_2014.08.29/'
        'c96L48_am4c1r2_2000climo/gfdl.ncrc2-intel-prod-openmp/pp/'
        'atmos/atmos.static.nc',
        '/archive/miz/tikal_201409_awgUpdates_mom6_2014.08.29/'
        'c96L48_am4c1r2_2000climo/gfdl.ncrc2-intel-prod-openmp/pp/'
        'atmos/ts/monthly/10yr/atmos.000101-001012.temp.nc'
    ),
    default_start_date=datetime.datetime(1, 1, 1),
    default_end_date=datetime.datetime(10, 12, 31),
    runs={
        runs.am4_c1c,
        runs.am4_c1p2k,
    }
)
