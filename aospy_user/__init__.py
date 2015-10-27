"""aospy_user: Library of user-defined aospy objects."""
from aospy import (LAT_STR, LON_STR, PHALF_STR, PFULL_STR, PLEVEL_STR,
                   TIME_STR, TIME_STR_IDEALIZED)

from . import regions
from . import units
from . import calcs
from . import variables
from . import runs
from . import models
from . import projs
from . import obj_from_name
from .obj_from_name import (to_proj, to_model, to_run, to_var, to_region,
                            to_iterable)
