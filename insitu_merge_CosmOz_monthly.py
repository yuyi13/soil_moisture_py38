import pandas as pd
import os

# daily time series
# path_insitu = 'E:/Userdata/yuy/downloads/insitu_comparison/CosmOz/'

# monthly time series
path_insitu = 'E:/Userdata/yuy/downloads/insitu_comparison/CosmOz/YearMonth/'
path_satellite = 'E:/Userdata/yuy/downloads/wetness_v3/insitu/CosmOz.csv'

for filename in os.listdir(path_insitu):
    if filename.endswith('.csv'):
        # print(filename)
        site_number = filename.split('.')[0]
        number = site_number[7:]
        # prepare the insitu dataframe
        df = pd.read_csv(path_insitu + filename)
        df = df.drop(index=[0])
        df['YearMonth'] = pd.to_datetime(df.YearMonth)

        # convert the string type time to datetime format
        df1 = pd.read_csv(path_satellite, usecols=['YearMonth', number])
        df1['YearMonth'] = pd.to_datetime(df1.YearMonth, format='%Y%m')

        # merge two dataframes according to the time series
        df = df.merge(df1, on=['YearMonth'], how='left')
        df = df.rename(columns={number: 'TCMerged'})

        df.to_csv(('E:/Userdata/yuy/downloads/wetness_v3/insitu/CosmOz_comparison/' +
                  site_number + '.csv'), index=False)