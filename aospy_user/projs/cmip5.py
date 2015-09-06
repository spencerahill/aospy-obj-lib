"""Spencer Hill's aospy.Proj object for CMIP5 data."""
from aospy.proj import Proj
from aospy_user import regions, models, variables


cmip5 = Proj(
    'cmip5',
    vars=variables.master_vars_list,
    direc_out='/archive/s1h/cmip5/',
    nc_dir_struc='one_dir',
    models=(
        models.bcc_csm1, models.bnu_esm, models.cccma_canam4,
        models.cccma_cancm4, models.cccma_canesm2, models.cmcc_cesm,
        models.cmcc_cm, models.cmcc_cms, models.cnrm_cm5, models.cnrm_cm5_2,
        models.cola_cfsv2, models.csiro_bom_access1_0,
        models.csiro_bom_access1_3, models.csiro_qccce_mk3_6_0, models.fio_esm,
        models.ichec_ec_earth, models.inm_cm4, models.inpe_hadgem2_es,
        models.ipsl_cm5a_lr, models.ipsl_cm5a_mr, models.ipsl_cm5b_lr,
        models.lasg_cess_fgoals_g2, models.lasg_iap_fgoals_g1,
        models.lasg_iap_fgoals_s2, models.miroc4h, models.miroc5,
        models.miroc_esm, models.miroc_esm_chem, models.mohc_hadcm3,
        models.mohc_hadgem2_a, models.mohc_hadgem2_cc,
        models.mohc_hadgem2_es, models.mpi_m_esm_lr, models.mpi_m_esm_mr,
        models.mpi_m_esm_p, models.mri_agcm3_2h, models.mri_agcm3_2s,
        models.mri_cgcm3, models.mri_esm1, models.nasa_giss_e2_h,
        models.nasa_giss_e2_h_cc, models.nasa_giss_e2_r,
        models.nasa_giss_e2_r_cc, models.nasa_gmao_geos_5, models.ncar_ccsm4,
        models.ncc_noresm1_m, models.ncc_noresm1_me, models.ncep_cfsv2_2011,
        models.nimr_kma_hadgem2_ao, models.gfdl_cm2_1, models.gfdl_cm3,
        models.gfdl_esm2m, models.gfdl_esm2g, models.gfdl_hiram_c180,
        models.gfdl_hiram_c360, models.cesm1_bgc, models.cesm1_cam5,
        models.cesm1_fastchem, models.cesm1_waccm, models.smhi_ec_earth,
        models.unsw_csiro_mk3l_1_2
    ),
    default_models=(
        models.bcc_csm1,
        models.cccma_canam4,
        models.cnrm_cm5,
        models.ichec_ec_earth,
        models.ipsl_cm5a_lr,
        models.ipsl_cm5b_lr,
        models.lasg_cess_fgoals_g2,
        models.miroc5,
        models.mohc_hadgem2_a,
        models.mpi_m_esm_lr,
        models.mpi_m_esm_mr,
        models.mri_cgcm3,
        models.ncar_ccsm4,
        models.cesm1_cam5
    ),
    regions=(
        regions.globe,
        regions.nh,
        regions.sh,
        regions.tropics,
        regions.wpwp,
        regions.epac,
        regions.sahel,
        regions.sahel2,
        regions.sahel3,
        regions.sahara,
        regions.ind_monsoon,
        regions.land,
        regions.ocean,
        regions.trop_land,
        regions.trop_ocean,
        regions.sahel_south,
        regions.sahel_north,
        regions.sahel_east,
        regions.sahel_west
    )
)
