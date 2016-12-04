"""gcm_input: An aospy.Proj for creating input files for GCM simulations"""
from aospy import Proj
from aospy_user import regions, models


gcm_input = Proj(
    'gcm_input',
    direc_out='/work/Spencer.Hill/',
    tar_direc_out='/archive/Spencer.Hill/',
    nc_dir_struc='one_dir',
    models=(
        models.am2,
        models.am3,
        models.hiram
    ),
    default_models=(
        models.am2,
        models.am3,
        models.hiram
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
        regions.sahel_west
    )
)
