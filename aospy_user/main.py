#! /usr/bin/env python
"""Main script for automating computations using aospy."""
from __future__ import print_function
import itertools

import aospy
import colorama

from aospy_user import projs, variables


class MainParams(object):
    """Container for parameters specified in main routine."""
    pass


class MainParamsParser(object):
    """Interface between specified parameters and resulting CalcSuite."""
    def str_to_aospy_obj(self, proj, model, var, region):
        proj_out = aospy.to_proj(proj, self.projs)
        model_out = aospy.to_model(model, proj_out, self.projs)
        var_out = aospy.to_var(var, variables)
        region_out = aospy.to_region(region, self.projs, proj=proj_out)
        return proj_out, model_out, var_out, region_out

    def aospy_obj_to_iterable(self, proj, model, var, region):
        return [aospy.to_iterable(obj) for obj in (proj, model, var, region)]

    def str_to_aospy_iterable(self, proj, model, var, region):
        p, m, v, r = self.str_to_aospy_obj(proj, model, var, region)
        return self.aospy_obj_to_iterable(p, m, v, r)

    def create_child_run_obj(self, models, runs, proj):
        """Create child Run object(s) for each Model object."""
        run_objs = []
        for model in models:
            for run in runs:
                try:
                    run_objs.append(aospy.to_run(run, model, proj, self.projs))
                except AttributeError as ae:
                    print(ae)
        # If flat list, return the list.  If nested, then flatten it.
        if all([isinstance(r, aospy.Run) for r in run_objs]):
            return run_objs
        return list(itertools.chain.from_iterable(run_objs))

    def __init__(self, main_params, projs):
        """Turn all inputs into aospy-ready objects."""
        self.__dict__ = vars(main_params)
        self.projs = projs
        self.proj, self.model, self.var, self.region = (
            self.str_to_aospy_iterable(main_params.proj, main_params.model,
                                       main_params.var, main_params.region)
            )
        self.run = self.create_child_run_obj(self.model, self.run, self.proj)
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
            ('Year ranges', self.date_range),
            ('Geographical regions', [r.values() for r in self.region]),
            ('Time interval of input data', self.intvl_in),
            ('Time interval for averaging', self.intvl_out),
            ('Input data time type', self.dtype_in_time),
            ('Input data vertical type', self.dtype_in_vert),
            ('Output data time type', self.dtype_out_time),
            ('Output data vertical type', self.dtype_out_vert),
            ('Vertical levels', self.level),
            ('Year chunks', self.chunk_len),
            ('Compute this data', self.compute),
            ('Print this data', self.print_table)
        )
        print('')
        colorama.init()
        color_left = colorama.Fore.BLUE
        color_right = colorama.Fore.RESET
        for left, right in pairs:
            print(color_left, left, ':', color_right, right)
        print(colorama.Style.RESET_ALL)

    def prompt_user_verify(self):
        try:
            input = raw_input
        except NameError:
            import builtins
            input = builtins.input
        if not input("Perform these computations? ").lower() in ('y', 'yes'):
            raise IOError('\n', 'Execution cancelled by user.')

    def create_params_all_calcs(self):
        attr_names = ('proj',
                      'model',
                      'run',
                      'ens_mem',
                      'var',
                      'date_range',
                      'level',
                      'region',
                      'intvl_in',
                      'intvl_out',
                      'dtype_in_time',
                      'dtype_out_time',
                      'dtype_in_vert',
                      'dtype_out_vert',
                      'verbose',
                      'chunk_len')
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

    def create_calcs(self, param_combos, exec_calcs=False, print_table=False):
        """Iterate through given parameter combos, creating needed Calcs."""
        calcs = []
        for params in param_combos:
            try:
                ci = aospy.CalcInterface(**params)
            # except AttributeError as ae:
                # print('aospy warning:', ae)
            except:
                raise
            else:
                calc = aospy.Calc(ci)
                if exec_calcs:
                    try:
                        calc.compute()
                    except:
                        raise
                        # print('Calc {} failed.  Skipping.'.format(calc))
                    else:
                        if print_table:
                            print("{}".format(calc.load('reg.av', False,
                                                        ci.region['sahel'],
                                                        plot_units=False)))
                calcs.append(calc)
        return calcs

    def exec_calcs(self, calcs):
        return [calc.compute() for calc in calcs]

    def print_results(self, calcs):
        for calc in calcs:
            for region in calc.region.values():
                print([calc.load(self.dtype_out_time[0],
                                 # dtype_out_vert=params[-2],
                                 region=region, plot_units=True)])


def main(main_params):
    """Main script for interfacing with aospy."""
    # Instantiate objects and load default/all models, runs, and regions.
    cs = CalcSuite(MainParamsParser(main_params, projs))
    cs.print_params()
    try:
        cs.prompt_user_verify()
    except IOError as e:
        print(e)
        return
    param_combos = cs.create_params_all_calcs()
    calcs = cs.create_calcs(param_combos, exec_calcs=True, print_table=True)
    return calcs

if __name__ == '__main__':
    mp = MainParams()
    mp.proj = 'aero_3agcm'
    mp.model = 'am2'
    mp.run = ['reyoi_cont', 'reyoi+2K', 'hurrell_cont', 'hurrell+2K']
    mp.ens_mem = [False]
    mp.var = ['energy_column_divg_adj', 'energy_column_source']
    mp.date_range = [('1983-01-01', '2012-12-31')]
    # mp.date_range = [('1983-01-01', '1983-12-31')]
    # mp.date_range = ['default']
    mp.region = 'all'
    mp.intvl_in = ['monthly']
    # mp.intvl_in = ['3hr']
    mp.intvl_out = ['jas']
    mp.dtype_in_time = ['ts']
    # mp.dtype_in_time = ['inst']
    # mp.dtype_in_vert = [False]
    mp.dtype_in_vert = ['sigma']
    # mp.dtype_in_vert = ['pressure']
    # mp.dtype_out_time = [('av', 'eddy.av', 'eddy.reg.av', 'reg.av')]
    mp.dtype_out_time = [('av', 'std', 'reg.av', 'reg.ts', 'reg.std')]
    # mp.dtype_out_time = [(
        # 'av', 'std', 'reg.av', 'reg.ts', 'reg.std', 'eddy.av', 'eddy.std',
        # 'eddy.reg.av', 'eddy.reg.ts', 'eddy.reg.std', 'time-mean.av',
        # 'time-mean.std', 'time-mean.reg.av', 'time-mean.reg.std',
        # 'time-mean.reg.ts'
    # )]
    # mp.dtype_out_vert = [False]
    mp.dtype_out_vert = ['vert_int']
    # mp.dtype_out_vert = [False, 'vert_int']
    mp.level = [False]
    mp.chunk_len = [False]
    mp.verbose = [True]
    mp.compute = True
    mp.print_table = False

    calcs = main(mp)
