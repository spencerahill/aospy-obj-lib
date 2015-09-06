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
        n_row=1,
        n_col=1,
        n_ax='all',
        n_plot=1,
        # n_data=[[1, 1, 2]],
        n_data=2,

        row_size=4,
        col_size=5,
        subplot_lims={'left': 0.13, 'right': 0.95, 'wspace': 0.05,
                      'bottom': 0.1, 'top': 0.9, 'hspace': 0.06},

        plot_type='scatter',
        # plot_type=[['contourf', 'contour']],# 'quiver']],
        x_dim='x',
        y_dim='y',

        min_cntr=-200,
        max_cntr=200,
        num_cntr=15,
        # min_cntr=[[-3.75, 0]],# False]],
        # max_cntr=[[3.75, 20]],# False]],
        # num_cntr=[[15, 10]],# False]],
        # contours_extend='both',  # 'neither' 'min' 'max' 'both'
        contour_labels=False,
        # contour_labels=[[False, True]],# False]],
        colormap='default',
        # colormap=[['BrBG', False]],# False]],
        do_colorbar=False,      # 'all' 'column' 'row' False True
        # do_colorbar=[['all', False]],# False]],
        cbar_ax_lim=(0.11, 0.05, 0.8, 0.02),
        cbar_ticks=False,
        cbar_ticklabels=False,
        cbar_label='units',

        intvl_in='monthly',
        # intvl_in=['monthly'] + ['3hr']*2,
        intvl_out='jas',
        dtype_in_time='ts',
        # dtype_in_time=['ts'] + ['inst']*2,
        # dtype_in_vert='pressure',
        dtype_in_vert=[[['pressure', False]]],
        # dtype_in_vert=['pressure']*5 + [False]*1,
        # dtype_out_time='av',
        dtype_out_time='reg.ts',
        # dtype_out_vert='vert_int',
        dtype_out_vert=[[['vert_int', False]]],
        # level=700,
        level=False,
        yr_range='default',
        # yr_range=(1983, 1983),

        # fig_title=False,
        fig_title=r'AM2.1 AMIP, Sahel JAS, interannual $P$ v. $\{\omega\partial_ph\}$',
        ax_title=False,
        # ax_title=['Total', 'Vertical', 'Horizontal'],
        # ax_left_label=False,
        # ax_left_label=['AM2.1', 'AM3', 'HiRAM', 'c48-HiRAM'],
        ax_right_label=False,
        # ax_right_label=['Total', 'Vertical', 'Horizontal'],
        # ax_right_label=['AM2.1', 'AM3'],# 'HiRAM', 'c48-HiRAM'],

        # x_lim=False,
        x_lim=(-20, 20),
        x_ticks=False,
        x_ticklabels=False,
        # x_label=False,
        x_label=r'W m$^{-2}$',
        do_mark_x0=True,

        # y_lim=False,
        y_lim=(-2, 2),
        y_ticks=False,
        y_ticklabels=False,
        # y_label=False,
        y_label=r'mm day$^{-1}$',
        do_mark_y0=True,

        lat_lim=(-5, 35),
        # lat_lim=(12.5, 50),
        # lat_lim=(-50, 50),
        lat_ticks=False,
        lat_ticklabels=False,
        lat_label=False,

        lon_lim=(-43, 65),
        # lon_lim=(70, 152.5),
        # lon_lim=(-180, 180),
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
        # latlon_rect=[[(-18, 40, 10, 20), False]],# False]],
        # latlon_rect=[[(100, 122.5, 22.5, 40), False]],
        do_mask_oceans=False,

        do_legend=False,
        # do_legend=[True, False, False],
        # legend_labels=('Control', r'Control $h$, +2K $(\mathbf{v},\omega)$',
        #                r'+2K $h$, Control $(\mathbf{v},\omega)$', '+2K'),
        legend_labels=('AM2.1', 'AM3', 'HiRAM', 'c48-HiRAM'),
        legend_loc=0,

        # plot_kwargs={'color': c,
        plot_kwargs={'color': 'r',
                      'linestyle': '-',
                      'linewidth': 1.5,
                      'marker': None,
                      'markersize': 10,
                      'markerfacecolor': 'k'},
                      # for c in ('red', 'orange', 'green', 'blue')]],
        scatter_kwargs={'s': 10,
                        'c': '0.4',
                        'marker': 'o',
                        'cmap': None,
                        'edgecolors': None,
                        'facecolors': None,
                        'linewidths': None,
                        'linestyles': 'solid'
        },
        contour_kwargs={'extend': 'both',
                        'colors': '0.2',
                        # 'levels': [0],
                        'linestyles': '-',
                        'linewidths': 2
        },
        quiver_kwargs={'angles': 'uv',
                       'scale': 1,
                       'latlon': False,
                       'scale_units': 'xy',
                       'angles': 'xy'
        },
        quiver_n_lon=40,
        quiver_n_lat=20,
        do_quiverkey=True,
        quiverkey_args=(-0.06, 0.5, 2, '2 m s$^{-1}$'),
        quiverkey_kwargs={'labelpos': 'S',
                          'coordinates': 'axes',
                          'fontproperties': {'size': 'xx-small'}},

        do_best_fit_line=True,
        print_best_fit_slope=True,
        print_corr_coeff = True,

        do_subtract_mean=True,
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
    # params.proj = p.obs
    # params.model = m.merra
    params.proj = p.aero_3agcm
    params.model = m.am2
    # params.model = [[m.am2, m.am3, m.hiram, m.hiram_c48]]

    dam2 = aospy.plotting.Operator('-', (r.am2_reyoi_p2, r.am2_reyoi_cont))
    dam3 = aospy.plotting.Operator('-', (r.am3_hp2k, r.am3_hc))
    dhir = aospy.plotting.Operator('-', (r.hiram_gtm, r.hiram_cont))
    dc48 = aospy.plotting.Operator('-', (r.hiram_c48_0_p2K, r.hiram_c48_0))
    # params.run = [[dam2, r.am2_reyoi_p2, dam2]]
    # params.run = [[dam2, dam3, dhir, dc48]]
    # params.run = r.merra
    params.run = r.am2_amip
    # params.run = [[dam2, r.am2_reyoi_cont],
                  # [dam3, r.am3_hc],
                  # [dhir, r.hiram_cont],
                  # [dc48, r.hiram_c48_0]]
    # params.run = [[dam2, r.am2_reyoi_cont, dam2],
                  # [dam3, r.am3_hc, dam3],
                  # [dhir, r.hiram_cont, dhir],
                  # [dc48, r.hiram_c48_0, dc48]]

    params.ens_mem = False
    # params.var = [[v.hght, v.hght, [v.ucomp, v.vcomp]]]
    # params.var = [[v.column_energy, v.column_energy],
                  # [v.mse_vert_advec_upwind, v.column_energy],
                  # [v.mse_horiz_advec_upwind, v.column_energy],
                  # [v.mse_total_advec_upwind, v.column_energy]]*1
    params.var = [[[v.mse_vert_advec_upwind,
                    v.precip]]]
    params.region = reg.sahel

    fig = main(params)
