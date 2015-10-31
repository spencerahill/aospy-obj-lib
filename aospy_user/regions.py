"""Library of Region objects I use in my research"""
from aospy.region import Region


globe = Region(
    name='globe',
    description='Entire globe',
    lat_bounds=(-90, 90),
    lon_bounds=(0, 360),
    land_mask=False
)
land = Region(
    name='land',
    description='Land',
    lat_bounds=(-90, 90),
    lon_bounds=(0, 360),
    land_mask=True
)
ocean = Region(
    name='ocean',
    description='Ocean',
    lat_bounds=(-90, 90),
    lon_bounds=(0, 360),
    land_mask='ocean'
)
nh = Region(
    name='nh',
    description='Northern hemisphere',
    lat_bounds=(0, 90),
    lon_bounds=(0, 360),
    land_mask=False
)
sh = Region(
    name='sh',
    description='Southern hemisphere',
    lat_bounds=(-90, 0),
    lon_bounds=(0, 360),
    land_mask=False
)
eh = Region(
    name='eh',
    description='Eastern hemisphere',
    lat_bounds=(-90, 90),
    lon_bounds=(0, 180),
    land_mask=False
)
wh = Region(
    name='wh',
    description='Western hemisphere',
    lat_bounds=(-90, 90),
    lon_bounds=(180, 360),
    land_mask=False
)
tropics = Region(
    name='tropics',
    description='Tropics (30S-30N)',
    lat_bounds=(-30, 30),
    lon_bounds=(0, 360),
    land_mask=False
)
trop_land = Region(
    name='tropics_land',
    description='All land 30S-30N',
    lat_bounds=(-30, 30),
    lon_bounds=(0, 360),
    land_mask=True
)
trop_ocean = Region(
    description='All ocean 30S-30N',
    name='tropics_ocean',
    lat_bounds=(-30, 30),
    lon_bounds=(0, 360),
    land_mask='ocean'
)
deep_tropics = Region(
    name='deep_tropics',
    description='Deep tropics (10S-10N)',
    lat_bounds=(-10, 10),
    lon_bounds=(0, 360),
    land_mask=False
)
atlantic = Region(
    name='atlantic',
    description='Atlantic Ocean',
    land_mask='ocean',
# atlantic.mask_bounds=[((-90, 90), (0, 25)), ((-90, 90), (290, 360)),
# # Atlantic 1
# ((xlat(j) ge -90. and (xlon(i) gt 290. or xlon(i) lt 25.)) or $
#  (xlat(j) gt 0. and xlat(j) lt 20. and ((xlon(i)+xlat(j)) gt 290.)) or $
#  (xlat(j) le 65. and xlat(j) gt 15 and (xlon(i) gt 260. or xlon(i) lt 50.)) or $
#  (xlat(j) gt 65.))
# # Atlantic 2
# ((xlat(j) ge -90. and (xlon(i) gt 290. or xlon(i) lt 25.)) or $
#  (xlat(j) gt 0. and xlat(j) lt 20. and ((xlon(i)+xlat(j)) gt 290.)) or $
#  (xlat(j) le 65. and xlat(j) gt 15 and (xlon(i) gt 260. or xlon(i) lt 50.)) or $
#  (xlat(j) gt 65.))
# # Indian
# (xlon(i) le 100.5 or (xlon(i) gt 100.5 and xlon(i) lt 128.5 $
# and (28.*(xlat(j)+14.5)+14.*(xlon(i)-100.5)) le 14.*28.) $
# or (xlon(i) lt 145.5 and xlat(j) lt -29.5))
)
sahel = Region(
    name='sahel',
    description='African Sahel',
    mask_bounds=[((10, 20), (0, 40)), ((10, 20), (342, 360))],
    land_mask=True
)
sahel2 = Region(
    name='sahel2',
    description='African Sahel w/ longitude bounds 15W-30E',
    mask_bounds=[((10, 20), (0, 30)), ((10, 20), (345, 360))],
    land_mask='strict'
)
sahel3 = Region(
    name='sahel3',
    description=('Western part of African Sahel.  Used by some to '
                 'specify the whole Sahel.'),
    mask_bounds=[((10, 20), (0, 10)), ((10, 20), (340, 360))],
    land_mask=False
)
sahel_north = Region(
    name='sahel_north',
    description='Northern half of African Sahel',
    mask_bounds=[((15, 20), (0, 40)), ((15, 20), (342, 360))],
    land_mask=True
)
sahel_south = Region(
    name='sahel_south',
    description='Southern half of African Sahel',
    mask_bounds=[((10, 15), (0, 40)), ((10, 15), (342, 360))],
    land_mask=True
)
sahel_west = Region(
    name='sahel_west',
    description='Western half of African Sahel',
    mask_bounds=[((10, 20), (0, 11)), ((10, 20), (342, 360))],
    land_mask=True
)
sahel_east = Region(
    name='sahel_east',
    description='Eastern half of African Sahel',
    lat_bounds=(10, 20),
    lon_bounds=(11, 40),
    land_mask=True
)
sahara = Region(
    name='sahara',
    description='African Sahara, as defined by Biasutti et al 2009',
    mask_bounds=[((20, 30), (0, 35)), ((20, 30), (350, 360))],
    land_mask=True
)
ind_monsoon = Region(
    name='ind_monsoon',
    description='Indian monsoon',
    lat_bounds=(10, 30),
    lon_bounds=(60, 100),
    land_mask=False
)
warm_pool = Region(
    name='warm_pool',
    description='Indo-Pacific warm pool. Ocean mask',
    lat_bounds=(-20, 20),
    lon_bounds=(60, 180),
    land_mask='ocean'
)
wpwp = Region(
    name='wpwp',
    description='West Pacific Warm Pool',
    lat_bounds=(-5, 5),
    lon_bounds=(80, 160),
    land_mask=False
)
epac = Region(
    name='epac',
    description='East Pacific cold tongue',
    lat_bounds=(-5, 5),
    lon_bounds=(200, 280),
    land_mask=False
)
epac_watl = Region(
    name='epac_watl',
    description='East Pacific and West Atlantic, including C. and S. America',
    lat_bounds=(0, 15),
    lon_bounds=(240, 300),
    land_mask=False
)
epac_itcz = Region(
    name='epac_itcz',
    description='East Pacific ITCZ for NH summer',
    lat_bounds=(0, 20),
    lon_bounds=(180, 250),
    land_mask=False
)
atl_itcz = Region(
    name='atl_itcz',
    description='Atlantic ITCZ for NH summer',
    lat_bounds=(0, 20),
    lon_bounds=(300, 345),
    land_mask=False
)
burls_wpac = Region(
    name='burls_wpac',
    description='Equatorial W. Pacific region used by Burls and Fedorov 2014',
    lat_bounds=(-8, 8),
    lon_bounds=(130, 205),
    land_mask=False
)
burls_epac = Region(
    name='burls_epac',
    description='Equatorial E. Pacific region used by Burls and Fedorov 2014',
    lat_bounds=(-8, 8),
    lon_bounds=(205, 280),
    land_mask=False
)
burls_pac = Region(
    name='burls_pac',
    description='Pacific region used by Burls and Fedorov 2014',
    mask_bounds=[(( 15, 65), (100, 260)),
                 (( 10, 15), (100, 275)),
                 (( -5, 10), (100, 290)),
                 ((-65, -5), (130, 290))],
    land_mask='strict_ocean'
)
burls_trop_pac = Region(
    name='burls_trop_pac',
    description='Tropical Pacific region used by Burls and Fedorov 2014',
    mask_bounds=[(( -5, 8), (100, 290)),
                 (( -8,  -5), (130, 290))],
    land_mask='strict_ocean'
)
burls_ext_pac = Region(
    name='burls_ext_pac',
    description='Extratropical Pacific region used by Burls and Fedorov 2014',
    mask_bounds=[(( 15, 65), (100, 260)),
                 (( 10, 15), (100, 275)),
                 (( 8, 10), (100, 290)),
                 ((-65, -8), (130, 290))],
    land_mask='strict_ocean'
)
nino1_2 = Region(
    name='nino1_2',
    description='Standard Nino 1+2 regions of equatorial E. Pacific',
    lat_bounds=(-10, 0),
    lon_bounds=(270, 280),
    land_mask=False
)
nino3 = Region(
    name='nino3',
    description='Standard Nino 3 region of equatorial E. Pacific',
    lat_bounds=(-5, 5),
    lon_bounds=(210, 270),
    land_mask=False
)
nino3_4 = Region(
    name='nino3.4',
    description='Standard Nino 3.4 region of equatorial E. Pacific',
    lat_bounds=(-5, 5),
    lon_bounds=(190, 240),
    land_mask=False
)
nino4 = Region(
    name='nino4',
    description='Standard Nino 4 region of equatorial E. Pacific',
    lat_bounds=(-5, 5),
    lon_bounds=(160, 210),
    land_mask=False
)
cld_seed_np = Region(
    name='cld_seed_np',
    description='North Pacific region of Hill & Ming 2012 GRL cloud brightening geoengineering study',
    lat_bounds=(10, 30),
    lon_bounds=(204, 244),
    land_mask='ocean'
)
cld_seed_sp = Region(
    name='cld_seed_sp',
    description='South Pacific region of Hill & Ming 2012 GRL cloud brightening geoengineering study',
    lat_bounds=(-30, -5),
    lon_bounds=(240, 285),
    land_mask='ocean'
)
cld_seed_sa = Region(
    name='cld_seed_sa',
    description='South Atlantic region of Hill & Ming 2012 GRL cloud brightening geoengineering study',
    mask_bounds=[((-30, 5), (0, 12)),
                 ((-30, 5), (342, 360))],
    land_mask='ocean'
)
cld_seed_all = Region(
    name='cld_seed_all',
    description='All 3 regions from Hill & Ming 2012 GRL',
    mask_bounds=[((-30, 5), (0, 12)),
                 ((-30, 5), (342, 360)),
                 ((-30, -5), (240, 285)),
                 ((10, 30), (204, 244))],
    land_mask='ocean'
)
east_asia_monsoon = Region(
    name='east_asia_monsoon',
    description='East Asian Monsoon land region',
    lat_bounds=(22.5, 40),
    lon_bounds=(100, 122.5),
    land_mask=False
)
extrop = Region(
    name='extratropics',
    description='Extratropics (poleward of 30S/N)',
    mask_bounds=[((-90, -30), (0, 360)),
                 ((30, 90), (0, 360))],
    land_mask=False
)
nh_tropics = Region(
    name='nh_tropics',
    description='Northern hemisphere tropics: 0-30N',
    lat_bounds=(0, 30),
    lon_bounds=(0, 360),
    land_mask=False
)
sh_tropics = Region(
    name='sh_tropics',
    description='Southern hemisphere tropics: 30S-0',
    lat_bounds=(-30, 0),
    lon_bounds=(0, 360),
    land_mask=False
)
nh_land = Region(
    name='nh_land',
    description='Northern hemisphere land',
    lat_bounds=(0, 90),
    lon_bounds=(0, 360),
    land_mask=True
)
nh_ocean = Region(
    name='nh_ocean',
    description='Northern hemisphere ocean',
    lat_bounds=(0, 90),
    lon_bounds=(0, 360),
    land_mask='ocean'
)
sh_land = Region(
    name='sh_land',
    description='Southern hemisphere land',
    lat_bounds=(-90, 0),
    lon_bounds=(0, 360),
    land_mask=True
)
sh_ocean = Region(
    name='sh_ocean',
    description='Southern hemisphere ocean',
    lat_bounds=(-90, 0),
    lon_bounds=(0, 360),
    land_mask='ocean'
)
extratrop_land = Region(
    name='extratrop_land',
    description='Extratropical (poleward of 30S/N) land',
    mask_bounds=[((-90, -30), (0, 360)),
                 ((30, 90), (0, 360))],
    land_mask=True
)
extratrop_ocean = Region(
    name='extratrop_ocean',
    description='Extratropical (poleward of 30S/N) ocean',
    mask_bounds=[((-90, -30), (0, 360)),
                 ((30, 90), (0, 360))],
    land_mask='ocean'
)
nh_extratrop = Region(
    name='nh_extratrop',
    description='Northern hemisphere extratropics (30-90N)',
    lat_bounds=(30, 90),
    lon_bounds=(0, 360),
    land_mask=False
)
sh_extratrop = Region(
    name='sh_extratrop',
    description='Southern hemisphere extratropics (90S-30S)',
    lat_bounds=(-90, -30),
    lon_bounds=(0, 360),
    land_mask=False
)
