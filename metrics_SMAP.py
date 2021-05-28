# coding=utf-8
import math
import os
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

for i in range(1,39):
    # file_path = 'E:/Userdata/yuy/downloads/insitu_comparison/0_monthly_comparison/CosmOz.xlsx'
    # file_path = 'E:/Userdata/yuy/downloads/insitu_comparison/0_monthly_comparison/OzFlux.xlsx'
    file_path = 'E:/Userdata/yuy/downloads/insitu_comparison/0_monthly_comparison/OzNet.xlsx'
    # file_path = 'E:/Userdata/yuy/downloads/insitu_comparison/0_monthly_comparison/Boorowa.xlsx'
    sheetName = str(i)
    df = pd.read_excel(file_path, sheet_name=sheetName, usecols=['insitu', 'SMAP_original'])
    df = df.dropna()
    insitu = (df.insitu)/100
    SMAP = df.SMAP_original

    # RMSE = math.sqrt(mean_squared_error(insitu, SMAP))
    # print(RMSE)
    # MAE = mean_absolute_error(insitu, SMAP)
    bias = (np.sum(SMAP - insitu)) / len(insitu)
    print(bias)
    # corr = np.corrcoef(insitu, SMAP)
    # print((corr)[0, 1])
print("OK")

'''
from mlxtend.evaluate import bias_variance_decomp
from sklearn.linear_model import LinearRegression

# split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)
# define the model
model = LinearRegression()
# estimate bias and variance
mse, bias, var = bias_variance_decomp(model, X_train, y_train, X_test, y_test, loss='mse', num_rounds=200, random_seed=1)
# summarize results
print('MSE: %.3f' % mse)
print('Bias: %.3f' % bias)
print('Variance: %.3f' % var)
'''