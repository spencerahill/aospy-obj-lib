#! /usr/bin/env python
"""Main script for automating computations using aospy."""
import itertools

import colorama

import aospy
import aospy_user


class MainParams(object):
    """Container for parameters specified in main routine."""
    pass


class MainParamsParser(object):
    """Interface between specified parameters and resulting CalcSuite."""
    def str_to_aospy_obj(self, proj, model, var, region):
        proj_out = aospy_user.to_proj(proj)
        model_out = aospy_user.to_model(model, proj_out)
        var_out = aospy_user.to_var(var)
        region_out = aospy_user.to_region(region, proj=proj_out)
        return proj_out, model_out, var_out, region_out

    def aospy_obj_to_iterable(self, proj, model, var, region):
        return [aospy_user.to_iterable(obj)
                for obj in (proj, model, var, region)]

    def str_to_aospy_iterable(self, proj, model, var, region):
        projo, modelo, varo, regiono = self.str_to_aospy_obj(proj, model,
                                                             var, region)
        return self.aospy_obj_to_iterable(projo, modelo, varo, regiono)

    def create_child_run_obj(self, models, runs, proj):
        """Create child Run object(s) for each Model object."""
        run_objs = []
        for model in models:
            for run in runs:
                try:
                    run_objs.append(aospy_user.to_run(run, model, proj))
                except AttributeError as ae:
                    print ae
        if len(run_objs) == 1 and not isinstance(run_objs[0], (list, tuple)):
            return run_objs
        else:
            return list(itertools.chain.from_iterable(run_objs))

    def __init__(self, main_params):
        """Turn all inputs into aospy-ready objects."""
        self.__dict__ = vars(main_params)
        self.proj, self.model, self.var, self.region = (
            self.str_to_aospy_iterable(main_params.proj, main_params.model,
                                       main_params.var, main_params.region)
            )
        self.run = self.create_child_run_obj(self.model, self.run, self.proj)
        print self.run
        self.region = [aospy.utils.dict_name_keys(self.region)]


class CalcSuite(object):
    """Creates suite of Calc objects based on inputted specifications. """
    def __init__(self, calc_suite_interface):
        self.__dict__ = vars(calc_suite_interface)

    def print_params(self):
        pairs = (
            ('Project', self.proj),
            ('Models', self.model),
            ('Runs', self.run),
            ('Ensemble members', self.ens_mem),
            ('Variables', self.var),
            ('Year ranges', self.yr_range),
            ('Geographical regions', [r.values() for r in self.region]),
            ('Time interval of input data', self.intvl_in),
            ('Time interval for averaging', self.intvl_out),
            ('Input data time type', self.dtype_in_time),
            ('Input data vertical type', self.dtype_in_vert),
            ('Output data time type', self.dtype_out_time),
            ('Output data vertical type', self.dtype_out_vert),
            ('Vertical levels', self.level),
            ('Year chunks', self.yr_chunk_len),
            ('Compute this data', self.compute),
            ('Print this data', self.print_table)
        )
        print ''
        colorama.init()
        color_left = colorama.Fore.BLUE
        color_right = colorama.Fore.RESET
        for left, right in pairs:
            print color_left, left, ':', color_right, right
        print colorama.Style.RESET_ALL

    def prompt_user_verify(self):
        if not raw_input("Proceed using these parameters? ").lower() == 'y':
            raise IOError('\nExecution cancelled by user.')
        print '\n\tVariable time averages and statistics:'

    def create_params_all_calcs(self):
        attr_names = ('proj',
                      'model',
                      'run',
                      'ens_mem',
                      'var',
                      'yr_range',
                      'level',
                      'region',
                      'intvl_in',
                      'intvl_out',
                      'dtype_in_time',
                      'dtype_out_time',
                      'dtype_in_vert',
                      'dtype_out_vert',
                      'verbose',
                      'yr_chunk_len')
        attrs = tuple([getattr(self, name) for name in attr_names])

        # Each permutation becomes a dictionary, with the keys being the attr
        # names and the values being the corresponding value for that
        # permutation.  These dicts can then be directly passed to the
        # CalcInterface class to make the Calc objects.
        permuter = itertools.product(*attrs)
        param_combos = []
        for permutation in permuter:
            param_combos.append(dict(zip(attr_names, permutation)))
        return param_combos

    def create_calcs(self, param_combos):
        """Iterate through given parameter combos, creating needed Calcs."""
        calcs = []
        for params in param_combos:
            try:
                calc_int = aospy.CalcInterface(**params)
            except AttributeError as ae:
                print ae
            else:
                calc = aospy.Calc(calc_int)
                calcs.append(calc)
        return calcs

    def exec_calcs(self, calcs):
        return [calc.compute() for calc in calcs]

    def print_results(self, calcs):
        for calc in calcs:
            for region in calc.region.values():
                print [calc.load(self.dtype_out_time[0],
                                 # dtype_out_vert=params[-2],
                                 region=region, plot_units=True)]


def main(main_params):
    """Main script for interfacing with aospy."""
    # Instantiate objects and load default/all models, runs, and regions.
    cs = CalcSuite(MainParamsParser(main_params))
    cs.print_params()
    cs.prompt_user_verify()
    param_combos = cs.create_params_all_calcs()
    calcs = cs.create_calcs(param_combos)
    print '\n\tVariable time averages and statistics:'
    if main_params.compute:
        cs.exec_calcs(calcs)
    if main_params.print_table[0]:
        cs.print_results(calcs)
    print "Calculations finished."
    return calcs

if __name__ == '__main__':
    mp = MainParams()
    mp.proj = 'aero_3agcm'
    mp.model = ['am2', 'am3']
    mp.run = ['reyoi_cont']
    mp.ens_mem = [None]
    mp.var = ['t_surf']
    # mp.yr_range = [(1983, 1983)]
    mp.yr_range = ['default']
    mp.region = 'all'
    mp.intvl_in = ['monthly']
    mp.intvl_out = ['jas']
    mp.dtype_in_time = ['ts']
    # mp.dtype_in_vert = [False]
    mp.dtype_in_vert = ['pressure']
    # mp.dtype_out_time = [('reg.av',)]
    mp.dtype_out_time = [('av', 'std', 'reg.av', 'reg.ts', 'reg.std')]
    mp.dtype_out_vert = [False]
    # mp.dtype_out_vert = ['vert_int']
    mp.level = [False]
    mp.yr_chunk_len = [False]
    mp.compute = [True]
    mp.verbose = [True]
    mp.print_table = [False]

    calcs = main(mp)
