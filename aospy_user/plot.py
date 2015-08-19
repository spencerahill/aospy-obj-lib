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
        n_row=3,
        n_col=1,
        n_ax='all',
        n_plot=2,
        n_data=1,

        row_size=4,
        col_size=4,
        subplot_lims={'left': 0.12, 'right': 0.92, 'wspace': 0.1,
                      'bottom': 0.1, 'top': 0.96, 'hspace': 0.1},

        min_cntr=-1500,
        max_cntr=1500,
        num_cntr=15,
        contourf_extend='both',  # 'auto' 'neither' 'min' 'max' 'both'
        col_map='default',
        do_colorbar=False,      # 'all' 'column' 'row' False True
        cbar_ax_lim=(0.1, 0.08, 0.8, 0.03),
        cbar_ticks=False,
        cbar_ticklabels=False,
        cbar_label='units',

        # intvl_in=['monthly'] + ['3hr']*2,
        intvl_in='monthly',
        intvl_out='jas',
        # dtype_in_time=['ts'] + ['inst']*2,
        dtype_in_time='ts',
        # dtype_in_vert=[False] + ['sigma']*2,
        dtype_in_vert='pressure',
        # dtype_out_time='av',
        dtype_out_time='reg.av',
        # dtype_out_vert=[False] + ['vert_int']*2,
        dtype_out_vert=False,
        level=False,
        # yr_range=(1983, 1983),
        yr_range='default',
        plot_type='line',
        x_dim='x',
        y_dim='p',

        # Titles and labels
        # fig_title=False,
        fig_title=r'AM2.1 Sahara JAS',
        ax_title=False,
        ax_left_label=False,
        # ax_right_label=False,
        ax_right_label=['MSE', r'$T$', r'$q$'],
        # ax_right_label=['divg', 'adjusted divg'],
        # Axis limits
        # x_lim=False,
        x_lim=[(300, 400), (180, 320), (0, 18)],
        x_ticks=False,
        x_ticklabels=False,
        x_label=False,
        # x_label=[False, False, r'W kg$^{-1}$'],

        y_lim=False,
        y_ticks=False,
        y_ticklabels=False,
        y_label=False,

        # lat_lim=(-5, 35),
        lat_lim=(-50, 50),
        lat_ticks=False,
        lat_ticklabels=False,
        lat_label=False,

        # lon_lim=(-43, 65),
        lon_lim=(-180, 180),
        lon_ticks=False,
        lon_ticklabels=False,
        lon_label=False,

        p_lim=(1000, 100),
        p_ticks=False,
        p_ticklabels=False,
        p_label='hPa',

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

        # do_legend=False,
        do_legend=[True, False, False],
        # legend_labels=('Control', r'Control $h$, +2K $(\mathbf{v},\omega)$',
        #                r'+2K $h$, Control $(\mathbf{v},\omega)$', '+2K'),
        legend_labels=('Control', '+2K'),
        legend_loc=0,

        # line_color=False,
        # linestyle=False,
        # line_color=[['b', '0.2', '0.6', 'r']],
        line_color=[['b','r']],
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
    def __init__(self):
        pass

    def prep_data(self):
        proj = aospy_user.to_proj(self.proj)
        model = aospy_user.to_model(self.model, proj)
        run = aospy_user.to_run(self.run, model, proj)
        var = aospy_user.to_var(self.var)
        region = aospy_user.to_region(self.region, proj=proj)
        proj, model, var, region = [aospy_user.to_iterable(obj)
                                    for obj in (proj, model, var, region)]
        self.proj = proj
        self.model = model
        self.run = run
        self.var = var
        self.region = region


def main(main_params):
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['font.sans-serif'] = 'Helvetica'
    main_params.prep_data()
    return plot(main_params)

if __name__ == '__main__':
    params = MainParams()
    params.proj = p.aero_3agcm
    params.model = m.am2
    params.run = [[r.am2_reyoi_cont, r.am2_reyoi_p2]]
    # params.run = [[
    #     r.am3_hc,
    #     (r.am3_hc,)*3 + (r.am3_hp2k,)*5,
    #     (r.am3_hp2k,)*3 + (r.am3_hc,)*5,
    #     r.am3_hp2k
    # ]]
    params.ens_mem = False
    params.var = [v.mse, v.temp, v.sphum]
    params.region = reg.sahara
    # params.region = False

    fig = main(params)
