import pandas as pd
import os

path_insitu = 'E:/Userdata/yuy/downloads/insitu_comparison/CosmOz/'
path_satellite = 'E:/Userdata/yuy/downloads/insitu_comparison/experiment8/0_corrected_process/3_in_situ_validation/CosmOz.csv'

for filename in os.listdir(path_insitu):
    if filename.endswith('_output.csv'):
        # print(filename)
        site_number = filename.split('_')[0]
        number = site_number[7:]
        # prepare the insitu dataframe
        df = pd.read_csv(path_insitu + filename)
        df = df.drop(index=[0])
        df['UTC_TIMESTAMP'] = pd.to_datetime(df.UTC_TIMESTAMP)

        # convert the string type time to datetime format
        df1 = pd.read_csv(path_satellite, usecols=['UTC_TIMESTAMP', number])
        df1['UTC_TIMESTAMP'] = pd.to_datetime(df1.UTC_TIMESTAMP, format='%Y%m%d')

        # merge two dataframes according to the time series
        df = df.merge(df1, on=['UTC_TIMESTAMP'], how='left')
        df = df.rename(columns={number: 'fitted_corrected'})

        df.to_csv(('E:/Userdata/yuy/downloads/insitu_comparison/experiment8/0_corrected_process/3_in_situ_validation/CosmOz_comparison/' +
                  site_number + '.csv'), index=False)