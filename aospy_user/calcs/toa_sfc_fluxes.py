"""Top-of-atmosphere and surface flux quantities"""
from aospy.constants import L_v
import numpy as np


def albedo(swdn_toa, swup_toa):
    """Net column albedo, i.e. fraction of insolation reflected back."""
    return np.ma.masked_where(swdn_toa == 0., swup_toa/swdn_toa)


def sfc_albedo(swdn_sfc, swup_sfc):
    """Net surface albedo, i.e. fraction of SW at surface reflected back."""
    return np.ma.masked_where(swdn_sfc == 0., swup_sfc/swdn_sfc)


def toa_sw(swdn_toa, swup_toa):
    """All-sky TOA net shortwave radiative flux into atmosphere."""
    return swdn_toa - swup_toa


def cre_sw(swup_toa, swup_toa_clr):
    """Cloudy-sky TOA net shortwave radiative flux into atmosphere."""
    return -1*swup_toa + swup_toa_clr


def cre_lw(olr, olr_clr):
    """Cloudy-sky outgoing longwave radiation"""
    return -1*olr + olr_clr


def cre_net(swup_toa, olr, swup_toa_clr, olr_clr):
    """Cloudy-sky TOA downward radiative flux."""
    return cre_sw(swup_toa, swup_toa_clr) + cre_lw(olr, olr_clr)


def toa_rad(swdn_toa, swup_toa, olr):
    """All-sky TOA downward radiative flux."""
    return swdn_toa - swup_toa - olr


def toa_rad_clr(swdn_toa_clr, swup_toa_clr, olr_clr):
    """Clear-sky TOA downward radiative flux."""
    return swdn_toa_clr - swup_toa_clr - olr_clr


def sfc_sw(swup_sfc, swdn_sfc):
    """All-sky surface upward shortwave radiative flux."""
    return swup_sfc - swdn_sfc


def sfc_sw_cld(swup_sfc, swup_sfc_clr, swdn_sfc, swdn_sfc_clr):
    """Cloudy-sky surface upward shortwave radiative flux."""
    return swup_sfc - swup_sfc_clr - swdn_sfc + swdn_sfc_clr


def sfc_lw(lwup_sfc, lwdn_sfc):
    """All-sky surface net longwave radiative flux into atmosphere."""
    return lwup_sfc - lwdn_sfc


def sfc_lw_cld(lwup_sfc, lwup_sfc_clr, lwdn_sfc, lwdn_sfc_clr):
    """Cloudy-sky surface net longwave radiative flux into atmosphere."""
    return lwup_sfc - lwup_sfc_clr - lwdn_sfc + lwdn_sfc_clr


def sfc_rad(swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc):
    """All-sky surface upward radiative flux."""
    return swup_sfc - swdn_sfc + lwup_sfc - lwdn_sfc


def sfc_rad_cld(swup_sfc, swup_sfc_clr, swdn_sfc, swdn_sfc_clr,
                lwup_sfc, lwup_sfc_clr, lwdn_sfc, lwdn_sfc_clr):
    """Cloudy-sky upward surface radiative flux."""
    return (swup_sfc - swup_sfc_clr - swdn_sfc + swdn_sfc_clr +
            lwup_sfc - lwup_sfc_clr - lwdn_sfc + lwdn_sfc_clr)


def sfc_energy(swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap):
    """All sky net upward surface radiative plus enthalpy flux."""
    return swup_sfc - swdn_sfc + lwup_sfc - lwdn_sfc + shflx + L_v*evap


def column_energy(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
                  lwup_sfc, lwdn_sfc, shflx, evap):
    """All sky net TOA and surface radiative and enthalpy flux into atmos."""
    return (toa_rad(swdn_toa, swup_toa, olr) +
            sfc_energy(swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap))


def column_sw(swdn_toa, swup_toa, swup_sfc, swdn_sfc):
    """All sky net SW flux into atmosphere."""
    return toa_sw(swdn_toa, swup_toa) + sfc_sw(swup_sfc, swdn_sfc)


def column_lw(olr, lwup_sfc, lwdn_sfc):
    """All sky net LW flux into atmosphere."""
    return -1*olr + sfc_lw(lwup_sfc, lwdn_sfc)


def bowen_ratio(shflx, evap):
    """Bowen ratio: surface SH/LH."""
    return shflx/(L_v * evap)


def evap_frac(evap, shflx):
    """Evaporative fraction: surface LH/(SH+LH)."""
    return L_v*evap / (L_v*evap + shflx)
