"""Collection of aospy.Var objects for use in my research."""
from aospy.constants import r_e
from aospy.var import Var

from . import calcs, units


# Define pressure, pressure thickness, and their dependencies first.
p = Var(
    name='p',
    units=units.Pa,
    domain='atmos',
    description='Pressure of model half levels.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
ps = Var(
    name='ps',
    units=units.Pa,
    domain='atmos',
    description='Surface pressure.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
bk = Var(
    name='bk',
    units=units.Pa,
    domain='atmos_level',
    description='Sigma part of hybrid sigma coordinate.',
    def_time=False,
    def_vert=True,
    def_lat=False,
    def_lon=False,
    in_nc_grid=True
)
pk = Var(
    name='pk',
    units=units.Pa,
    domain='atmos_level',
    description='Pressure part of hybrid sigma coordinate.',
    def_time=False,
    def_vert=True,
    def_lat=False,
    def_lon=False,
    in_nc_grid=True
)
temp = Var(
    name='temp',
    alt_names=('ta',),
    units=units.K,
    domain='atmos',
    description='Air temperature.',
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    in_nc_grid=False,
    colormap='RdBu_r'
)
dp = Var(
    name='dp',
    domain='atmos',
    description=('Pressure thickness of model levels.  For data interpolated '
                 'to uniform pressure levels, this does not vary in time or '
                 'space.  For data on model native coordinates, this varies '
                 'in space and time due to the spatiotemporal variations in '
                 'surface pressure.'),
    # Last arg is just dummy variable from which to get the pfull coordinate.
    variables=(ps, bk, pk, temp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False,
    func=calcs.dp,
    units=units.Pa,
)

# All other variables.
alb_sfc = Var(
    name='alb_sfc',
    units=units.unitless,
    domain='atmos',
    description='Surface albedo.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
cld_amt = Var(
    name='cld_amt',
    alt_names=('cl',),
    units=units.unitless,
    domain='atmos',
    description='Cloud fraction at each level.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
divg = Var(
    name='divg',
    math_str=r"\nabla\cdot\vec{v}",
    units=units.s1,
    domain='atmos',
    description='Divergence.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False,
    colormap='RdBu'
)
esf = Var(
    name='esf',
    units=units.kg_s1,
    domain='atmos',
    description='Eddy streamfunction',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
evap = Var(
    name='evap',
    alt_names=('ET_mean', 'evspsbl'),
    math_str=r"$E$",
    units=units.kg_m2_s1,
    domain='atmos',
    description='Surface evaporation',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
high_cld_amt = Var(
    name='high_cld_amt',
    units=units.unitless,
    domain='atmos',
    description='High cloud fraction.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
lai = Var(
    name='lai',
    alt_names=('LAI',),
    units=units.unitless,
    domain='land',
    description='Leaf area index.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
low_cld_amt = Var(
    name='low_cld_amt',
    units=units.unitless,
    domain='atmos',
    description='Low cloud fraction.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
lwdn_sfc = Var(
    name='lwdn_sfc',
    alt_names=('rlds',),
    math_str="$R^{LW\downarrow_{sfc}$",
    description='All-sky downwelling longwave radiation at the surface.',
    domain='atmos',
    units=units.W_m2,
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
lwdn_sfc_clr = Var(
    name='lwdn_sfc_clr',
    alt_names=('rldscs',),
    units=units.W_m2,
    domain='atmos',
    description='Clear-sky downwelling longwave radiation at the surface.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
lwup_sfc = Var(
    name='lwup_sfc',
    alt_names=('rlus',),
    units=units.W_m2,
    domain='atmos',
    description='All-sky upwelling longwave radiation at the surface.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
lwup_sfc_clr = Var(
    name='lwup_sfc_clr',
    alt_names=('rluscs',),
    units=units.W_m2,
    domain='atmos',
    description='Clear-sky upwelling longwave radiation at the surface.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
hght = Var(
    name='hght',
    alt_names=('zg',),
    units=units.m,
    domain='atmos',
    description='Geopotential height.',
    def_time=True,
    def_vert='phalf',
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
ice_mask = Var(
    name='ice_mask',
    units=units.unitless,
    domain='atmos',
    description='Ice mask.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
ice_wat = Var(
    name='ice_wat',
    units=units.specific_mass,
    domain='atmos',
    description='Cloud ice water specific humidity.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
liq_wat = Var(
    name='liq_wat',
    units=units.specific_mass,
    domain='atmos',
    description='Cloud liquid water specific humidity.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
mc = Var(
    name='mc',
    units=units.kg_m2_s1_mass,
    domain='atmos',
    description='Convective mass flux.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
mc_full = Var(
    name='mc_full',
    units=units.kg_m2_s1_mass,
    domain='atmos',
    description='Convective mass flux at full levels.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
mc_half = Var(
    name='mc_half',
    units=units.kg_m2_s1_mass,
    domain='atmos',
    description='Convective mass flux at half levels.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
mid_cld_amt = Var(
    name='mid_cld_amt',
    units=units.unitless,
    domain='atmos',
    description='Mid-level cloud fraction.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
olr = Var(
    name='olr',
    alt_names=('rlut',),
    units=units.W_m2,
    domain='atmos',
    description='All-sky outgoing longwave radiation at TOA.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
olr_clr = Var(
    name='olr_clr',
    alt_names=('rlutcs',),
    units=units.W_m2,
    domain='atmos',
    description='Clear-sky outgoing longwave radiation at TOA.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
omega = Var(
    name='omega',
    alt_names=('wap',),
    units=units.Pa_s1,
    domain='atmos',
    description='Pressure vertical velocity.',
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
precip = Var(
    name='precip',
    alt_names=('pr', 'pre'),
    units=units.kg_m2_s1,
    domain='atmos',
    description='Liquid precipitation reaching surface.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False,
    colormap='BrBG'
)
prec_conv = Var(
    name='prec_conv',
    alt_names=('prc',),
    units=units.kg_m2_s1,
    domain='atmos',
    description='Liquid precip reaching surface from convection scheme.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False,
    colormap='BrBG'
)
prec_ls = Var(
    name='prec_ls',
    units=units.kg_m2_s1,
    domain='atmos',
    description='Liquid precip reaching surface from large scale ascent.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False,
    colormap='BrBG'
)
pv = Var(
    name='pv',
    units=units.s1,
    domain='atmos',
    description='Potential vorticity',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
rh = Var(
    name='rh',
    alt_names=('hur',),
    units=units.unitless,
    domain='atmos',
    description='Relative humidity',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
rh_ref = Var(
    name='rh_ref',
    units=units.unitless,
    domain='atmos',
    description='Relative humidity at 2m above surface',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
shflx = Var(
    name='shflx',
    alt_names=('hfss',),
    units=units.W_m2,
    domain='atmos',
    description='Surface sensible heat flux into the atmosphere.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
slp = Var(
    name='slp',
    alt_names=('psl',),
    units=units.hPa,
    domain='atmos',
    description='Sea level pressure.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
snow_conv = Var(
    name='snow_conv',
    units=units.kg_m2_s1,
    domain='atmos',
    description='Snow reaching surface from convection scheme.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
snow_ls = Var(
    name='snow_ls',
    units=units.kg_m2_s1,
    domain='atmos',
    description='Snow reaching surface from large scale ascent.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
soil_liq = Var(
    name='soil_liq',
    units=units.kg_m2,
    domain='land',
    description='Soil liquid in each level of land model',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
soil_moisture = Var(
    name='soil_moisture',
    alt_names=('water', 'water_soil',),
    units=units.kg_m2,
    domain='land',
    description='Mass of water in land bucket',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
sphum = Var(
    name='sphum',
    alt_names=('hus',),
    units=units.specific_mass,
    domain='atmos',
    description='Specific humidity.',
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    in_nc_grid=False,
    colormap='Greys'
)
sst = Var(
    name='sst',
    alt_names=('ts', 'SST'),
    units=units.K,
    domain='ocean',
    description='Sea surface temperature.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
swdn_sfc = Var(
    name='swdn_sfc',
    alt_names=('rsds',),
    units=units.W_m2,
    domain='atmos',
    description='All-sky downwelling shortwave radiation at the surface.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
swdn_sfc_clr = Var(
    name='swdn_sfc_clr',
    alt_names=('rsdscs',),
    units=units.W_m2,
    domain='atmos',
    description='Clear-sky downwelling shortwave radiation at the surface.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
swup_sfc = Var(
    name='swup_sfc',
    alt_names=('rsus',),
    units=units.W_m2,
    domain='atmos',
    description='All-sky upwelling shortwave radiation at the surface.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
swup_sfc_clr = Var(
    name='swup_sfc_clr',
    alt_names=('rsuscs',),
    units=units.W_m2,
    domain='atmos',
    description='Clear-sky upwelling shortwave radiation at the surface.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
swdn_toa = Var(
    name='swdn_toa',
    alt_names=('rsdt',),
    units=units.W_m2,
    domain='atmos',
    description='Downwelling shortwave radiation at TOA.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
swdn_toa_clr = Var(
    name='swdn_toa_clr',
    alt_names=('rsdtcs',),
    units=units.W_m2,
    domain='atmos',
    description='Downwelling shortwave radiation at TOA.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
swup_toa = Var(
    name='swup_toa',
    alt_names=('rsut',),
    units=units.W_m2,
    domain='atmos',
    description='All-sky Upwelling shortwave radiation at TOA.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
swup_toa_clr = Var(
    name='swup_toa_clr',
    alt_names=('rsutcs',),
    units=units.W_m2,
    domain='atmos',
    description='Clear-sky upwelling shortwave radiation at TOA.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
t_surf = Var(
    name='t_surf',
    alt_names=('tas', 'tmp'),
    units=units.K,
    domain='atmos',
    description='Surface air temperature.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
tdt_conv = Var(
    name='tdt_conv',
    units=units.K_s1,
    domain='atmos',
    description='Convective heating rate.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False,
    valid_range=(-20, 20)
)
tdt_ls = Var(
    name='tdt_ls',
    units=units.K_s1,
    domain='atmos',
    description='Large-scale heating rate.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
tdt_lw = Var(
    name='tdt_lw',
    units=units.K_s1,
    domain='atmos',
    description='All-sky longwave heating rate.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
tdt_lw_clr = Var(
    name='tdt_lw_clr',
    units=units.K_s1,
    domain='atmos',
    description='Clear-sky longwave heating rate.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
tdt_sw = Var(
    name='tdt_sw',
    units=units.K_s1,
    domain='atmos',
    description='All-sky shortwave heating rate.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
tdt_sw_clr = Var(
    name='tdt_sw_clr',
    units=units.K_s1,
    domain='atmos',
    description='Clear-sky shortwave heating rate.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
tdt_vdif = Var(
    name='tdt_vdif',
    units=units.K_s1,
    domain='atmos',
    description='Temperature tendency from vertical diffusion.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
tot_cld_amt = Var(
    name='tot_cld_amt',
    alt_names=('clt',),
    units=units.unitless,
    domain='atmos',
    description='Total cloud fraction.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
ucomp = Var(
    name='ucomp',
    alt_names=('ua',),
    units=units.m_s1,
    domain='atmos',
    description='Eastward velocity.',
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
u_ref = Var(
    name='u_ref',
    units=units.m_s1,
    domain='atmos',
    description='Eastward velocity at 2 meters above ground.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
vcomp = Var(
    name='vcomp',
    alt_names=('va',),
    units=units.m_s1,
    domain='atmos',
    description='Northward velocity.',
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
v_ref = Var(
    name='v_ref',
    units=units.m_s1,
    domain='atmos',
    description='Northward velocity at 2 meters above ground.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
vort = Var(
    name='vort',
    units=units.s1_vort,
    domain='atmos',
    description='Vorticity',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
wvp = Var(
    name='wvp',
    alt_names=('WVP', 'prw'),
    units=units.kg_m2,
    domain='atmos',
    description='Water vapor path',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False,
    colormap='Greys'
)
# Grid variables.
land_mask = Var(
    name='land_mask',
    units=units.unitless,
    description='Land mask',
    def_time=False,
    def_vert=True,
    def_lat=True,
    def_lon=False,
    in_nc_grid=True
)
lat = Var(
    name='lat',
    units=units.latlon,
    description='Latitude',
    def_time=False,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    in_nc_grid=True
)
lon = Var(
    name='lon',
    units=units.latlon,
    description='Longitude.',
    def_time=False,
    def_vert=False,
    def_lat=False,
    def_lon=True,
    in_nc_grid=True
)
level = Var(
    name='level',
    units=units.hPa,
    domain='atmos',
    description='Pressure level for data interpolated to uniform pressures.',
    def_time=False,
    def_vert=True,
    def_lat=False,
    def_lon=False,
    in_nc_grid=True
)
pfull = Var(
    name='pfull',
    units=units.hPa,
    domain='atmos_level',
    description=('Reference pressure of model native coordinate full levels. '
                 'Importantly, NOT the actual value at a particular lat, lon, '
                 'or time, which depends on the spatiotemporally varying '
                 'surface pressure.'),
    def_time=False,
    def_vert=True,
    def_lat=False,
    def_lon=False,
    in_nc_grid=False
)
phalf = Var(
    name='phalf',
    units=units.hPa,
    domain='atmos_level',
    description=('Reference pressure of model native coordinate half levels. '
                 'Importantly, NOT the actual value at a particular lat, lon, '
                 'or time, which depends on the spatiotemporally varying '
                 'surface pressure.'),
    def_time=False,
    def_vert=True,
    def_lat=False,
    def_lon=False,
    in_nc_grid=True
)
sfc_area = Var(
    name='sfc_area',
    units=units.m2,
    domain=None,
    description='Grid surface area.',
    def_time=False,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
zsurf = Var(
    name='zsurf',
    units=units.m,
    domain=None,
    description='Surface elevation.',
    def_time=False,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=True
)

# Calculations involving one or more model-native variables.
aht = Var(
    name='aht',
    domain='atmos',
    description='Total northward atmospheric heat transport.',
    variables=(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc, lwup_sfc,
          lwdn_sfc, shflx, evap, snow_ls, snow_conv, sfc_area),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.aht,
    units=units.W
)
albedo = Var(
    name='albedo',
    domain='atmos',
    description=('Column albedo: fraction of incoming SW at TOA reflected '
                 'back to space.'),
    variables=(swdn_toa, swup_toa),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.albedo,
    units=units.unitless
)
ang_mom = Var(
    name='ang_mom',
    domain='atmos',
    description='Angular momentum per unit mass.',
    variables=(ucomp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.ang_mom,
    units=units.unitless
)
bowen_ratio = Var(
    name='bowen_ratio',
    domain='atmos',
    description='Bowen Ratio: ratio of surface sensible to latent heat flux',
    variables=(shflx, evap),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.bowen_ratio,
    units=units.unitless
)
column_energy = Var(
    name='column_energy',
    math_str=r'$F_\mathrm{net}$',
    domain='atmos',
    description='Net energy flux into atmosphere at surface and at TOA.',
    variables=(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
               lwup_sfc, lwdn_sfc, shflx, evap),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.column_energy,
    units=units.W_m2,
    colormap='RdBu_r'
)
cre_lw = Var(
    name='cre_lw',
    domain='atmos',
    description='Cloudy-sky outgoing longwave radiation at TOA.',
    variables=(olr, olr_clr),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.cre_lw,
    units=units.W_m2
)
cre_net = Var(
    name='cre_net',
    domain='atmos',
    description='Net cloudy-sky top-of-atmosphere radiative flux, signed positive downwards.',
    variables=(swup_toa, olr, swup_toa_clr, olr_clr),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.cre_net,
    units=units.W_m2
)
cre_sw = Var(
    name='cre_sw',
    domain='atmos',
    description='Net cloudy-sky top-of-atmosphere shortwave radiative flux, signed positive downwards.',
    variables=(swup_toa, swup_toa_clr),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.cre_sw,
    units=units.W_m2
)
divg_3d = Var(
    name='divg_3d',
    domain='atmos',
    description='3-d divergence',
    variables=(ucomp, vcomp, omega, r_e, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.divg_3d,
    units=units.s1
)
divg_mass_bal = Var(
    name='divg_mass_bal',
    domain='atmos',
    description=('Horizontal divergence, adjusted to exact mass balance in '
                 'each column integral.'),
    variables=(divg, dp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.field_vert_int_bal,
    units=units.s1
)
dry_static_stab = Var(
    name='dry_static_stab',
    domain='atmos',
    description=('Local upper minus lower level DSE for fixed lower level and '
                 'varying upper level over all levels.'),
    variables=(temp, hght, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.dry_static_stab,
    units=units.K
)
dse = Var(
    name='dse',
    domain='atmos',
    description='Dry static energy.',
    variables=(temp, hght),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.dse,
    units=units.J_kg1
)
dse_horiz_advec = Var(
    name='dse_horiz_advec',
    domain='atmos',
    description='Horizontal advection of dry static energy.',
    variables=(temp, hght, ucomp, vcomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.dse_horiz_advec,
    units=units.J_kg1_s1
)
dse_times_horiz_divg = Var(
    name='dse_times_horiz_divg',
    domain='atmos',
    description='Horizontal mass flux divergence times dry static energy.',
    variables=(temp, hght, ucomp, vcomp, r_e, dp),
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    func=calcs.dse_times_horiz_divg,
    units=units.J_kg1_s1
)
dse_horiz_flux_divg = Var(
    name='dse_horiz_flux_divg',
    domain='atmos',
    description='Horizontal flux divergence of dry static energy.',
    variables=(temp, hght, ucomp, vcomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.dse_horiz_flux_divg,
    units=units.J_kg1_s1
)
dse_horiz_advec_divg_sum = Var(
    name='dse_horiz_advec_divg_sum',
    domain='atmos',
    description='Sum of DSE horizontal divergence and advection.',
    variables=(temp, hght, ucomp, vcomp, r_e, dp),
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    func=calcs.dse_horiz_advec_divg_sum,
    units=units.J_kg1_s1
)
du_dx = Var(
    name='du_dx',
    domain='atmos',
    description='',
    variables=(ucomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.d_dx_from_latlon,
    units=units.s1
)
dv_dy = Var(
    name='dv_dy',
    domain='atmos',
    description='',
    variables=(vcomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.d_dy_from_lat,
    units=units.s1
)
equiv_pot_temp = Var(
    name='equiv_pot_temp',
    domain='atmos',
    description='Equivalent potential temperature.',
    variables=(temp, level, sphum),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.equiv_pot_temp,
    units=units.K
)
esf = Var(
    name='esf',
    domain='atmos',
    description='Eddy streamfunction.',
    variables=(level, vcomp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=None,
    units=units.kg_s1
)
evap_frac = Var(
    name='evap_frac',
    domain='atmos',
    description='Evaporative fraction, i.e. ratio of LH to (LH+SH).',
    variables=(evap, shflx),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.evap_frac,
    units=units.kg_s1
)
fmse = Var(
    name='fmse',
    domain='atmos',
    description='Frozen moist static energy.',
    variables=(temp, hght, sphum, ice_wat),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.fmse,
    units=units.J_kg1,
    colormap='RdBu_r'
)
fmse_budget_advec_residual = Var(
    name='fmse_budget_advec_residual',
    domain='atmos',
    description=(
        'Residual in vertically integrated frozen MSE budget, with frozen '
        'MSE transport computed as sum of horizontal and vertical advection '
        'terms.'
    ),
    variables=(
        temp, hght, sphum, ice_wat, ucomp, vcomp, omega, p, dp,
        r_e, swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc,
        shflx, evap
    ),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.fmse_budget_advec_residual,
    units=units.W_m2,
    colormap='RdBu'
)
gms_change_est = Var(
    name='gms_change_est',
    domain='atmos',
    description='Gross moist stability estimated as near surface MSE at ITCZ minus at the local latitude.',
    variables=(temp, temp, sphum, precip, p),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.gms_change_est,
    units=units.K
)
gms_change_est2 = Var(
    name='gms_change_est2',
    domain='atmos',
    description='Gross moist stability estimated as near surface MSE at ITCZ minus at the local latitude.',
    variables=(temp, temp, sphum, precip, level, lat),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.gms_change_est2,
    units=units.K
)
gms_h01 = Var(
    name='gms_h01',
    domain='atmos',
    description='Gross moist stability estimated as near surface MSE at ITCZ minus at the local latitude.',
    variables=(temp, hght, sphum, precip, p),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.gms_h01,
    units=units.K
)
gms_h01est = Var(
    name='gms_h01est',
    domain='atmos',
    description='Gross moist stability estimated as near surface MSE at ITCZ minus at the local latitude, but neglecting the geopotential term.',
    variables=(temp, sphum, precip, p),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.gms_h01est,
    units=units.K
)
gms_h01est2 = Var(
    name='gms_h01est2',
    domain='atmos',
    description='Gross moist stability estimated as MSE aloft at ITCZ minus near surface MSE at the local latitude.',
    variables=(temp, hght, sphum, precip, p),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.gms_h01est2,
    units=units.K
)
gms_moc = Var(
    name='gms_moc',
    domain='atmos',
    description='Gross moist stability using only MMC MSE transport',
    variables=(temp, hght, sphum, precip, p),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.gms_moc,
    units=units.K
)
gms_msf = Var(
    name='gms_msf',
    domain='atmos',
    description='Gross moist stability using MMC plus stationary eddy MSE transport.',
    variables=(temp, hght, sphum, precip, p),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.gms_msf,
    units=units.K
)
gms_up_low = Var(
    name='gms_up_low',
    domain='atmos',
    description='Gross moist stability estimated as uppper minus lower level MSE.',
    variables=(temp, hght, sphum, p),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.gms_up_low,
    units=units.K
)
gms_each_level = Var(
    name='gms_each_level',
    domain='atmos',
    description='Local upper minus lower level MSE for fixed lower level and varying upper level over all levels.',
    variables=(temp, hght, sphum, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.gms_each_level,
    units=units.K
)
gross_dry_stab = Var(
    name='gross_dry_stab',
    domain='atmos',
    description='Gross dry stability.',
    variables=(temp, hght, ucomp, vcomp, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.gross_dry_stab,
    units=units.J_kg1
)
gross_moist_stab = Var(
    name='gross_moist_stab',
    domain='atmos',
    description='Gross dry stability.',
    variables=(temp, hght, sphum, ucomp, vcomp, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.gross_moist_stab,
    units=units.J_kg1
)
gross_moist_strat = Var(
    name='gross_moist_strat',
    domain='atmos',
    description='',
    variables=(sphum, ucomp, vcomp, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.gross_moist_strat,
    units=units.J_kg1
)
hght_horiz_advec = Var(
    name='hght_horiz_advec',
    domain='atmos',
    description='Horizontal advection of geopotential height.',
    variables=(hght, ucomp, vcomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.horiz_advec,
    units=units.J_kg1_s1
)
hght_times_horiz_divg = Var(
    name='hght_times_horiz_divg',
    domain='atmos',
    description='Horizontal mass flux divergence times geopotential height.',
    variables=(hght, ucomp, vcomp, r_e, dp),
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    func=calcs.field_times_horiz_divg,
    units=units.J_kg1_s1
)
hght_horiz_flux_divg = Var(
    name='hght_horiz_flux_divg',
    domain='atmos',
    description='Horizontal flux divergence of geopotential height.',
    variables=(hght, ucomp, vcomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.field_horiz_flux_divg,
    units=units.J_kg1_s1
)
hght_horiz_advec_divg_sum = Var(
    name='hght_horiz_advec_divg_sum',
    domain='atmos',
    description='Sum of geopotential height horizontal divergence and advection.',
    variables=(hght, ucomp, vcomp, r_e, dp),
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    func=calcs.field_horiz_advec_divg_sum,
    units=units.J_kg1_s1
)
horiz_divg = Var(
    name='horiz_divg',
    math_str=r'$\nabla\cdot\mathbf{v}$',
    domain='atmos',
    description='Horizontal mass divergence',
    variables=(ucomp, vcomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.horiz_divg,
    units=units.s1,
    colormap='RdBu'
)
horiz_divg_spharm = Var(
    name='horiz_divg_spharm',
    math_str=r'$\nabla\cdot\mathbf{v}$',
    domain='atmos',
    description='Horizontal mass divergence',
    variables=(ucomp, vcomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.horiz_divg_spharm,
    units=units.s1,
    colormap='RdBu'
)
horiz_divg_mass_adj = Var(
    name='horiz_divg_mass_adj',
    domain='atmos',
    description='',
    variables=(ucomp, vcomp, evap, precip, ps, r_e, dp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.horiz_divg_mass_adj,
    units=units.s1_mass,
    colormap='RdBu'
)
horiz_divg_mass_adj_spharm = Var(
    name='horiz_divg_mass_adj_spharm',
    domain='atmos',
    description='',
    variables=(ucomp, vcomp, evap, precip, ps, r_e, dp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.horiz_divg_mass_adj_spharm,
    units=units.s1_mass,
    colormap='RdBu'
)
horiz_divg_mass_adj_from_eta = Var(
    name='horiz_divg_mass_adj_from_eta',
    domain='atmos',
    description='',
    variables=(ucomp, vcomp, evap, precip, ps, r_e, dp, bk, pk),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.horiz_divg_mass_adj_from_eta,
    units=units.s1_mass,
    colormap='RdBu'
)
horiz_divg_vert_int_max = Var(
    name='horiz_divg_vert_int_max',
    domain='atmos',
    description=('Integral of horizontal divergence from surface to level '
                 'that maximizes its magnitude'),
    variables=(ucomp, vcomp, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.horiz_divg_vert_int_max,
    units=units.kg_m2_s1_mass
)
dry_mass_column_tendency = Var(
    name='dry_mass_column_tendency',
    domain='atmos',
    description=('Monthly time-tendency of surface pressure minus gravity '
                 'times water vapor path monthly time tendency.'),
    variables=(ps, sphum, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.dry_mass_column_tendency,
    units=units.Pa_s1_mass,
    math_str=r'$\partial p_s/\partial t - g\partial \mathrm{WVP}/\partial t$',
    colormap='RdBu_r'
)
dry_mass_column_divg = Var(
    name='dry_mass_column_divg',
    domain='atmos',
    description=('Divergence of vertical integral of (one minus specific '
                 'humidity) times horizontal flow.'),
    variables=(ucomp, vcomp, sphum, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.dry_mass_column_divg,
    units=units.Pa_s1_mass,
    math_str=(r'$\nabla\cdot\int_{p_\mathrm{t}}^{p_\mathrm{s}}'
              '(1-q)\mathbf{v}\,\mathrm{d}p$'),
    colormap='RdBu'
)
dry_mass_column_budget_residual = Var(
    name='dry_mass_column_budget_residual',
    domain='atmos',
    description=('Divergence of vertical integral of (one minus specific '
                 'humidity) times horizontal flow.'),
    variables=(ps, ucomp, vcomp, sphum, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.dry_mass_column_budget_residual,
    units=units.Pa_s1_mass,
    colormap='RdBu'
)
dry_mass_column_divg_with_adj = Var(
    name='dry_mass_column_divg_with_adj',
    domain='atmos',
    description=('Divergence of vertical integral of (one minus specific '
                 'humidity) times horizontal flow.'),
    variables=(ucomp, vcomp, sphum, ps, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.dry_mass_column_divg_with_adj,
    units=units.Pa_s1_mass,
    math_str=(r'$\nabla\cdot\int_{p_\mathrm{t}}^{p_\mathrm{s}}'
              '(1-q)\mathbf{v}\,\mathrm{d}p$'),
    colormap='RdBu'
)
dry_mass_column_budget_with_adj_residual = Var(
    name='dry_mass_column_budget_with_adj_residual',
    domain='atmos',
    description=('Residual of mass budget with explicit correction applied '
                 'to transport term'),
    variables=(ps, ucomp, vcomp, sphum, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.dry_mass_column_budget_with_adj_residual,
    units=units.Pa_s1_mass,
    colormap='RdBu'
)
energy_column_source = Var(
    name='energy_column_source',
    math_str=r'$F_\mathrm{net}$',
    domain='atmos',
    description='Net energy flux into atmosphere at surface and at TOA.',
    variables=(swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc,
               lwup_sfc, lwdn_sfc, shflx, evap),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_column_source,
    units=units.W_m2,
    colormap='RdBu_r'
)
energy_column_divg = Var(
    name='energy_column_divg',
    domain='atmos',
    description='Column flux divergence of energy.  No mass adjustment.',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, dp, r_e),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_column_divg,
    units=units.W_m2,
    colormap='RdBu'
)
energy_column_tendency = Var(
    name='energy_column_tendency',
    domain='atmos',
    description='Monthly time-tendency of column integrated energy.',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_column_tendency,
    units=units.W_m2,
    colormap='RdBu_r'
)
energy_column_tendency_each_timestep = Var(
    name='energy_column_tendency_each_timestep',
    domain='atmos',
    description='Monthly time-tendency of column integrated energy.',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_column_tendency_each_timestep,
    units=units.W_m2,
    colormap='RdBu_r'
)
energy_column_budget_residual = Var(
    name='energy_column_budget_residual',
    domain='atmos',
    description='Residual in column-integrated energy budget.',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp,
               r_e),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_column_budget_residual,
    units=units.W_m2,
    colormap='RdBu_r'
)
energy_column_divg_adj = Var(
    name='energy_column_divg_adj',
    domain='atmos',
    description='',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
               precip, ps, dp, r_e),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_column_divg_adj,
    units=units.W_m2,
    colormap='RdBu_r'
)
energy_column_divg_adj_time_mean = Var(
    name='energy_column_divg_adj_time_mean',
    domain='atmos',
    description='',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
               precip, ps, dp, r_e),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_column_divg_adj_time_mean,
    units=units.W_m2,
    colormap='RdBu_r'
)
energy_column_divg_adj_eddy = Var(
    name='energy_column_divg_adj_eddy',
    domain='atmos',
    description='',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
               precip, ps, dp, r_e),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_column_divg_adj_eddy,
    units=units.W_m2,
    colormap='RdBu_r'
)
energy_column_divg_mass_adj = Var(
    name='energy_column_divg_mass_adj',
    domain='atmos',
    description='',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, evap, precip, ps,
               dp, r_e),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_column_divg_mass_adj,
    units=units.W_m2,
    colormap='RdBu_r'
)
energy_column_budget_adj_residual = Var(
    name='energy_column_budget_adj_residual',
    domain='atmos',
    description='Residual in column-integrated energy budget.',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
               precip, ps, dp, r_e),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_column_budget_adj_residual,
    units=units.W_m2,
    colormap='RdBu_r'
)
energy_ps_horiz_advec = Var(
    name='energy_ps_horiz_advec',
    domain='atmos',
    description='Advection of surface energy times surface pressure',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
               precip, ps, dp, r_e),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_sfc_ps_advec,
    units=units.W_m2,
    colormap='RdBu'
)
energy_ps_horiz_advec_as_resid = Var(
    name='energy_ps_horiz_advec_as_resid',
    domain='atmos',
    description='Advection of surface energy times surface pressure',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
               precip, ps, dp, r_e, bk, pk),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_sfc_ps_advec_as_resid,
    units=units.W_m2,
    colormap='RdBu'
)
energy_horiz_advec_from_eta = Var(
    name='energy_horiz_advec_from_eta',
    domain='atmos',
    description='Horizontal advection of energy from model coordinates',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
               precip, ps, dp, r_e, bk, pk),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_horiz_advec_from_eta,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
energy_horiz_advec_from_eta_time_mean = Var(
    name='energy_horiz_advec_from_eta_time_mean',
    domain='atmos',
    description='Horizontal advection of energy from model coordinates',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
               precip, ps, dp, r_e, bk, pk),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_horiz_advec_from_eta_time_mean,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
energy_horiz_advec = Var(
    name='energy_horiz_advec',
    domain='atmos',
    description='Horizontal advection of energy from model coordinates',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
               precip, ps, dp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_horiz_advec,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
energy_horiz_divg_from_eta = Var(
    name='energy_horiz_divg_from_eta',
    domain='atmos',
    description='Energy times horizontal divergence from model coordinates',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
               precip, ps, dp, r_e, bk, pk),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_horiz_divg_from_eta,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
energy_column_vert_advec_as_resid_from_eta_time_mean = Var(
    name='energy_column_vert_advec_as_resid_from_eta_time_mean',
    domain='atmos',
    description='',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
               precip, ps, dp, r_e, bk, pk),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_column_vert_advec_as_resid_from_eta_time_mean,
    units=units.W_m2,
    colormap='RdBu'
)
energy_column_vert_advec_as_resid = Var(
    name='energy_column_vert_advec_as_resid',
    domain='atmos',
    description='',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
               precip, ps, dp, r_e),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_column_vert_advec_as_resid,
    units=units.W_m2,
    colormap='RdBu'
)
energy_vert_advec_from_eta = Var(
    name='energy_vert_advec_from_eta',
    domain='atmos',
    description='Vertical advection of energy from model coordinates',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, omega, ps, bk, pk),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_vert_advec_from_eta,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
energy_vert_advec_adj_from_eta = Var(
    name='energy_vert_advec_adj_from_eta',
    domain='atmos',
    description='Vertical advection of energy from model coordinates',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, omega, swdn_toa,
               swup_toa, olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx,
               evap, precip, ps, dp, r_e, bk, pk),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_vert_advec_adj_from_eta,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
energy_vert_advec = Var(
    name='energy_vert_advec',
    domain='atmos',
    description='Vertical advection of energy',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, omega),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.energy_vert_advec,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
mass_column = Var(
    name='mass_column',
    math_str=r'$p_s/g$',
    domain='atmos',
    description=('Total mass per square meter of the atmospheric column, '
                 'based on surface pressure.'),
    variables=(ps,),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.mass_column,
    func_input_dtype='numpy',
    units=units.kg_m2,
    colormap='RdBu_r'
)
mass_column_integral = Var(
    name='mass_column_integral',
    math_str=r'$\int^{p_s}_{p_t}\,\mathrm{d}p/g$',
    domain='atmos',
    description=('Total mass per square meter of the atmospheric column,'
                 'computed by explicitly integrating pressure.  Temperature '
                 'variable (temp) is a dummy -- aospy.Calc needs at '
                 'least one netCDF variable per aospy.Var.'),
    variables=(temp, dp,),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.mass_column_integral,
    units=units.kg_m2,
    colormap='RdBu_r'
)
mass_column_divg = Var(
    name='mass_column_divg',
    domain='atmos',
    description='Column mass divergence, computed w/ finite differencing.',
    variables=(ucomp, vcomp, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.mass_column_divg,
    units=units.Pa_s1_mass,
    math_str=(r'$\nabla\cdot\int_{p_\mathrm{t}}^{p_\mathrm{s}}'
              '\mathbf{v}\,\mathrm{d}p$'),
    colormap='RdBu'
)
mass_column_divg_spharm = Var(
    name='mass_column_divg_spharm',
    domain='atmos',
    description='Column mass divergence, computed spectrally.',
    variables=(ucomp, vcomp, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.mass_column_divg_spharm,
    units=units.Pa_s1_mass,
    math_str=(r'$\nabla\cdot\int_{p_\mathrm{t}}^{p_\mathrm{s}}'
              '\mathbf{v}\,\mathrm{d}p$'),
    colormap='RdBu'
)
mass_column_divg_adj = Var(
    name='mass_column_divg_adj',
    domain='atmos',
    description='',
    variables=(ps, ucomp, vcomp, evap, precip, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.mass_column_divg_adj,
    units=units.Pa_s1_mass,
    math_str=(r'$\nabla\cdot\int_{p_\mathrm{t}}^{p_\mathrm{s}}'
              '\mathbf{v}_\mathrm{adj}\,\mathrm{d}p$'),
    colormap='RdBu'
)
mass_column_source = Var(
    name='mass_column_source',
    domain='atmos',
    description='',
    variables=(evap, precip),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.mass_column_source,
    units=units.Pa_s1_mass,
    math_str=r'$g(E-P)$',
    colormap='RdBu'
)
mass_column_tendency = Var(
    name='mass_column_tendency',
    domain='atmos',
    description='Monthly time-tendency of surface pressure.',
    variables=(ps,),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.time_tendency_first_to_last,
    # func=calcs.time_tendency_each_timestep,
    units=units.Pa_s1_mass,
    colormap='RdBu_r'
)
mass_column_budget_lhs = Var(
    name='mass_column_budget_lhs',
    domain='atmos',
    description=(
        'Tendency plus flux divergence of column integrated mass.'
    ),
    variables=(ps, ucomp, vcomp, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.mass_column_budget_lhs,
    units=units.Pa_s1_mass,
    colormap='RdBu_r'
)
mass_column_budget_with_adj_lhs = Var(
    name='mass_column_budget_with_adj_lhs',
    domain='atmos',
    description=(
        'Tendency plus flux divergence of column integrated mass.'
    ),
    variables=(ps, ucomp, vcomp, sphum, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.mass_column_budget_with_adj_lhs,
    units=units.Pa_s1_mass,
    colormap='RdBu_r'
)
mass_column_budget_residual = Var(
    name='mass_column_budget_residual',
    domain='atmos',
    description=(
        'Residual in vertically integrated mass budget.'
    ),
    variables=(ps, ucomp, vcomp, evap, precip, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.mass_column_budget_residual,
    units=units.Pa_s1_mass,
    colormap='RdBu_r'
)
mass_column_budget_adj_residual = Var(
    name='mass_column_budget_adj_residual',
    domain='atmos',
    description=(
        'Residual in column mass budget with imposed mass balance adjustment.'
    ),
    variables=(ps, ucomp, vcomp, evap, precip, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.mass_column_budget_adj_residual,
    units=units.Pa_s1_mass,
    colormap='RdBu_r'
)
moisture_column_source = Var(
    name='moisture_column_source',
    domain='atmos',
    description='Column water vapor source, i.e. evap minus precip.',
    variables=(precip, evap),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.moisture_column_source,
    units=units.kg_m2_s1,
    colormap='BrBG'
)
moisture_column_divg = Var(
    name='moisture_column_divg',
    domain='atmos',
    description='Column flux divergence of water vapor.  No mass adjustment.',
    variables=(sphum, ucomp, vcomp, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.column_flux_divg,
    units=units.kg_m2_s1,
    colormap='BrBG_r'
)
moisture_column_divg_with_adj = Var(
    name='moisture_column_divg_with_adj',
    domain='atmos',
    description=('Column flux divergence of water vapor.  '
                 'Uses mass adjusted winds.'),
    variables=(sphum, ps, ucomp, vcomp, evap, precip, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.column_flux_divg_adj,
    units=units.kg_m2_s1,
    colormap='BrBG_r'
)
moisture_column_divg_with_adj2 = Var(
    name='moisture_column_divg_with_adj2',
    domain='atmos',
    description=('Column flux divergence of water vapor.  '
                 'Uses mass adjusted winds.'),
    variables=(sphum, ps, ucomp, vcomp, evap, precip, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.moisture_column_divg_with_adj2,
    units=units.kg_m2_s1,
    colormap='BrBG_r'
)
moisture_column_tendency = Var(
    name='moisture_column_tendency',
    domain='atmos',
    description='Monthly time-tendency of column-integrated water vapor.',
    variables=(sphum, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.moisture_column_tendency,
    units=units.kg_m2_s1
)
moisture_column_budget_lhs = Var(
    name='moisture_column_budget_lhs',
    domain='atmos',
    description=('Left-hand-side of moisture budget with applied mass '
                 'correction, where LHS = time tendency plus transport.'),
    variables=(ucomp, vcomp, sphum, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.moisture_column_budget_lhs,
    units=units.kg_m2_s1,
    colormap='BrBG_r'
)
moisture_column_budget_with_adj_lhs = Var(
    name='moisture_column_budget_with_adj_lhs',
    domain='atmos',
    description=('Left-hand-side of moisture budget with applied mass '
                 'correction, where LHS = time tendency plus transport.'),
    variables=(ps, ucomp, vcomp, sphum, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.moisture_column_budget_with_adj_lhs,
    units=units.kg_m2_s1,
    colormap='BrBG_r'
)
moisture_column_budget_with_adj2_lhs = Var(
    name='moisture_column_divg_with_adj2_lhs',
    domain='atmos',
    description=('Column flux divergence of water vapor.  '
                 'Mass adjusted by subtracting off column mass residual times '
                 'column average specific humidity.'),
    variables=(ps, ucomp, vcomp, sphum, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.moisture_column_budget_with_adj2_lhs,
    units=units.kg_m2_s1,
    colormap='BrBG_r'
)
moisture_column_budget_residual = Var(
    name='moisture_column_budget_residual',
    domain='atmos',
    description=(
        'Residual in vertically integrated moisture budget.'
    ),
    variables=(sphum, ucomp, vcomp, omega, dp, r_e, evap, precip),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.moisture_column_budget_residual,
    units=units.kg_m2_s1,
    colormap='BrBG_r'
)
moist_static_stab = Var(
    name='moist_static_stab',
    domain='atmos',
    description='Moist static stability, \partial MSE/\partial p',
    variables=(temp, hght, sphum, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.moist_static_stab,
    units=units.J_kg1_Pa1,
    colormap='RdBu_r'
)
mse = Var(
    name='mse',
    domain='atmos',
    math_str=r'$h$',
    description='Moist static energy.',
    variables=(temp, hght, sphum),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.mse,
    units=units.J_kg1,
    valid_range=(3.05e5, 5e6),
    colormap='RdBu_r'
)
mse_horiz_advec = Var(
    name='mse_horiz_advec',
    math_str=r'$\mathbf{v}\cdot\nabla h$',
    domain='atmos',
    description='Horizontal advection of moist static energy.',
    # variables=(temp, hght, sphum, ucomp, vcomp, r_e),
    variables=(temp, hght, sphum, ucomp, vcomp, ps, r_e, bk, pk),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.mse_horiz_advec,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
mse_times_horiz_divg = Var(
    name='mse_times_horiz_divg',
    math_str=r'$h\nabla\cdot\mathbf{v}$',
    domain='atmos',
    description='Horizontal mass flux divergence times moist static energy.',
    variables=(temp, hght, sphum, ucomp, vcomp, r_e, dp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.mse_times_horiz_divg,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
mse_horiz_flux_divg = Var(
    name='mse_horiz_flux_divg',
    math_str=r'$\nabla\cdot(h\mathbf{v})$',
    domain='atmos',
    description='Horizontal flux divergence of moist static energy.',
    variables=(temp, hght, sphum, ucomp, vcomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.mse_horiz_flux_divg,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
mse_horiz_advec_divg_sum = Var(
    name='mse_horiz_advec_divg_sum',
    math_str=r'$h\nabla\cdot\mathbf{v}+\mathbf{v}\cdot\nabla h$',
    domain='atmos',
    description='Sum of MSE horizontal divergence and advection.',
    variables=(temp, hght, sphum, ucomp, vcomp, r_e, dp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.mse_horiz_advec_divg_sum,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
mse_vert_flux_divg = Var(
    name='mse_vert_flux_divg',
    domain='atmos',
    description='Vertical flux divergence of moist static energy.',
    variables=(temp, hght, sphum, omega, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.mse_vert_flux_divg,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
mse_vert_advec = Var(
    name='mse_vert_advec',
    math_str=r'$h\frac{\partial\omega}{\partial p}$',
    domain='atmos',
    description='Moist static energy times vertical divergence.',
    variables=(temp, hght, sphum, omega, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.mse_vert_advec,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
mse_total_advec = Var(
    name='mse_total_advec',
    domain='atmos',
    description=('MSE transport computed as sum of horizontal and '
                 'vertical advection terms.'),
    variables=(temp, hght, sphum, ucomp, vcomp, omega, p, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.mse_total_advec,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
mse_budget_advec_residual = Var(
    name='mse_budget_advec_residual',
    domain='atmos',
    description=(
        'Residual in vertically integrated MSE budget, with MSE transport '
        'computed as sum of horizontal and vertical advection terms.'
    ),
    variables=(
        temp, hght, sphum, ucomp, vcomp, omega, p, dp, r_e,
        swdn_toa, swup_toa, olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx,
        evap
    ),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.mse_budget_advec_residual,
    units=units.W_m2,
    colormap='RdBu'
)
mse_horiz_advec_upwind = Var(
    name='mse_horiz_advec_upwind',
    domain='atmos',
    description=('Horizontal advection of moist static energy using upwind '
                 'finite differencing scheme for derivatives.'),
    variables=(temp, hght, sphum, ucomp, vcomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.mse_horiz_advec_upwind,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
mse_vert_advec_upwind = Var(
    name='mse_vert_advec_upwind',
    domain='atmos',
    description=('Vertical advection of moist static energy using upwind '
                 'finite differencing scheme for derivatives.'),
    variables=(temp, hght, sphum, omega, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.mse_vert_advec_upwind,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
mse_total_advec_upwind = Var(
    name='mse_total_advec_upwind',
    domain='atmos',
    description=('Total advection of moist static energy using upwind '
                 'finite differencing scheme for derivatives.'),
    variables=(temp, hght, sphum, ucomp, vcomp, omega, p, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.mse_total_advec_upwind,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
msf = Var(
    name='msf',
    domain='atmos',
    description='Eulerian meridional mass streamfunction.',
    variables=(level, vcomp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=False,
    func=calcs.msf,
    units=units.kg_s1
)
mass_flux = Var(
    name='mass_flux',
    domain='atmos',
    description=('Mass flux: Eulerian meridional mass streamfunction '
                 'integrated to the level of its maximum magnitude.'),
    variables=(level, vcomp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.msf_max,
    units=units.kg_s1
)
p_minus_e = Var(
    name='p-e',
    domain='atmos',
    description='Precipitation minus evaporation',
    variables=(precip, evap),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.p_minus_e,
    units=units.kg_m2_s1,
    colormap='BrBG'
)
pot_temp = Var(
    name='pot_temp',
    domain='atmos',
    description='Potential temperature.',
    variables=(temp, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.pot_temp,
    units=units.K
)
prec_conv_frac = Var(
    name='prec_conv_frac',
    domain='atmos',
    description=('Fraction of liquid precipitation reaching surface '
                 'originating from convection scheme (as opposed to '
                 'large-scale condensation.'),
    variables=(prec_conv, precip),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.prec_conv_frac,
    units=units.unitless
)
ps_horiz_advec = Var(
    name='ps_horiz_advec',
    domain='atmos',
    description='Horizontal advection of surface pressure',
    variables=(ps, ucomp, vcomp, evap, precip, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.ps_horiz_advec,
    units=units.Pa_s1_mass,
    colormap='RdBu'
)
q_zonal_advec = Var(
    name='q_zonal_advec',
    domain='atmos',
    description='Zonal advection of specific humidity.',
    variables=(sphum, ucomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.zonal_advec,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_merid_advec = Var(
    name='q_merid_advec',
    domain='atmos',
    description='Meridional advection of specific humidity.',
    variables=(sphum, vcomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.merid_advec,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_horiz_advec = Var(
    name='q_horiz_advec',
    domain='atmos',
    description='Horizontal advection of specific humidity.',
    variables=(sphum, ucomp, vcomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.horiz_advec,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_horiz_advec_mass_adj = Var(
    name='q_horiz_advec_mass_adj',
    domain='atmos',
    description='',
    variables=(sphum, ucomp, vcomp, sphum, ps, r_e, dp, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.horiz_advec_mass_adj,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_horiz_advec_const_p_from_eta = Var(
    name='q_horiz_advec_const_p_from_eta',
    domain='atmos',
    description='',
    variables=(sphum, ucomp, vcomp, ps, r_e, bk, pk),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.horiz_advec_const_p_from_eta,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_times_horiz_divg_mass_adj = Var(
    name='q_times_horiz_divg_mass_adj',
    domain='atmos',
    description='',
    variables=(sphum, ucomp, vcomp, sphum, ps, r_e, dp, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.field_times_horiz_divg_mass_adj,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_horiz_flux_divg_mass_adj = Var(
    name='q_horiz_flux_divg_mass_adj',
    domain='atmos',
    description='',
    variables=(sphum, ucomp, vcomp, sphum, ps, r_e, dp, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.field_horiz_flux_divg_mass_adj,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_vert_advec = Var(
    name='q_vert_advec',
    domain='atmos',
    description='Vertical advection of specific humidity.',
    variables=(sphum, omega, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.vert_advec,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_vert_advec_from_eta = Var(
    name='q_vert_advec_from_eta',
    domain='atmos',
    description='Vertical advection of specific humidity.',
    variables=(sphum, omega, ps, bk, pk),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.vert_advec_from_eta,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_zonal_advec_upwind = Var(
    name='q_zonal_advec_upwind',
    domain='atmos',
    description=('Zonal advection of specific humidity using upwind '
                 'finite differencing scheme for derivatives.'),
    variables=(sphum, ucomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.zonal_advec_upwind,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_merid_advec_upwind = Var(
    name='q_merid_advec_upwind',
    domain='atmos',
    description=('Meridional advection of specific humidity using upwind '
                 'finite differencing scheme for derivatives.'),
    variables=(sphum, vcomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.merid_advec_upwind,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_horiz_advec_upwind = Var(
    name='q_horiz_advec_upwind',
    domain='atmos',
    description=('Horizontal advection of specific humidity using upwind '
                 'finite differencing scheme for derivatives.'),
    variables=(sphum, ucomp, vcomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.horiz_advec_upwind,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_vert_advec_upwind = Var(
    name='q_vert_advec_upwind',
    domain='atmos',
    description=('Vertical advection of specific humidity using upwind '
                 'finite differencing scheme for derivatives.'),
    variables=(sphum, omega, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.vert_advec_upwind,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_total_advec_upwind = Var(
    name='q_total_advec_upwind',
    domain='atmos',
    description=('Total advection of specific humidity using upwind '
                 'finite differencing scheme for derivatives.'),
    variables=(sphum, ucomp, vcomp, omega, p, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.total_advec_upwind,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_times_horiz_divg = Var(
    name='q_times_horiz_divg',
    domain='atmos',
    description='Horizontal flux divergence times specific humidity.',
    variables=(sphum, ucomp, vcomp, r_e, dp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.field_times_horiz_divg,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_horiz_flux_divg = Var(
    name='q_horiz_flux_divg',
    domain='atmos',
    description='Horizontal flux divergence of specific humidity.',
    variables=(sphum, ucomp, vcomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.field_horiz_flux_divg,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_horiz_advec_divg_sum = Var(
    name='q_horiz_advec_divg_sum',
    domain='atmos',
    description='Sum of Q horizontal divergence and advection.',
    variables=(sphum, ucomp, vcomp, r_e, dp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.field_horiz_advec_divg_sum,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_vert_flux_divg = Var(
    name='q_vert_flux_divg',
    domain='atmos',
    description='Vertical flux divergence of specific humidity.',
    variables=(sphum, omega, p),
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    func=calcs.field_vert_flux_divg,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_total_advec = Var(
    name='q_total_advec',
    domain='atmos',
    description=('Moisture transport computed as sum of horizontal and '
                 'vertical advection terms.'),
    variables=(sphum, ucomp, vcomp, omega, p, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.field_total_advec,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
sfc_albedo = Var(
    name='sfc_albedo',
    domain='atmos',
    description='Surface albedo, masked where downwelling surface SW is zero.',
    variables=(swdn_sfc, swup_sfc),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.sfc_albedo,
    units=units.unitless
)
sfc_energy = Var(
    name='sfc_energy',
    domain='atmos',
    description='Net surface energy flux, signed positive upwards.',
    variables=(swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.sfc_energy,
    units=units.W_m2
)
sfc_lw = Var(
    name='sfc_lw',
    domain='atmos',
    description='Net all-sky longwave radiative flux at surface, signed positive upwards.',
    variables=(lwup_sfc, lwdn_sfc),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.sfc_lw,
    units=units.W_m2
)
sfc_lw_cld = Var(
    name='sfc_lw_cld',
    domain='atmos',
    description='Net cloudy-sky longwave radiative flux at surface, signed positive upwards.',
    variables=(lwup_sfc, lwup_sfc_clr, lwdn_sfc, lwdn_sfc_clr),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.sfc_lw_cld,
    units=units.W_m2
)
sfc_rad = Var(
    name='sfc_rad',
    domain='atmos',
    description='Net all-sky surface radiative flux, signed positive upwards.',
    variables=(swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.sfc_rad,
    units=units.W_m2
)
sfc_rad_cld = Var(
    name='sfc_rad_cld',
    domain='atmos',
    description='Net cloudy-sky surface radiative flux, signed positive upwards.',
    variables=(swup_sfc, swup_sfc_clr, swdn_sfc, swdn_sfc_clr,
          lwup_sfc, lwup_sfc_clr, lwdn_sfc, lwdn_sfc_clr),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.sfc_rad_cld,
    units=units.W_m2
)
sfc_rad_clr = Var(
    name='sfc_rad_clr',
    domain='atmos',
    description='Net clear-sky surface radiative flux, positive upwards.',
    variables=(swup_sfc_clr, swdn_sfc_clr, lwup_sfc_clr, lwdn_sfc_clr),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.sfc_rad,
    units=units.W_m2
)
sfc_sw = Var(
    name='sfc_sw',
    domain='atmos',
    description='Net all-sky shortwave radiative flux at surface, signed positive upwards.',
    variables=(swup_sfc, swdn_sfc),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.sfc_sw,
    units=units.W_m2
)
sfc_sw_cld = Var(
    name='sfc_sw_cld',
    domain='atmos',
    description='Net cloudy-sky shortwave radiative flux at surface, signed positive upwards.',
    variables=(swup_sfc, swup_sfc_clr, swdn_sfc, swdn_sfc_clr),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.sfc_sw_cld,
    units=units.W_m2
)
temp_horiz_advec = Var(
    name='temp_horiz_advec',
    domain='atmos',
    description='Horizontal advection of temperature.',
    variables=(temp, ucomp, vcomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.horiz_advec,
    units=units.K_s1
)
temp_times_horiz_divg = Var(
    name='temp_times_horiz_divg',
    domain='atmos',
    description='Horizontal mass flux divergence times temperature.',
    variables=(temp, ucomp, vcomp, r_e, dp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.field_times_horiz_divg,
    units=units.K_s1
)
temp_horiz_flux_divg = Var(
    name='temp_horiz_flux_divg',
    domain='atmos',
    description='Horizontal flux divergence of temperature.',
    variables=(temp, ucomp, vcomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.field_horiz_flux_divg,
    units=units.K_s1
)
temp_horiz_advec_divg_sum = Var(
    name='temp_horiz_advec_divg_sum',
    domain='atmos',
    description='Sum of temperature horizontal divergence and advection.',
    variables=(temp, ucomp, vcomp, r_e, dp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.field_horiz_advec_divg_sum,
    units=units.K_s1
)
temp_vert_advec = Var(
    name='temp_vert_advec',
    domain='atmos',
    description='Vertical advection of temperature.',
    variables=(temp, omega, p),
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    func=calcs.vert_advec,
    units=units.K_s1
)
tdt_diab = Var(
    name='tdt_diab',
    domain='atmos',
    description='Net temperature tendency from diabatic terms: LW, SW, convective, large-scale, and vertical diffusion.',
    variables=(tdt_lw, tdt_sw, tdt_conv, tdt_ls),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.tdt_diab,
    units=units.K_s1
)
tdt_lw_cld = Var(
    name='tdt_lw_cld',
    domain='atmos',
    description='Cloudy-sky temperature tendency from longwave radiation.' ,
    variables=(tdt_lw, tdt_lw_clr),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.tdt_lw_cld,
    units=units.K_s1
)
tdt_sw_cld = Var(
    name='tdt_sw_cld',
    domain='atmos',
    description='Cloudy-sky temperature tendency from shortwave radiation.' ,
    variables=(tdt_sw, tdt_sw_clr),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.tdt_sw_cld,
    units=units.K_s1
)
toa_rad = Var(
    name='toa_rad',
    math_str=r'$R_\mathrm{toa}$',
    domain='atmos',
    description='Net top-of-atmosphere radiative flux, signed positive downwards.',
    variables=(swdn_toa, swup_toa, olr),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.toa_rad,
    units=units.W_m2,
    colormap='RdBu_r'
)
toa_rad_clr = Var(
    name='toa_rad_clr',
    domain='atmos',
    description='Clear-sky TOA radiative flux, positive downwards.',
    variables=(swdn_toa_clr, swup_toa_clr, olr_clr),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.toa_rad_clr,
    units=units.W_m2
)
toa_sw = Var(
    name='toa_sw',
    domain='atmos',
    description='Net all-sky top-of-atmosphere shortwave radiative flux, signed positive downwards.',
    variables=(swdn_toa, swup_toa),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.toa_sw,
    units=units.W_m2
)
total_gms = Var(
    name='total_gms',
    domain='atmos',
    description='Total gross moist stability, i.e. GMS using MMC plus stationary and transient eddy MSE transports.',
    variables=(temp, hght, sphum, precip, p),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.total_gms,
    units=units.K
)
cre_sw_precip_corr = Var(
    name='cre_sw_precip_corr',
    domain='atmos',
    description='Pointwise temporal correlation of SW CRE and precip',
    variables=(swup_toa, swup_toa_clr, precip),
    def_time=False,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.corr_cre_sw,
    units=units.unitless
)
cre_lw_precip_corr = Var(
    name='cre_lw_precip_corr',
    domain='atmos',
    description='Pointwise temporal correlation of LW CRE and precip',
    variables=(olr, olr_clr, precip),
    def_time=False,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.corr_cre_lw,
    units=units.unitless
)
cre_net_precip_corr = Var(
    name='cre_net_precip_corr',
    domain='atmos',
    description='Pointwise temporal correlation of net CRE and precip',
    variables=(swup_toa, olr, swup_toa_clr, olr_clr, precip),
    def_time=False,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.corr_cre_net,
    units=units.unitless
)
evap_precip_corr = Var(
    name='evap_precip_corr',
    domain='atmos',
    description='Pointwise temporal correlation of evap and precip',
    variables=(evap, precip),
    def_time=False,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.pointwise_corr,
    units=units.unitless
)
toa_rad_clr_precip_corr = Var(
    name='toa_rad_clr_precip_corr',
    domain='atmos',
    description='',
    variables=(swdn_toa_clr, swup_toa_clr, olr_clr, precip),
    def_time=False,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.corr_toa_rad_clr,
    units=units.unitless
)
t_surf_precip_corr = Var(
    name='t_surf_precip_corr',
    domain='atmos',
    description='Pointwise temporal correlation of t_surf and precip',
    variables=(t_surf, precip),
    def_time=False,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.pointwise_corr,
    units=units.unitless
)
cre_net_precip_lin_regr = Var(
    name='cre_net_precip_lin_regr',
    domain='atmos',
    description='',
    variables=(swup_toa, olr, swup_toa_clr, olr_clr, precip),
    def_time=False,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.lin_regr_cre_net,
    units=units.unitless,
)
toa_rad_clr_precip_lin_regr = Var(
    name='toa_rad_clr_precip_lin_regr',
    domain='atmos',
    description='',
    variables=(swdn_toa_clr, swup_toa_clr, olr_clr, precip),
    def_time=False,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.lin_regr_toa_rad_clr,
    units=units.unitless,
)
t_surf_precip_lin_regr = Var(
    name='t_surf_precip_lin_regr',
    domain='atmos',
    description=('Pointwise temporal least squares linear regression of '
                 't_surf and precip'),
    variables=(t_surf, precip),
    def_time=False,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.pointwise_lin_regr,
    units=units.unitless
)
u_energy_adjustment = Var(
    name='u_energy_adjustment',
    domain='atmos',
    description='',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp,
               r_e),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.u_energy_adjustment,
    units=units.m_s1
)
u_energy_adjusted = Var(
    name='u_energy_adjusted',
    domain='atmos',
    description='',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp,
               r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.u_energy_adjusted,
    units=units.m_s1
)
u_mass_adjustment = Var(
    name='u_mass_adjustment',
    domain='atmos',
    description='',
    variables=(ps, ucomp, vcomp, evap, precip, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.u_mass_adjustment,
    units=units.m_s1
)
u_mass_adjusted = Var(
    name='u_mass_adjusted',
    domain='atmos',
    description='',
    variables=(ps, ucomp, vcomp, evap, precip, r_e, dp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.u_mass_adjusted,
    units=units.m_s1
)
u_mass_energy_adjustment = Var(
    name='u_mass_energy_adjustment',
    domain='atmos',
    description='',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
               precip, ps, dp, r_e),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.u_mass_energy_adjustment,
    units=units.m_s1
)
u_mass_energy_adjusted = Var(
    name='u_mass_energy_adjusted',
    domain='atmos',
    description='',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
               precip, ps, dp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.u_mass_energy_adjusted,
    units=units.m_s1
)
v_energy_adjustment = Var(
    name='v_energy_adjustment',
    domain='atmos',
    description='',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp,
               r_e),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.v_energy_adjustment,
    units=units.m_s1
)
v_energy_adjusted = Var(
    name='v_energy_adjusted',
    domain='atmos',
    description='',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap, dp,
               r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.v_energy_adjusted,
    units=units.m_s1
)
v_mass_adjustment = Var(
    name='v_mass_adjustment',
    domain='atmos',
    description='',
    variables=(ps, ucomp, vcomp, evap, precip, r_e, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.v_mass_adjustment,
    units=units.m_s1
)
v_mass_adjusted = Var(
    name='v_mass_adjusted',
    domain='atmos',
    description='',
    variables=(ps, ucomp, vcomp, evap, precip, r_e, dp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.v_mass_adjusted,
    units=units.m_s1
)
v_mass_energy_adjustment = Var(
    name='v_mass_energy_adjustment',
    domain='atmos',
    description='',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
               precip, ps, dp, r_e),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.v_mass_energy_adjustment,
    units=units.m_s1
)
v_mass_energy_adjusted = Var(
    name='v_mass_energy_adjusted',
    domain='atmos',
    description='',
    variables=(temp, hght, sphum, ice_wat, ucomp, vcomp, swdn_toa, swup_toa,
               olr, swup_sfc, swdn_sfc, lwup_sfc, lwdn_sfc, shflx, evap,
               precip, ps, dp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.v_mass_energy_adjusted,
    units=units.m_s1
)
vert_divg = Var(
    name='vert_divg',
    domain='atmos',
    description='',
    variables=(omega, p),
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    func=calcs.vert_divg,
    units=units.s1
)
vert_divg_vert_int_max = Var(
    name='vert_divg_vert_int_max',
    domain='atmos',
    description=('Integral of vertical divergence from surface to level '
                 'that maximizes its magnitude'),
    variables=(omega, p, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.vert_divg_vert_int_max,
    units=units.kg_m2_s1_mass
)
virt_pot_temp = Var(
    name='virt_pot_temp',
    domain='atmos',
    description='Virtual potential temperature.',
    variables=(temp, p, sphum, liq_wat),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.virt_pot_temp,
    units=units.K
)
