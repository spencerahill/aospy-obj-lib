from aospy.proj import Proj
from aospy.utils import _set_named_attr_dict, _load_user_data

regions = _load_user_data('regions')
models = _load_user_data('models')
variables = _load_user_data('variables')

a3gcm = Proj(
    'aero_3agcm',
    vars=variables.master_vars_list,
    direc_out='/archive/s1h/aero_3agcm/',
    nc_dir_struc='gfdl',
)

_set_named_attr_dict(a3gcm, 'models', [
    models.am2, models.am3, models.hiram, models.hiram_c48, models.am4a1,
    models.am4c1, models.sm2, models.am3c90, models.am2p5, models.am4a2
])
_set_named_attr_dict(a3gcm, 'default_models', [
                     models.am2, models.am3, models.hiram, models.hiram_c48
])

a3gcm.regions = [
    regions.globe, regions.nh, regions.sh, regions.tropics, regions.wpwp,
    regions.epac, regions.sahel, regions.sahel2, regions.sahel3,
    regions.sahara, regions.ind_monsoon, regions.land, regions.ocean,
    regions.trop_land, regions.trop_ocean, regions.sahel_south,
    regions.sahel_north, regions.sahel_east, regions.sahel_west
]

def aero_3agcm():
    return a3gcm
