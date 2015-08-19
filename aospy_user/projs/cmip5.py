"""Spencer Hill's aospy.Proj object for CMIP5 data."""
from aospy.proj import Proj
from aospy_user import regions, models, variables


cmip5 = Proj(
    'cmip5',
    vars=variables.master_vars_list,
    direc_out='/archive/s1h/cmip5/',
    nc_dir_struc='one_dir',
    models=(
        models.gfdl_cm3,
    ),
    default_models='all',
    regions=(
        regions.globe, regions.nh, regions.sh, regions.tropics, regions.wpwp,
        regions.epac, regions.sahel, regions.sahel2, regions.sahel3,
        regions.sahara, regions.ind_monsoon, regions.land, regions.ocean,
        regions.trop_land, regions.trop_ocean, regions.sahel_south,
        regions.sahel_north, regions.sahel_east, regions.sahel_west
    )
)
