#! /usr/bin/env python
"""Main script for automating computations using aospy."""
import itertools

import colorama

import aospy
import aospy_user


class MainParams(object):
    """Interface to main routine."""
    pass


class CalcParams(object):
    """Interface to Calc class."""
    pass

    def print_params(self):
        pairs = (
            ('Project', self.proj),
            ('Models', self.model),
            ('Runs', self.run),
            ('Ensemble members', self.ens_mem),
            ('Variables', self.var),
            ('Year ranges', self.yr_range),
            ('Geographical regions', self.region),
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


def prompt_user_verify():
    if not raw_input("Proceed using these parameters? ").lower() == 'y':
        raise IOError('\nExecution cancelled by user.')


def main(main_params):
    """Main script for interfacing with aospy."""
    # Instantiate objects and load default/all models, runs, and regions.
    proj = aospy_user.to_proj(main_params.proj)
    model = aospy_user.to_model(main_params.model, proj)
    var = aospy_user.to_var(main_params.var)
    region = aospy_user.to_region(main_params.region, proj=proj)

    cp = CalcParams()
    cp.proj, cp.model, cp.var, cp.region = [
        aospy_user.to_iterable(obj) for obj in (proj, model, var, region)
    ]
    cp.region = aospy.utils.dict_name_keys(cp.region)
    cp.run = main_params.run
    cp.ens_mem = main_params.ens_mem
    cp.yr_range = main_params.yr_range
    cp.intvl_in = main_params.intvl_in
    cp.intvl_out = main_params.intvl_out
    cp.dtype_in_time = main_params.dtype_in_time
    cp.dtype_in_vert = main_params.dtype_in_vert
    cp.dtype_out_time = main_params.dtype_out_time
    cp.dtype_out_vert = main_params.dtype_out_vert
    cp.level = main_params.level
    cp.yr_chunk_len = main_params.yr_chunk_len
    cp.compute = main_params.compute
    cp.verbose = main_params.verbose
    cp.print_table = main_params.print_table

    cp.print_params()
    prompt_user_verify()

    # Iterate through given parameter combos, saving resulting calculations.
    print '\n\tVariable time averages and statistics:'
    calcs = []
    data = []
    for mod in cp.model:
        runs = aospy_user.to_run(main_params.run, mod, cp.proj)
        mod = aospy_user.to_iterable(mod)

        for params in itertools.product(
                cp.proj, mod, runs, cp.ens_mem, cp.var, cp.yr_range,
                [cp.region], cp.intvl_in, cp.intvl_out, cp.dtype_in_time,
                cp.dtype_in_vert, [cp.dtype_out_time], cp.dtype_out_vert,
                cp.level
        ):
            calc = aospy.Calc(*params, verbose=cp.verbose,
                              yr_chunk_len=cp.yr_chunk_len)
            if cp.compute:
                calc.compute()
                calcs.append(calc)

            if cp.print_table:
                for reg in cp.region.values():
                    dat = calc.load(
                        cp.dtype_out_time[0], dtype_out_vert=params[-2],
                        region=reg, plot_units=True
                    )
                    print dat
                    data.append(dat)
    print "Calculations finished."
    return calcs, data


if __name__ == '__main__':
    mp = MainParams()
    mp.proj = 'aero_3agcm'
    mp.model = 'default'
    mp.run = 'default'
    mp.ens_mem = [None]
    mp.var = ['sphum']
    mp.yr_range = ['default']
    mp.region = 'all'
    mp.intvl_in = ['monthly']
    mp.intvl_out = ['ann']
    mp.dtype_in_time = ['ts']
    # mp.dtype_in_vert = [False]
    mp.dtype_in_vert = ['pressure']
    # mp.dtype_out_time = ('reg.av',)
    mp.dtype_out_time = ('av', 'std', 'reg.av', 'reg.ts', 'reg.std')
    # mp.dtype_out_vert = [False]
    mp.dtype_out_vert = [False]
    mp.level = [False]
    mp.yr_chunk_len = False
    mp.compute = True
    mp.verbose = True
    mp.print_table = False

    calc, data = main(mp)
