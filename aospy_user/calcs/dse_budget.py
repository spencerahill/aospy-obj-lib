"""Functions relating to budget of dry static energy."""
from .advection import horiz_advec, vert_advec
from .transport import (field_horiz_flux_divg, field_times_horiz_divg,
                        field_horiz_advec_divg_sum)
from .thermo import dse


def dse_horiz_flux_divg(temp, hght, u, v, radius):
    """Horizontal flux convergence of dry static energy."""
    return field_horiz_flux_divg(dse(temp, hght), u, v, radius)


def dse_horiz_advec(temp, hght, u, v, radius):
    """Horizontal advection of dry static energy."""
    return horiz_advec(dse(temp, hght), u, v, radius)


def dse_times_horiz_divg(temp, hght, u, v, radius, dp):
    """Horizontal divergence of dry static energy."""
    return field_times_horiz_divg(dse(temp, hght), u, v, radius, dp)


def dse_horiz_advec_divg_sum(T, z, u, v, rad, dp):
    return field_horiz_advec_divg_sum(dse(T, z), u, v, rad, dp)


def dse_vert_advec(temp, hght, omega, p):
    """Vertical advection of dry static energy."""
    return vert_advec(dse(temp, hght), omega, p)
