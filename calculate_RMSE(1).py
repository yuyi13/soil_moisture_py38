# coding=utf-8
import math
import xlrd
import os
import pandas as pd
from sklearn.metrics import mean_squared_error  # 用于评估模型

for n in range(2,3):
    path = 'E:/Userdata/yuy/downloads/southeast_test/test' + str(n) + '/test_set/'
    for file in os.listdir(path):
        if file.endswith('.csv'):
            year = file.split('_')[1]
            date = file.split('_')[2]
            test_set = 'test_' + year + '_' + date
            df = pd.read_csv((path + test_set), usecols=['SM_true', 'SM_pre'])

            true = df.SM_true  # 第二列为真实值
            predict = df.SM_pre  # 第三列为预测值

            Score = math.sqrt(mean_squared_error(predict, true))
            print(Score)