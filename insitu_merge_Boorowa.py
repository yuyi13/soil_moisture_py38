import pandas as pd
import os

path_insitu = 'E:/Userdata/yuy/downloads/insitu_comparison/Boorowa/pixel_comparison.v2.xlsx'
path_satellite = 'E:/Userdata/yuy/downloads/insitu_comparison/experiment8/0_corrected_process/3_in_situ_validation/Boorowa.csv'

for i in [1,2,3,5,6,8,9]:
    # prepare the insitu dataframe
    df = pd.read_excel(path_insitu, sheet_name=('pixel' + str(i)), usecols=['Date', 'insitu'])
    df['Date'] = pd.to_datetime(df.Date)

    # convert the string type time to datetime format
    df1 = pd.read_csv(path_satellite, usecols=['Date', str(i)])
    df1['Date'] = pd.to_datetime(df1.Date, format='%Y%m%d')

    # merge two dataframes according to the time series
    df = df.merge(df1, on=['Date'], how='left')
    df = df.rename(columns={str(i): 'fitted_corrected'})

    df.to_csv(('E:/Userdata/yuy/downloads/insitu_comparison/experiment8/0_corrected_process/3_in_situ_validation/Boorowa_comparison/pixel_' +
               str(i) + '.csv'), index=False)