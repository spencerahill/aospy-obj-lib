"""aospy.Run objects for simulations from various GFDL models."""
import datetime

from aospy import Run
from aospy.data_loader import GFDLDataLoader

# SM2.1
sm2_cont = Run(
    name='cont',
    data_loader=GFDLDataLoader(
        data_direc=('/archive/Yi.Ming/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie'
                    '_rerun6.YIM/pp'),
        data_dur=20,
        data_start_date=datetime.datetime(1, 1, 1),
        data_end_date=datetime.datetime(120, 12, 31),
    ),
)
sm2_aero = Run(
    name='aero',
    data_loader=GFDLDataLoader(
        data_direc=('/archive/Yi.Ming/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie2'
                    '_rerun6.YIM/pp'),
        data_dur=100,
        data_start_date=datetime.datetime(1, 1, 1),
        data_end_date=datetime.datetime(100, 12, 31),
    ),
)
sm2_gas = Run(
    name='gas',
    data_loader=GFDLDataLoader(
        data_direc=('/archive/Yi.Ming/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie3'
                    '_rerun8.YIM/pp'),
        data_dur=5,
        data_start_date=datetime.datetime(1, 1, 1),
        data_end_date=datetime.datetime(80, 12, 31),
    ),
)
sm2_both = Run(
    name='both',
    data_loader=GFDLDataLoader(
        data_direc=('/archive/Yi.Ming/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie4'
                    '_rerun6.YIM/pp'),
        data_dur=100,
        data_start_date=datetime.datetime(1, 1, 1),
        data_end_date=datetime.datetime(100, 12, 31),
    ),
)

# c48-HiRAM
hiram_c48_0 = Run(
    name='ming0',
    data_loader=GFDLDataLoader(
        data_direc=('/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0/'
                    'gfdl.ncrc2-intel-prod/pp'),
        data_start_date=datetime.datetime(1981, 1, 1),
        data_end_date=datetime.datetime(1995, 12, 31),
    ),
)
hiram_c48_0_p2K = Run(
    name='ming0_p2K',
    data_loader=GFDLDataLoader(
        template=hiram_c48_0.data_loader,
        data_direc=('/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0'
                    '_p2K/gfdl.ncrc2-intel-prod/pp'),
    ),
)
hiram_c48_1 = Run(
    name='ming1',
    data_loader=GFDLDataLoader(
        template=hiram_c48_0.data_loader,
        data_direc=('/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0b/'
                    'gfdl.ncrc2-intel-prod/pp'),
    ),
)
hiram_c48_1_p2K = Run(
    name='ming1_p2K',
    data_loader=GFDLDataLoader(
        template=hiram_c48_0.data_loader,
        data_direc=('/archive/Ming.Zhao/hiramdp/siena_201204/'
                    'c48l32_him_X0b_p2K/gfdl.ncrc2-intel-prod/pp'),
    ),
)
hiram_c48_2 = Run(
    name='ming2',
    data_loader=GFDLDataLoader(
        template=hiram_c48_0.data_loader,
        data_direc=('/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0e/'
                    'gfdl.ncrc2-intel-prod/pp'),
    ),
)
hiram_c48_2_p2K = Run(
    name='ming2_p2K',
    data_loader=GFDLDataLoader(
        template=hiram_c48_0.data_loader,
        data_direc=('/archive/Ming.Zhao/hiramdp/siena_201204/'
                    'c48l32_him_X0e_p2K/gfdl.ncrc2-intel-prod/pp'),
    ),
)
hiram_c48_3 = Run(
    name='ming3',
    data_loader=GFDLDataLoader(
        template=hiram_c48_0.data_loader,
        data_direc=('/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0f/'
                    'gfdl.ncrc2-intel-prod/pp'),
    ),
)
hiram_c48_3_p2K = Run(
    name='ming3_p2K',
    data_loader=GFDLDataLoader(
        template=hiram_c48_0.data_loader,
        data_direc=('/archive/Ming.Zhao/hiramdp/siena_201204/'
                    'c48l32_him_X0f_p2K/gfdl.ncrc2-intel-prod/pp'),
    ),
)
hiram_c48_4 = Run(
    name='ming4',
    data_loader=GFDLDataLoader(
        template=hiram_c48_0.data_loader,
        data_direc=('/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X0c/'
                    'gfdl.ncrc2-intel-prod/pp'),
    ),
)
hiram_c48_4_p2K = Run(
    name='ming4_p2K',
    data_loader=GFDLDataLoader(
        template=hiram_c48_0.data_loader,
        data_direc=('/archive/Ming.Zhao/hiramdp/siena_201204/'
                    'c48l32_him_X0c_p2K/gfdl.ncrc2-intel-prod/pp'),
    ),
)
hiram_c48_5 = Run(
    name='ming5',
    data_loader=GFDLDataLoader(
        template=hiram_c48_0.data_loader,
        data_direc=('/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X01/'
                    'gfdl.ncrc2-intel-prod/pp'),
    ),
)
hiram_c48_5_p2K = Run(
    name='ming5_p2K',
    data_loader=GFDLDataLoader(
        template=hiram_c48_0.data_loader,
        data_direc=('/archive/Ming.Zhao/hiramdp/siena_201204/'
                    'c48l32_him_X01_p2K/gfdl.ncrc2-intel-prod/pp'),
    ),
)
hiram_c48_6 = Run(
    name='ming6',
    data_loader=GFDLDataLoader(
        template=hiram_c48_0.data_loader,
        data_direc=('/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X02/'
                    'gfdl.ncrc2-intel-prod/pp'),
    ),
)
hiram_c48_6_p2K = Run(
    name='ming6_p2K',
    data_loader=GFDLDataLoader(
        template=hiram_c48_0.data_loader,
        data_direc=('/archive/Ming.Zhao/hiramdp/siena_201204/'
                    'c48l32_him_X02_p2K/gfdl.ncrc2-intel-prod/pp'),
    ),
)
hiram_c48_7 = Run(
    name='ming7',
    data_loader=GFDLDataLoader(
        template=hiram_c48_0.data_loader,
        data_direc=('/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X03/'
                    'gfdl.ncrc2-intel-prod/pp'),
    ),
)
hiram_c48_7_p2K = Run(
    name='ming7_p2K',
    data_loader=GFDLDataLoader(
        template=hiram_c48_0.data_loader,
        data_direc=('/archive/Ming.Zhao/hiramdp/siena_201204/'
                    'c48l32_him_X03_p2K/gfdl.ncrc2-intel-prod/pp'),
    ),
)
hiram_c48_8 = Run(
    name='ming8',
    data_loader=GFDLDataLoader(
        template=hiram_c48_0.data_loader,
        data_direc=('/archive/Ming.Zhao/hiramdp/siena_201204/c48l32_him_X04/'
                    'gfdl.ncrc2-intel-prod/pp'),
    ),
)
hiram_c48_8_p2K = Run(
    name='ming8_p2K',
    data_loader=GFDLDataLoader(
        template=hiram_c48_0.data_loader,
        data_direc=('/archive/Ming.Zhao/hiramdp/siena_201204/'
                    'c48l32_him_X04_p2K/gfdl.ncrc2-intel-prod/pp'),
    ),
)

# AM3_c90
am3c90_cont = Run(
    name='cont',
    data_loader=GFDLDataLoader(
        data_direc=('/archive/h1g/FMS/siena_201203/c90L48_am3p10_v6_clim/'
                    'gfdl.ncrc2-intel-prod-openmp/pp'),
        data_start_date=datetime.datetime(1981, 1, 1),
        data_end_date=datetime.datetime(1990, 12, 31),
    ),
)
am3c90_p2K = Run(
    name='p2K',
    data_loader=GFDLDataLoader(
        data_direc=('/archive/h1g/FMS/siena_201203/c90L48_am3p10_v6_clim_p2k/'
                    'gfdl.ncrc2-intel-prod-openmp/pp'),
        data_start_date=datetime.datetime(1981, 1, 1),
        data_end_date=datetime.datetime(1990, 12, 31),
    ),
)

# AM2.5
am2p5_cont = Run(
    name='cont',
    data_loader=GFDLDataLoader(
        data_direc=('/archive/miz/hiramdp/siena_201204/c180l32_am2_C0/'
                    'gfdl.ncrc2-intel-prod/pp'),
        data_dur=10,
        data_start_date=datetime.datetime(1981, 1, 1),
        data_end_date=datetime.datetime(2000, 12, 31),
    ),
)
am2p5_p2K = Run(
    name='p2K',
    data_loader=GFDLDataLoader(
        data_direc=('/archive/miz/hiramdp/siena_201204/c180l32_am2_C0_p2K/'
                    'gfdl.ncrc2-intel-prod/pp'),
        data_dur=10,
        data_start_date=datetime.datetime(1981, 1, 1),
        data_end_date=datetime.datetime(2000, 12, 31),
    ),
)

# AM4 prototypes
am4_a1c = Run(
    name='cont',
    data_loader=GFDLDataLoader(
        data_direc=('/archive/Ming.Zhao/awg/tikal_201403/c96L48_am4a1_'
                    '2000climo_highsen1/gfdl.ncrc2-intel-prod-openmp/pp'),
    ),
)
am4_a1p2k = Run(
    name='+2K',
    data_loader=GFDLDataLoader(
        data_direc=('/archive/Ming.Zhao/awg/tikal_201403/c96L48_am4a1_'
                    '2000climo_highsen1_p2K/gfdl.ncrc2-intel-prod-openmp/pp'),
    ),
)
am4_a2c = Run(
    name='cont',
    data_loader=GFDLDataLoader(
        data_direc=('/archive/cjg/awg/tikal_201403/c96L48_am4a2r1_'
                    '2000climo/gfdl.ncrc2-intel-prod-openmp/pp'),
    ),
)
am4_a2p2k = Run(
    name='+2K',
    data_loader=GFDLDataLoader(
        data_direc=('/archive/cjg/awg/tikal_201403/c96L48_am4a2r1_'
                    '2000climo_p2K/gfdl.ncrc2-intel-prod-openmp/pp'),
    ),
)
am4_c1c = Run(
    name='cont',
    data_loader=GFDLDataLoader(
        data_direc=('/archive/miz/tikal_201409_awgUpdates_mom6_2014.08.29/'
                    'c96L48_am4c1r2_2000climo/'
                    'gfdl.ncrc2-intel-prod-openmp/pp'),
    ),
)
am4_c1p2k = Run(
    name='+2K',
    data_loader=GFDLDataLoader(
        data_direc=('/archive/miz/tikal_201409_awgUpdates_mom6_2014.08.29/'
                    'c96L48_am4c1r2_2000climo_p2K/gfdl.ncrc2-intel-prod-'
                    'openmp/pp'),
    ),
)
