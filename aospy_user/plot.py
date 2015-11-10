#! /usr/bin/env python
"""Script that interfaces w/ aospy.plotting to create multi-panel plots."""
import aospy
from aospy_user import projs
from aospy_user import variables as v
from aospy_user import regions
import matplotlib


def plot(plot_params, fig_kwargs):
    fig = aospy.plotting.Fig(plot_params, fig_kwargs)
    fig.create_fig()
    fig.make_plots()
    matplotlib.pyplot.show()
    return fig


class PlotMainParams(object):
    """Interface to main routine."""
    def __init__(self):
        pass

    def prep_data(self):
        proj = aospy.to_proj(self.proj, projs)
        model = aospy.to_model(self.model, proj, projs)
        run = aospy.to_run(self.run, model, proj, projs)
        var = aospy.to_var(self.var, v)
        region = aospy.to_region(self.region, regions, proj=proj)
        proj, model, var, region = [aospy.to_iterable(obj)
                                    for obj in (proj, model, var, region)]
        self.proj = proj
        self.model = model
        self.run = run
        self.var = var
        self.region = region


def plot_main(main_params):
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['font.sans-serif'] = 'Helvetica'
    main_params.prep_data()
    return plot(main_params)
