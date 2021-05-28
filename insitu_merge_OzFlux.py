import pandas as pd
import os

path_insitu = 'E:/Userdata/yuy/downloads/CDFM/insitu_extract/1_OzFlux_comparison.xlsx'
path_satellite = 'E:/Userdata/yuy/downloads/insitu_comparison/experiment8/0_corrected_process/3_in_situ_validation/OzFlux.csv'

for i in ['AliceSpringsMulga', 'Calperum', 'DalyUncleared', 'DryRiver', 'Gingin', 'GreatWesternWoodlands',
          'HowardSprings', 'RiggsCreek', 'RobsonCreek', 'Samford', 'TiTreeEast', 'Tumbarumba', 'Whroo', 'Yanco']:
    # prepare the insitu dataframe
    df = pd.read_excel(path_insitu, sheet_name=str(i), usecols=['Date', 'insitu'])
    df['Date'] = pd.to_datetime(df.Date)

    # convert the string type time to datetime format
    df1 = pd.read_csv(path_satellite, usecols=['Date', str(i)])
    df1['Date'] = pd.to_datetime(df1.Date, format='%Y%m%d')

    # merge two dataframes according to the time series
    df = df.merge(df1, on=['Date'], how='left')
    df = df.rename(columns={str(i): 'fitted_corrected'})

    df.to_csv(('E:/Userdata/yuy/downloads/insitu_comparison/experiment8/0_corrected_process/3_in_situ_validation/OzFlux_comparison/' +
               str(i) + '.csv'), index=False)