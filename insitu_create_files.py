import os
import pandas as pd
import numpy as np
from openpyxl import load_workbook

for i in ['OzNet']:  # , ,
    for j in ['K6', 'K7', 'K10', 'K11', 'K12', 'K14', 'Y1', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11', 'Y12',
              'Y13', 'YA1', 'YA3', 'YA4a', 'YA4b', 'YA4c', 'YA4d', 'YA4e', 'YA5', 'YA7a', 'YA7b', 'YA7d', 'YA7e',
              'YA9', 'YB1', 'YB3', 'YB5a', 'YB5b', 'YB5e', 'YB7a', 'YB7c', 'YB7d', 'YB7e']:

    # for j in ['Daly', 'Gnangara', 'Robson', 'Temora', 'Tullochgorum', 'Tumbarumba', 'Weany', 'Yanco', 'Namadgi',
    #                   'Hamilton', 'Bishes', 'Bennets', 'Bullawarrie']:

    # for j in ['AliceSpringsMulga', 'Calperum', 'DalyUncleared', 'DryRiver', 'Gingin', 'GreatWesternWoodlands',
    #               'HowardSprings', 'RiggsCreek', 'RobsonCreek', 'Samford', 'TiTreeEast', 'Tumbarumba', 'Whroo', 'Yanco']:

        # read the data from fitted or satellite soil moisture and the insitu data and build dataframes
        input = 'E:/Userdata/yuy/downloads/CDFM/insitu_extract/CCI/' + str(i) + '.csv'
        exl_file = 'E:/Userdata/yuy/downloads/CDFM/insitu_extract/AWRA/' + str(i) + '_validation.xlsx'

        df1 = pd.read_csv(input, usecols=['date', str(j)])
        df2 = pd.read_excel(exl_file, sheet_name=str(j))
        df2 = df2.merge(df1, on=['date'], how='left')
        df2 = df2.rename(columns={str(j): 'cci_corrected'})
        print(j)

        # df2.to_csv('E:/Userdata/yuy/downloads/CDFM/insitu_extract/weighted_cop/test.csv')
        # write the output data into a single excel file
        output = 'E:/Userdata/yuy/downloads/CDFM/insitu_extract/CCI/' + str(i) + '_validation.xlsx'
        writer = pd.ExcelWriter(output, engine='openpyxl')
        book = load_workbook(writer.path)
        writer.book = book
        df2.to_excel(excel_writer=writer, sheet_name=str(j), index=False)
        writer.save()
        writer.close()