#! /usr/bin/env python
"""Main script for automating computations using aospy."""
import itertools

import aospy

from .obj_from_name import to_proj, to_model, to_region


def main(proj=None, model=None, run=None, ens_mem=None, var=None,
         yr_range=None, region=None, intvl_in=None, intvl_out=None,
         dtype_in_time=None, dtype_in_vert=None, dtype_out_time=None,
         dtype_out_vert=None, level=None, yr_chunk_len=False, verbose=True,
         compute=True, print_table=False):
    """Main script for interfacing with aospy."""

    # Instantiate objects and load default/all models, runs, and regions.
    proj = to_proj(proj)
    model = to_model(model, proj)
    region = to_region(region)

    # Iterate through given parameter combos, saving resulting calculations.
    print '\n\tVariable time averages and statistics:'
    calcs = []
    data = []
    for mod in model:
        runs = to_run(run, mod, proj)

        for params in itertools.product(
                [proj], [mod], runs, ens_mem, var, yr_range, [region],
                intvl_in, intvl_out, dtype_in_time, dtype_in_vert,
                [dtype_out_time], dtype_out_vert, level
        ):
            calc = aospy.Calc(*params, verbose=verbose,
                              yr_chunk_len=yr_chunk_len)
            if compute:
                try:
                    calc.compute()
                except:
                    raise
                calcs.append(calc)
            if print_table:
                try:
                    dat = calc.load(
                        dtype_out_time[0], dtype_out_vert=params[-2],
                        region=params[6][0], plot_units=True
                    )
                    print dat
                except:
                    raise
                data.append(dat)
    print "Calculations finished."
    return calcs

if __name__ == '__main__':
    proj = 'aero_3agcm'
    model = ['am2']
    run = ['amip']
    ens_mem = [None]
    var = ['toa_rad_clr_precip_lin_regr', 'toa_rad_clr_precip_corr']
    yr_range = ['default']
    region = ['all']
    intvl_in = ['monthly']
    intvl_out = [1, 7]
    dtype_in_time = ['ts']
    dtype_in_vert = [False]
    # dtype_out_time = ('av', 'std', 'reg.av', 'reg.ts', 'reg.std')
    dtype_out_time = ('',)
    dtype_out_vert = [False]
    level = [None]
    yr_chunk_len = False
    compute = True
    verbose = True
    print_table = False

    print '\nProject:', proj
    print 'Models:', model
    print 'Runs:', run
    print 'Ensemble members:', ens_mem
    print 'Variables:', var
    print 'Year ranges:', yr_range
    print 'Geographical regions:', region
    print 'Time interval of input data:', intvl_in
    print 'Time intervals for averaging:', intvl_out
    print 'Input data time type:', dtype_in_time
    print 'Input data vertical type:', dtype_in_vert
    print 'Output data time types:', dtype_out_time
    print 'Output data vert types:', dtype_out_vert
    print 'Vertical levels:', level
    print 'Year chunks:', yr_chunk_len
    print 'Compute this data:', compute
    print 'Print this data:', print_table

    if not raw_input("\nProceed using these parameters? ").lower() == 'y':
        raise IOError('\nExecution cancelled by user.')

    try:
        if compute:
            calc = main(
                proj=proj, model=model, run=run, ens_mem=ens_mem, var=var,
                yr_range=yr_range, region=region, intvl_in=intvl_in,
                intvl_out=intvl_out, dtype_in_time=dtype_in_time,
                dtype_in_vert=dtype_in_vert, dtype_out_time=dtype_out_time,
                dtype_out_vert=dtype_out_vert, level=level,
                yr_chunk_len=yr_chunk_len, verbose=verbose, compute=compute,
                print_table=print_table
            )
        if print_table:
            calc = main(
                proj=proj, model=model, run=run, ens_mem=ens_mem, var=var,
                yr_range=yr_range, region=print_table, intvl_in=intvl_in,
                intvl_out=intvl_out, dtype_in_time=dtype_in_time,
                dtype_in_vert=dtype_in_vert, dtype_out_time=('reg.ts',),
                dtype_out_vert=dtype_out_vert, level=level,
                yr_chunk_len=yr_chunk_len, verbose=verbose, compute=compute,
                print_table=True
            )
    except:
        raise
