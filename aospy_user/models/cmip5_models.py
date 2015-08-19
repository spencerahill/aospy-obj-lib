"""aospy.Model objects corresponding to CMIP5 data."""
from aospy.model import Model
from aospy_user import runs

# BCC
cmip5_bcc_csm1 = Model(
    name='bcc_csm1-1',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/BCC/BCC-CSM1-1',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)

# BNU
cmip5_bnu_esm = Model(
    name='bnu_esm',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/BNU/BNU-ESM',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)

# CCCma
cmip5_cccma_canam4 = Model(
    name='cccma_canam4',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/CCCma/CanAM4',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)
cmip5_cccma_cancm4 = Model(
    name='cccma_cancm4',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/CCCma/CanCM4',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)
cmip5_cccma_canesm2 = Model(
    name='cccma_canesm2',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/CCCma/CanESM2',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)

# CMCC
cmip5_cmcc_cesm = Model(
    name='cmcc-cesm',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/CMCC/CMCC-CESM',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)
cmip5_cmcc_cm = Model(
    name='cmcc-cm',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/CMCC/CMCC-CM',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)
cmip5_cmcc_cms = Model(
    name='cmcc-cms',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/CMCC/CMCC-CMS',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)

# CNRM-CERFACS
cmip5_cnrc_cms = Model(
    name='cnrc-cms',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/CNRC/CNRC-CMS',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)
cmip5_cnrc_cms_2 = Model(
    name='cnrc-cms-2',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/CNRC/CNRC-CMS-2',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)

# COLA-CFS
cmip5_cola_cfsv2 = Model(
    name='cola-cfsv2-2011',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/COLA/CFSv2-2011',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)

# CSIRO-BOM
cmip5_csiro_bom_access1_0 = Model(
    name='csiro-bom-access1-0',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/CSIRO-BOM/CSIRO-ACCESS1-0',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)
cmip5_csiro_bom_access1_3 = Model(
    name='csiro-bom-access1-3',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/CSIRO-BOM/CSIRO-ACCESS1-3',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)

# CSIRO-QCCCE
cmip5_csiro_qccce_mk3_6_0 = Model(
    name='csiro-qccce-mk3-6-0',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/CSIRO-QCCCE/CSIRO-Mk3-6-0',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)

# FIO
cmip5_fio_esm = Model(
    name='fio-esm',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/FIO/FIO-ESM',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)

# ICHEC
cmip5_ichec_ec_earth = Model(
    name='ichec-ec-earth',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/ICHEC/EC-EARTH',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)

# INM
cmip5_inm_cm4 = Model(
    name='inm-cm4',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/INM/INM-CM4',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)

# INPE
cmip5_ichec_ec_earth = Model(
    name='inpe-hadgem2-es',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/INPE/HadGEM2-ES',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)

# IPSL
cmip5_ipsl_cm5a_lr = Model(
    name='ipsl-cm5a-lr',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/IPSL/CM5A-LR',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)
cmip5_ipsl_cm5a_mr = Model(
    name='ipsl-cm5a-mr',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/IPSL/CM5A-MR',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)
cmip5_ipsl_cm5b_lr = Model(
    name='ipsl-cm5b-lr',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/IPSL/CM5B-LR',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)

# LASG-CESS
cmip5_lasg_cess = Model(
    name='lasg-cess-fgoals-g2',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/LASG-CESS/FGOALS-g2',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)

# LASG-IAP
cmip5_lasg_iap = Model(
    name='lasg-iap-fgoals-g2',
    description='',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/LASG-IAP/FGOALS-g2',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)


# NOAA-GFDL
cmip5_gfdl_cm21 = Model(
    name='gfdl_cm2.1',
    description='NOAA GFDL CM2.1 AOGCM',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/NOAA-GFDL/GFDL-CM2',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)
cmip5_gfdl_cm3 = Model(
    name='gfdl_cm3',
    description='NOAA GFDL CM3 AOGCM',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/NOAA-GFDL/GFDL-CM3',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)
cmip5_gfdl_esm2m = Model(
    name='gfdl_esm2m',
    description='NOAA GFDL ESM2M earth-system model',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/NOAA-GFDL/GFDL-ESM2M',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)
cmip5_gfdl_esm2g = Model(
    name='gfdl_esm2g',
    description='NOAA GFDL ESM2G earth-system model',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/NOAA-GFDL/GFDL-ESM2G',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)
cmip5_gfdl_hiram_c180 = Model(
    name='gfdl_hiram-c180',
    description='NOAA GFDL HIRAM-C180 AGCM',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/NOAA-GFDL/GFDL-HIRAM-C180',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)
cmip5_gfdl_hiram_c360 = Model(
    name='gfdl_hiram-c360',
    description='NOAA GFDL HIRAM-C360 AGCM',
    nc_grid_paths='/archive/pcmdi/repo/CMIP5/output/NOAA-GFDL/GFDL-HIRAM-C360',
    nc_dur=113,
    nc_start_yr=1901,
    nc_end_yr=2013,
    default_yr_range=(1901, 2013),
    runs=[runs.cru_v322],
    default_runs=[runs.cru_v322]
)
