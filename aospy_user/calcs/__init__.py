"""My library of functions for use in aospy.

Except for helper functions, all assume input variables with the first axis
denoting time and the subsequent axes either (pressure, lat, lon) or, if not
vertically defined, (lat, lon).
"""
import scipy.stats
import numpy as np

from aospy.constants import (c_p, grav, kappa, L_f, L_v, r_e, Omega, p_trip,
                             T_trip, c_va, c_vv, c_vl, c_vs, R_a, R_v,
                             E_0v, E_0s, s_0v, s_0s)
from aospy.utils import (level_thickness, to_pascal, to_radians,
                         int_dp_g, weight_by_delta)


# General finite differencing functions.
def fwd_diff1(f, dx):
    """1st order accurate forward differencing."""
    if isinstance(dx, (float, int)):
        return (f[1:] - f[:-1]) / dx
    else:
        return (f[1:] - f[:-1]) / (dx[1:] - dx[:-1])


def cen_diff2(f, dx):
    """2nd order accurate centered differencing."""
    if isinstance(dx, (float, int)):
        return (f[2:] - f[:-2]) / (2.*dx)
    else:
        return (f[2:] - f[:-2]) / (dx[:-1] + dx[:1])


def cen_diff4(f, dx):
    """4th order accurate centered differencing."""
    if isinstance(dx, (float, int)):
        return (8*(f[3:-1] - f[1:-3]) - (f[4:] - f[:-4])) / (12.*dx)
    else:
        # Assume len(dx) == len(f) - 1.
        d1 = (f[3:-1] - f[1:-3]) / (dx[1:-2] + dx[2:-1])
        d2 = (f[4:] - f[:-4]) / (dx[:-3] + dx[1:-2] + dx[2:-1] + dx[3:])
        return (4*d1 - d2) / 3.


def upwind_order1(df_fwd, df_bwd, a):
    """1st order upwind differencing scheme for advection.

    :param df_fwd: Forward difference of the field.
    :oaram df_bwd: Backard difference of the field.
    :param a: Flow that is advecting the field `f`.
    """
    a_pos = np.ma.where(a >= 0., a, 0)
    a_neg = np.ma.where(a < 0., a, 0)
    return a_pos*df_bwd + a_neg*df_fwd


# Functions for derivatives in x, y, and p.
def latlon_deriv_prefactor(lat, radius, d_dy_of_scalar_field=False):
    """Factor that multiplies del operations in spherical coordinates."""
    if d_dy_of_scalar_field:
        return 1. / radius
    else:
        return 1. / (radius*np.cos(to_radians(lat)))


def dlon_from_lon(lon):
    "Compute longitude spacing and confirm it is uniform as assumed."""
    dlon = lon[1] - lon[0]
    assert np.allclose(360. - (lon[-1] - lon[0]), dlon)
    assert np.allclose(lon[2:] - lon[1:-1], lon[1:-1] - lon[:-2])
    lon_rad = to_radians(lon)
    return lon_rad[1] - lon_rad[0]


def d_dx_from_latlon(field, lat, lon, radius):
    """Compute \partial(field)/\partial x using centered differencing."""
    dlon = dlon_from_lon(lon)
    lat = to_radians(lat)
    prefactor = latlon_deriv_prefactor(lat, radius)[:,np.newaxis]
    # Assume latitude and longitude are last two axes.
    # Transpose the arrays: lon is 1st axis, lat is 2nd.
    f = field.T
    # Wrap around at 0/360 degrees longitude.
    f = np.ma.concatenate((f[-2:], f, f[:2]), axis=0)
    df_dx = cen_diff4(f, dlon)
    # Transpose again to regain original axis order.
    return prefactor*df_dx.T


def d_dy_from_latlon(field, lat, lon, radius, vec_field=False):
    """Compute \partial(field)/\partial y using centered differencing."""
    lat = to_radians(lat)
    dlat = lat[1:] - lat[:-1]
    # Assume latitude and longitude are last two axes.
    if field.ndim == 2:
        lat = lat[np.newaxis,:]
        dlat = dlat[np.newaxis,:]
    if field.ndim == 3:
        lat = lat[np.newaxis,:,np.newaxis]
        dlat = dlat[np.newaxis,:,np.newaxis]
    elif field.ndim == 4:
        lat = lat[np.newaxis,:,np.newaxis,np.newaxis]
        dlat = dlat[np.newaxis,:,np.newaxis,np.newaxis]
    f = field.T
    prefactor = 1. / radius
    # Del operator differs in spherical coords for scalar v. vector fields.
    if vec_field:
        f *= np.cos(lat)
        prefactor /= np.cos(lat)
        prefactor = prefactor.T
    # Roll lat to be leading axis for broadcasting.
    f = np.rollaxis(f, 1, 0)
    dlat = np.rollaxis(dlat, 1, 0)
    df_dy = np.ma.empty(f.shape)
    df_dy[2:-2] = cen_diff4(f,      dlat)
    df_dy[1]    = cen_diff2(f[:3],  dlat[:2])
    df_dy[-2]   = cen_diff2(f[-3:], dlat[-2:])
    df_dy[0]    = fwd_diff1(f[:2],  dlat[0])
    df_dy[-1]   = fwd_diff1(f[-2:], dlat[-1])
    # Roll axis and transpose again to regain original axis order.
    df_dy = np.rollaxis(df_dy, 0, 2)
    return prefactor*df_dy.T


def d_dp_from_p(field, p):
    """Derivative in pressure of a given field."""
    # Assume pressure is 3rd to last axis: ([time,] p, lat, lon)
    f = field.T
    p = to_pascal(p)
    # Amend array dimensions as necessary for broadcasting purposes.
    if p.ndim == 1:
        p = p[np.newaxis,np.newaxis,:,np.newaxis]
    elif p.ndim == 3:
        p = p[np.newaxis,:,:,:].T
    else:
        p = p.T
    # One-sided difference at TOA and surface; centered difference elsewhere.
    df_dp = np.ma.empty(f.shape)
    df_dp[:,:,1:-1] = (f[:,:,2:] - f[:,:,:-2]) / (p[:,:,2:] - p[:,:,:-2])
    df_dp[:,:,0]    = (f[:,:,1]  - f[:,:,0])   / (p[:,:,1]  - p[:,:,0])
    df_dp[:,:,-1]   = (f[:,:,-1] - f[:,:,-2])  / (p[:,:,-1] - p[:,:,-2])
    # Transpose again to regain original axis order.
    return df_dp.T


def zonal_advec_upwind(field, u, lat, lon, radius):
    """Advection in the zonal direction using upwind differencing."""
    prefactor = latlon_deriv_prefactor(lat, radius)[:,np.newaxis]
    # Assume latitude and longitude are last two axes.
    # Transpose the arrays: lon is 1st axis, lat is 2nd.
    f = field.T
    # Wrap around at 0/360 degrees longitude.
    # Assumes longitude array starts at 0 and goes to 360.
    f = np.ma.concatenate((f, f[:1]), axis=0)
    lon = to_radians(lon)[:,np.newaxis,np.newaxis,np.newaxis]
    lon = np.ma.concatenate((lon, 2*np.pi + lon[:1]), axis=0)
    df_fwd = fwd_diff1(f, lon)
    df_bwd = np.ma.concatenate((df_fwd[-1:], df_fwd[:-1]), axis=0)
    # Transpose again to regain original axis order.
    return prefactor*upwind_order1(df_fwd.T, df_bwd.T, u)


def merid_advec_upwind(field, v, lat, radius, vec_field=False):
    """Advection in the meridional direction using upwind differencing."""
    lat = to_radians(lat)
    # Assume latitude and longitude are last two axes.
    if field.ndim == 2:
        lat = lat[np.newaxis,:]
    if field.ndim == 3:
        lat = lat[np.newaxis,:,np.newaxis]
    elif field.ndim == 4:
        lat = lat[np.newaxis,:,np.newaxis,np.newaxis]
    f = field.T
    prefactor = 1. / radius
    # Del operator differs in spherical coords for scalar v. vector fields.
    if vec_field:
        f *= np.cos(lat)
        prefactor /= np.cos(lat)
        prefactor = prefactor.T
    # Roll lat to be leading axis for broadcasting.
    f = np.rollaxis(f, 1, 0)
    lat = np.rollaxis(lat, 1, 0)
    # Create arrays holding positive and negative values, each with forward
    # differencing at south pole and backward differencing at north pole.
    df_fwd_except_np = fwd_diff1(f, lat)
    df_bwd_except_sp = fwd_diff1(f[::-1], lat[::-1])[::-1]
    df_fwd = np.ma.concatenate((df_fwd_except_np,
                                df_bwd_except_sp[-1:]), axis=0)
    df_bwd = np.ma.concatenate((df_fwd_except_np[:1],
                                df_bwd_except_sp), axis=0)
    # Roll axis and transpose again to regain original axis order.
    df_fwd = np.rollaxis(df_fwd, 0, 2).T
    df_bwd = np.rollaxis(df_bwd, 0, 2).T
    return prefactor*upwind_order1(df_fwd, df_bwd, v)


def horiz_advec_upwind(field, u, v, lat, lon, radius, vec_field=False):
    return (zonal_advec_upwind(field, u, lat, lon, radius) +
            merid_advec_upwind(field, v, lat, radius, vec_field=vec_field))


def vert_advec_upwind(field, omega, p):
    """Advection in pressure using upwind differencing."""
    # Assume pressure is 3rd to last axis: ([time,] p, lat, lon)
    f = field.T
    p = to_pascal(p)
    # Amend array dimensions as necessary for broadcasting purposes.
    if p.ndim == 1:
        p = p[np.newaxis,np.newaxis,:,np.newaxis]
    elif p.ndim == 3:
        p = p[np.newaxis,:,:,:].T
    else:
        p = p.T
    # Roll pressure to be leading axis for broadcasting.
    f = np.rollaxis(f, 2, 0)
    p = np.rollaxis(p, 2, 0)
    # Create arrays holding positive and negative values, each with forward
    # differencing at south pole and backward differencing at north pole.
    df_fwd_partial = fwd_diff1(f, p)
    df_bwd_partial = fwd_diff1(f[::-1], p[::-1])[::-1]
    df_fwd = np.ma.concatenate((df_fwd_partial, df_bwd_partial[-1:]), axis=0)
    df_bwd = np.ma.concatenate((df_fwd_partial[:1], df_bwd_partial), axis=0)
    # Roll axis and transpose again to regain original axis order.
    df_fwd = np.rollaxis(df_fwd, 0, -1).T
    df_bwd = np.rollaxis(df_bwd, 0, -1).T
    return upwind_order1(df_fwd, df_bwd, omega)

def total_advec_upwind(field, u, v, omega, lat, lon, p, radius,
                       vec_field=False):
    return (horiz_advec_upwind(field, u, v, lat, lon, radius, vec_field) +
            vert_advec_upwind(field, omega, p))


# Trenberth mass balance & energy budget quantities
def column_total_mass(ps):
    """Total mass of atmospheric column (from Trenberth 1991)"""
    return ps / grav


def column_dry_air_mass(ps, wvp):
    """Total mass of dry air in an atmospheric column (from Trenberth 1991)"""
    return ps / grav - wvp


def column_dry_air_mass_tendency(q, u, v, lat, lon, radius, dp):
    """Time tendency of column dry air mass.  Trenberth 1991, Eq. (3)"""
    dry_air = 1 - q
    dry_air_flux_divg = field_horiz_flux_divg(dry_air, u, v, lat, lon, radius)
    return -1*int_dp_g(dry_air_flux_divg, dp)


def global_integral(field, sfc_area, dp):
    """Mass-weighted global integral of the given field."""
    vert_int = int_dp_g(field, dp)
    vert_int_flat = np.reshape(vert_int, (vert_int.shape[0], -1))
    # Assume first axis is time.
    return np.ma.sum(vert_int_flat*sfc_area.ravel(), axis=1)


def field_zero_global_mean(field, sfc_area, dp):
    """Subtract the global mean value from the given field."""
    ones = np.ma.ones(np.shape(field), mask=field.mask)
    global_mean = (global_integral(field, sfc_area, dp) /
                   global_integral(ones, sfc_area, dp))
    return field - global_mean[:,np.newaxis,np.newaxis,np.newaxis]


# Advection and divergence functions.
def zonal_advec(field, u, lat, lon, radius):
    """Zonal advection of the given field."""
    return u*d_dx_from_latlon(field, lat, lon, radius)


def meridional_advec(field, v, lat, lon, radius, vec_field=False):
    """Zonal advection of the given field."""
    return v*d_dy_from_latlon(field, lat, lon, radius, vec_field=vec_field)


def horiz_advec(field, u, v, lat, lon, radius, vec_field=False):
    """Horizontal advection of the given field."""
    return (zonal_advec(field, u, lat, lon, radius) +
            meridional_advec(field, v, lat, lon, radius, vec_field=vec_field))


def vert_advec(field, omega, p):
    """Vertical advection of the given field."""
    return omega*d_dp_from_p(field, p)


def total_advec(field, u, v, omega, lat, lon, p, radius, vec_field=False):
    """Total advection of the given field."""
    return (horiz_advec(field, u, v, lat, lon, radius, vec_field=vec_field) +
            vert_advec(field, omega, p))


def vert_advec_omega_zero_mean(field, omega, sfc_area, p, dp):
    """Vertical advection, with omega adjusted to equal 0 in global mean."""
    omega_adj = field_zero_global_mean(omega, sfc_area, dp)
    return omega_adj*d_dp_from_p(field, p)


def horiz_divg(u, v, lat, lon, radius):
    """Flow horizontal divergence."""
    du_dx = d_dx_from_latlon(u, lat, lon, radius)
    dv_dy = d_dy_from_latlon(v, lat, lon, radius, vec_field=True)
    return du_dx + dv_dy


def horiz_divg_from_windspharm(u, v):
    """Horizontal divergence computed using the windspharm package.

    The windspharm package can't handle masked data, so the procedure is as
    follows:

    1. Unmask the data, setting masked gridpoints to 0.
    2. Reshape the array, moving lat and lon to the first two dimensions
       and combining time and level into a single 3rd dimension.
    3. Perform the windspharm computations.
    4. Reshape the array back to its original shape.
    5. Re-apply the original mask and return the resulting array.

    Windspharm can handle 3-D data, but lat and lon have to be the first two
    dimensions.  So we have to reshape the array, moving time and/or level
    to be after lat and lon, and then reshape the array back.
    through the vertical and time indices.

    All steps except #3 are independent of the windspharm function being called.
    So we should have a single function that performs all steps, taking the
    function to be called in #3 as an argument.
    """
    from windspharm.standard import VectorWind
    w = VectorWind(u, v)
    return w.divergence()


def vert_divg(omega, p):
    """Flow vertical divergence."""
    return d_dp_from_p(omega, p)


def field_vert_int_bal(field, dp):
    """Impose vertical balance to the field, i.e. column integral = 0.

    Most frequently used for mass flux divergence to impose mass balance.
    """
    pos = np.ma.where(field > 0, field, 0)
    neg = np.ma.where(field < 0, field, 0)
    pos_int = int_dp_g(pos, dp)[:,np.newaxis,:,:]
    neg_int = int_dp_g(neg, dp)[:,np.newaxis,:,:]
    return pos - (pos_int/neg_int)*neg


def horiz_divg_mass_bal(u, v, lat, lon, radius, dp):
    """Horizontal divergence with column mass-balance correction applied."""
    div = horiz_divg(u, v, lat, lon, radius)
    return field_vert_int_bal(div, dp)


def vert_divg_mass_bal(omega, p, dp):
    """Vertical divergence with column mass-balance correction applied."""
    div = vert_divg(omega, p)
    return field_vert_int_bal(div, dp)


def divg_3d(u, v, omega, lat, lon, radius, p):
    """Total (3-D) divergence.  Should equal 0 by continuity."""
    horiz = horiz_divg(u, v, lat, lon, radius)
    vert = vert_divg(omega, p)
    return horiz + vert


def field_times_horiz_divg(field, u, v, lat, lon, radius):
    """Scalar field times horizontal divergence."""
    return field*horiz_divg(u, v, lat, lon, radius)


def field_times_horiz_divg_mass_bal(field, u, v, lat, lon, radius, dp):
    """Scalar field times horizontal divergence."""
    return field*horiz_divg_mass_bal(u, v, lat, lon, radius, dp)


def field_times_vert_divg_mass_bal(field, omega, p, dp):
    """Scalar field times vertical divergence."""
    return field*vert_divg_mass_bal(omega, p, dp)


def field_horiz_flux_divg(field, u, v, lat, lon, radius):
    """Horizontal flux divergence of given scalar field."""
    dfu_dx = d_dx_from_latlon(u*field, lat, lon, radius)
    dfv_dy = d_dy_from_latlon(v*field, lat, lon, radius, vec_field=True)
    return dfu_dx + dfv_dy


def field_vert_flux_divg(field, omega, p):
    """Vertical flux divergence of a scalar field."""
    return d_dp_from_p(omega*field, p)


def field_horiz_advec_divg_sum(field, u, v, lat, lon, radius, dp):
    return (
        field_times_horiz_divg_mass_bal(field, u, v, lat, lon, radius, dp) +
        horiz_advec(field, u, v, lat, lon, radius)
    )


def field_horiz_vert_advec_sum(field, u, v, omega, lat, lon, p, radius):
    return (horiz_advec(field, u, v, lat, lon, radius) +
            vert_advec(field, omega, p))


# Advection, divergence etc. applied to specific fields.
def mse_horiz_flux_divg(temp, hght, sphum, u, v, lat, lon, radius):
    """Horizontal flux convergence of moist static energy."""
    return field_horiz_flux_divg(mse(temp, hght, sphum),
                                 u, v, lat, lon, radius)


def mse_horiz_advec(temp, hght, sphum, u, v, lat, lon, radius):
    """Horizontal advection of moist static energy."""
    return horiz_advec(mse(temp, hght, sphum), u, v, lat, lon, radius)


def mse_times_horiz_divg(temp, hght, sphum, u, v, lat, lon, radius, dp):
    """Horizontal divergence of moist static energy."""
    return field_times_horiz_divg_mass_bal(
        mse(temp, hght, sphum), u, v, lat, lon, radius, dp
    )


def mse_horiz_advec_divg_sum(T, gz, q, u, v, lat, lon, rad, dp):
    return field_horiz_advec_divg_sum(mse(T, gz, q), u, v, lat, lon, rad, dp)


def mse_vert_flux_divg(T, gz, q, omega, p):
    """Vertical divergence times moist static energy."""
    return field_vert_flux_divg(mse(T, gz, q), omega, p)


def mse_vert_advec(temp, hght, sphum, omega, p):
    """Vertical advection of moist static energy."""
    return vert_advec(mse(temp, hght, sphum), omega, p)


def mse_times_vert_divg(T, gz, q, omega, p, dp):
    """Vertical divergence times moist static energy."""
    return field_times_vert_divg_mass_bal(mse(T, gz, q), omega, p, dp)


def mse_horiz_vert_advec_sum(temp, hght, sphum, u, v, omega, lat, lon, p,
                             radius):
    mse_ = mse(temp, hght, sphum)
    return field_horiz_vert_advec_sum(mse_, u, v, omega, lat, lon, p, radius)



def mse_horiz_advec_upwind(temp, hght, sphum, u, v, lat, lon, radius,
                           vec_field=False):
    return horiz_advec_upwind(mse(temp, hght, sphum), u, v, lat, lon, radius,
                              vec_field=vec_field)


def mse_vert_advec_upwind(temp, hght, sphum, omega, p):
    return vert_advec_upwind(mse(temp, hght, sphum), omega, p)


def mse_total_advec_upwind(temp, hght, sphum, u, v, omega, lat, lon, p, radius,
                           vec_field=False):
    return total_advec_upwind(mse(temp, hght, sphum), u, v, omega, lat, lon, p,
                              radius, vec_field=vec_field)


def mse_budget_advec_residual(temp, hght, sphum, ucomp, vcomp, omega, lat, lon,
                              p, dp, radius, swdn_toa, swup_toa, olr, swup_sfc,
                              swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap):
    """Residual in vertically integrated MSE budget."""
    mse_ = mse(temp, hght, sphum)
    transport = field_horiz_vert_advec_sum(
        mse_, ucomp, vcomp, omega, lat, lon, p, radius
    )
    trans_vert_int = int_dp_g(transport, dp)[:,np.newaxis,:,:]
    f_net = column_energy(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
                          lwup_sfc, lwdn_sfc, shflx, evap)
    return f_net - trans_vert_int


def fmse_budget_advec_residual(temp, hght, sphum, ice_wat, ucomp, vcomp, omega,
                               lat, lon, p, dp, radius, swdn_toa, swup_toa,
                               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc,
                               shflx, evap):
    """Residual in vertically integrated MSE budget."""
    fmse_ = fmse(temp, hght, sphum, ice_wat)
    transport = field_horiz_vert_advec_sum(
        fmse_, ucomp, vcomp, omega, lat, lon, p, radius
    )
    trans_vert_int = int_dp_g(transport, dp)[:,np.newaxis,:,:]
    f_net = column_energy(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
                          lwup_sfc, lwdn_sfc, shflx, evap)
    return f_net - trans_vert_int

def q_budget_advec_residual(sphum, ucomp, vcomp, omega, lat, lon, p, dp,
                            radius, evap, precip):
    """Residual in vertically integrated MSE budget."""
    transport = field_horiz_vert_advec_sum(
        sphum, ucomp, vcomp, omega, lat, lon, p, radius
    )
    trans_vert_int = int_dp_g(transport, dp)[:,np.newaxis,:,:]
    e_minus_p = evap - precip
    return e_minus_p - trans_vert_int

def q_budget_horiz_flux_divg_residual(sphum, ucomp, vcomp, lat, lon, dp,
                                      radius, evap, precip):
    """Residual in vertically integrated MSE budget."""
    transport = field_horiz_flux_divg(sphum, ucomp, vcomp, lat, lon, radius)
    trans_vert_int = int_dp_g(transport, dp)[:,np.newaxis,:,:]
    e_minus_p = evap - precip
    return e_minus_p - trans_vert_int


def dse_horiz_flux_divg(temp, hght, u, v, lat, lon, radius):
    """Horizontal flux convergence of moist static energy."""
    return field_horiz_flux_divg(dse(temp, hght), u, v, lat, lon, radius)


def dse_horiz_advec(temp, hght, u, v, lat, lon, radius):
    """Horizontal advection of moist static energy."""
    return horiz_advec(dse(temp, hght), u, v, lat, lon, radius)


def dse_times_horiz_divg(temp, hght, u, v, lat, lon, radius, dp):
    """Horizontal divergence of moist static energy."""
    return field_times_horiz_divg_mass_bal(
        dse(temp, hght), u, v, lat, lon, radius, dp
    )


def dse_horiz_advec_divg_sum(T, gz, u, v, lat, lon, rad, dp):
    return field_horiz_advec_divg_sum(dse(T, gz), u, v, lat, lon, rad, dp)


def dse_vert_advec(temp, hght, omega, p):
    """Vertical advection of moist static energy."""
    return vert_advec(dse(temp, hght), omega, p)


def q_horiz_flux_divg(q, u, v, lat, lon, radius):
    """Horizontal flux convergence of specific humidity."""
    return field_horiz_flux_divg(q, u, v, lat, lon, radius)


def q_horiz_advec(q, u, v, lat, lon, radius):
    """Horizontal advection of specific humidity."""
    return horiz_advec(q, u, v, lat, lon, radius)


def q_times_horiz_divg(q, u, v, lat, lon, radius, dp):
    """Horizontal divergence of specific humidity."""
    return field_times_horiz_divg_mass_bal(q, u, v, lat, lon, radius, dp)


def q_vert_advec(q, omega, p):
    """Vertical advection of specific humidity."""
    return vert_advec(q, omega, p)


def qu(sphum, u):
    """"Zonal moisture flux."""
    return sphum*u


def qv(sphum, v):
    """Meridional moisture flux."""
    return sphum*v


# Eddy computations.
def covariance(array1, array2, axis=None, weights=None):
    """
    Average `covariance` along the specified axis of two arrays.


    :param array1, array2: The two arrays to compute the covariance of.
    :type array1 array2: numpy.ndarray or numpy.ma.core.MaskedArray
    :param axis: Array axis number over which average is taken.
    :type axis: int or None
    :param weights: Weights used to perform the average.
    :type weights: int or None
    """
    prod = np.ma.multiply(array1, array2)
    return np.ma.average(prod, axis=axis, weights=weights)


def eddy_component(array, axis=None, weights=None):
    """Compute the deviation from the average along the specified axis.

    :param array: The array on which to compute the eddy component.
    :type array: Numpy array.
    :param axis: The index of the axis on which to compute.
    :type axis: int
    :param weights: An array of weights used to compute the average.
    :type weights: Numpy array or `None`
    """
    avg = np.ma.average(array, axis=axis, weights=weights)
    return np.ma.subtract(array, avg)


def eddy_covar_avg(array1, array2, axis=None, weights=None):
    """Compute the average eddy covariance of two fields.

    :param array1, array2: The two arrays to compute the covariance of.
    :type array1 array2: numpy.ndarray or numpy.ma.core.MaskedArray
    :param axis: Array axis number over which average is taken.
    :type axis: int or None
    :param weights: Weights used to perform the average.
    :type weights: int or None
    """
    cov1 = eddy_component(array1, axis=axis, weights=weights)
    cov2 = eddy_component(array2, axis=axis, weights=weights)
    return covariance(cov1, cov2, axis=axis, weights=weights)


# Thermodynamic functions.
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


# def mse_romps(T, q_v, q_s, z):
#     """Moist static energy defined in Romps 2015, JAS."""
#     pass


def specific_entropy_dry_air(T, p):
    """Specific entropy of dry air.  From Romps."""
    return c_p*np.log(T/T_trip) - R_d*np.log(p / p_trip)


def specific_entropy_water_vapor(T, p):
    """Specific entropy of water vapor.  From Romps."""
    return c_pv*np.log(T/T_trip) - R_d*np.log(p / p_trip)


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


# Gross moist stability-related quantities
def field_vert_int_max(field, dp):
    """Maximum magnitude of integral of a field from surface up."""
    dp = to_pascal(dp)
    # 2015-05-15: Problem: Sigma data indexing starts at TOA, while pressure
    #             data indexing starts at 1000 hPa.  So for now only do for
    #             sigma data and flip array direction to start from sfc.
    field_dp_g = weight_by_delta(field, dp)[::-1] / grav
    # Input array dimensions are assumed ([time dims,] level, lat, lon).
    pos_max = np.amax(np.cumsum(field_dp_g, axis=0), axis=-3)
    neg_max = np.amin(np.cumsum(field_dp_g, axis=0), axis=-3)
    # Flip sign because integrating from p_sfc up, i.e. with dp negative.
    return -1*np.where(pos_max > -neg_max, pos_max, neg_max)


def horiz_divg_vert_int_max(u, v, lat, lon, radius, dp):
    """Maximum magnitude of integral upwards of horizontal divergence."""
    return field_vert_int_max(horiz_divg_mass_bal(u, v, lat, lon, radius, dp),
                              dp)


def vert_divg_vert_int_max(omega, p, dp):
    """Maximum magnitude of integral from surface up of vertical divergence."""
    return field_vert_int_max(vert_divg_mass_bal(omega, p, dp), dp)


def gms_like_ratio(weights, tracer, dp):
    """Compute ratio of integrals in the style of gross moist stability."""
    # Integrate weights over lower tropospheric layer
    dp = to_pascal(dp)
    denominator = field_vert_int_max(weights, dp)
    # Integrate tracer*weights over whole column and divide.
    numerator = np.sum(weight_by_delta(weights*tracer, dp), axis=-3) / grav
    return numerator / denominator


def gross_moist_strat(sphum, u, v, lat, lon, radius, dp):
    """Gross moisture stratification, in horizontal divergence form."""
    divg = horiz_divg(u, v, lat, lon, radius)
    return L_v*gms_like_ratio(divg, sphum, dp)


def gross_dry_stab(temp, hght, u, v, lat, lon, radius, dp):
    """Gross dry stability, in horizontal divergence form."""
    divg = horiz_divg(u, v, lat, lon, radius)
    return -gms_like_ratio(divg, dse(temp, hght), dp)


def gross_moist_stab(temp, hght, sphum, u, v, lat, lon, radius, dp):
    """Gross moist stability, in horizontal divergence form."""
    divg = horiz_divg(u, v, lat, lon, radius)
    return -gms_like_ratio(divg, mse(temp, hght, sphum), dp)


# Radiative transfer quantities.
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
    return  -1*swup_toa + swup_toa_clr
# def cre_sw(swdn_toa, swup_toa, swdn_toa_clr, swup_toa_clr):
#     """Cloudy-sky TOA net shortwave radiative flux into atmosphere."""
#     return swdn_toa - swup_toa - swdn_toa_clr + swup_toa_clr


def cre_lw(olr, olr_clr):
    """Cloudy-sky OLR (outgoing longwave radiation, i.e. upwelling longwave radiative flux at TOA."""
    return -1*olr + olr_clr


def cre_net(swup_toa, olr, swup_toa_clr, olr_clr):
    """Cloudy-sky TOA downward radiative flux."""
    return cre_sw(swup_toa, swup_toa_clr) + cre_lw(olr, olr_clr)
# def cre_net(swdn_toa, swup_toa, olr, swdn_toa_clr, swup_toa_clr, olr_clr):
#     """Cloudy-sky TOA downward radiative flux."""
#     return swdn_toa - swup_toa - olr - swdn_toa_clr + swup_toa_clr + olr_clr


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
    return swup_sfc - swdn_sfc + lwup_sfc -lwdn_sfc


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


def tdt_diab(tdt_lw, tdt_sw, tdt_conv, tdt_ls):
    """Net diabatic heating rate."""
    return tdt_lw + tdt_sw + tdt_conv + tdt_ls


def tdt_lw_cld(tdt_lw, tdt_lw_clr):
    """Cloudy-sky temperature tendency from longwave radiation."""
    return tdt_lw - tdt_lw_clr


def tdt_sw_cld(tdt_sw, tdt_sw_clr):
    """Cloudy-sky temperature tendency from shortwave radiation."""
    return tdt_sw - tdt_sw_clr


def p_minus_e(precip, evap):
    """Precipitation minus evaporation."""
    return precip - evap


def bowen_ratio(shflx, evap):
    """Bowen ratio: surface SH/LH."""
    return shflx/(L_v * evap)


def evap_frac(evap, shflx):
    """Evaporative fraction: surface LH/(SH+LH)."""
    return L_v*evap / (L_v*evap + shflx)


# Zonal-mean, meridional circulation and mass transport quantities.
def msf(lats, levs, v):
    """Meridional mass streamfunction."""
    # Compute half level boundaries and widths.
    p_top = 5.; p_bot = 1005.
    p_half = 0.5*(levs[1:] + levs[:-1])
    p_half = np.insert(np.append(p_half, p_top), 0, p_bot)
    dp = to_pascal(p_half[:-1] - p_half[1:])[np.newaxis, ::-1, np.newaxis]
    geom_factor = (2.*np.pi*r_e/grav *
                   np.cos(np.deg2rad(lats))[np.newaxis, np.newaxis, :])
    # Integrate from TOA down to surface.
    msf_ = geom_factor * np.cumsum(v.mean(axis=-1) * dp, axis=1)[::-1]
    # Average the values calculated at half levels; flip sign by convention.
    msf_[:,:-1] = -0.5*(msf_[:,1:] + msf_[:,:-1])
    # Uppermost level goes to 0 hPa (so divide by 2); surface value is zero.
    msf_[:,-1]*=0.5; msf_[:,0] = 0.
    return msf_


def msf_max(lats, levs, v):
    """Maximum meridional mass streamfunction magnitude at each latitude."""
    strmfunc = msf(lats, levs, v)
    pos_max = np.amax(strmfunc, axis=1)
    neg_max = np.amin(strmfunc, axis=1)
    return np.where(pos_max > -neg_max, pos_max, neg_max)


def aht(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc,
        shflx, evap, snow_ls, snow_conv, sfc_area):
    """Total atmospheric northward energy flux."""
    # Calculate energy balance at each grid point.
    local = (column_energy(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
                           lwup_sfc, lwdn_sfc, shflx, evap) +
             L_f*(snow_ls + snow_conv))
    # Calculate meridional heat transport.
    local_flat = local.reshape((local.shape[0],-1))
    global_mean = np.ma.average(loc_flat, weights=sfc_area.ravel(), axis=1)
    zonal_integral = np.sum(
        sfc_area * (local_flat - global_mean[:,np.newaxis,np.newaxis]),
        axis=-1
    )
    return np.ma.cumsum(zonal_integral, axis=-1)


def gms_up_low(temp, hght, sphum, level, lev_up=400., lev_dn=925.):
    """Gross moist stability. Upper minus lower level MSE."""
    m = mse(temp, hght, sphum)
    return (np.squeeze(m[np.where(level == lev_up)] -
                       m[np.where(level == lev_dn)])/c_p)


def gms_each_level(temp, hght, sphum, level, lev_dn=925.):
    m = mse(temp, hght, sphum)
    return (m - m[np.where(level == lev_dn)])/c_p


def dry_static_stab(temp, hght, level, lev_dn=925.):
    d = dse(temp, hght)
    return (d - d[np.where(level == lev_dn)])/c_p


def moist_static_stab(temp, hght, sphum, p):
    mse_ = mse(temp, hght, sphum)
    return d_dp_from_p(mse_, p)
# def moist_static_stab(temp, p, sphum, p0=1000., lev_dn=925.):
#     theta_e = equiv_pot_temp(temp, p, sphum, p0=p0)
#     return (theta_e - theta_e[np.where(p == lev_dn)])


def gms_change_up_therm_low(temp, hght, sphum, level, lev_up=200., lev_dn=850.):
    """Gross moist stability. Upper minus lower level MSE with thermodynamic
    scaling estimate for low level MSE."""
    m = mse(temp, hght, sphum).mean(axis=-1)
    return (m[np.where(level == lev_up)] - m[np.where(level == lev_dn)])/c_p


def gms_h01(temp, hght, sphum, precip, level, lev_sfc=925.):
    """
    Approximation of gross moist stability from Held (2001).

    Near surface MSE diff b/w ITCZ and the given latitude.
    """
    # ITCZ defined as latitude with maximum zonal mean precip.
    itcz_ind = np.argmax(precip.mean(axis=-1))
    m = mse(np.squeeze(temp[np.where(level == lev_sfc)].mean(axis=-1)),
            np.squeeze(hght[np.where(level == lev_sfc)].mean(axis=-1)),
            np.squeeze(sphum[np.where(level == lev_sfc)].mean(axis=-1)))
    return (m[itcz_ind] - m)/c_p


def gms_h01est(temp, sphum, precip, level, lev_sfc=925.):
    """
    Approximation of gross moist stability from Held (2001).

    Near surface MSE diff b/w ITCZ and the given latitude, neglecting the
    geopotential term.
    """
    sphum = np.squeeze(sphum[np.where(level == lev_sfc)].mean(axis=-1))
    temp = np.squeeze(temp[np.where(level == lev_sfc)].mean(axis=-1))
    # ITCZ defined as latitude with maximum zonal mean precip.
    itcz_ind = np.argmax(np.mean(precip, axis=-1))
    # GMS is difference between surface values
    return temp[itcz_ind] - temp + L_v*(sphum[itcz_ind] - sphum)/c_p


def gms_h01est2(temp, hght, sphum, precip, level, lev_up=200., lev_sfc=925.):
    """
    Approximation of gross moist stability from Held (2001).

    MSE diff b/w ITCZ aloft and near surface at the given latitude.
    """
    # ITCZ defined as latitude with maximum zonal mean precip.
    itcz_ind = np.argmax(precip.mean(axis=-1))
    m_up = mse(np.squeeze(temp[np.where(level == lev_up)].mean(axis=-1)),
            np.squeeze(hght[np.where(level == lev_up)].mean(axis=-1)),
            np.squeeze(sphum[np.where(level == lev_up)].mean(axis=-1)))
    m_sfc = mse(np.squeeze(temp[np.where(level == lev_sfc)].mean(axis=-1)),
            np.squeeze(hght[np.where(level == lev_sfc)].mean(axis=-1)),
            np.squeeze(sphum[np.where(level == lev_sfc)].mean(axis=-1)))
    return (m_up[itcz_ind] - m_sfc)/c_p


def gms_change_est(T_cont, T_pert, q_cont, precip, level, lev_sfc=925.):
    """
    Gross moist stability change estimate.

    Near surface MSE difference between ITCZ and local latitude, neglecting
    geopotential term and applying a thermodynamic scaling for the moisture
    term.
    """
    # ITCZ defined as latitude with maximum zonal mean precip.
    itcz_ind = np.argmax(precip.mean(axis=-1))
    # Need temperature change at
    T_pert = np.squeeze(T_pert[np.where(level == lev_sfc)].mean(axis=-1))
    T_cont = np.squeeze(T_cont[np.where(level == lev_sfc)].mean(axis=-1))
    dT = T_pert - T_cont
    dT_itcz = T_pert[itcz_ind] - T_cont[itcz_ind]
    q_cont = np.squeeze(q_cont[np.where(level == lev_sfc)].mean(axis=-1))
    # GMS is difference between surface
    alpha = 0.07
    return ((c_p + L_v*alpha*q_cont[itcz_ind])*dT_itcz -
            (c_p + L_v*alpha*q_cont)*dT)/c_p


def gms_change_est2(T_cont, T_pert, q_cont, precip, level, lat,
                    lev_sfc=925., gamma=1.):
    """
    Gross moist stability change estimate.

    Near surface MSE difference between ITCZ and local latitude, neglecting
    geopotential term and applying a thermodynamic scaling for the moisture
    term, and multiplying the ITCZ terms by cos(lat) and a fixed fraction gamma
    to account for deviation of upper level MSE from the near surface ITCZ
    value.
    """
    # ITCZ defined as latitude with maximum zonal mean precip.
    itcz_ind = np.argmax(precip.mean(axis=-1))
    # Need temperature change at
    T_pert = np.squeeze(T_pert[np.where(level == lev_sfc)].mean(axis=-1))
    T_cont = np.squeeze(T_cont[np.where(level == lev_sfc)].mean(axis=-1))
    dT = T_pert - T_cont
    dT_itcz = T_pert[itcz_ind] - T_cont[itcz_ind]
    q_cont = np.squeeze(q_cont[np.where(level == lev_sfc)].mean(axis=-1))
    # GMS is difference between surface
    alpha = 0.07
    return (np.cos(np.deg2rad(lat))**2*gamma*
            (c_p + L_v*alpha*q_cont[itcz_ind])*dT_itcz -
            (c_p + L_v*alpha*q_cont)*dT)/c_p


def prec_conv_frac(prec_conv, precip, prec_ls=False):
    """Fraction of precipitation coming from convection scheme."""
    # Mask where precip is zero to avoid dividing by zero.
    prec_conv = np.ma.masked_where(precip == 0., prec_conv)
    precip = np.ma.masked_where(precip == 0., precip)
    if prec_ls:
        return prec_conv/(precip + prec_conv)
    else:
        return prec_conv/precip


def descent_tot(omega, mc):
    """Vertical motion from both convection and large-scale."""
    return omega + grav*mc


def ascent_ls(omega):
    """Large-scale vertically upward motion."""
    # Get positive values and replace negative ones with zero.
    return np.where(omega > 0., omega, 0)


def vert_centroid(field, level, p_bot=850., p_top=150.):
    """
    Compute the vertical centroid of some vertically defined field.
    """
    desired_levs = np.where((level <= p_bot) & (level >= p_top))
    lev_thick = level_thickness(level)/100.
    # Add axes for later broadcasting and truncate to desired vertical levels.
    level = level[desired_levs]; level = level[:,np.newaxis,np.newaxis]
    lev_thick = lev_thick[desired_levs]
    lev_thick = lev_thick[:,np.newaxis,np.newaxis]
    field = field[desired_levs]
    # For 1D arrays, have to move the vertical coordinate to leftmost dim.
    if field.ndim == 1:
        field = np.atleast_3d(field).swapaxes(0,1)
    else:
        field = np.atleast_3d(field)
    return (np.sum(field*level*lev_thick, axis=0) /
            np.sum(field*lev_thick, axis=0))


# Functions below this line haven't been converted to new argument format.
def tht(variables, **kwargs):
    """Total atmospheric plus oceanic northward energy flux."""
    # Calculate energy balance at each grid point.
    loc = -1*(variables[0] - variables[1] - variables[2])
    # Calculate meridional heat transport.
    len_dt = variables[0].shape[0]
    sfc_area = grid_sfc_area(nc)
    glb = np.average(loc.reshape(len_dt, -1),
                     weights=sfc_area.ravel(), axis=1)
    # AHT is meridionally integrated energy flux divergence.
    flux_div = np.sum(sfc_area*(glb[:,np.newaxis,np.newaxis] - loc), axis=-1)
    return np.cumsum(flux_div, axis=-1)


def oht(variables, **kwargs):
    """Total oceanic northward energy flux as residual of total minus atmospheric flux."""
    # Calculate energy balance at each grid point.
    loc = (variables[0] - variables[1] + variables[2] - variables[3] +   # sfc radiation
           variables[4] +                                 # sfc SH flux
           L_f*(variables[5] + variables[6]) + L_v*variables[7])   # column LH flux
    # Calculate meridional heat transport.
    len_dt = variables[0].shape[0]
    sfc_area = grid_sfc_area(nc)
    glb = np.average(loc.reshape(len_dt, -1),
                     weights=sfc_area.ravel(), axis=1)
    # AHT is meridionally integrated energy flux divergence.
    flux_div = np.sum(sfc_area*(glb[:,np.newaxis,np.newaxis] - loc), axis=-1)
    return np.cumsum(flux_div, axis=-1)
    #return tht(variables, **kwargs) - aht(variables, **kwargs)


def moc_flux(variables, **kwargs):
    """Mass weighted column integrated meridional flux by time and
    zonal mean flow."""
    # Specify upper bound of vertical integrals.
    p_top = kwargs.get('p_top', 0.)
    trop = np.where(nc.variables['level'][:] >= p_top)
    # Apply mass flux correction to zonal mean data.
    v_znl = np.squeeze(variables[-1][:,trop]).mean(axis=-1)
    v_north = np.where(v_znl > 0., v_znl, 0.)
    v_south = np.where(v_znl < 0., v_znl, 0.)
    lev_thick = np.squeeze(level_thickness(nc)[:,trop])/grav
    lev_thick = lev_thick[np.newaxis,:,np.newaxis]
    # Adjustment imposes that column integrated mass flux is zero.
    mass_adj = -((v_north*lev_thick).sum(axis=1) /
                 (v_south*lev_thick).sum(axis=1))
    # Integrate the specified flux by the adjusted v vertically and zonally.
    flux_type = kwargs['flux_type']
    if flux_type == 'dse':
        flux = (np.squeeze(dse(variables[:2])[:,trop]).mean(axis=-1) *
                (v_north + v_south * mass_adj[:,np.newaxis,:]))
    elif flux_type == 'mse':
        flux = (np.squeeze(mse(variables[:3])[:,trop]).mean(axis=-1) *
                (v_north + v_south * mass_adj[:,np.newaxis,:]))
    elif flux_type == 'moisture':
        flux = L_v*(np.squeeze(variables[0][:,trop]).mean(axis=-1) *
                (v_north + v_south * mass_adj[:,np.newaxis,:]))
    return (2.*np.pi*r_e*np.cos(np.deg2rad(nc.variables['lat'][:])) *
            (flux*lev_thick).sum(axis=1))


def moc_flux_raw(variables, **kwargs):
    """Mass weighted column integrated meridional flux by time and zonal mean flow, without applying column mass flux correction."""
    # Specify upper bound of vertical integrals.
    p_top = kwargs.get('p_top', 0.)
    trop = np.where(nc.variables['level'][:] >= p_top)
    # Take zonal mean and calculate grid level thicknesses.
    v_znl = np.squeeze(variables[-1][:,trop]).mean(axis=-1)
    lev_thick = np.squeeze(level_thickness(nc)[:,trop])/grav
    lev_thick = lev_thick[np.newaxis,:,np.newaxis]
    # Integrate the specified flux vertically and zonally.
    flux_type = kwargs.get('flux_type', 'mse')
    if flux_type == 'dse':
        flux = np.squeeze(dse(variables[:2])[:,trop]).mean(axis=-1) * v_znl
    elif flux_type == 'mse':
        flux = np.squeeze(mse(variables[:3])[:,trop]).mean(axis=-1) * v_znl
    elif flux_type == 'moisture':
        flux = L_v*np.squeeze(variables[0][:,trop]).mean(axis=-1) * v_znl
    return (2.*np.pi*r_e*np.cos(np.deg2rad(nc.variables['lat'][:])) *
            (flux*lev_thick).sum(axis=1))


def st_eddy_flux(variables, **kwargs):
    """Mass weighted column integrated meridional flux by stationary eddies."""
    p_top = kwargs.get('p_top', 0.)
    trop = np.where(nc.variables['level'][:] >= p_top)
    v = np.squeeze(variables[-1][:,trop])
    flux_type = kwargs['flux_type']
    if flux_type == 'dse':
        m = np.squeeze(dse(variables[:2])[:,trop])
    elif flux_type == 'mse':
        m = np.squeeze(mse(variables[:3])[:,trop])
    elif flux_type == 'moisture':
        m = np.squeeze(variables[0][:,trop])*L_v
    lev_thick = np.squeeze(level_thickness(nc)[:,trop])/grav
    lev_thick = lev_thick[np.newaxis,:,np.newaxis,np.newaxis]
    flux = ((m - m.mean(axis=-1)[:,:,:,np.newaxis]) *
            (v - v.mean(axis=-1)[:,:,:,np.newaxis]))
    return (2.*np.pi*r_e*np.cos(np.deg2rad(nc.variables['lat'][:])) *
            (flux*lev_thick).sum(axis=1).mean(axis=-1))


def moc_st_eddy_flux(variables, **kwargs):
    """Mass weighted column integrated flux by time mean flow."""
    return moc_flux(variables, **kwargs) + st_eddy_flux(variables, **kwargs)


def trans_eddy_flux(variables, **kwargs):
    """Meridional flux by transient eddies."""
    return aht(variables[4:], **kwargs) - moc_st_eddy_flux(variables[:4], **kwargs)


def eddy_flux(variables, **kwargs):
    """Meridional flux by stationary and transient eddies."""
    return aht(variables[4:], **kwargs) - moc_flux(variables[:4], **kwargs)


def mse_flux(variables, **kwargs):
    """Column integrated moist static energy meridional flux."""
    flux_type = kwargs.get('flux_type', 'moc')
    if flux_type == 'moc':
        return moc_flux(variables[:4], **kwargs)
    elif flux_type == 'st_eddy':
        return st_eddy_flux(variables[:4], **kwargs)
    elif flux_type == 'moc_st_eddy':
        return moc_st_eddy_flux(variables[:4], **kwargs)
    elif flux_type =='trans_eddy':
        return trans_eddy_fux(variables, **kwargs)
    elif flux_type == 'all':
        return aht(variables[4:], **kwargs)
    elif flux_type == 'eddy':
        return eddy_flux(variables, **kwargs)


def mass_flux(variables, **kwargs):
    """Meridional mass flux by time and zonal mean flow."""

    # Apply mass flux correction.
    lev_thick = level_thickness(nc)[np.newaxis,:,np.newaxis]/grav
    v_znl = variables[0].mean(axis=-1)
    v_north = np.where(v_znl > 0., v_znl, 0.)
    v_south = np.where(v_znl < 0., v_znl, 0.)
    mass_adj = -((v_north*lev_thick).sum(axis=1) /
                 (v_south*lev_thick).sum(axis=1))
    # Integrate vertically and pick level where magnitude maximized.
    int_flux = ((v_north + v_south*mass_adj[:,np.newaxis,:]) *
                lev_thick).cumsum(axis=1)
    flux_pos = np.amax(int_flux, axis=1)
    flux_neg = np.amin(int_flux, axis=1)
    return (2.*np.pi*r_e*np.cos(np.deg2rad(nc.variables['lat'][:])) *
            np.where(flux_pos > - flux_neg, flux_pos, flux_neg))


def gms_moc(variables, **kwargs):
    """Gross moist stability."""
    return -moc_flux(variables, **kwargs)/msf_max([variables[-1]], **kwargs)/c_p


def gms_msf(variables, **kwargs):
    """Gross moist stability."""
    return -(moc_st_eddy_flux(variables, **kwargs) /
            (msf_max([variables[-1]], **kwargs)*c_p))


def total_gms(variables, **kwargs):
    """Total (mean plus eddy) gross moist stability."""
    return -(aht(variables[:-1], **kwargs) /
             msf_max([variables[-1]], **kwargs))/c_p


def aht_no_snow(variables, **kwargs):
    """Total atmospheric northward energy flux."""
    # Calculate energy balance at each grid point.
    loc = -1*(variables[0] - variables[1] - variables[2] +             # TOA radiation
              variables[3] - variables[4] + variables[5] - variables[6] +   # sfc radiation
              variables[7] +                                 # sfc SH flux
              L_v*variables[-1])   # column LH flux
    # Calculate meridional heat transport.
    len_dt = variables[0].shape[0]
    sfc_area = grid_sfc_area(nc)
    glb = np.average(loc.reshape(len_dt, -1),
                     weights=sfc_area.ravel(), axis=1)
    # AHT is meridionally integrated energy flux divergence.
    flux_div = np.sum(sfc_area*(glb[:,np.newaxis,np.newaxis] - loc), axis=-1)
    return np.cumsum(flux_div, axis=-1)


def hadley_bounds(lats, levs, vcomp):
    """Poleward extent of Hadley Cell."""
    # Get meridional mass streamfunction at 500 hPa.
    p_ind = np.where(levs == 500.)
    sf = np.squeeze(msf(lats, levs, vcomp)[p_ind])
    zero_cross = np.where(np.diff(np.sign(sf)))[0]
    # Hadley Cell center is the zero crossing nearest the equator.
    ind_cent = np.argmin(np.abs(zero_cross - lats.size/2))
    # Hadley cell poleward boundaries are the zero crossings on either side.
    ind = [zero_cross[ind_cent + i] for i in range(-1,2)]
    # Linearly interpolate to true zero crossings.
    return np.array([lats[ind[i]+1] - (lats[ind[i]+1] - lats[ind[i]]) /
                (sf[ind[i]+1] - sf[ind[i]])*sf[ind[i]+1]
                for i in range(3)])


def had_bounds(strmfunc, lat, return_max=False):
    """Hadley cell poleward extent and center location."""

    # Get data max and min values and indices, such that min is north of max.
    z_max_ind, y_max_ind = np.where(strmfunc == strmfunc.max())
    z_max_ind = z_max_ind[0]; y_max_ind=y_max_ind[0]
    z_min_ind, y_min_ind = np.where(strmfunc[:,y_max_ind:] ==
                                    strmfunc[:,y_max_ind:].min())
    z_min_ind = z_min_ind[0]; y_min_ind = y_min_ind[0] + y_max_ind
    min_north = strmfunc[z_min_ind, y_min_ind]
    # Return locations and values of Hadley cells' strengths.
    if return_max:
        return [z_min_ind, y_min_ind, strmfunc[z_min_ind, y_min_ind],
                z_max_ind, y_max_ind, strmfunc[z_max_ind, y_max_ind]]
    # Find latitude where streamfunction at its level of maximum decreases
    # to 10% of that maximum value.
    had_max = np.where(np.diff(np.sign(strmfunc[z_max_ind] -
                                       0.1*strmfunc.max())))[0]
    had_min = np.where(np.diff(np.sign(strmfunc[z_min_ind] -
                                       0.1*strmfunc.min())))[0]
    had_lims = (np.intersect1d(range(y_max_ind), had_max)[-1],
               np.intersect1d(range(y_min_ind, lat.size), had_min)[0])
    # Center is streamfunction zero crossing between the two cells at level
    # halfway between the levels of the two maxima.
    p_ind = 0.5*(z_min_ind + z_max_ind)
    zero_cross = np.where(np.diff(np.sign(np.squeeze(
        strmfunc[p_ind,y_max_ind:y_min_ind]))))[0]
    had_center = zero_cross[0] + y_max_ind
    return np.array([lat[had_lims[0]], lat[had_center], lat[had_lims[1]]])


def had_bounds500(strmfunc, lat):
    """Hadley cells extent based on 500 hPa streamfunction zero crossings."""

    # Find latitudes where streamfunction at 500 hPa changes sign.
    strmfunc = strmfunc[5]
    zero_cross = np.where(np.diff(np.sign(strmfunc)))[0]
    # Hadley Cell center is the zero crossing nearest the equator.
    ind_cent = np.argmin(np.abs(zero_cross - lat.size/2))
    # Hadley cell poleward boundaries are the zero crossings on either side.
    ind = [zero_cross[ind_cent + i] for i in range(-1,2)]
    # Linearly interpolate to true zero crossings.
    return np.array([lat[ind[i]+1] - (lat[ind[i]+1] - lat[ind[i]]) /
                    (strmfunc[ind[i]+1] - strmfunc[ind[i]])*strmfunc[ind[i]+1]
                    for i in range(3)])


def thermal_equator(flux, lat):
    """Location of zero-crossing of energy flux."""

    # Find latitude indices where flux changes sign.
    zero_cross = np.where(np.diff(np.sign(flux)))[0]
    # Thermal equator is the zero crossing nearest the equator.
    ind = zero_cross[np.argmin(np.abs(zero_cross - lat.size/2))]
    # Linearly interpolate to true zero crossing latitude.
    return (lat[ind+1] - (lat[ind+1] - lat[ind]) /
            (flux[ind+1] - flux[ind])*flux[ind+1])


def itcz_pos(precip, lat, return_indices=False):
    """Calculate ITCZ location."""
    # Find the latitude index with maximum precip and calculate dP/d(latitude)
    # for the adjacent grid latitudes.
    ind_max = precip.argmax()
    if return_indices:
        return ind_max
    dP = np.gradient(precip[ind_max-1:ind_max+2])
    phi = np.deg2rad(lat)[ind_max-1:ind_max+2]
    dphi = np.gradient(phi)
    dP_dphi = dP/dphi
    # Find on which side of the maximum does dP/d(latitude) change sign.
    i = np.where(np.diff(np.sign(dP)))[0][0]
    # Linearly interpolate to determine the latitude of max precip.
    zero_interp = phi[i] - (dP_dphi[i]*(phi[i+1] - phi[i]) /
                            (dP_dphi[i+1] - dP_dphi[i]))
    return np.rad2deg(zero_interp)


def itcz_loc(lats, precip):
    """Calculate ITCZ location."""
    # Find the latitude index with maximum precip and calculate dP/d(latitude)
    # for the adjacent grid latitudes.
    ind_max = precip.argmax()
    dP = np.gradient(precip[ind_max-1:ind_max+2])
    phi = np.deg2rad(lats)[ind_max-1:ind_max+2]
    dphi = np.gradient(phi)
    dP_dphi = dP/dphi
    # Find on which side of the maximum does dP/d(latitude) change sign.
    i = np.where(np.diff(np.sign(dP)))[0][0]
    # Linearly interpolate to determine the latitude of max precip.
    return np.deg2rad(phi[i] - (dP_dphi[i]*(phi[i+1] - phi[i]) /
                               (dP_dphi[i+1] - dP_dphi[i])))


def prec_centroid(precip, lat, lat_max=20.):
    """
    Calculate ITCZ location as the centroid of the area weighted zonal-mean P.
    """
    # Interpolate zonal mean precip to a 0.1 degree latitude grid for 20S-20N
    trop = np.where(np.abs(lat) < lat_max)
    lat_interp = np.arange(-lat_max, lat_max + 0.01, 0.1)
    prec = np.interp(lat_interp, lat[trop], precip[trop])
    # Integrate area-weighted precip and find median.
    prec_int = np.cumsum(prec*np.abs(np.cos(np.deg2rad(lat_interp))))
    return lat_interp[np.argmin(np.abs(prec_int - 0.5*prec_int[-1]))]


def precip_centroid(lats, precip, lat_max=20.):
    """
    Calculate ITCZ location as the centroid of the area weighted zonal-mean P.
    """
    # Interpolate zonal mean P to 0.1 degree latitude grid over desired extent.
    trop = np.where(np.abs(lats) < lat_max)
    precip = precip.mean(axis=-1)[trop]
    lat_interp = np.arange(-lat_max, lat_max + 0.01, 0.1)
    prec = np.interp(lat_interp, lats[trop], precip)
    # Integrate area-weighted precip and find median.
    prec_int = np.cumsum(prec*np.abs(np.cos(np.deg2rad(lat_interp))), axis=0)
    return lat_interp[np.argmin(np.abs(prec_int - 0.5*prec_int[-1]), axis=0)]


def ang_mom(lats, ucomp):
    """Angular momentum per unit mass."""
    cos_lat = np.cos(np.deg2rad(lats[np.newaxis,:,np.newaxis]))
    return (Omega*r_e*cos_lat + ucomp)*r_e*cos_lat


def trop_height(level, T):
    """
    Tropopause height of each column, based on Reichler et al 2003 GRL.
    """
    # Get pressure and temperature data.
    p = level[:,np.newaxis,np.newaxis]
    # Compute half levels of pressure^kappa
    kap = R_d/c_p
    pkap_half = 0.5*(p[1:]**kap + p[:-1]**kap)
    # Compute lapse rate at half-levels, assuming T linear in pressure^kappa.
    Gamma = ((T[1:] - T[:-1])*(p[:-1]**kap + p[1:]**kap) /
            ((T[1:] + T[:-1])*(p[:-1]**kap - p[1:]**kap)))*kap*grav/R_d
    # Find levels of continuous Gamma where dT/dz > -2 K/km.
    Gamma_crit = -2e-3
    Gamma_good = np.where(Gamma > Gamma_crit, Gamma, 0)
    # Check that avg dT/dz in 2 km above > -2 K/km.
    Gam_slope = (Gamma[1:] - Gamma[:-1]) / (pkap_half[1:] - pkap_half[:-1])
    # Take lowest level satisfying these criteria.
    tp = 8
    # Linearly interpolate to pressure level of critical Gamma value.
    pkap_tp = (pkap_half[tp-1] + ((pkap_half[tp] - pkap_half[tp-1]) *
               (Gamma_crit - Gamma[tp-1])/(Gamma[tp] - Gamma[tp-1])))
    # Convert from pressure^kappa to pressure.
    return pkap_tp**(1./kap)


def flatten_spatial_dims(data):
    """Flatten all spatial dimensions of an input array.

    Assumes input array has shape (time, vert, lat, lon).
    """
    n_lon, n_lat, n_lev = data.shape[-1], data.shape[-2], data.shape[-3]
    n_pt = n_lon*n_lat*n_lev
    return data.reshape((-1, n_pt))


def pointwise_corr(x, y):
    """Pointwise Pearson correlation coefficient in time of two arrays.

    Assumes input arrays have shape (time, vert, lat, lon).
    """
    if not np.all(np.shape(x) == np.shape(y)):
        raise ValueError("x and y must have same shapes")
    # pearsonr only accepts 1d arrays.  Must flatten, compute, then reshape.
    orig_shape = np.shape(x)
    x, y = [flatten_spatial_dims(z) for z in (x, y)]
    n_pt = x.shape[-1]
    # pearsonr returns (corr, p_value).  Retain only corr via '[0]'.
    corr = [scipy.stats.pearsonr(x[:,i], y[:,i])[0] for i in range(n_pt)]
    # Reshape to original shape, but dropping the time dimension.
    return np.reshape(corr, orig_shape[1:])


def pointwise_lin_regr(x, y):
    """Pointwise least squares linear regression in time of two arrays.

    Assumes input arrays have shape (time, vert, lat, lon).  The regression is
    of x against y, i.e. the slope returned is m, where y=mx+b.
    """
    if not np.all(np.shape(x) == np.shape(y)):
        raise ValueError("x and y must have same shapes")
    # linregress only accepts 1d arrays.  Must flatten, compute, then reshape.
    orig_shape = np.shape(x)
    x, y = [flatten_spatial_dims(x) for x in (x, y)]
    n_pt = x.shape[-1]
    # linregress returns (slope, ...).  Retain only slope via '[0]'.
    slope = [scipy.stats.linregress(x[:,i], y[:,i])[0] for i in range(n_pt)]
    # Reshape to original shape, but dropping the time dimension.
    return np.reshape(slope, orig_shape[1:])


def corr_cre_sw(swup_toa, swup_toa_clr, var2):
    return pointwise_corr(cre_sw(swup_toa, swup_toa_clr), var2)


def corr_cre_lw(olr, olr_clr, var2):
    return pointwise_corr(cre_lw(olr, olr_clr), var2)


def corr_cre_net(swup_toa, olr, swup_toa_clr, olr_clr, var2):
    return pointwise_corr(cre_net(swup_toa, olr, swup_toa_clr, olr_clr), var2)


def corr_toa_rad_clr(swdn_toa_clr, swup_toa_clr, olr_clr, var2):
    return pointwise_corr(
        toa_rad_clr(swdn_toa_clr, swup_toa_clr, olr_clr), var2
    )


def lin_regr_cre_net(swup_toa, olr, swup_toa_clr, olr_clr, var2):
    return pointwise_lin_regr(
        var2, cre_net(swup_toa, olr, swup_toa_clr, olr_clr)
    )


def lin_regr_toa_rad_clr(swdn_toa_clr, swup_toa_clr, olr_clr, var2):
    return pointwise_lin_regr(
        var2, toa_rad_clr(swdn_toa_clr, swup_toa_clr, olr_clr)
    )
