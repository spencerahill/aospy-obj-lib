from aospy.units import Units
from aospy.constants import c_p, seconds_in_day

unitless = Units(units='')
specific_mass = Units(
    units='',
    plot_units=r'g kg$^{-1}$',
    plot_units_conv=1e3,
    vert_int_plot_units='kg m$^{-2}$',
    vert_int_plot_units_conv=1.
)
K = Units(units='K')
m = Units(units='m')
m2 = Units(units=r'm$^2$')
latlon = Units(units=r'$^\circ$')
W = Units(
    units='W',
    plot_units='PW',
    plot_units_conv=1e-15
)
s = Units(
    units=r's',
    plot_units=r'day',
    plot_units_conv=1. / seconds_in_day
)
s1 = Units(
    units=r's$^{-1}$',
    plot_units=r'day$^{-1}$',
    plot_units_conv=seconds_in_day,
)
s1_vort = Units(
    units=r's$^{-1}$',
    plot_units=r'10$^{-6}$ s$^{-1}$',
    plot_units_conv=1e6
)
K_s1 = Units(
    units=r'K s$^{-1}$',
    vert_int_plot_units=r'W m$^{-2}$',
    vert_int_plot_units_conv=c_p
)
m_s1 = Units(
    units=r'm s$^{-1}$',
    vert_int_units=r'kg m$^{-1}$ s$^{-1}$'
)
m_s2 = Units(
    units=r'm s$^{-2}$',
    vert_int_units=r'kg m$^{-1}$ s$^{-2}$'
)
kg_m2 = Units(
     units=r'kg m$^{-2}$',
)
kg_m2_s1 = Units(
    units=r'kg m$^{-2}$ s$^{-1}$',
    plot_units=r'mm day$^{-1}$',
    plot_units_conv=seconds_in_day
)
# For vertical integrals of divergence.
kg_m2_s1_mass = Units(
    units=r'kg m$^{-2}$ s$^{-1}$',
    plot_units=r'10$^{-2}$ kg m$^{-2}$ s',
    plot_units_conv=1e2
)
kg_s1 = Units(
    units=r'kg s$^{-1}$',
    plot_units=r'kg day$^{-1}$',
    plot_units_conv=seconds_in_day
)
W_m2 = Units(
    units=r'W m$^{-2}$',
    vert_int_units=r''
    )
J_kg1 = Units(
    units=r'J kg$^{-1}$',
    plot_units='K',
    plot_units_conv=1/c_p,
    vert_int_units='J m$^{-2}$',
    vert_int_plot_units='10$^6$ J m$^{-2}$',
    vert_int_plot_units_conv=1e-6
)
J_kg1_s1 = Units(
    units=r'J kg$^{-1}$ s$^{-1}$',
    plot_units='K day$^{-1}',
    plot_units_conv=seconds_in_day / c_p,
    vert_int_units='W m$^{-2}$',
    vert_int_plot_units='W m$^{-2}$',
    vert_int_plot_units_conv=1
)
J_kg1_Pa1 = Units(
    units=r'J kg$^{-1}$ Pa$^{-1}$',
    plot_units='J kg$^{-1}$ hPa$^{-1}',
    plot_units_conv=1e2
)
Pa = Units(
    units=r'Pa',
    plot_units=r'hPa',
    plot_units_conv=1e-2
)
hPa = Units(
    units=r'hPa',
)
Pa_s1 = Units(
    units=r'Pa s$^{-1}$',
    plot_units=r'hPa day$^{-1}$',
    plot_units_conv=24.*3600./100.
)
