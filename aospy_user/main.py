#! /usr/bin/env python
"""Main script for automating computations using aospy."""
from __future__ import print_function
import itertools
import logging

import aospy
import colorama
import multiprocess

from . import projs, variables


class ObjectsForCalc(tuple):
    """Container of aospy objects to be used for a single Calc."""
    def __new__(cls, *objects):
        return super(ObjectsForCalc, cls).__new__(cls, objects)

    def __init__(self, *objects):
        self.objects = objects

    def __repr__(self):
        return 'ObjectsForCalc' + repr(tuple(self.objects))


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
        for run in runs:
            for model in models:
                try:
                    run_obj = aospy.to_run(run, model, proj, self.projs)
                    if isinstance(run, ObjectsForCalc):
                        run_objs.append(ObjectsForCalc(run_obj))
                    else:
                        run_objs.append(run_obj)
                except AttributeError as ae:
                    logging.info(str(ae))
            # Retain the original type (e.g. list v. ObjectsForCalc).
            run_objs = type(runs)(run_objs)
        if 'cmip5' in [p.name for p in proj]:
            if isinstance(run_objs[0], list):
                return run_objs[0]
            return [run_objs[0]]
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
        self.region = [aospy.utils.io.dict_name_keys(self.region)]


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
                      'verbose',)
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
            except:
                raise
            calc = aospy.Calc(ci)
            if exec_calcs:
                try:
                    calc.compute()
                except RuntimeError as e:
                    logging.warn(repr(e))
                except IOError as e:
                    logging.warn(repr(e))
                except:
                    raise
                if print_table:
                    print("{}".format(calc.load(
                        'reg.av', dtype_out_vert=False,
                        region=ci.region['sahel'], plot_units=True))
                    )
            calcs.append(calc)
        return calcs

    def exec_calcs(self, calcs):
        out = []
        for calc in calcs:
            try:
                o = calc.compute()
            except RuntimeError as e:
                logging.warn(repr(e))
            else:
                out.append(o)
        return out

    def print_results(self, calcs):
        for calc in calcs:
            for region in calc.region.values():
                print([calc.load(self.dtype_out_time[0],
                                 # dtype_out_vert=params[-2],
                                 region=region, plot_units=True)])


def main(main_params, exec_calcs=True, print_table=True, prompt_verify=True,
         parallelize=False):
    """Main script for interfacing with aospy."""
    # Instantiate objects and load default/all models, runs, and regions.
    cs = CalcSuite(MainParamsParser(main_params, projs))
    cs.print_params()
    if prompt_verify:
        try:
            cs.prompt_user_verify()
        except IOError as e:
            logging.warn(repr(e))
            return
    param_combos = cs.create_params_all_calcs()
    if parallelize and exec_calcs:
        calcs = cs.create_calcs(param_combos, exec_calcs=False,
                                print_table=print_table)
        p = multiprocess.Pool()
        return p.map(lambda calc: calc.compute(), calcs)
    else:
        calcs = cs.create_calcs(param_combos, exec_calcs=exec_calcs,
                                print_table=print_table)
    return calcs
