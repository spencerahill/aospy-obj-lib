"""Thermodynamic functions."""
from aospy import PLEVEL_STR
from aospy.constants import (c_p, grav, kappa, L_f, L_v, p_trip, T_trip, c_va,
                             c_vv, c_vl, c_vs, R_a, R_v, R_d, epsilon)
from aospy.utils import dp_from_p, get_dim_name, to_pascal
import numpy as np


def dse(temp, hght):
    """Dry static energy.  Units: Joules per kilogram.

    :param temp: Temperature.  Units: Kelvin.
    :param hght: Geopotential height. Units: meters.
    """
    return c_p.value*temp + grav.value*hght


def mse(temp, hght, sphum):
    """Moist static energy, in Joules per kilogram."""
    return dse(temp, hght) + L_v.value*sphum


def fmse(temp, hght, sphum, ice_wat):
    """Frozen moist static energy, in Joules per kilogram."""
    return mse(temp, hght, sphum) - L_f.value*ice_wat


def pot_temp(temp, p, p0=1000.):
    """Potential temperature.  Units: Kelvin."""
    return temp*(p0/p)**kappa.value


def virt_pot_temp(temp, p, sphum, liq_wat, p0=1000.):
    """Virtual potential temperature, approximating the mixing ratios as
    specific humidities.
    """
    return pot_temp(temp, p, p0=p0) * (1. + 0.61*sphum - liq_wat)


def equiv_pot_temp(temp, p, sphum, p0=1000.):
    """Equivalent potential temperature."""
    return pot_temp(temp + L_v.value*sphum/c_p, p, p0=p0)


def mixing_ratio_from_specific_mass(mass):
    return mass / (1 - mass)


def virt_temp(temp, sphum, is_mixing_ratio=False):
    """Virtual temperature computed from temperature and specific humidity."""
    if is_mixing_ratio:
        wv_mix = sphum
    else:
        wv_mix = mixing_ratio_from_specific_mass(sphum)
    return temp * (wv_mix + epsilon.value) / (epsilon.value * (1. + wv_mix))


def z_from_hypso(ps, temp, sphum):
    """Compute height using the hypsometric equation w/ virtual temperature."""
    p_names = (PLEVEL_STR, 'plev')
    p_str = get_dim_name(temp, p_names)
    p_ax_num = temp.get_axis_num(p_str)
    p = to_pascal(temp[p_str])
    dp = dp_from_p(p, ps)
    t_virt = virt_temp(temp, sphum)
    temp_na0 = t_virt.fillna(0.)
    z = R_d.value / grav.value * np.cumsum(temp_na0 / p * dp.fillna(0.),
                                           axis=p_ax_num)
    return z.where(temp_na0)


def mse_from_hypso(ps, temp, sphum):
    """Moist static energy, with height computed using hypsometric eq."""
    return mse(temp, z_from_hypso(ps, temp, sphum), sphum)


def specific_mass_dry_air(q_v, q_l, q_s):
    """Specific mass of dry air from the specific masses of water phases."""
    return 1. - q_v - q_l - q_s


def specific_gas_constant_moist_air(q_v, q_l, q_s):
    """Specific gas constant of moist air with the given water masses."""
    q_a = specific_mass_dry_air(q_v, q_l, q_s)
    return q_a*R_a.value + q_v*R_v.value


def heat_capacity_moist_air_constant_volume(q_v, q_l, q_s):
    """Heat capacity at constant volume of moist air."""
    q_a = specific_mass_dry_air(q_v, q_l, q_s)
    return c_va.value*q_a + c_vv.value*q_v + c_vl.value*q_l + c_vs.value*q_s


def specific_entropy_dry_air(T, p):
    """Specific entropy of dry air.  From Romps."""
    return (c_p.value*np.log(T/T_trip.value) -
            R_d.value*np.log(p / p_trip.value))


def specific_entropy_water_vapor(T, p):
    """Specific entropy of water vapor.  From Romps."""
    return (c_p.value*np.log(T/T_trip.value) -
            R_d.value*np.log(p / p_trip.value))
