import pandas as pd
import os

path_insitu = 'E:/Userdata/yuy/downloads/insitu_comparison/OzNet/YearMonth/'
path_satellite = 'E:/Userdata/yuy/downloads/wetness_v3/insitu/OzNet.csv'

for i in ['K6', 'K7', 'K10', 'K11', 'K12', 'K14', 'Y1', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11', 'Y12',
          'Y13', 'YA1', 'YA3', 'YA4a', 'YA4b', 'YA4c', 'YA4d', 'YA4e', 'YA5', 'YA7a', 'YA7b', 'YA7d', 'YA7e',
          'YA9', 'YB1', 'YB3', 'YB5a', 'YB5b', 'YB7a', 'YB7c', 'YB7d', 'YB7e']: # 'YB5e',
    # prepare the insitu dataframe
    filename = str.lower(i) + '_2010_2019.csv'
    # prepare the insitu dataframe
    df = pd.read_csv(path_insitu + filename)
    df = df.drop(index=[0])
    df['YearMonth'] = pd.to_datetime(df.YearMonth)

    # convert the string type time to datetime format
    df1 = pd.read_csv(path_satellite, usecols=['YearMonth', i])
    df1['YearMonth'] = pd.to_datetime(df1.YearMonth, format='%Y%m')

    # merge two dataframes according to the time series
    df = df.merge(df1, on=['YearMonth'], how='left')
    df.columns = ['YearMonth', 'insitu', 'TCMerged']

    df.to_csv(('E:/Userdata/yuy/downloads/wetness_v3/insitu/OzNet_comparison/' +
               str(i) + '.csv'), index=False)