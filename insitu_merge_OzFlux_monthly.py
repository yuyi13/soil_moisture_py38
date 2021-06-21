import pandas as pd
import os

# daily time series
# path_insitu = 'E:/Userdata/yuy/downloads/CDFM/insitu_extract/1_OzFlux_comparison.xlsx'

# monthly time series
path_insitu = 'E:/Userdata/yuy/downloads/insitu_comparison/OzFlux/YearMonth/'
path_satellite = 'E:/Userdata/yuy/downloads/wetness_v3/insitu/OzFlux.csv'

for i in ['AliceSpringsMulga', 'Calperum', 'DalyUncleared', 'DryRiver', 'Gingin', 'GreatWesternWoodlands',
          'HowardSprings', 'RiggsCreek', 'RobsonCreek', 'Samford', 'TiTreeEast', 'Tumbarumba', 'Whroo', 'Yanco']:
    # prepare the insitu dataframe
    filename = i + '.csv'
    # prepare the insitu dataframe
    df = pd.read_csv(path_insitu + filename)
    df = df.drop(index=[0])
    df['YearMonth'] = pd.to_datetime(df.YearMonth)

    # convert the string type time to datetime format
    df1 = pd.read_csv(path_satellite, usecols=['YearMonth', i])
    df1['YearMonth'] = pd.to_datetime(df1.YearMonth, format='%Y%m')

    # merge two dataframes according to the time series
    df = df.merge(df1, on=['YearMonth'], how='left')
    df = df.rename(columns={i: 'TCMerged'})
    df = df.rename(columns={'Sws': 'insitu'})

    df.to_csv(('E:/Userdata/yuy/downloads/wetness_v3/insitu/OzFlux_comparison/'
               + str(i) + '.csv'), index=False)