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
        # n_row=3,
        # n_col=2,
        n_row=2,
        n_col=1,
        n_ax='all',
        n_plot=1,
        # n_plot=2,
        # n_data=[[1, 1, 2]],
        n_data=1,

        row_size=2,
        col_size=5,
        subplot_lims={'left': 0.05, 'right': 0.98, 'wspace': 0.05,
                      'bottom': 0.1, 'top': 0.9, 'hspace': 0.06},

        plot_type='contourf',
        # plot_type=[['contourf', 'contour']],# 'quiver']],
        x_dim='lon',
        y_dim='lat',

        min_cntr=-1.9e1,
        max_cntr=1.9e1,
        num_cntr=19,
        # min_cntr=[[-3.75, 0]],# False]],
        # max_cntr=[[3.75, 20]],# False]],
        # num_cntr=[[15, 10]],# False]],
        # contours_extend='both',  # 'neither' 'min' 'max' 'both'
        contour_labels=False,
        # contour_labels=[[False, True]],# False]],
        colormap='default',
        # colormap=[['default', False]],# False]],
        do_colorbar='all',      # 'all' 'column' 'row' False True
        # do_colorbar=[['all', False]],# False]],
        cbar_ax_lim=(0.11, 0.08, 0.8, 0.02),
        cbar_ticks=False,
        # cbar_ticks=range(-170, -49, 40) + [-10, 10] +  range(50, 171, 40),
        cbar_ticklabels=False,
        cbar_label='units',

        # intvl_in='monthly',
        intvl_in='3hr',
        # intvl_in=['monthly'] + ['3hr']*2,
        intvl_out='jas',
        # dtype_in_time='ts',
        dtype_in_time='inst',
        # dtype_in_time=['ts'] + ['inst']*2,
        # dtype_in_vert=False,
        dtype_in_vert='sigma',
        # dtype_in_vert='pressure',
        # dtype_in_vert=[False]*2 + [['pressure', False]]*4,
        dtype_out_time='av',
        # dtype_out_time='reg.ts',
        dtype_out_vert=False,
        # dtype_out_vert='vert_int',
        # dtype_out_vert=[False]*2 + [['vert_int', False]]*4,
        # level=700,
        level=False,
        # date_range='default',
        # date_range=('1983-01-01', '2012-12-31'),
        # date_range=('1983-01-01', '1983-12-31'),
        date_range=('1983-01-01', '1984-12-31'),

        # fig_title=False,
        # fig_title=r'AM2.1 1983-1984 JAS column mass budget terms',
        fig_title=r'AM2.1 1983-1984 JAS column mass budget residual',
        # fig_title=r'Control JAS MSE budget terms',
        # ax_title=False,
        ax_title=['Without mass adjustment', 'With mass adjustment'],
        # ax_title=['AM2.1', 'c48-HiRAM'] + ['']*4,
        # ax_title=[r'Tendency term',
                  # r'Transport term',
                  # r'Residual (Tendency + transport)'],
        ax_left_label=False,
        # ax_left_label=[r'$F_\mathrm{net}$', '',
                       # r'$\{\omega\frac{\partial h}{\partial p}\}$', '',
                       # r'$\{\mathbf{v}\cdot\nabla h\}$', ''],
        ax_left_label_coords=(-0.02, 0.5),
        ax_left_label_kwargs={
            'verticalalignment': 'center',
            'horizontalalignment': 'right',
            # 'rotation': 'vertical',
            'rotation': 'horizontal',
            'fontsize': 'small',
        },
        ax_right_label=False,
        # ax_right_label=['Total', 'Vertical', 'Horizontal'],
        ax_right_label_coords=(1.02, 0.5),
        ax_right_label_kwargs={
            'verticalalignment': 'center',
            'horizontalalignment': 'left',
            # 'rotation': 'vertical',
            'rotation': 'horizontal',
            'fontsize': 'small',
        },

        # x_lim=False,
        x_lim=(-25, 25),
        x_ticks=False,
        x_ticklabels=False,
        x_label=False,
        # x_label=[r'mm day$^{-1}$', 'Kelvin'],
        # do_mark_x0=True,
        do_mark_x0=False,

        # y_lim=False,
        y_lim=(-25, 25),
        y_ticks=False,
        y_ticklabels=False,
        y_label=False,
        # y_label='W m$^{-2}$',
        # do_mark_y0=True,
        do_mark_y0=False,

        # lat_lim=(-5, 35),
        # lat_lim=(12.5, 50),
        lat_lim=(-50, 50),
        lat_ticks=False,
        lat_ticklabels=False,
        lat_label=False,

        # lon_lim=(-43, 65),
        # lon_lim=(70, 152.5),
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
        # latlon_rect=[[(-18, 40, 10, 20), False]],# False]],
        # latlon_rect=[[(100, 122.5, 22.5, 40), False]],
        do_mask_oceans=False,

        do_legend=False,
        # do_legend=[True, False, False],
        # legend_labels=('Control', r'Control $h$, +2K $(\mathbf{v},\omega)$',
        #                r'+2K $h$, Control $(\mathbf{v},\omega)$', '+2K'),
        legend_labels=('AM2.1', 'AM3', 'HiRAM', 'c48-HiRAM'),
        legend_loc=0,

        # plot_kwargs=[[{
        plot_kwargs={
            # 'color': c,
            'color': 'r',
            'linestyle': '-',
            'linewidth': 1.5,
            'marker': None,
            'markersize': 10,
            'markerfacecolor': 'k'
        },
        # for c in ('red', 'orange', 'green', 'blue')]],
        scatter_kwargs={
            's': 10,
            'c': '0.4',
            'marker': 'o',
            'cmap': None,
            'edgecolors': None,
            'facecolors': None,
            'linewidths': None,
            'linestyles': 'solid'
        },
        contourf_kwargs={
            'extend': 'both',
            # 'hatches': None,
        },
        contour_kwargs={
            'extend': 'both',
            'colors': 'gray',
            'levels': [0],
            'linestyles': '-',
            'linewidths': 0.5
        },
        quiver_kwargs={
            'angles': 'uv',
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
        print_corr_coeff=True,

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
    params.proj = p.aero_3agcm
    params.model = m.am2
    # params.model = [m.am2, m.hiram_c48]*3
    # params.model = [[m.am2, m.am3, m.hiram, m.hiram_c48]]

    dam2 = aospy.plotting.Operator('-', (r.am2_reyoi_p2, r.am2_reyoi_cont))
    dam3 = aospy.plotting.Operator('-', (r.am3_hp2k, r.am3_hc))
    dhir = aospy.plotting.Operator('-', (r.hiram_gtm, r.hiram_cont))
    dc48 = aospy.plotting.Operator('-', (r.hiram_c48_0_p2K, r.hiram_c48_0))
    # params.run = [[dam2, r.am2_reyoi_p2, dam2]]
    # params.run = [[dam2, dam3, dhir, dc48]]
    # params.run = [r.am2_reyoi_cont, r.hiram_c48_0]*3
    params.run = r.am2_reyoi_cont
    # params.run = [[dam2, r.am2_reyoi_cont],
                  # [dam3, r.am3_hc],
                  # [dhir, r.hiram_cont],
                  # [dc48, r.hiram_c48_0]]
    # params.run = [[dam2, r.am2_reyoi_cont, dam2],
                  # [dam3, r.am3_hc, dam3],
                  # [dhir, r.hiram_cont, dhir],
                  # [dc48, r.hiram_c48_0, dc48]]

    params.ens_mem = False
    # params.var = v.u_mass_adjustment
    params.var = [  # v.mass_budget_tendency_term,
                    # v.mass_budget_transport_term,
        v.mass_budget_residual,
        v.mass_budget_with_adj_residual]
    # params.var = [v.q_horiz_advec_const_p_from_eta,
                  # v.q_horiz_advec]
    # params.var = [v.divg_of_vert_int_horiz_flow,
                  # v.divg_of_vert_int_mass_adj_horiz_flow]
                  # v.ps_monthly_tendency]
    # params.var = ([v.column_energy]*2 +
                  # [v.mse_vert_advec_upwind]*2 +
                  # [v.mse_horiz_advec_upwind]*2)
    # params.var = ([[v.toa_rad, v.column_energy]]*2 +
                  # [[v.mse_vert_advec_upwind, v.column_energy]]*2 +
                  # [[v.mse_horiz_advec_upwind, v.column_energy]]*2)
    # params.var = [[v.hght, v.hght, [v.ucomp, v.vcomp]]]
    # params.var = [[v.column_energy, v.column_energy],
                  # [v.mse_vert_advec_upwind, v.column_energy],
                  # [v.mse_horiz_advec_upwind, v.column_energy],
                  # [v.mse_total_advec_upwind, v.column_energy]]*1
    # params.var = [[[v.column_energy, v.mse_total_advec_upwind]]]
    # params.var = [[[v.precip, v.cre_net]]]

    params.region = False
    # params.region = reg.sahel

    fig = main(params)
