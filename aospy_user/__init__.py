"""My library of aospy objects used for my research."""
from aospy.internal_names import (LAT_STR, LON_STR, PHALF_STR, PFULL_STR,
                                  PLEVEL_STR, TIME_STR)

from . import units
from . import regions
from . import calcs
from . import variables
from . import runs
from . import models
from . import projs
from .main import MainParams, MainParamsParser, CalcSuite, ObjectsForCalc, main
from . import plot
from .plot import PlotMainParams, plot_main
