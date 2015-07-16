#! /usr/bin/env python
"""Main script for automating computations using aospy."""
import itertools

import aospy
import aospy_user


class CalcParams(object):
    """Interface to Calc class."""
    pass


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

    print '\nProject:', cp.proj
    print 'Models:', cp.model
    print 'Runs:', cp.run
    print 'Ensemble members:', cp.ens_mem
    print 'Variables:', cp.var
    print 'Year ranges:', cp.yr_range
    print 'Geographical regions:', region
    print 'Time interval of input data:', cp.intvl_in
    print 'Time intervals for averaging:', cp.intvl_out
    print 'Input data time type:', cp.dtype_in_time
    print 'Input data vertical type:', cp.dtype_in_vert
    print 'Output data time types:', cp.dtype_out_time
    print 'Output data vert types:', cp.dtype_out_vert
    print 'Vertical levels:', cp.level
    print 'Year chunks:', cp.yr_chunk_len
    print 'Compute this data:', cp.compute
    print 'Print this data:', cp.print_table

    if not raw_input("\nProceed using these parameters? ").lower() == 'y':
        raise IOError('\nExecution cancelled by user.')

    # Iterate through given parameter combos, saving resulting calculations.
    print '\n\tVariable time averages and statistics:'
    calcs = []
    data = []
    for mod in cp.model:
        runs = aospy_user.to_run(main_params.run, mod, cp.proj)
        mod = aospy_user.to_iterable(mod)

        for params in itertools.product(
                cp.proj, mod, runs, cp.ens_mem, cp.var, cp.yr_range, cp.region,
                cp.intvl_in, cp.intvl_out,  cp.dtype_in_time, cp.dtype_in_vert,
                [cp.dtype_out_time], cp.dtype_out_vert, cp.level
        ):
            calc = aospy.Calc(*params, verbose=cp.verbose,
                              yr_chunk_len=cp.yr_chunk_len)
            if cp.compute:
                calc.compute()
                calcs.append(calc)

            if cp.print_table:
                dat = calc.load(
                    cp.dtype_out_time[0], dtype_out_vert=params[-2],
                    region=params[6][0], plot_units=True
                )
                print dat
                data.append(dat)
    print "Calculations finished."
    return calcs, data


class MainParams(object):
    """Interface to main routine."""
    pass

if __name__ == '__main__':
    mp = MainParams()
    mp.proj = 'aero_3agcm'
    mp.model = 'default'
    mp.run = 'default'
    mp.ens_mem = [None]
    mp.var = ['precip']
    mp.yr_range = ['default']
    mp.region = ['all']
    mp.intvl_in = ['monthly']
    mp.intvl_out = ['jas']
    mp.dtype_in_time = ['ts']
    mp.dtype_in_vert = [False]
    mp.dtype_out_time = ('av', 'std', 'reg.av', 'reg.ts', 'reg.std')
    mp.dtype_out_vert = [False]
    mp.level = [None]
    mp.yr_chunk_len = False
    mp.compute = True
    mp.verbose = True
    mp.print_table = False

    calc, data = main(mp)
