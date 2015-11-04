"""Interface with windspharm/spharm for spherical harmonics analyses."""
import logging

from aospy.constants import r_e
import numpy as np
import spharm
import windspharm
import xray

LAT_STR = 'lat'
LON_STR = 'lon'
TIME_STR = 'time'


class SpharmInterface(object):
    """Interface between aospy data and spharm and windspharm packages.

    Windspharm has built-in tools for converting to and from common array
    shapes such as (time, p, lat, lon) to the required (lat, lon, records).
    However, the tools do *not* unmask and then re-mask data.  So need to
    write a wrapper that does that part.  Otherwise can just use the
    package's built-in tools.
    """
    @staticmethod
    def fill_mask(arr, fill_value=0.):
        """Replace masked entries with the specified fill value."""
        arr_filled = arr.to_masked_array()
        arr_filled = np.ma.filled(arr_filled, fill_value=fill_value)
        return xray.DataArray(arr_filled, dims=arr.dims, coords=arr.coords)

    @staticmethod
    def flag_flip_lat(arr, out_north_to_south=True):
        # Input could be xray.DataArray or a numpy array
        try:
            # xray has bugs re: diff-ing coords.  So grab the numpy array.
            lat = arr[LAT_STR].values
        except AttributeError:
            lat = arr
        in_south_to_north = all(lat[1:] - lat[:-1])
        return ((in_south_to_north and out_north_to_south) or
                (not in_south_to_north and not out_north_to_south))

    @classmethod
    def flip_lat_order(cls, arr, out_north_to_south=True):
        """Flip latitude order from S-N to N-S or vice versa, as specified."""
        if cls.flag_flip_lat(arr, out_north_to_south=out_north_to_south):
            logging.debug("Flipping latitude order of: {}".format(arr))
            return arr.isel(**{LAT_STR: slice(-1, None, -1)})
        return arr.copy()

    @staticmethod
    def format_axes_for_spharm(arr):
        """Make numpy array with axes adhering to spharm requirements.

        In particular, lat and lon are the first two axes, respectively, and
        all other axes are collapsed into one.

        Returns a numpy array, *not* an xray.DataArray.
        """
        ax_lat, ax_lon = arr.get_axis_num(LAT_STR), arr.get_axis_num(LON_STR)
        rolled = np.rollaxis(np.rollaxis(arr.copy().values, ax_lat, 0),
                             ax_lon, 1)
        return rolled.reshape(rolled.shape[0], rolled.shape[1], -1)

    @classmethod
    def prep_for_spharm(cls, arr):
        """Prep an array for usage by the spharm/windspharm packages.

        Namely, replace masked values with zeros, flip latitude direction from
        S-N to N-S, combine time and vertical dimensions, and put the remaining
        three dimensions into the order (lat, lon, time&vertical).
        """
        arr_spharm = cls.fill_mask(arr)
        arr_spharm = cls.flip_lat_order(arr_spharm)
        return cls.format_axes_for_spharm(arr_spharm)

    def __init__(self, u, v, gridtype='regular', rsphere=r_e,
                 legfunc='computed'):
        """Create a SpharmInterface object."""
        self._u = u
        self._v = v
        try:
            self.mask = u.mask
        except AttributeError:
            self.mask = False

        self._gridtype = gridtype
        self._rsphere = rsphere
        self._legfunc = legfunc

        self.u = self.prep_for_spharm(self._u)
        self.v = self.prep_for_spharm(self._v)
        self.n_lat, self.n_lon = self.u.shape[:2]

    def make_vectorwind(self):
        self.vectorwind = windspharm.standard.VectorWind(
            self.u, self.v, gridtype=self._gridtype
        )

    def make_spharmt(self):
        try:
            self.spharmt = self.vectorwind.s
        except AttributeError:
            self.spharmt = spharm.Spharmt(
                self.n_lon, self.n_lat, rsphere=self._rsphere,
                gridtype=self._gridtype, legfunc=self._legfunc
            )

    def to_xray(self, ndarray, dropped_dims=[]):
        """Create xray object matching original one from spharm object."""
        # Re-expand collapsed non-lat/lon dims.
        arr_orig = self._u
        ax_lat_orig = arr_orig.get_axis_num(LAT_STR)
        ax_lon_orig = arr_orig.get_axis_num(LON_STR)
        ax_other_dims = set(range(arr_orig.ndim)) - {ax_lat_orig, ax_lon_orig}
        shape_other_dims = [axlen for n, axlen in enumerate(arr_orig.shape)
                            if n in ax_other_dims]
        arr_new = ndarray.reshape([ndarray.shape[0], ndarray.shape[1]] +
                                  shape_other_dims)
        # Return to original axis order.
        arr_new = np.rollaxis(arr_new, 2, 0)
        if arr_orig.ndim == 4:
            arr_new = np.rollaxis(arr_new, -1, 1)
        # Return to original latitude orientation.
        # If the original array got flipped, flip it back.
        if self.flag_flip_lat(arr_orig, out_north_to_south=True):
            arr_new = np.swapaxes(arr_new.swapaxes(ax_lat_orig, 0)[::-1],
                                  ax_lat_orig, 0)
        # Reapply the mask and return to an xray object.
        return xray.DataArray(np.ma.array(arr_new, mask=self.mask),
                              dims=arr_orig.dims, coords=arr_orig.coords)
