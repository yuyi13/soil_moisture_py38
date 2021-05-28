import pandas as pd
import os

path_insitu = 'E:/Userdata/yuy/downloads/CDFM/insitu_extract/1_OzNet_comparison.xlsx'
path_satellite = 'E:/Userdata/yuy/downloads/insitu_comparison/experiment8/0_corrected_process/3_in_situ_validation/OzNet.csv'

for i in ['K6', 'K7', 'K10', 'K11', 'K12', 'K14', 'Y1', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11', 'Y12',
          'Y13', 'YA1', 'YA3', 'YA4a', 'YA4b', 'YA4c', 'YA4d', 'YA4e', 'YA5', 'YA7a', 'YA7b', 'YA7d', 'YA7e',
          'YA9', 'YB1', 'YB3', 'YB5a', 'YB5b', 'YB5e', 'YB7a', 'YB7c', 'YB7d', 'YB7e']:
    # prepare the insitu dataframe
    df = pd.read_excel(path_insitu, sheet_name=str(i), usecols=['Date', 'insitu'])
    df['Date'] = pd.to_datetime(df.Date)

    # convert the string type time to datetime format
    df1 = pd.read_csv(path_satellite, usecols=['Date', str(i)])
    df1['Date'] = pd.to_datetime(df1.Date, format='%Y%m%d')

    # merge two dataframes according to the time series
    df = df.merge(df1, on=['Date'], how='left')
    df = df.rename(columns={str(i): 'fitted_corrected'})

    df.to_csv(('E:/Userdata/yuy/downloads/insitu_comparison/experiment8/0_corrected_process/3_in_situ_validation/OzNet_comparison/' +
               str(i) + '.csv'), index=False)