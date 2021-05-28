# coding=utf-8
import math
import xlrd
import os
import pandas as pd
from sklearn.metrics import mean_squared_error  # 用于评估模型

for i in range(1,2):
    path = 'E:/Userdata/yuy/downloads/AWRA/test_set/'
    for file in os.listdir(path):
        if file.endswith('.csv'):

            df = pd.read_csv(path + file)

            predict = df.SM_pre
            true = df.SM_true

            Score = math.sqrt(mean_squared_error(predict, true))
            print('The rmse is', Score)

