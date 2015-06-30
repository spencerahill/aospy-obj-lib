"""gcm_input: An aospy.Proj for creating input files for GCM simulations"""
from aospy import Proj, Model, Run
from aospy_user import regions, models, variables


gcm_input = Proj(
    'gcm_input',
    vars=variables.master_vars_list,
    direc_out='/archive/s1h/gcm_input',
    nc_dir_struc='one_dir',
    models=(models.am2, models.am3, models.hiram),
    default_models=(models.am2, models.am3, models.hiram),
    regions=(
        regions.globe, regions.nh, regions.sh, regions.tropics, regions.wpwp,
        regions.epac, regions.sahel, regions.sahel2, regions.sahel3,
        regions.sahara, regions.ind_monsoon, regions.land, regions.ocean,
        regions.trop_land, regions.trop_ocean, regions.sahel_south,
        regions.sahel_north, regions.sahel_east, regions.sahel_west
    )
)
