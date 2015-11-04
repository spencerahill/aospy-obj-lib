import xray

from aospy_user import SpharmInterface

path = ('/archive/Spencer.Hill/am2/am2clim_reyoi/gfdl.ncrc2-default-prod/pp/'
        'atmos_level/ts/monthly/1yr/atmos_level.198301-198312.')

# Vertically defined, sigma levels.
u_arr = xray.open_dataset(path + 'ucomp.nc').ucomp
v_arr = xray.open_dataset(path + 'vcomp.nc').vcomp

sphint = SpharmInterface(u_arr, v_arr)
sphint.make_vectorwind()
sphint.make_spharmt()

vort, divg = sphint.vectorwind.vrtdiv()
vort_arr = sphint.to_xray(vort)

# Not vertically defined.
u_arr = u_arr[:,0]
v_arr = v_arr[:,0]

sphint = SpharmInterface(u_arr, v_arr)
sphint.make_vectorwind()
sphint.make_spharmt()

vort, divg = sphint.vectorwind.vrtdiv()
vort_arr = sphint.to_xray(vort)
