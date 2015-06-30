from aospy.units import Units
from aospy.constants import c_p, day2sec, sec2day

unitless = Units(units='')
K = Units(units='K')
s=Units(
    units=r's',
    plot=r'day',
    plot_conv=sec2day
)
s1=Units(
    units=r's$^{-1}$',
    plot=r'day$^{-1}$',
    plot_conv=day2sec,
)
K_s1=Units(
    units=r'K s$^{-1}$',
    vert_int_plot=r'W m$^{-2}$',
    vert_int_plot_conv=c_p
)
m_s=Units(
    units=r'm s$^{-1}$',
    vert_int=r'kg m$^{-1}$ s$^{-1}$'
)
m_s2 = Units(
    units=r'm s$^{-2}$',
    vert_int=r'kg m$^{-1}$ s$^{-2}$'
)
kg_m2_s = Units(
    units=r'kg m$^{-2}$ s$^{-1}$',
    plot=r'mm day$^{-1}$',
    plot_conv=day2sec
)
kg_m2_s_mass = Units(           # For vertical integrals of divergence.
    units=r'kg m$^{-2}$ s$^{-1}$',
    plot=r'10$^{-2}$ kg m$^{-2}$ s',    
    plot_conv=1e2
)
W_m2 = Units(
    units=r'W m$^{-2}$',
    vert_int=r''
    )
J_kg1 = Units(
    units=r'J kg$^{-1}$',
    plot='K',
    plot_conv=1/c_p,
    vert_int='J m$^{-2}$',
    vert_int_plot='10$^6$ J m$^{-2}$',
    vert_int_plot_conv=1e-6
)
J_kg1_s1 = Units(
    units=r'J kg$^{-1}$ s$^{-1}$',
    plot='K day$^{-1}',
    plot_conv=day2sec/c_p,
    vert_int='W m$^{-2}$',
    vert_int_plot='W m$^{-2}$',
    vert_int_plot_conv=1
)
Pa=Units(
    units=r'Pa',
    plot=r'hPa',
    plot_conv=1e-2
)
hPa=Units(
    units=r'hPa',
)
