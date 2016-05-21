"""Spencer Hill's aospy.Proj object for main GFDL GCM research."""
from aospy.proj import Proj
from aospy_user import regions, models


aero_3agcm = Proj(
    'aero_3agcm',
    direc_out='/archive/Spencer.Hill/aero_3agcm/',
    nc_dir_struc='gfdl',
    models=(
        models.am2,
        models.am3,
        models.hiram,
        models.hiram_c48,
        models.am4a1,
        models.am4c1,
        models.sm2,
        models.am3c90,
        models.am2p5,
        models.am4a2
    ),
    default_models=(
        models.am2,
        models.am3,
        models.hiram,
        models.hiram_c48
    ),
    regions=(
        regions.globe,
        regions.nh,
        regions.sh,
        regions.tropics,
        regions.wpwp,
        regions.epac,
        regions.sahel,
        regions.sahel2,
        regions.sahel3,
        regions.sahara,
        regions.ind_monsoon,
        regions.land,
        regions.ocean,
        regions.trop_land,
        regions.trop_ocean,
        regions.sahel_south,
        regions.sahel_north,
        regions.sahel_east,
        regions.sahel_west,
        regions.east_asia_monsoon,
        regions.china_east,
        regions.china_west,
    )
)
