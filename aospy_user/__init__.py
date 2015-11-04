"""My library of aospy objects used for my research."""
from aospy import (LAT_STR, LON_STR, PHALF_STR, PFULL_STR, PLEVEL_STR,
                   TIME_STR, TIME_STR_IDEALIZED)

from . import units
from . import regions
from . import sphere_harm
from .sphere_harm import SpharmInterface
from . import calcs
from . import variables
from . import runs
from . import models
from . import projs
