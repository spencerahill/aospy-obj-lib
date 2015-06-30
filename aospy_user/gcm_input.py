"""gcm_input: An aospy.Proj: for creating input files for GCM simulations"""
from aospy import Proj, Model, Run
from aospy.utils import _set_named_attr_dict, _load_user_data

regions = _load_user_data('regions')
variables = _load_user_data('variables')

gcmi = Proj(
    'gcm_input',
    vars=variables.master_vars_list,
    direc_out='/archive/s1h/gcm_input',
    nc_dir_struc='one_dir',
)



if __name__ == '__main__':
    pass
