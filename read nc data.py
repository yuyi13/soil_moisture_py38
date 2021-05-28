import netCDF4 as nc
file_path = 'E:/Userdata/yuy/downloads/climate/rain_day_2017.nc'
file_obj = nc.Dataset(file_path)
rain_day = file_obj.variables['time']
print(rain_day)