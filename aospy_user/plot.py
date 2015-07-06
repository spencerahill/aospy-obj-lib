#! /usr/bin/env python
"""Script that interfaces w/ aospy.plotting to create multi-panel plots."""
import matplotlib
import matplotlib.pyplot as plt

import aospy
import aospy_user


def plot(proj, model, run, ens_mem, var, region):
    fig = aospy.plotting.Fig(
        proj=proj,
        model=model,
        run=run,
        ens_mem=ens_mem,
        var=var,
        region=region,

        n_row=1,
        n_col=1,
        n_ax='all',
        n_plot=1,
        n_data=1,

        row_size=1.7,
        col_size=5,
        subplot_lims={'left': 0.05, 'right': 0.95, 'wspace': 0.1,
                      'bottom': 0.12, 'top': 0.88, 'hspace': 0.15},

        min_cntr=-7.5,
        max_cntr=7.5,
        num_cntr=15,
        contourf_extend='both',  # 'auto' 'neither' 'min' 'max' 'both'
        col_map='RdBu_r',
        do_colorbar='all',      # 'all' 'column' 'row' False True
        cbar_ax_lim=(0.1, 0.1, 0.8, 0.03),
        cbar_ticks=False,
        cbar_ticklabels=False,
        cbar_label='units',

        intvl_in='monthly',
        intvl_out=['jas'],
        dtype_in_time='ts',
        dtype_in_vert=False,
        dtype_out_time='av',
        dtype_out_vert=False,
        level=None,
        yr_range='default',

        plot_type='map',
        x_dim='lon',
        y_dim='lat',

        # Titles and labels
        fig_title=(r'$B_t$ v. $P$ correlation in AM2.1 1870-1999 '
                   'AMIP simulation'),
        ax_title=False,
        ax_left_label=False,
        ax_right_label=False,

        # Axis limits
        x_lim=False,
        x_ticks=False,
        x_ticklabels=False,
        x_label=False,

        y_lim=False,
        y_ticks=False,
        y_ticklabels=False,
        y_label=False,

        lat_lim=(-45, 45),
        lat_ticks=False,
        lat_ticklabels=False,
        lat_label=False,

        lon_lim=(-180, 180),
        lon_ticks=False,
        lon_ticklabels=False,
        lon_label=False,

        p_lim=(1000, 100),
        p_ticks=False,
        p_ticklabels=False,
        p_label=False,

        sigma_lim=(1, 0.1),
        sigma_ticks=False,
        sigma_ticklabels=False,
        sigma_label=False,

        time_lim='ann_cycle',
        time_ticks=False,
        time_ticklabels=False,
        time_label=False,

        map_proj='cyl',                # 'moll',
        map_res='c',
        shiftgrid_start=False,
        shiftgrid_cyclic=360.0,
        latlon_rect=(-18, 40, 10, 20),

        do_quiver=False,

        line_color='k',
        linestyle='-',

        marker_size=10,
        marker_color='k',
        marker_shape='.',

        do_subtract_mean=False,
    )

    fig.create_fig()
    fig.make_plots()
    plt.show()
    return fig


def main(proj, model, run, ens_mem, var, region):
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['font.sans-serif'] = 'Helvetica'

    # Instantiate objects and load default/all models, runs, and regions.
    proj = aospy_user.to_proj(proj)
    model = aospy_user.to_model(model, proj)
    run = aospy_user.to_run(run, model, proj)
    var = aospy_user.to_var(var)
    region = aospy_user.to_region(region, proj=proj)
    proj, model, var, region = [aospy_user.to_iterable(obj)
                                for obj in (proj, model, var, region)]
    return plot(proj, model, run, ens_mem, var, region)

if __name__ == '__main__':
    proj = 'aero_3agcm'
    model = 'am2'
    run = {('reyoi+2K', 'reyoi_cont'): '-'}
    ens_mem = False
    var = 'precip'
    region = False
    fig = main(proj, model, run, ens_mem, var, region)
