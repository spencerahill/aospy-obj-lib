"""aospy.Model objects corresponding to CMIP5 data."""
import os

from aospy.model import Model
from aospy_user import runs

root_dir = '/archive/pcmdi/repo/CMIP5/output/'

# BCC
bcc_csm1 = Model(
    name='bcc_csm1-1',
    description='',
    nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'BCC/BCC-CSM1-1')),
    # nc_dur=30,
    # nc_start_yr=1979,
    # nc_end_yr=2008,
    # default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)

# BNU
bnu_esm = Model(
    name='bnu_esm',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'BNU/BNU-ESM')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    # default_yr_range=(1979, 2008),
    runs=[runs.amip],
    default_runs=False
)

# CCCma
cccma_canam4 = Model(
    name='cccma_canam4',
    description='',
    nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'CCCma/CanAM4')),
    # nc_dur=30,
    # nc_start_yr=1950,
    # nc_end_yr=2009,
    # default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=[runs.amip, runs.amip4K]
)
cccma_cancm4 = Model(
    name='cccma_cancm4',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'CCCma/CanCM4')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip],
    default_runs=False
)
cccma_canesm2 = Model(
    name='cccma_canesm2',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'CCCma/CanESM2')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip],
    default_runs=False
)

# CMCC
cmcc_cesm = Model(
    name='cmcc-cesm',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'CMCC/CMCC-CESM')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip],
    default_runs=False
)
cmcc_cm = Model(
    name='cmcc-cm',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'CMCC/CMCC-CM')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip],
    default_runs=False
)
cmcc_cms = Model(
    name='cmcc-cms',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'CMCC/CMCC-CMS')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip],
    default_runs=False
)

# CNRM-CERFACS
cnrm_cm5 = Model(
    name='cnrc-cm5',
    description='',
    nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'CNRM-CERFACS/CNRM-CM5')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
cnrm_cm5_2 = Model(
    name='cnrc-cm5-2',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'CNRM-CERFACS/CNRC-CM5-2')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# COLA-CFS
cola_cfsv2 = Model(
    name='cola-cfsv2-2011',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'COLA/CFSv2-2011')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# CSIRO-BOM
csiro_bom_access1_0 = Model(
    name='csiro-bom-access1-0',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'CSIRO-BOM/CSIRO-ACCESS1-0')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
csiro_bom_access1_3 = Model(
    name='csiro-bom-access1-3',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'CSIRO-BOM/CSIRO-ACCESS1-3')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# CSIRO-QCCCE
csiro_qccce_mk3_6_0 = Model(
    name='csiro-qccce-mk3-6-0',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'CSIRO-QCCCE/CSIRO-Mk3-6-0')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# FIO
fio_esm = Model(
    name='fio-esm',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'FIO/FIO-ESM')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# ICHEC
ichec_ec_earth = Model(
    name='ichec-ec-earth',
    description='',
    nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'ICHEC/EC-EARTH')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# INM
inm_cm4 = Model(
    name='inm-cm4',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'INM/INM-CM4')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# INPE
inpe_hadgem2_es = Model(
    name='inpe-hadgem2-es',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'INPE/HadGEM2-ES')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# IPSL
ipsl_cm5a_lr = Model(
    name='ipsl-cm5a-lr',
    description='',
    nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'IPSL/IPSL-CM5A-LR')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
ipsl_cm5a_mr = Model(
    name='ipsl-cm5a-mr',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'IPSL/IPSL-CM5A-MR')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
ipsl_cm5b_lr = Model(
    name='ipsl-cm5b-lr',
    description='',
    nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'IPSL/IPSL-CM5B-LR')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# LASG-CESS
lasg_cess_fgoals_g2 = Model(
    name='lasg-cess-fgoals-g2',
    description='',
    nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'LASG-CESS/FGOALS-g2')),
    repo_version=0,
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# LASG-IAP
lasg_iap_fgoals_g1 = Model(
    name='lasg-iap-fgoals-g1',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'LASG-IAP/FGOALS-g1')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
lasg_iap_fgoals_s2 = Model(
    name='lasg-iap-fgoals-s2',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'LASG-IAP/FGOALS-s2')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# MIROC
miroc4h = Model(
    name='miroc4h',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'MIROC/MIROC4h')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
miroc5 = Model(
    name='miroc5',
    description='',
    nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'MIROC/MIROC5')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
miroc_esm = Model(
    name='miroc-esm',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'MIROC/MIROC-ESM')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
miroc_esm_chem = Model(
    name='miroc-esm-chem',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'MIROC/MIROC-ESM-CHEM')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# MOHC (Met Office Hadley Centre)
mohc_hadcm3 = Model(
    name='hadcm3',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'MOHC/HadCM3')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
mohc_hadgem2_a = Model(
    name='hadgem2-a',
    description='',
    nc_dir_struc='gfdl_repo',
    repo_version=1,
    nc_direc=os.path.realpath(os.path.join(root_dir, 'MOHC/HadGEM2-A')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
mohc_hadgem2_cc = Model(
    name='hadgem2-cc',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'MOHC/HadGEM2-CC')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
mohc_hadgem2_es = Model(
    name='hadgem2-es',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'MOHC/HadGEM2-ES')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# MPI-M
mpi_m_esm_lr = Model(
    name='mpi-esm-lr',
    description='',
    nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'MPI-M/MPI-ESM-LR')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
mpi_m_esm_mr = Model(
    name='mpi-esm-mr',
    description='',
    nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'MPI-M/MPI-ESM-MR')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
mpi_m_esm_p = Model(
    name='mpi-esm-p',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'MPI-M/MPI-ESM-P')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# MRI
mri_agcm3_2h = Model(
    name='mri-agcm3-2h',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'MRI/MRI-AGCM3-2H')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
mri_agcm3_2s = Model(
    name='mri-agcm3-2s',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'MRI/MRI-AGCM3-2S')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
mri_cgcm3 = Model(
    name='mri-cgcm3',
    description='',
    nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'MRI/MRI-CGCM3')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
mri_esm1 = Model(
    name='mri-esm1',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'MRI/MRI-ESM1')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# NASA-GISS
nasa_giss_e2_h = Model(
    name='giss-e2-h',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NASA-GISS/GISS-E2-H')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
nasa_giss_e2_h_cc = Model(
    name='giss-e2-h-cc',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NASA-GISS/GISS-E2-H-CC')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
nasa_giss_e2_r = Model(
    name='giss-e2-r',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NASA-GISS/GISS-E2-R')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
nasa_giss_e2_r_cc = Model(
    name='giss-e2-r-cc',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NASA-GISS/GISS-E2-R-CC')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# NASA-GMAO
nasa_gmao_geos_5 = Model(
    name='gmao-geos-5',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NASA-GMAO/GEOS-5')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# NCAR
ncar_ccsm4 = Model(
    name='ncar-ccsm4',
    description='',
    nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NCAR/CCSM4')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# NCC
ncc_noresm1_m = Model(
    name='ncc-noresm1-m',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NCC/NorESM1-M')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
ncc_noresm1_me = Model(
    name='ncc-noresm1-me',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NCC/NorESM1-me')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# NCEP
ncep_cfsv2_2011 = Model(
    name='ncep_cfsv2-2011',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NCEP/CFSv2-2011')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# NIMR-KMA
nimr_kma_hadgem2_ao = Model(
    name='nimr-kma-hadgem2-ao',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NIMR-KMA/HadGEM2-AO')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# NOAA-GFDL
gfdl_cm2_1 = Model(
    name='gfdl_cm2.1',
    description='NOAA GFDL CM2.1 AOGCM',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NOAA-GFDL/GFDL-CM2')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
gfdl_cm3 = Model(
    name='gfdl_cm3',
    description='NOAA GFDL CM3 AOGCM',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NOAA-GFDL/GFDL-CM3')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
gfdl_esm2m = Model(
    name='gfdl_esm2m',
    description='NOAA GFDL ESM2M earth-system model',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NOAA-GFDL/GFDL-ESM2M')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
gfdl_esm2g = Model(
    name='gfdl_esm2g',
    description='NOAA GFDL ESM2G earth-system model',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NOAA-GFDL/GFDL-ESM2G')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
gfdl_hiram_c180 = Model(
    name='gfdl_hiram-c180',
    description='NOAA GFDL HIRAM-C180 AGCM',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NOAA-GFDL/GFDL-HIRAM-C180')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
gfdl_hiram_c360 = Model(
    name='gfdl_hiram-c360',
    description='NOAA GFDL HIRAM-C360 AGCM',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NOAA-GFDL/GFDL-HIRAM-C360')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# NSF-DOE-NCAR
cesm1_bgc = Model(
    name='cesm1-bgc',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NSF-DOE-NCAR/CESM1-BGC')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
cesm1_cam5 = Model(
    name='cesm1-cam5',
    description='',
    nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NSF-DOE-NCAR/CESM1-CAM5')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
cesm1_cam5_1_fv2 = Model(
    name='cesm1-cam5-1-fv2',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NSF-DOE-NCAR/CESM1-CAM5-1-FV2')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
cesm1_fastchem = Model(
    name='cesm1-fastchem',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NSF-DOE-NCAR/CESM1-FASTCHEM')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
cesm1_waccm = Model(
    name='cesm1-waccm',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'NSF-DOE-NCAR/CESM1-WACCM')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# SMHI
smhi_ec_earth = Model(
    name='smhi_ec_earth',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'SMHI/EC-EARTH')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)

# UNSW
unsw_csiro_mk3l_1_2 = Model(
    name='unsw-csiro-mk3l-1-2',
    description='',
    # nc_dir_struc='gfdl_repo',
    nc_direc=os.path.realpath(os.path.join(root_dir, 'UNSW/CSIRO-Mk3L-1-2')),
    nc_dur=30,
    nc_start_yr=1979,
    nc_end_yr=2008,
    default_yr_range=(1979, 2008),
    runs=[runs.amip, runs.amip4K],
    default_runs=False
)
