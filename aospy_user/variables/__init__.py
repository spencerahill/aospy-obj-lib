"""Collection of aospy.Var objects for use in my research."""
from aospy.constants import r_e
from aospy.var import Var
from aospy_user import calcs, units


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
    description='Pressure level.',
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
column_mass = Var(
    name='column_mass',
    math_str=r'$p_s/g$',
    domain='atmos',
    description=('Total mass per square meter of the atmospheric column, '
                 'based on surface pressure.'),
    variables=(ps,),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.column_mass,
    func_input_dtype='numpy',
    units=units.kg_m2,
    colormap='RdBu_r'
)
column_mass_integral = Var(
    name='column_mass_integral',
    math_str=r'$\int^{p_s}_{p_t}\,\mathrm{d}p/g$',
    domain='atmos',
    description=('Total mass per square meter of the atmospheric column,'
                 'computed by explicitly integrating pressure.  Temperature '
                 'variable (temp) is a dummy -- aospy.Calc needs at '
                 'least one netCDF variable per aospy.Var.'),
    variables=(temp, 'dp',),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.column_mass_integral,
    units=units.kg_m2,
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
descent_tot = Var(
    name='descent_tot',
    domain='atmos',
    description='Total vertical pressure velocity (i.e. signed positive moving vertically downwards) per unit surface area. Includes both convective and large scale.',
    variables=(omega, mc),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.descent_tot,
    units=units.Pa_s1
)
divg_3d = Var(
    name='divg_3d',
    domain='atmos',
    description='3-d divergence',
    variables=(ucomp, vcomp, omega, r_e, 'p'),
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
    variables=(divg, 'dp'),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.field_vert_int_bal,
    units=units.s1
)
# divg_spharm = Var(
#     name='divg_spharm',
#     domain='atmos',
#     description='Horizontal divergence using spharm spherical harmonics.',
#     variables=(ucomp, vcomp),
#     def_time=True,
#     def_vert=True,
#     def_lat=True,
#     def_lon=True,
#     func=calcs.divg_spharm,
#     units=units.s1
# )
dry_static_stab = Var(
    name='dry_static_stab',
    domain='atmos',
    description=('Local upper minus lower level DSE for fixed lower level and '
                 'varying upper level over all levels.'),
    variables=('temp', 'hght', 'p'),
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
    variables=(temp, hght, ucomp, vcomp, r_e, 'dp'),
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
    variables=(temp, hght, ucomp, vcomp, r_e, 'dp'),
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    func=calcs.dse_horiz_advec_divg_sum,
    units=units.J_kg1_s1
)
d_dx_of_vert_int_u = Var(
    name='d_dx_of_vert_int_u',
    domain='atmos',
    description='',
    variables=(ucomp, r_e, 'dp'),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.d_dx_of_vert_int,
    units=units.kg_m2_s1_mass
)
d_dy_of_vert_int_v = Var(
    name='d_dy_of_vert_int_v',
    domain='atmos',
    description='',
    variables=(vcomp, r_e, 'dp'),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.d_dy_of_vert_int,
    units=units.kg_m2_s1_mass
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
        temp, hght, sphum, ice_wat, ucomp, vcomp, omega, 'p', 'dp',
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
    variables=(temp, temp, sphum, precip, 'p'),
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
    variables=(temp, hght, sphum, precip, 'p'),
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
    variables=(temp, sphum, precip, 'p'),
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
    variables=(temp, hght, sphum, precip, 'p'),
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
    variables=(temp, hght, sphum, precip, 'p'),
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
    variables=(temp, hght, sphum, precip, 'p'),
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
    variables=(temp, hght, sphum, 'p'),
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
    variables=(temp, hght, sphum, 'p'),
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
    variables=(temp, hght, ucomp, vcomp, r_e, 'dp'),
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
    variables=(temp, hght, sphum, ucomp, vcomp, r_e, 'dp'),
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
    variables=(sphum, ucomp, vcomp, r_e, 'dp'),
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
    variables=(hght, ucomp, vcomp, r_e, 'dp'),
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    func=calcs.field_times_horiz_divg_mass_bal,
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
    variables=(hght, ucomp, vcomp, r_e, 'dp'),
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
    description='',
    variables=(ucomp, vcomp, r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.horiz_divg,
    units=units.s1,
    colormap='RdBu'
)
horiz_divg_mass_bal = Var(
    name='horiz_divg_mass_bal',
    domain='atmos',
    description='',
    variables=(ucomp, vcomp, r_e, 'dp'),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.horiz_divg_mass_bal,
    units=units.s1,
    colormap='RdBu'
)
horiz_divg_mass_adj = Var(
    name='horiz_divg_mass_adj',
    domain='atmos',
    description='',
    variables=(ucomp, vcomp, sphum, ps, r_e, 'dp', 'p'),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.horiz_divg_mass_adj,
    units=units.s1,
    colormap='RdBu'
)
divg_of_vert_int_horiz_flow = Var(
    name='divg_of_vert_int_horiz_flow',
    domain='atmos',
    description='',
    variables=(ucomp, vcomp, r_e, 'dp'),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.divg_of_vert_int_horiz_flow,
    units=units.Pa_s1_mass,
    math_str=(r'$\nabla\cdot\int_{p_\mathrm{t}}^{p_\mathrm{s}}'
              '\mathbf{v}\,\mathrm{d}p$'),
    colormap='RdBu'
)
horiz_advec_sfc_pressure = Var(
    name='horiz_advec_sfc_pressure',
    domain='atmos',
    description='',
    variables=(ps, ucomp, vcomp, r_e, 'p'),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.horiz_advec_sfc_pressure,
    units=units.s1,
    colormap='RdBu'
)
horiz_divg_vert_int_max = Var(
    name='horiz_divg_vert_int_max',
    domain='atmos',
    description=('Integral of horizontal divergence from surface to level '
                 'that maximizes its magnitude'),
    variables=(ucomp, vcomp, r_e, 'dp'),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.horiz_divg_vert_int_max,
    units=units.kg_m2_s1_mass
)
mass_budget_tendency_term = Var(
    name='mass_budget_tendency_term',
    domain='atmos',
    description=('Monthly time-tendency of surface pressure minus gravity '
                 'times water vapor path monthly time tendency.'),
    variables=(ps, sphum, 'dp'),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.mass_budget_tendency_term,
    units=units.Pa_s1_mass,
    math_str=r'$\partial p_s/\partial t - g\partial \mathrm{WVP}/\partial t$',
    colormap='RdBu_r'
)
mass_budget_transport_term = Var(
    name='mass_budget_transport_term',
    domain='atmos',
    description=('Divergence of vertical integral of (one minus specific '
                 'humidity) times horizontal flow.'),
    variables=(ucomp, vcomp, sphum, r_e, 'dp'),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.mass_budget_transport_term,
    units=units.Pa_s1_mass,
    math_str=(r'$\nabla\cdot\int_{p_\mathrm{t}}^{p_\mathrm{s}}'
              '(1-q)\mathbf{v}\,\mathrm{d}p$'),
    colormap='RdBu'
)
mass_budget_residual = Var(
    name='mass_budget_transport_term',
    domain='atmos',
    description=('Divergence of vertical integral of (one minus specific '
                 'humidity) times horizontal flow.'),
    variables=(ps, ucomp, vcomp, sphum, r_e, 'dp'),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.mass_budget_residual,
    units=units.Pa_s1_mass,
    colormap='RdBu'
)
moist_static_stab = Var(
    name='moist_static_stab',
    domain='atmos',
    description='Moist static stability, \partial MSE/\partial p',
    variables=(temp, hght, sphum, 'p'),
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
    variables=(temp, hght, sphum, ucomp, vcomp, r_e),
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
    variables=(temp, hght, sphum, ucomp, vcomp, r_e, 'dp'),
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
    variables=(temp, hght, sphum, ucomp, vcomp, r_e, 'dp'),
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
    variables=(temp, hght, sphum, omega, 'p'),
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
    variables=(temp, hght, sphum, omega, 'p'),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.mse_vert_advec,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
mse_times_vert_divg = Var(
    name='mse_times_vert_divg',
    domain='atmos',
    description='Vertical advection of moist static energy.',
    variables=(temp, hght, sphum, omega, 'p', 'dp'),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.mse_times_vert_divg,
    units=units.J_kg1_s1,
    colormap='RdBu'
)
mse_total_advec = Var(
    name='mse_total_advec',
    domain='atmos',
    description=('MSE transport computed as sum of horizontal and '
                 'vertical advection terms.'),
    variables=(temp, hght, sphum, ucomp, vcomp, omega, 'p', r_e),
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
        temp, hght, sphum, ucomp, vcomp, omega, 'p', 'dp', r_e,
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
    variables=(temp, hght, sphum, omega, 'p'),
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
    variables=(temp, hght, sphum, ucomp, vcomp, omega, 'p', r_e),
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
    variables=(temp, 'p'),
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
ps_monthly_tendency = Var(
    name='ps_monthly_tendency',
    domain='atmos',
    description='Monthly time-tendency of surface pressure.',
    variables=(ps,),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.time_tendency,
    units=units.Pa_s1_mass
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
    variables=(sphum, ucomp, vcomp, sphum, ps, r_e, 'dp', 'p'),
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
    variables=(sphum, ucomp, vcomp, sphum, ps, r_e, 'dp', 'p'),
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
    variables=(sphum, ucomp, vcomp, sphum, ps, r_e, 'dp', 'p'),
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
    variables=(sphum, omega, 'p'),
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
    variables=(sphum, omega, 'p'),
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
    variables=(sphum, ucomp, vcomp, omega, 'p', r_e),
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
    variables=(sphum, ucomp, vcomp, r_e, 'dp'),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.field_times_horiz_divg_mass_bal,
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
    variables=(sphum, ucomp, vcomp, r_e, 'dp'),
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
    variables=(sphum, omega, 'p'),
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    func=calcs.field_vert_flux_divg,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_times_vert_divg = Var(
    name='q_times_vert_divg',
    domain='atmos',
    description='Specific humidity times vertical divergence.',
    variables=(sphum, omega, 'p', 'dp'),
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    func=calcs.field_times_vert_divg_mass_bal,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_total_advec = Var(
    name='q_total_advec',
    domain='atmos',
    description=('Moisture transport computed as sum of horizontal and '
                 'vertical advection terms.'),
    variables=(sphum, ucomp, vcomp, omega, 'p', r_e),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.field_total_advec,
    units=units.s1_spec_mass,
    colormap='BrBG_r'
)
q_budget_advec_residual = Var(
    name='q_budget_advec_residual',
    domain='atmos',
    description=(
        'Residual in vertically integrated moisture budget, with moisture '
        'transport computed as sum of horizontal and vertical advection '
        'terms.'
    ),
    variables=(sphum, ucomp, vcomp, omega, 'p', 'dp',
               r_e, evap, precip),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.q_budget_advec_residual,
    units=units.kg_m2_s1,
    colormap='BrBG_r'
)
qu = Var(
    name='qu',
    domain='atmos',
    description='Zonal specific humidity flux.',
    variables=(sphum, ucomp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.qu,
    units=units.m_s1
)
qv = Var(
    name='qv',
    domain='atmos',
    description='Meridional specific humidity flux.',
    variables=(sphum, vcomp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.qv,
    units=units.m_s1
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
    variables=(temp, ucomp, vcomp, r_e, 'dp'),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.field_times_horiz_divg_mass_bal,
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
    variables=(temp, ucomp, vcomp, r_e, 'dp'),
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
    variables=(temp, omega, 'p'),
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
    variables=(temp, hght, sphum, precip, 'p'),
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
vert_divg = Var(
    name='vert_divg',
    domain='atmos',
    description='',
    variables=(omega, 'p'),
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    func=calcs.vert_divg,
    units=units.s1
)
vert_divg_mass_bal = Var(
    name='vert_divg_mass_bal',
    domain='atmos',
    description='',
    variables=(omega, 'p', 'dp'),
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    func=calcs.vert_divg_mass_bal,
    units=units.s1
)
vert_divg_vert_int_max = Var(
    name='vert_divg_vert_int_max',
    domain='atmos',
    description=('Integral of vertical divergence from surface to level '
                 'that maximizes its magnitude'),
    variables=(omega, 'p', 'dp'),
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
    variables=(temp, 'p', sphum, liq_wat),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.virt_pot_temp,
    units=units.K
)
wvp_monthly_tendency = Var(
    name='wvp_monthly_tendency',
    domain='atmos',
    description='Monthly tendency of water vapor path.',
    variables=(sphum, 'dp'),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.wvp_time_tendency,
    units=units.kg_m2_s1_mass
)

master_vars_list = [
    alb_sfc, cld_amt, divg, esf, evap, hght, high_cld_amt, ice_wat, liq_wat,
    low_cld_amt, lwdn_sfc, lwdn_sfc_clr, lwup_sfc, lwup_sfc_clr, mc, mc_full,
    mc_half, mid_cld_amt, olr, olr_clr, omega, precip, prec_conv, prec_ls, ps,
    pv, rh, rh_ref, shflx, slp, snow_conv, snow_ls, soil_liq, soil_moisture,
    sphum, sst, swdn_sfc, swdn_sfc_clr, swup_sfc, swup_sfc_clr, swdn_toa,
    swdn_toa_clr, swup_toa, swup_toa_clr, t_surf, tdt_conv, tdt_ls, tdt_lw,
    tdt_lw_clr, tdt_sw, tdt_sw_clr, tdt_vdif, temp, tot_cld_amt, ucomp, u_ref,
    v_ref, vcomp, vort, wvp, lat, lon, level, pk, bk, sfc_area, aht, albedo,
    sfc_albedo, ang_mom, bowen_ratio, column_energy, cre_net, cre_lw, cre_sw,
    descent_tot, equiv_pot_temp, esf, evap_frac, fmse, gms_change_est,
    gms_change_est2, gms_h01, gms_h01est, gms_h01est2, gms_moc, gms_msf,
    gms_up_low, gms_each_level, gross_dry_stab, gross_moist_stab,
    dry_static_stab, total_gms, dse, horiz_divg, moist_static_stab,
    gross_moist_strat, mse, mse_horiz_advec, mse_times_horiz_divg,
    mse_vert_advec, msf, mass_flux, p_minus_e, pot_temp, prec_conv_frac,
    sfc_albedo, sfc_energy, sfc_lw, sfc_lw_cld, sfc_rad, sfc_rad_cld,
    sfc_rad_clr, sfc_sw, sfc_sw_cld, tdt_diab, tdt_lw_cld, tdt_sw_cld, toa_rad,
    toa_rad_clr, toa_sw, vert_divg, virt_pot_temp, divg_mass_bal,
    horiz_divg_mass_bal, vert_divg_mass_bal, mse_horiz_flux_divg,
    q_horiz_advec, q_vert_advec, q_times_horiz_divg, q_horiz_flux_divg, qu, qv,
    du_dx, dv_dy, dse_horiz_flux_divg, dse_times_horiz_divg, dse_horiz_advec,
    temp_horiz_flux_divg, temp_times_horiz_divg, temp_horiz_advec,
    hght_horiz_flux_divg, hght_times_horiz_divg, hght_horiz_advec,
    mse_horiz_advec_divg_sum, q_horiz_advec_divg_sum,
    temp_horiz_advec_divg_sum, hght_horiz_advec_divg_sum,
    dse_horiz_advec_divg_sum, q_times_vert_divg, q_vert_flux_divg,
    mse_times_vert_divg, mse_vert_flux_divg, horiz_divg_vert_int_max,
    vert_divg_vert_int_max, temp_vert_advec, t_surf_precip_corr,
    evap_precip_corr, cre_net_precip_corr, cre_sw_precip_corr,
    cre_lw_precip_corr, t_surf_precip_lin_regr, cre_net_precip_lin_regr,
    toa_rad_clr_precip_corr, toa_rad_clr_precip_lin_regr,
    mse_budget_advec_residual, fmse_budget_advec_residual,
    q_budget_advec_residual, q_total_advec, mse_total_advec,
    q_horiz_advec_upwind,
    q_vert_advec_upwind, q_total_advec_upwind, q_zonal_advec_upwind,
    q_merid_advec_upwind, q_zonal_advec, q_merid_advec, mse_horiz_advec_upwind,
    mse_vert_advec_upwind, mse_total_advec_upwind, column_mass,
    column_mass_integral,
    # divg_spharm,
    horiz_divg_mass_adj, divg_3d,
    divg_of_vert_int_horiz_flow,
    horiz_advec_sfc_pressure,
    q_horiz_advec_mass_adj,
    q_times_horiz_divg_mass_adj,
    q_horiz_flux_divg_mass_adj,
    ps_monthly_tendency,
    d_dx_of_vert_int_u,
    d_dy_of_vert_int_v,
    q_horiz_advec_const_p_from_eta,
    wvp_monthly_tendency,
    mass_budget_tendency_term
]
