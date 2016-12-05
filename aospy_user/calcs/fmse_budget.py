"""Functions relating to the budget of frozen moist static energy."""
from aospy.utils.vertcoord import int_dp_g
from indiff.advec import SphereEtaUpwind
from indiff.deriv import SphereEtaCenDeriv

from .transport import field_total_advec
from .toa_sfc_fluxes import column_energy
from .thermo import fmse
from .gms import frozen_moist_static_stab


def fmse_merid_deriv_eta(temp, z, q, q_ice, ps, bk, pk):
    """Meridional derivative of frozen MSE on model native-coordinates."""
    deriv_obj = SphereEtaCenDeriv(fmse(temp, z, q, q_ice), pk, bk, ps)
    return deriv_obj.d_dy_const_p()


def fmse_zonal_deriv_eta(temp, z, q, q_ice, ps, bk, pk):
    """Zonal derivative of frozen MSE on model native-coordinates."""
    deriv_obj = SphereEtaCenDeriv(fmse(temp, z, q, q_ice), pk, bk, ps)
    return deriv_obj.d_dx_const_p()


def fmse_horiz_advec_eta_upwind(temp, z, q, q_ice, u, v, ps, bk, pk,
                                order=2):
    """Horizontal advection of frozen MSE using upwind scheme."""
    return SphereEtaUpwind(fmse(temp, z, q, q_ice), pk, bk, ps,
                           order=order).advec_horiz_const_p(u, v)


def fmse_budget_advec_residual(temp, hght, sphum, ice_wat, ucomp, vcomp, omega,
                               p, dp, radius, swdn_toa, swup_toa, olr,
                               swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx,
                               evap):
    """Residual in vertically integrated frozen MSE budget."""
    fmse_ = fmse(temp, hght, sphum, ice_wat)
    transport = field_total_advec(fmse_, ucomp, vcomp, omega, p, radius)
    trans_vert_int = int_dp_g(transport, dp)
    f_net = column_energy(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
                          lwup_sfc, lwdn_sfc, shflx, evap)
    return f_net - trans_vert_int


def omega_change_from_fmse_budget(temp_cont, z_cont, q_cont, q_ice_cont,
                                  u_cont, v_cont, ps_cont, temp_pert, z_pert,
                                  q_pert, q_ice_pert, u_pert, v_pert, ps_pert,
                                  bk, pk, horiz_thermo=False, min_dhdp=0.05):
    """Approximation for omega change based on MSE budget.

    Specifically, based on leading order balance in perturbation MSE budget
    between anomalous horizontal MSE avection and the dynamic component of the
    anomalous vertical MSE avection.

    If `horiz_thermo` is `True`, further assume that the anomalous horizontal
    MSE advection is dominated by the thermodynamic component.
    """
    if horiz_thermo:
        advec_anom = fmse_horiz_advec_eta_upwind(
            temp_pert - temp_cont, z_pert - z_cont, q_pert - q_cont,
            q_ice_pert - q_ice_cont, u_cont, v_cont, ps_cont, bk, pk
        )
    else:
        advec_cont = fmse_horiz_advec_eta_upwind(
            temp_cont, z_cont, q_cont, q_ice_cont, u_cont, v_cont, ps_cont,
            bk, pk
        )
        advec_pert = fmse_horiz_advec_eta_upwind(
            temp_pert, z_pert, q_pert, q_ice_pert, u_pert, v_pert, ps_pert,
            bk, pk
        )
        advec_anom = advec_pert - advec_cont
    dh_dp = frozen_moist_static_stab(temp_cont, z_cont, q_cont, q_ice_cont,
                                     ps_cont, bk, pk)
    # Mask where denominator nearly zero.
    return -1*advec_anom / dh_dp.where(abs(dh_dp) > min_dhdp)
