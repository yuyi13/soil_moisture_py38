# coding=utf-8
import math
import os
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error  # 用于评估模型

for i in range(1,11):
    for j in range(1,18):
        path = 'E:/Userdata/yuy/downloads/test_set.v2/v' + str(i) + '/experiment' + str(j) + \
               '/test_set/'
        output = 'E:/Userdata/yuy/downloads/test_set.v2/v' + str(i) + '/experiment' + str(j) + \
               '/month1.csv'
        all_result = []
        for file in os.listdir(path):
            if file.endswith('1.csv'):
                year = file.split('_')[1]
                date = file.split('_')[2]
                test_set = 'test_' + year + '_' + date
                df = pd.read_csv((path + test_set), usecols=['SM_true', 'SM_pre'])

                true = df.SM_true  # 第二列为真实值
                predict = df.SM_pre  # 第三列为预测值

                Score = math.sqrt(mean_squared_error(predict, true))
                result = np.array(Score)
                all_result.append(result)
        mean_value = np.mean(all_result)
        print(mean_value)
        dataframe = pd.DataFrame(np.array([mean_value]), columns=['mean_value'])
        print(output)
        dataframe.to_csv(output)