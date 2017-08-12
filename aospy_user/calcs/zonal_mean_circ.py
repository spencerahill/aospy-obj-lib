"""Zonal-mean meridional circulation and mass transport quantities."""
from aospy.constants import c_p, grav, L_v, Omega, r_e, R_d
from aospy.internal_names import (LAT_STR, LON_STR, PLEVEL_STR, PFULL_STR,
                                  SFC_AREA_STR)
from aospy.region import _sum_over_lat_lon
from aospy.utils.vertcoord import level_thickness, to_pascal, int_dp_g
import numpy as np
import xarray as xr


from .thermo import dse, mse
from .toa_sfc_fluxes import toa_rad


def _cosdeg(arg):
    """Cosine, including conversion from degrees to radians."""
    return xr.ufuncs.cos(xr.ufuncs.deg2rad(arg))


def _lat_area_weight(lat):
    """Geometric factor corresponding to surface area at each latitude."""
    return 2.*np.pi*r_e*_cosdeg(lat)


def ang_mom(ucomp):
    """Angular momentum per unit mass."""
    cos_lat = _cosdeg(ucomp[LAT_STR])
    return (Omega*r_e*cos_lat + ucomp)*r_e*cos_lat


def merid_streamfunc(v, dp, impose_zero_col_flux=True):
    """Meridional mass streamfunction.

    Parameters
    ----------
    v : xarray.DataArray
        Meridional wind field.
    dp : xarray.DataArray
        Pressure thickness of each gridbox

    Returns
    -------
    xarray.DataArray
        The meridional mass streamfunction.
    """
    # Zonally average v and dp.
    v_znl_mean = v.mean(dim=LON_STR)
    dp_znl_mean = to_pascal(dp).mean(dim=LON_STR)
    # If desired, Impose zero net mass flux at each level.
    if impose_zero_col_flux:
        v_znl_mean = _subtract_col_avg(v_znl_mean, dp_znl_mean)
    # At each vertical level, integrate from TOA to that level.
    streamfunc = (v_znl_mean * dp_znl_mean).cumsum(dim=PFULL_STR) / grav.value
    # Weight by surface area to get a mass overturning rate.
    lats = v[LAT_STR]
    return _lat_area_weight(lats) * streamfunc


def _subtract_col_avg(arr, dp):
    """Impoze zero column integral by subtracting column average at each level.

    Used e.g. for computing the zonally integrated mass flux.  In the time-mean
    and neglecting tendencies in column mass, the column integrated meridional
    mass transport should be zero at each latitude; otherwise there would be a
    build up of mass on one side.

    """
    col_avg = int_dp_g(arr, dp) / int_dp_g(1., dp)
    return arr - col_avg


def _merid_mass_overturning(streamfunc):
    """Meridional overturning mass rate at each latitude.

    Calculated as the signed maximum magnitude of the meridional mass
    streamfunction at each latitude, which at different latitudes may occur at
    different levels.

    Parameters
    ----------
    streamfunc : xarray.DataArray
        Meridional mass streamfunction

    Returns
    -------
    xarray.DataArray
        The signed mass overturning strength at each latitude
    """
    # Get positive and negative extrema at each latitude.
    pos_max = streamfunc.max(dim=PFULL_STR)
    neg_max = streamfunc.min(dim=PFULL_STR)
    # Keep only the larger magnitude value at each latitude.
    max_magnitude = (pos_max.where(pos_max > -neg_max).fillna(0.) +
                     neg_max.where(pos_max <= -neg_max).fillna(0.))
    # Re-mask any latitudes that were originally masked; those masks would have
    # been lost via the above 'fillna' calls.
    return max_magnitude.where(pos_max).where(neg_max)


def merid_mass_overturning(v, dp):
    return _merid_mass_overturning(merid_streamfunc(v, dp))


def _merid_implied_flux(boundary_fluxes, adjust_global_mean=True):
    """Column-integrated meridional flux that balances given boundary fluxes.

    Strictly speaking, by not incorporating the time tendency, this is
    imperfect for non-steady states.

    Parameters
    ----------
    boundary_fluxes: xarray.DataArray
        The net flux of the given quantity into each column through both the
        top and bottom boundaries.  Assumed defined in longitude.
    adjust_global_mean : bool, default True
        Whether to subtract off any global mean of the boundary fluxes before
        integrating meridionally, thereby ensuring that the global mean of the
        transport is zero.

    Returns
    -------
    xarray.DataArray
       The column-integrated meridional flux of the given tracer at each
       latitude.  Array shape and coordinates will be the same as the original
       data.
    """
    if adjust_global_mean:
        sfc_area = boundary_fluxes[SFC_AREA_STR]
        global_mean = (_sum_over_lat_lon(boundary_fluxes * sfc_area) /
                       _sum_over_lat_lon(sfc_area))
        boundary_fluxes -= global_mean
    zonal_integral = (boundary_fluxes * sfc_area).sum(dim=LON_STR)
    return zonal_integral.cumsum(dim=LAT_STR)


def merid_total_energy_transport(swdn_toa, swup_toa, olr):
    """Atmosphere plus ocean energy flux that balances the given TOA fluxes.

    Parameters
    ----------
    swdn_toa, swup_toa, olr : xarray.DataArray
        Downwelling shortwave, upwelling shortwave, and upwelling (outgoing)
        longwave radiative flux, respectively.

    Returns
    -------
    xarray.DataArray
        The total atmosphere plus ocean energy transport that would balance the
        given TOA flux.
    """
    return _merid_implied_flux(toa_rad(swdn_toa, swup_toa, olr))


def merid_ocean_energy_transport(sw_net_sfc, lw_net_sfc, sens_heat_flux,
                                 latent_heat_flux):
    """Ocean energy flux that balances the given surface fluxes.

    Parameters
    ----------
    sw_net_sfc, lw_net_sfc : xarray.DataArray
        Net (upwelling minus downwelling) shortwave and longwave radiative flux
        at the surface, respectively.
    sens_heat_flux, latent_heat_flux : xarray.DataArray
        Surface sensible and latent heat fluxes, respectively.

    Returns
    -------
    xarray.DataArray
        The total ocean energy transport that would balance the given surface
        flux.
    """
    energy_sfc = sw_net_sfc + lw_net_sfc + sens_heat_flux + latent_heat_flux
    # Flip sign to get flux into the ocean, instead of into the atmosphere.
    return _merid_implied_flux(-1*energy_sfc)


def merid_atmos_energy_transport(swdn_toa, swup_toa, olr, sw_net_sfc,
                                 lw_net_sfc, sens_heat_flux, latent_heat_flux):
    """Atmospheric energy flux that balances the given surface + TOA fluxes.

    Parameters
    ----------
    swdn_toa, swup_toa, olr : xarray.DataArray
        Downwelling shortwave, upwelling shortwave, and upwelling (outgoing)
        longwave radiative flux at top-of-atmosphere (TOA), respectively.
    sw_net_sfc, lw_net_sfc : xarray.DataArray
        Net (upwelling minus downwelling) shortwave and longwave radiative flux
        at the surface, respectively.
    sens_heat_flux, latent_heat_flux : xarray.DataArray
        Surface sensible and latent heat fluxes, respectively.

    Returns
    -------
    xarray.DataArray
        The total atmosphere energy transport that would balance the given TOA
        plus surface flux.
    """
    col_energy = (swdn_toa - swup_toa - olr + sw_net_sfc + lw_net_sfc +
                  sens_heat_flux + latent_heat_flux)
    return _merid_implied_flux(col_energy)


def _gross_stab(energy_flux, mass_overturning, mass_threshold=1e9):
    """Ratio of an energy flux to a mass overturning strength.

    Utility function for use in various flavors of "gross moist stability", all
    of which are ultimately the ratio of an energy transport or divergence to a
    mass transport or divergence.
    """
    gross_stab = energy_flux / mass_overturning / c_p.value
    if mass_threshold:
        cond = xr.ufuncs.fabs(mass_overturning) > mass_threshold
        gross_stab = gross_stab.where(cond)
    return gross_stab


def total_gross_moist_stab(v, dp, swdn_toa, swup_toa, olr, sw_net_sfc,
                           lw_net_sfc, sens_heat_flux, latent_heat_flux):
    """Total atmospheric gross moist stability.

    Ratio of the total atmospheric energy transport (as inferred from the net
    radiative and turbulent fluxes at the surface and TOA) to the mass
    overturning strength.

    The "total" in the title signifies that the energy transport includes all
    sources, namely both eddies (transient and stationary) plus the time-mean
    flow.  A more traditional formulation is to use only the energy transport
    by the time-mean flow.

    References
    ----------
    Kang, Sarah M., Dargan M. W. Frierson, and Isaac M. Held.  "The Tropical
    Response to Extratropical Thermal Forcing in an Idealized GCM: The
    Importance of Radiative Feedbacks and Convective Parameterization."
    Journal of the Atmospheric Sciences 66, no. 9 (September 1, 2009):
    2812–27.  doi:10.1175/2009JAS2924.1.

    """
    aht = merid_atmos_energy_transport(swdn_toa, swup_toa, olr, sw_net_sfc,
                                       lw_net_sfc, sens_heat_flux,
                                       latent_heat_flux)
    return _gross_stab(aht, merid_mass_overturning(v, dp))


def _impose_zero_col_mass_flux(v_znl_mean, dp_znl_mean):
    """Impose zero column-integrated meridional mass transport.

    This is the expectation for steady states; otherwise there would be a
    build-up of mass in one direction or the other.  But calculations using
    post-processed model data can lead to slight imbalances, which then affect
    downstream calculations of meridional transports of energy, water, or other
    tracers.  As such it can be necessary to adjust the zonal-mean winds such
    that this zero-net-mass-flux condition is ensured.

    There are multiple ways in which the residual can be removed; this
    particular method is that described in the Appendix of Hill et al 2015,
    J. Climate.

    """
    v_north = v_znl_mean.where(v_znl_mean > 0.).fillna(0)
    v_south = v_znl_mean.where(v_znl_mean < 0.).fillna(0)
    mass_adj = int_dp_g(v_north, dp_znl_mean) / int_dp_g(v_south, dp_znl_mean)
    return v_north - v_south * mass_adj


def _merid_tracer_flux(dp, v, tracer):
    """Zonally and column-integrated meridional flux of a tracer."""
    return _lat_area_weight(v[LAT_STR]) * int_dp_g(tracer*v, dp)


def _merid_mmc_tracer_flux(dp, v, tracer, p_top=0., do_fix_mass=True):
    """Meridional energy flux by mean meridional circulation.

    Parameters
    ----------
    dp : xarray.DataArray
        Pressure thickness of each gridbox
    v : xarray.DataArray
        Meridional wind of each gridbox
    tracer : xarray.DataArray
        Tracer being transported
    p_top : float, int, or xarray.DataArray (default 0.0)
        Minimum pressure (i.e. highest vertical extent) over which column
        integrals will be performed.
    do_fix_mass : bool, default True
        Whether to apply an adjustment to the wind field after zonally
        integrating at each level such that the column integral at each
        latitude is (almost) exactly zero.  This is the expectation for steady
        states; otherwise there would be a build-up of mass in one direction or
        the other.

    Returns
    -------
    xarray.DataArray
        The column integrated transport of the given tracer by the time-mean,
        zonal-mean circulation (i.e. the "mean meridional circulation") at each
        latitude.

    """
    # Specify upper bound for column integrals.
    p_top_cond = tracer[PFULL_STR] >= p_top
    v_znl_mean = v.where(p_top_cond).mean(dim=LON_STR)
    dp_znl_mean = dp.where(p_top_cond).mean(dim=LON_STR)
    # Apply mass flux correction to zonal mean data.
    if do_fix_mass:
        v_znl_mean = _impose_zero_col_mass_flux(v_znl_mean, dp_znl_mean)
    # Integrate the specified flux by the adjusted v vertically and zonally.
    tracer_znl_mean = tracer.where(p_top_cond).mean(dim=LON_STR)
    return _merid_tracer_flux(dp_znl_mean, v_znl_mean, tracer_znl_mean)


def mean_merid_circ_mse_flux(dp, v, temp, hght, sphum):
    """Column-integrated MSE flux by mean meridional circulation (MMC)."""
    return _merid_mmc_tracer_flux(dp, v, mse(temp, hght, sphum))


def mean_merid_circ_gross_moist_stab(dp, v, temp, hght, sphum):
    """Gross moist stability of mean meridional circulation."""
    return _gross_stab(mean_merid_circ_mse_flux(dp, v, temp, hght, sphum),
                       merid_mass_overturning(v, dp))


def _zonal_asym_component(field, lon_str=LON_STR):
    """Field minus its zonal mean at each latitude."""
    return field - field.mean(dim=lon_str)


def _stationary_eddy_merid_tracer_flux(dp, v, tracer):
    """Column-integrated tracer flux by stationary eddies."""
    v_st_edd = _zonal_asym_component(v)
    tracer_st_edd = _zonal_asym_component(tracer)
    st_edd_flux = (v_st_edd*tracer_st_edd).mean(dim=LON_STR)
    dp_znl_mean = dp.mean(dim=LON_STR)
    return _lat_area_weight(v[LAT_STR])*int_dp_g(st_edd_flux, dp_znl_mean)


def stationary_eddy_merid_mse_flux(dp, v, temp, hght, sphum):
    """Column-integrated MSE flux by stationary eddies."""
    return _stationary_eddy_merid_tracer_flux(dp, v, mse(temp, hght, sphum))


def gms_change_up_therm_low(temp, hght, sphum, lev_up=200., lev_dn=850.):
    """Approximation to Hadley cell gross moist stability.

    Upper minus lower level MSE with thermodynamic scaling estimate for low
    level MSE.

    """
    m = mse(temp, hght, sphum).mean(dim=LAT_STR)
    return (m.sel(**{PLEVEL_STR: lev_up}) - m.sel(**{PLEVEL_STR: lev_dn}))/c_p


def gms_h01(temp, hght, sphum, precip, level, lev_sfc=925.):
    """Approximation of gross moist stability from Held (2001).

    Near surface MSE diff b/w ITCZ and the given latitude.
    """
    # ITCZ defined as latitude with maximum zonal mean precip.
    itcz_ind = precip.mean(dim=LON_STR).argmax(dim=LAT_STR)
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
    return (_cosdeg(lat)**2*gamma*
            (c_p + L_v*alpha*q_cont[itcz_ind])*dT_itcz -
            (c_p + L_v*alpha*q_cont)*dT)/c_p


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


def had_bounds(strmfunc, return_max=False):
    """Hadley cell poleward extent and center location."""
    lat = strmfunc[LAT_STR]
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


def itcz_pos(precip, return_indices=False):
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


def prec_centroid(precip, lat_max=20.):
    """
    Calculate ITCZ location as the centroid of the area weighted zonal-mean P.
    """
    # Interpolate zonal mean precip to a 0.1 degree latitude grid for 20S-20N
    lat = precip[LAT_STR]
    trop = np.where(np.abs(lat) < lat_max)
    lat_interp = np.arange(-lat_max, lat_max + 0.01, 0.1)
    prec = np.interp(lat_interp, lat[trop], precip[trop])
    # Integrate area-weighted precip and find median.
    prec_int = np.cumsum(prec*np.abs(_cosdeg(lat_interp)))
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
    prec_int = np.cumsum(prec*np.abs(_cosdeg(lat_interp)), axis=0)
    return lat_interp[np.argmin(np.abs(prec_int - 0.5*prec_int[-1]), axis=0)]


def trop_height(level, T):
    """
    Tropopause height of each column, based on Reichler et al 2003 GRL.
    """
    # Get pressure and temperature data.
    p = level[:,np.newaxis,np.newaxis]
    # Compute half levels of pressure^kappa
    kap = R_d / c_p
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
