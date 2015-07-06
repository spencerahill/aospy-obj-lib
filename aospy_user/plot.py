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

        # do_cont_cntrs=True,
        # cont_run=([['reyoi_cont']] + [['hurrell_cont']] + ,
        #             [['cont']] + [['ming0']]),
        # cntrs_color='0.85',
        # cont_cntr_levs=False,
        # cont_cntr_levs=range(-60, 61, 10), # omega; cre_net/sw/lw; shflx,
        # cont_cntr_levs=range(-30, 31, 10), # ucomp,
        # cont_cntr_levs=range(-30, 31, 3), # vort, pv,
        # cont_cntr_levs=range(-20, 21, 4), # p-e,
        # cont_cntr_levs=range(-10, 51, 10), # gms_each_level,
        # cont_cntr_levs=range(-4, 5, 1), # vcomp,
        # cont_cntr_levs=list(np.arange(-2, 2.1,0.5)),
        # cont_cntr_levs=list(np.arange(-2, 2.51, 0.5)), # tdt_conv/ls,
        # cont_cntr_levs=list(np.arange(0.5, 6.6, 1)), # mc,
        # cont_cntr_levs=range(1, 20, 3), # sphum,
        # cont_cntr_levs=range(1, 12, 2), # evap,
        # cont_cntr_levs=range(2,26,3), # precip,
        # cont_cntr_levs=range(5, 36, 5), # cld_amt,
        # cont_cntr_levs=range(10, 101, 20), # rh,
        # cont_cntr_levs=range(210,311,20), # temp,
        # cont_cntr_levs=range(200,331,5), # t_surf,
        # cont_cntr_levs=range(200, 361, 10), # equiv_pot_temp; virt_pot_temp; MSE,
        # cont_cntr_levs=range(990,1041,3), # slp,
        # cont_cntr_levs=range(200, 301, 20), # temp,
        # cont_cntr_levs=[[range(200,331,5)],[range(10,101,10)]],
        # cont_cntr_labels: 'True', '%d' for integer, '%0.1f' for decimal,
        # cont_cntr_labels='%d',

        ## Latitude plot parameters.
        # x_data=[['lat']],
        # lat_bounds=[-90,90],
        # lat_ticks=range(-90,91,30),
        # lat_ticks=list(np.sin(np.deg2rd(np.arange(-90., 91., 10.)))),
        # lat_labels=[r'90$^\circ$S', '', '', '', '', '', '30$^\circ$S', '', '', 'EQ', ,
                   # '', '', '30$^\circ$N', '', '', '', '', '', '90$^\circ$N']
        # lat_labels=[r'90$^\circ$S', '60$^\circ$S', '30$^\circ$S', 'EQ',,
        #               '30$^\circ$N', '60$^\circ$N', '90$^\circ$N'],

        ## Longitude plot parameters.
        # x_data=[['lon']],
        # lon_bounds=(-90,60),
        # lat_avg_range=(10, 20),
        # lon_ticks=range(Fig.lon_bounds[0], Fig.lon_bounds[1]+1, 30),
        # lon_ticks=False,

        # def make_lon_ticklabels(lon_ticks, circ=True):,
        #     lon_labels=[],
        #     c=r'$^\circ$' if circ else '',
        #     for tick in lon_ticks:,
        #         if tick < 0:,
        #             lon_labels.append(r'%d%sW' % (abs(tick), c)),
        #         elif tick > 0:,
        #             lon_labels.append(r'%d%sE' % (abs(tick), c)),
        #         else:,
        #             lon_labels.append(r"0%s" % c),
        #     return lon_labels,

        # lon_labels=make_lon_ticklabels(lon_ticks),
        # lon_labels=[str(x) for x in lon_ticks],
        # lon_labels=False,

        ## Zonal-seasonal and zonal-1d plot parameters
        # do_itcz=False,
        # had_bnds_type='500hPa',
        # plot_had_bnds=[False, False, False],
        # mask_hadley=True,
        # lat_type='reg',

        ## Vert plot parameters.
        # z_data=[['level']],
        # lev_type='linear',             # 'linear' 'exp',
        # lev_bounds=[1000, 100],
        # lev_ticks=range(1000, 99, -100),
        # lev_ticklabel=['1000', '', '800', '', '600', '', '400', '', '200', ''],
        # lev_label='hPa',

        # do_vert_centroid=(100, 1000),
        # centroid_xpos=0,
        # centroid_xpos=[[xlim[0]]*4 + [xlim[0] + 5]*2],
        # do_plot_avg=False,
        # do_plot_shading=True,

        ## Time-1D plot paramters
        # time_lim='ann_cycle',          # 'ann_cycle',
        # time_ticks=False,
        # time_ticklabels=False,

        ## Map plot parameters.
        map_proj='cyl',                # 'moll',
        map_res='c',
        # left_lon=0,
        shiftgrid_start=False,
        shiftgrid_cyclic=360.0,
        latlon_rect=(-18, 40, 10, 20),

        ## Quiver (i.e. arrow) plot overlayed on maps.
        do_quiver=False,
        # level_quiv=level,
        # xvar_quiv='ucomp',
        # yvar_quiv='vcomp',
        # xrun_quiv=cont_run,
        # yrun_quiv=xrun_quiv,
        # scalar_quiv=None,
        # quiv_skip=False,
        # quiv_kwargs={'color': 'red', 'edgecolors': 'red'},
        # do_quiv_key=True,
        # scale_quiv_key=10,
        # label_quiv_key=str(scale_quiv_key) + r' g kg$^{-1}$ m s$^{-1}$',

        ## Line plot parameters.
        line_color='k',
        linestyle='-',

        ## Scatter plot parameters
        marker_size=10,
        marker_color='k',
        marker_shape='.',
        # do_best_fit_line=[True] + [[True, False]]*3,
        # print_best_fit_slope=[True] + [[True, False]]*3,
        # print_corr_coeff=[True] + [[True, False]]*3,

        ## Statistical masking parameters.
        # do_stat_mask='ttest'             # False 'ttest',
        # do_stat_mask=[[False], ['ttest']],
        # stat_mask_cntrs=[0, 0.05] # Mark where significant.,
        # stat_mask_cntrs=[0.05, 1] # Mark where insignificant.,
        # stat_mask_hatch=['///'] # ['...'] ['XXX'],
        # stat_mask_hatch='mask',
        # stat_mask_color='b', # 2015-02-27: not yet working,

        ## Transformations to apply to data.
        do_subtract_mean=False,
        # do_zasym=False,
        # do_norm_cont=False,
        # do_normalize=False,
        # norm_region='sahel',
        # norm_var='precip,' # False
        # norm_run=cont_run, # runs

        ## 1d plot parameters
        # colors=['brown', 'orange', 'cyan', 'blue', 'gray'],
        # linestyles='-', # [':', '-', '--']
        # linewidths=[1.5],
        # do_legend=True,             # 'first', True
        # legend_labels='models',
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
