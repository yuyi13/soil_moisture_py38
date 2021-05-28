# coding=utf-8
import math
import os
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

path = '/g/data/fj4/users/yu/ML_train/test/test_set/'
output = '/g/data/fj4/users/yu/ML_train/test/RMSE.csv'
all_result = []
for file in os.listdir(path):
    if file.endswith('.csv'):
        year = file.split('_')[1]
        month = file.split('_')[2]
        ntree = file.split('=')[1].split('.')[0]
        test_set = 'test_' + year + '_' + month + '_' + ntree
        df = pd.read_csv((path + file), usecols=['SM_true', 'SM_pre'])

        true = df.SM_true
        predict = df.SM_pre

        Score = math.sqrt(mean_squared_error(predict, true))
        result = pd.DataFrame(np.array([Score]), columns=test_set)
        all_result = all_result.append(result)
        all_result = pd.DataFrame(all_result)
        output = all_result.to_csv(output, mode='a')
        print(output)
print("OK")