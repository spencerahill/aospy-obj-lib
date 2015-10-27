"""Thermodynamic functions."""
from aospy.constants import (c_p, grav, kappa, L_f, L_v, p_trip, T_trip, c_va,
                             c_vv, c_vl, c_vs, R_a, R_v, R_d)
import numpy as np


def dse(temp, hght):
    """Dry static energy.  Units: Joules per kilogram.

    :param temp: Temperature.  Units: Kelvin.
    :param hght: Geopotential height. Units: meters.
    """
    try:
        ds = c_p*temp + grav*hght
    except ValueError:
        # On sigma coords, hght is at half levels; temp and sphum on full.
        try:
            ds = c_p*temp + grav*0.5*(hght[:,:-1] + hght[:,1:])
        except ValueError:
            ds = c_p*temp + grav*0.5*(hght[:,:,:-1] + hght[:,:,1:])
    return ds


def mse(temp, hght, sphum):
    """Moist static energy, in Joules per kilogram."""
    return dse(temp, hght) + L_v*sphum


def fmse(temp, hght, sphum, ice_wat):
    """Frozen moist static energy, in Joules per kilogram."""
    return mse(temp, hght, sphum) - L_f*ice_wat



def pot_temp(temp, p, p0=1000.):
    """Potential temperature.  Units: Kelvin."""
    return temp*(p0/p[:,np.newaxis,np.newaxis])**kappa


def virt_pot_temp(temp, p, sphum, liq_wat, p0=1000.):
    """Virtual potential temperature, approximating the mixing ratios as
    specific humidities.

    """
    return ((temp*(p0/p[:,np.newaxis,np.newaxis])**kappa) *
            (1. + 0.61*sphum - liq_wat))


def equiv_pot_temp(temp, p, sphum, p0=1000.):
    """Equivalent potential temperature."""

    return (temp + L_v*sphum/c_p)*(p0/p[:,np.newaxis,np.newaxis])**kappa


def mixing_ratio_from_specific_mass(mass):
    return mass / (1 - mass)


def specific_mass_dry_air(q_v, q_l, q_s):
    """Specific mass of dry air from the specific masses of water phases."""
    return 1. - q_v - q_l - q_s


def specific_gas_constant_moist_air(q_v, q_l, q_s):
    """Specific gas constant of moist air with the given water masses."""
    q_a = specific_mass_dry_air(q_v, q_l, q_s)
    return q_a*R_a + q_v*R_v


def heat_capacity_moist_air_constant_volume(q_v, q_l, q_s):
    """Heat capacity at constant volume of moist air."""
    q_a = specific_mass_dry_air(q_v, q_l, q_s)
    return c_va*q_a + c_vv*q_v + c_vl*q_l + c_vs*q_s


def specific_entropy_dry_air(T, p):
    """Specific entropy of dry air.  From Romps."""
    return c_p*np.log(T/T_trip) - R_d*np.log(p / p_trip)


def specific_entropy_water_vapor(T, p):
    """Specific entropy of water vapor.  From Romps."""
    return c_p*np.log(T/T_trip) - R_d*np.log(p / p_trip)
