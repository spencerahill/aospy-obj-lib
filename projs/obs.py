"""Spencer Hill's aospy.Proj object for observational data."""
from aospy.proj import Proj
from aospy.utils import load_user_data

regions = load_user_data('regions')
models = load_user_data('models')
variables = load_user_data('variables')


obs = Proj(
    name='obs',
    vars=variables.master_vars_list,
    direc_out='/archive/s1h/obs/',
    models=(
        models.cru, models.prec_l, models.gpcp, models.ceres, models.trmm,
        models.cmap, models.udel, models.merra, models.era, models.jra,
        models.cfsr, models.landflux, models.landflux95
    ),
    default_models=(
        models.cru, models.prec_l, models.gpcp,
        models.trmm, models.cmap, models.udel
    ),
    regions=(
        regions.globe, regions.nh, regions.sh, regions.tropics, regions.wpwp,
        regions.epac, regions.sahel, regions.sahel2, regions.sahel3,
        regions.sahara, regions.ind_monsoon, regions.land, regions.ocean,
        regions.trop_land, regions.trop_ocean, regions.sahel_south,
        regions.sahel_north, regions.sahel_east, regions.sahel_west
    )
)
