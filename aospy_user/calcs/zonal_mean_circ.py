"""Zonal-mean meridional circulation and mass transport quantities."""
from aospy import LAT_STR
from aospy.constants import c_p, grav, L_f, L_v, Omega, r_e, R_d
from aospy.utils import level_thickness, to_pascal
import numpy as np

from .thermo import dse, mse
from .toa_sfc_fluxes import column_energy


def msf(lats, levs, v):
    """Meridional mass streamfunction."""
    # Compute half level boundaries and widths.
    p_top = 5.
    p_bot = 1005.
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
    msf_[:,-1]*=0.5
    msf_[:,0] = 0.
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
    global_mean = np.ma.average(local_flat, weights=sfc_area.ravel(), axis=1)
    zonal_integral = np.sum(
        sfc_area * (local_flat - global_mean[:,np.newaxis,np.newaxis]),
        axis=-1
    )
    return np.ma.cumsum(zonal_integral, axis=-1)


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
    return (2.*np.pi*r_e*np.cos(np.deg2rad(nc.variables[LAT_STR][:])) *
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
    return (2.*np.pi*r_e*np.cos(np.deg2rad(nc.variables[LAT_STR][:])) *
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
    return (2.*np.pi*r_e*np.cos(np.deg2rad(nc.variables[LAT_STR][:])) *
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
    return (2.*np.pi*r_e*np.cos(np.deg2rad(nc.variables[LAT_STR][:])) *
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
