#! /usr/bin/env python
"""Script that interfaces w/ aospy.plotting to create multi-panel plots."""
import matplotlib

import aospy
import aospy_user
from aospy_user import projs as p
from aospy_user import models as m
from aospy_user import runs as r
from aospy_user import variables as v
from aospy_user import regions as reg


def plot(plot_params):
    fig = aospy.plotting.Fig(
        plot_params,
        n_row=2,
        n_col=2,
        n_ax='all',
        n_plot=1,
        n_data=1,

        row_size=4,
        col_size=3,
        subplot_lims={'left': 0.05, 'right': 0.95, 'wspace': 0.1,
                      'bottom': 0.1, 'top': 0.95, 'hspace': 0.1},

        min_cntr=200,
        max_cntr=300,
        num_cntr=20,
        contourf_extend='min',  # 'auto' 'neither' 'min' 'max' 'both'
        col_map='default',
        do_colorbar=False,      # 'all' 'column' 'row' False True
        cbar_ax_lim=(0.1, 0.05, 0.8, 0.02),
        cbar_ticks=False,
        cbar_ticklabels=False,
        cbar_label='units',

        intvl_in='monthly',
        intvl_out='jas',
        dtype_in_time='ts',
        dtype_in_vert='pressure',
        dtype_out_time='reg.av',
        dtype_out_vert=False,
        level=False,
        yr_range='default',

        plot_type='line',
        x_dim='x',
        y_dim='p',

        # Titles and labels
        fig_title=False,
        # ax_title=['3 hr, model levels', 'Monthly, $p$ levels', '', ''],
        # ax_left_label = [r'$\{\omega\partial h/\partial p\}$', '',
        #                  r'$\{\mathbf{v}\cdot\nabla h\}$', ''],
        # ax_left_label=['AM2.1', 'AM3', 'HiRAM', 'c48-HiRAM'],
        ax_left_label=False,
        ax_right_label=False,

        # Axis limits
        x_lim=[(-60, 5), (-1, 1), (-20, 20), (-0.2, 0.2)],
        x_ticks=False,
        x_ticklabels=False,
        x_label=False,

        y_lim=False,
        y_ticks=False,
        y_ticklabels=False,
        y_label=False,

        lat_lim=(-5, 35),
        lat_ticks=False,
        lat_ticklabels=False,
        lat_label=False,

        lon_lim=(-43, 65),
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

        line_color='r',
        linestyle='-',

        marker_shape=None,
        marker_size=10,
        marker_color='k',

        do_subtract_mean=False,
    )

    fig.create_fig()
    fig.make_plots()
    matplotlib.pyplot.show()
    return fig


class MainParams(object):
    """Interface to main routine."""
    pass


class PlotParams(object):
    """Interface to plot routine."""
    pass


class AxParamParser(object):
    """Container designating that the contents correspond to an Ax."""
    def __init__(self, params):
        self.params = params
        self.n_param = len(params)


def main(params):
    # Instantiate objects and load default/all models, runs, and regions.
    proj = aospy_user.to_proj(params.proj)
    model = aospy_user.to_model(params.model, proj)
    run = aospy_user.to_run(params.run, model, proj)
    var = aospy_user.to_var(params.var)
    region = aospy_user.to_region(params.region, proj=proj)
    proj, model, var, region = [aospy_user.to_iterable(obj)
                                for obj in (proj, model, var, region)]
    plot_params = PlotParams()
    plot_params.proj = proj
    plot_params.model = model
    plot_params.run = run
    plot_params.ens_mem = params.ens_mem
    plot_params.var = var
    plot_params.region = region
    return plot(plot_params)

if __name__ == '__main__':
    params = MainParams()
    params.proj = p.aero_3agcm
    params.model = m.am2
    params.run = ([r.am2_reyoi_cont]*2 +
                  [{(r.am2_reyoi_p2, r.am2_reyoi_cont): '-'}]*2)
    # params.model = [m.am2, m.am3, m.hiram, m.hiram_c48]
    # params.run = [r.am2_reyoi_cont, r.am3_hc, r.hiram_cont, r.hiram_c48_0]
    # params.run = [r.am2_reyoi_p2, r.am3_hp2k, r.hiram_gtm, r.hiram_c48_0_p2K]
    # params.run = [{(r.am2_reyoi_p2, r.am2_reyoi_cont): '-'},
    #               {(r.am3_hp2k, r.am3_hc): '-'},
    #               {(r.hiram_gtm, r.hiram_cont): '-'},
    #               {(r.hiram_c48_0_p2K, r.hiram_c48_0): '-'}]
    params.ens_mem = False
    params.var = [v.omega, v.moist_static_stab]*2
    params.region = reg.sahel_north

    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['font.sans-serif'] = 'Helvetica'

    fig = main(params)
