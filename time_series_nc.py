#!/usr/bin/env python
'''
Convert a bunch of GDAL readable grids to a NetCDF Time Series.
Here we read a bunch of files that have names like:
/usgs/data0/prism/1890-1899/us_tmin_1895.01
/usgs/data0/prism/1890-1899/us_tmin_1895.02
...
/usgs/data0/prism/1890-1899/us_tmin_1895.12
'''

import numpy as np
import datetime as dt
import os
from osgeo import gdal
import netCDF4
import re

ds = gdal.Open('E:/Userdata/yuy/downloads/CDFM/CCI/final_tiff/CCI_ACTIVE_reprojected_10km_Australia_20160101.tif')
a = ds.ReadAsArray()
nlat,nlon = np.shape(a)

b = ds.GetGeoTransform()  # bbox, interval
lon = np.arange(nlon)*b[1]+b[0]
lat = np.arange(nlat)*b[5]+b[3]

basedate = dt.datetime(1900, 1, 1, 0, 0, 0)

# create NetCDF file
nco = netCDF4.Dataset('E:/Userdata/yuy/downloads/CDFM/CCI_combined.nc', 'w', clobber=True)

'''
# chunking is optional, but can improve access a lot:
# (see: http://www.unidata.ucar.edu/blogs/developer/entry/chunking_data_choosing_shapes)
chunk_lon = 16
chunk_lat = 16
chunk_time = 12
'''

# create dimensions, variables and attributes:
nco.createDimension('x_coordinate', nlon)
nco.createDimension('y_coordinate', nlat)
nco.createDimension('time', None)
timeo = nco.createVariable('time', 'f4', ('time'))
timeo.units = 'days since 1900-01-01 00:00:00'
timeo.standard_name = 'time'

lono = nco.createVariable('x_coordinate', 'f4', ('x_coordinate'))
lono.units = 'meter'
lono.standard_name = 'projection_x_coordinate'

lato = nco.createVariable('y_coordinate', 'f4', ('y_coordinate'))
lato.units = 'meter'
lato.standard_name = 'projection_y_coordinate'

# create container variable for CRS: lon/lat WGS84 datum
crso = nco.createVariable('albers_conical_equal_area', 'i4')
crso.long_name = 'albers_conical_equal_area'
crso.grid_mapping_name = 'albers_conical_equal_area'
crso.longitude_of_central_meridian = 132
crso.latitude_of_projection_origin = 0.0
crso.standard_parallel = -18, -36
crso.semi_major_axis = 6378137.0
crso.inverse_flattening = 298.257223563

# create short integer variable for temperature data, with chunking
tmno = nco.createVariable('soil_moisture', 'f4',  ('time', 'y_coordinate', 'x_coordinate'),
   zlib=True)  # , chunksizes=[chunk_time, chunk_lat, chunk_lon], fill_value=-9999
# tmno.units = 'm3/m3'
# tmno.scale_factor = ''
# tmno.add_offset = 0.00
tmno.long_name = 'surface soil moisture'
tmno.standard_name = 'soil_moisture'
tmno.grid_mapping = 'albers_conical_equal_area'
tmno.set_auto_maskandscale(False)

nco.Conventions = 'CF-1.0'

#  write lon,lat
lono[:] = lon
lato[:] = lat

pat = re.compile('CCI_ACTIVE_reprojected_10km_Australia_[0-9]{8}.tif')
itime = 0

#  step through data, writing time and data to NetCDF
for root, dirs, files in os.walk('E:/Userdata/yuy/downloads/CDFM/CCI/final_tiff/'):
    dirs.sort()
    files.sort()
    for f in files:
        if f.endswith('.tif'):
            if re.match(pat, f):
                # read the time values by parsing the filename
                year = int(f[38:42])
                mon = int(f[42:44])
                day = int(f[44:46])
                date = dt.datetime(year, mon, day, 0, 0, 0)
                print(date)
                dtime = (date - basedate).total_seconds() / 86400.
                timeo[itime] = dtime
                # soil moisture value
                sm_path = os.path.join(root, f)
                print(sm_path)
                sm = gdal.Open(sm_path)
                a = sm.ReadAsArray()  # data
                tmno[itime, :, :] = a
                itime = itime + 1
nco.close()