"""aospy.Model objects corresponding to CMIP5 data."""
import datetime
import os

from aospy.model import Model

from .. import runs

root_dir = '/archive/pcmdi/repo/CMIP5/output/'

# BCC
bcc_csm1 = Model(
    name='bcc_csm1-1',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'BCC/BCC-CSM1-1')),
    grid_file_paths=[
        '/archive/pcmdi/repo/CMIP5/output/BCC/BCC-CSM1-1/historical/fx/atmos/'
        'fx/r0i0p0/v1/orog/orog_fx_bcc-csm1-1_historical_r0i0p0.nc',
        '/archive/pcmdi/repo/CMIP5/output/BCC/BCC-CSM1-1/historical/fx/atmos/'
        'fx/r0i0p0/v1/sftlf/sftlf_fx_bcc-csm1-1_historical_r0i0p0.nc',
        '/archive/pcmdi/repo/CMIP5/output/BCC/BCC-CSM1-1/historical/fx/atmos/'
        'fx/r0i0p0/v1/areacella/areacella_fx_bcc-csm1-1_historical_r0i0p0.nc',
    ],
    # data_dur=30,
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# BNU
bnu_esm = Model(
    name='bnu_esm',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'BNU/BNU-ESM')),
    runs=[runs.amip],
    default_runs=False
)

# CCCma
cccma_canam4 = Model(
    name='cccma_canam4',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'CCCma/CanAM4')),
    repo_version=0,
    # data_dur=30,
    # data_start_date=datetime.datetime(1950, 1, 1),
    # data_end_date=datetime.datetime(2009, 12, 31),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
cccma_cancm4 = Model(
    name='cccma_cancm4',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'CCCma/CanCM4')),
    runs=[runs.amip],
    default_runs=False
)
cccma_canesm2 = Model(
    name='cccma_canesm2',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'CCCma/CanESM2')),
    runs=[runs.amip],
    default_runs=False
)

# CMCC
cmcc_cesm = Model(
    name='cmcc-cesm',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'CMCC/CMCC-CESM')),
    runs=[runs.amip],
    default_runs=False
)
cmcc_cm = Model(
    name='cmcc-cm',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'CMCC/CMCC-CM')),
    runs=[runs.amip],
    default_runs=False
)
cmcc_cms = Model(
    name='cmcc-cms',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'CMCC/CMCC-CMS')),
    runs=[runs.amip],
    default_runs=False
)

# CNRM-CERFACS
cnrm_cm5 = Model(
    name='cnrc-cm5',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'CNRM-CERFACS/CNRM-CM5')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
cnrm_cm5_2 = Model(
    name='cnrc-cm5-2',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'CNRM-CERFACS/CNRC-CM5-2')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# COLA-CFS
cola_cfsv2 = Model(
    name='cola-cfsv2-2011',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'COLA/CFSv2-2011')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# CSIRO-BOM
csiro_bom_access1_0 = Model(
    name='csiro-bom-access1-0',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'CSIRO-BOM/CSIRO-ACCESS1-0')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
csiro_bom_access1_3 = Model(
    name='csiro-bom-access1-3',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'CSIRO-BOM/CSIRO-ACCESS1-3')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# CSIRO-QCCCE
csiro_qccce_mk3_6_0 = Model(
    name='csiro-qccce-mk3-6-0',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'CSIRO-QCCCE/CSIRO-Mk3-6-0')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# FIO
fio_esm = Model(
    name='fio-esm',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'FIO/FIO-ESM')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# ICHEC
ichec_ec_earth = Model(
    name='ichec_ec_earth',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'ICHEC/EC-EARTH')),
    repo_ens_mem='r3i1p1',
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# INM
inm_cm4 = Model(
    name='inm-cm4',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'INM/INM-CM4')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# INPE
inpe_hadgem2_es = Model(
    name='inpe-hadgem2-es',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'INPE/HadGEM2-ES')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# IPSL
ipsl_cm5a_lr = Model(
    name='ipsl-cm5a-lr',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'IPSL/IPSL-CM5A-LR')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
ipsl_cm5a_mr = Model(
    name='ipsl-cm5a-mr',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'IPSL/IPSL-CM5A-MR')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
ipsl_cm5b_lr = Model(
    name='ipsl-cm5b-lr',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'IPSL/IPSL-CM5B-LR')),
    grid_file_paths=[
        '/archive/pcmdi/repo/CMIP5/output/IPSL/IPSL-CM5B-LR/piControl/fx/'
        'atmos/fx/r0i0p0/v20120430/orog/'
        'orog_fx_IPSL-CM5B-LR_piControl_r0i0p0.nc',
        '/archive/pcmdi/repo/CMIP5/output/IPSL/IPSL-CM5B-LR/piControl/fx/'
        'atmos/fx/r0i0p0/v20120430/areacella/'
        'areacella_fx_IPSL-CM5B-LR_piControl_r0i0p0.nc',
        '/archive/pcmdi/repo/CMIP5/output/IPSL/IPSL-CM5B-LR/piControl/fx/'
        'atmos/fx/r0i0p0/v20120430/sftlf/'
        'sftlf_fx_IPSL-CM5B-LR_piControl_r0i0p0.nc',
    ],
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# LASG-CESS
lasg_cess_fgoals_g2 = Model(
    name='lasg-cess-fgoals-g2',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'LASG-CESS/FGOALS-g2')),
    repo_version=0,
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# LASG-IAP
lasg_iap_fgoals_g1 = Model(
    name='lasg-iap-fgoals-g1',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'LASG-IAP/FGOALS-g1')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
lasg_iap_fgoals_s2 = Model(
    name='lasg-iap-fgoals-s2',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'LASG-IAP/FGOALS-s2')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# MIROC
miroc4h = Model(
    name='miroc4h',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'MIROC/MIROC4h')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
miroc5 = Model(
    name='miroc5',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'MIROC/MIROC5')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
miroc_esm = Model(
    name='miroc-esm',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'MIROC/MIROC-ESM')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
miroc_esm_chem = Model(
    name='miroc-esm-chem',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'MIROC/MIROC-ESM-CHEM')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# MOHC (Met Office Hadley Centre)
mohc_hadcm3 = Model(
    name='mohc_hadcm3',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'MOHC/HadCM3')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
mohc_hadgem2_a = Model(
    name='mohc_hadgem2a',
    description='',
    # data_dir_struc='gfdl_repo',
    repo_version=1,
    # data_direc=os.path.realpath(os.path.join(root_dir, 'MOHC/HadGEM2-A')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
mohc_hadgem2_cc = Model(
    name='mohc_hadgem2cc',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'MOHC/HadGEM2-CC')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
mohc_hadgem2_es = Model(
    name='hadgem2-es',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'MOHC/HadGEM2-ES')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# MPI-M
mpi_m_esm_lr = Model(
    name='mpi-esm-lr',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'MPI-M/MPI-ESM-LR')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
mpi_m_esm_mr = Model(
    name='mpi-esm-mr',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'MPI-M/MPI-ESM-MR')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
mpi_m_esm_p = Model(
    name='mpi-esm-p',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'MPI-M/MPI-ESM-P')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# MRI
mri_agcm3_2h = Model(
    name='mri-agcm3-2h',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'MRI/MRI-AGCM3-2H')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
mri_agcm3_2s = Model(
    name='mri-agcm3-2s',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'MRI/MRI-AGCM3-2S')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
mri_cgcm3 = Model(
    name='mri-cgcm3',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'MRI/MRI-CGCM3')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
mri_esm1 = Model(
    name='mri-esm1',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'MRI/MRI-ESM1')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# NASA-GISS
nasa_giss_e2_h = Model(
    name='giss-e2-h',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NASA-GISS/GISS-E2-H')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
nasa_giss_e2_h_cc = Model(
    name='giss-e2-h-cc',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NASA-GISS/GISS-E2-H-CC')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
nasa_giss_e2_r = Model(
    name='giss-e2-r',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NASA-GISS/GISS-E2-R')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
nasa_giss_e2_r_cc = Model(
    name='giss-e2-r-cc',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NASA-GISS/GISS-E2-R-CC')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# NASA-GMAO
nasa_gmao_geos_5 = Model(
    name='gmao-geos-5',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NASA-GMAO/GEOS-5')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# NCAR
ncar_ccsm4 = Model(
    name='ncar-ccsm4',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NCAR/CCSM4')),
    grid_file_paths=[
        '/archive/pcmdi/repo/CMIP5/output/NCAR/CCSM4/piControl/fx/atmos/fx/'
        'r0i0p0/v20120413/orog/orog_fx_CCSM4_piControl_r0i0p0.nc',
        '/archive/pcmdi/repo/CMIP5/output/NCAR/CCSM4/piControl/fx/atmos/fx/'
        'r0i0p0/v20120413/sftlf/sftlf_fx_CCSM4_piControl_r0i0p0.nc',
        '/archive/pcmdi/repo/CMIP5/output/NCAR/CCSM4/piControl/fx/atmos/fx/'
        'r0i0p0/v20120213/areacella/areacella_fx_CCSM4_piControl_r0i0p0.nc',
        ],
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# NCC
ncc_noresm1_m = Model(
    name='ncc-noresm1-m',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NCC/NorESM1-M')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
ncc_noresm1_me = Model(
    name='ncc-noresm1-me',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NCC/NorESM1-me')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# NCEP
ncep_cfsv2_2011 = Model(
    name='ncep_cfsv2-2011',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NCEP/CFSv2-2011')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# NIMR-KMA
nimr_kma_hadgem2_ao = Model(
    name='nimr-kma-hadgem2-ao',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NIMR-KMA/HadGEM2-AO')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# NOAA-GFDL
gfdl_cm2_1 = Model(
    name='gfdl_cm2.1',
    description='NOAA GFDL CM2.1 AOGCM',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NOAA-GFDL/GFDL-CM2')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
gfdl_cm3 = Model(
    name='gfdl_cm3',
    description='NOAA GFDL CM3 AOGCM',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NOAA-GFDL/GFDL-CM3')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
gfdl_esm2m = Model(
    name='gfdl_esm2m',
    description='NOAA GFDL ESM2M earth-system model',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NOAA-GFDL/GFDL-ESM2M')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
gfdl_esm2g = Model(
    name='gfdl_esm2g',
    description='NOAA GFDL ESM2G earth-system model',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NOAA-GFDL/GFDL-ESM2G')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
gfdl_hiram_c180 = Model(
    name='gfdl_hiram-c180',
    description='NOAA GFDL HIRAM-C180 AGCM',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NOAA-GFDL/GFDL-HIRAM-C180')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
gfdl_hiram_c360 = Model(
    name='gfdl_hiram-c360',
    description='NOAA GFDL HIRAM-C360 AGCM',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NOAA-GFDL/GFDL-HIRAM-C360')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# NSF-DOE-NCAR
cesm1_bgc = Model(
    name='cesm1-bgc',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NSF-DOE-NCAR/CESM1-BGC')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
cesm1_cam5 = Model(
    name='ncar_cesm1_cam5',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NSF-DOE-NCAR/CESM1-CAM5')),
    grid_file_paths=['/archive/s1h/cmip5/cam5_land_mask/cam5_land_mask.nc'],
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
cesm1_cam5_1_fv2 = Model(
    name='cesm1-cam5-1-fv2',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NSF-DOE-NCAR/CESM1-CAM5-1-FV2')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
cesm1_fastchem = Model(
    name='cesm1-fastchem',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NSF-DOE-NCAR/CESM1-FASTCHEM')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
cesm1_waccm = Model(
    name='cesm1-waccm',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'NSF-DOE-NCAR/CESM1-WACCM')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# SMHI
smhi_ec_earth = Model(
    name='smhi_ec_earth',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'SMHI/EC-EARTH')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# UNSW
unsw_csiro_mk3l_1_2 = Model(
    name='unsw-csiro-mk3l-1-2',
    description='',
    # data_dir_struc='gfdl_repo',
    # data_direc=os.path.realpath(os.path.join(root_dir, 'UNSW/CSIRO-Mk3L-1-2')),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
