import os
import pandas as pd
import numpy as np

path = '/g/data/fj4/SatelliteSoilMoistureProducts/SMAP/global_daily_0.1deg/'
# path = 'E:/Userdata/yuy/OneDrive_ANU/ML/SMAP/2016_nc/'

def save_to_file(file_name, contents):
    fh = open(file_name, 'a')
    fh.write(contents)
    fh.write('\n')
    fh.close()

for filename in os.listdir(path):
    if filename.endswith('.nc'):
        year = int(filename[20:24])
        month = int(filename[24:26])
        day = int(filename[26:28])

        os.system('cdo settunits,days -settaxis,' + str(year) + '-' + str(month) + '-' + str(day) \
                + ',12:00:00,1day /g/data/fj4/users/yu/CDFM_nc/AWRA/' + filename + ' /g/data/fj4/users/yu/CDFM_nc/AWRA_settime/' + filename)


'''
path = '/g/data/fj4/users/yu/ncFiles/'
outPath = '/g/data/fj4/users/yu/ncProjection/'
for filename in os.listdir(path):
    if filename.endswith('.nc'):
        print(filename)
        os.system('gdal_translate -a_srs EPSG:4326 ' + path + filename + ' ' + outPath + filename)
'''
import os
def save_to_file(file_name, contents):
    fh = open(file_name, 'a')
    fh.write(contents)
    fh.write(' ')
    fh.close()

i = 2016 or 2017
pattern = str(i)
root = '/g/data/fj4/users/yu/ncProjection/'
for filename in os.listdir(root):
    if filename.endswith('.nc'):
        filePath = os.path.join(root, filename)
        if os.path.isfile(filePath) and pattern in filename:
            save_to_file('/g/data/fj4/users/yu/test.txt', filename)

# /g/data/fj4/SatelliteSoilMoistureProducts/SMAP/global_daily_0.1deg/annual/SMAP_L2SMP_10km_annual_2020.nc





# 'gdal_translate -a_srs EPSG:4326 SMAP_L2SMP_10km_daily_20210513.nc test.nc'
