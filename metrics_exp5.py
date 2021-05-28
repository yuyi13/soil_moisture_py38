# coding=utf-8
import math
import os
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

for i in range(1,39):
    # file_path = 'E:/Userdata/yuy/downloads/insitu_comparison/0_monthly_comparison/CosmOz.xlsx'
    # file_path = 'E:/Userdata/yuy/downloads/insitu_comparison/0_monthly_comparison/OzFlux.xlsx'
    file_path = 'E:/Userdata/yuy/downloads/insitu_comparison/0_monthly_comparison/OzNet.xlsx'
    # file_path = 'E:/Userdata/yuy/downloads/insitu_comparison/0_monthly_comparison/Boorowa.xlsx'
    sheetName = str(i)
    df = pd.read_excel(file_path, sheet_name=sheetName, usecols=['insitu', 'exp5'])
    df = df.dropna()
    insitu = (df.insitu)/100
    SMAP = df.exp5

    # RMSE = math.sqrt(mean_squared_error(insitu, SMAP))
    # print(RMSE)
    # MAE = mean_absolute_error(insitu, SMAP)
    bias = (np.sum(SMAP - insitu)) / len(insitu)
    print(bias)
    # corr = np.corrcoef(insitu, SMAP)
    # print((corr)[0, 1])
print("OK")