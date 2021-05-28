# coding=utf-8
import math
import os
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

for j in ['fitted_corrected']:  # 'smap', 'awra', 'cci',
    print(j)
    group = []
    for k in ['Boorowa', 'CosmOz', 'OzFlux', 'OzNet']:
        if k == 'Boorowa':
            file_path = 'E:/Userdata/yuy/downloads/insitu_comparison/experiment8/0_corrected_process/3_in_situ_validation/Boorowa_comparison/'
            for i in [1,2,3,5,6,8,9]:
                df = pd.read_csv((file_path + 'pixel_' + str(i) + '.csv'), usecols=['insitu', str(j)])
                df = df.replace(-9999, np.NaN)
                df = df.dropna()
                insitu = df['insitu']
                SMAP = df[str(j)]

                # RMSE = math.sqrt(mean_squared_error(insitu, SMAP))
                # print(RMSE)
                # MAE = mean_absolute_error(insitu, SMAP)
                # bias = (np.sum(SMAP - insitu)) / len(insitu)
                # print(bias)
                corr = np.corrcoef(insitu, SMAP)
                print((corr)[0, 1])
        elif k == 'CosmOz':
            file_path = 'E:/Userdata/yuy/downloads/insitu_comparison/experiment8/0_corrected_process/3_in_situ_validation/CosmOz_comparison/'
            for i in [2,3,6,7,8,9,10,11,12,13,15,18,19,21]:
                df = pd.read_csv((file_path + 'station' + str(i) + '.csv'), usecols=['SOIL_MOISTURE_percent', str(j)])
                df = df.replace(-9999, np.NaN)
                df = df.dropna()
                insitu = df['SOIL_MOISTURE_percent']
                SMAP = df[str(j)]

                # RMSE = math.sqrt(mean_squared_error(insitu, SMAP))
                # print(RMSE)
                # MAE = mean_absolute_error(insitu, SMAP)
                # bias = (np.sum(SMAP - insitu)) / len(insitu)
                # print(bias)
                corr = np.corrcoef(insitu, SMAP)
                print((corr)[0, 1])
        elif k == 'OzFlux':
            file_path = 'E:/Userdata/yuy/downloads/insitu_comparison/experiment8/0_corrected_process/3_in_situ_validation/OzFlux_comparison/'
            for i in ['AliceSpringsMulga', 'Calperum', 'DalyUncleared', 'DryRiver', 'Gingin', 'GreatWesternWoodlands',
                      'HowardSprings', 'RiggsCreek', 'RobsonCreek', 'Samford', 'TiTreeEast', 'Tumbarumba', 'Whroo', 'Yanco']:
                df = pd.read_csv((file_path + str(i) + '.csv'), usecols=['insitu', str(j)])
                df = df.replace(-9999, np.NaN)
                df = df.dropna()
                insitu = df['insitu']
                SMAP = df[str(j)]

                # RMSE = math.sqrt(mean_squared_error(insitu, SMAP))
                # print(RMSE)
                # MAE = mean_absolute_error(insitu, SMAP)
                # bias = (np.sum(SMAP - insitu)) / len(insitu)
                # print(bias)
                corr = np.corrcoef(insitu, SMAP)
                print((corr)[0, 1])
        elif k == 'OzNet':
            file_path = 'E:/Userdata/yuy/downloads/insitu_comparison/experiment8/0_corrected_process/3_in_situ_validation/OzNet_comparison/'
            for i in ['K6', 'K7', 'K10', 'K11', 'K12', 'K14', 'Y1', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11',
                      'Y12', 'Y13', 'YA1', 'YA3', 'YA4a', 'YA4b', 'YA4c', 'YA4d', 'YA4e', 'YA5', 'YA7a', 'YA7b', 'YA7d',
                      'YA7e', 'YA9', 'YB1', 'YB3', 'YB5a', 'YB5b', 'YB5e', 'YB7a', 'YB7c', 'YB7d', 'YB7e']:
                df = pd.read_csv((file_path + str(i) + '.csv'), usecols=['insitu', str(j)])
                df = df.replace(-9999, np.NaN)
                df = df.dropna()
                insitu = df['insitu']
                SMAP = df[str(j)]

                # RMSE = math.sqrt(mean_squared_error(insitu, SMAP))
                # print(RMSE)
                # MAE = mean_absolute_error(insitu, SMAP)
                # bias = (np.sum(SMAP - insitu)) / len(insitu)
                # print(bias)
                corr = np.corrcoef(insitu, SMAP)
                print((corr)[0, 1])
'''
    for i in ['K6', 'K7', 'K10', 'K11', 'K12', 'K14', 'Y1', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11', 'Y12',
              'Y13', 'YA1', 'YA3', 'YA4a', 'YA4b', 'YA4c', 'YA4d', 'YA4e', 'YA5', 'YA7a', 'YA7b', 'YA7d', 'YA7e',
              'YA9', 'YB1', 'YB3', 'YB5a', 'YB5b', 'YB5e', 'YB7a', 'YB7c', 'YB7d', 'YB7e']:
        # file_path = 'E:/Userdata/yuy/downloads/CDFM/insitu_extract/CCI/CosmOz_validation.xlsx'
        # ['Daly', 'Gnangara', 'Robson', 'Temora', 'Tullochgorum', 'Tumbarumba', 'Weany', 'Yanco', 'Namadgi',
        #  'Hamilton', 'Bishes', 'Bennets', 'Bullawarrie']:

        # file_path = 'E:/Userdata/yuy/downloads/CDFM/insitu_extract/CCI/OzFlux_validation.xlsx'
        # ['AliceSpringsMulga', 'Calperum', 'DalyUncleared', 'DryRiver', 'Gingin', 'GreatWesternWoodlands',
        #  'HowardSprings', 'RiggsCreek', 'RobsonCreek', 'Samford', 'TiTreeEast', 'Tumbarumba', 'Whroo', 'Yanco']:

        file_path = 'E:/Userdata/yuy/downloads/CDFM/insitu_extract/CCI/OzNet_validation.xlsx'
        #
        # file_path = 'E:/Userdata/yuy/downloads/AWRA/AWRA_original/Boorowa.xlsx'
        sheetName = str(i)
        df = pd.read_excel(file_path, sheet_name=sheetName, usecols=['insitu', str(j)])
        df = df.replace(-9999, np.NaN)
        df = df.dropna()
        insitu = df['insitu']
        SMAP = df[str(j)]

        # RMSE = math.sqrt(mean_squared_error(insitu, SMAP))
        # print(RMSE)
        # MAE = mean_absolute_error(insitu, SMAP)
        # bias = (np.sum(SMAP - insitu)) / len(insitu)
        # print(bias)
        corr = np.corrcoef(insitu, SMAP)
        print((corr)[0, 1])

'''