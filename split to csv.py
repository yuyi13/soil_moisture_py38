import numpy as np
import pandas as pd
import os

for i in ['CCI']:
    path = 'E:/Userdata/yuy/downloads/CDFM/' + str(i) + '/' + str(i) + '_CDFM.csv'
    df = pd.read_csv(path)
    time_series_path = 'E:/Userdata/yuy/downloads/CDFM/' + str(i) + '/daily_values/'
    for filename in os.listdir(time_series_path):
        if filename.endswith('.csv'):
            print(filename)

            # create a df for everyday
            df_daily = []
            df_daily = pd.DataFrame(df_daily)

            # get the coordinate for everyday

            pointX = df['POINT_X']
            pointX = np.array(pointX)
            pointY = df['POINT_Y']
            pointY = np.array(pointY)

            # get the pixel values for everyday
            date_value = filename.split('_')[-1].split('.')[0]
            daily_value = df[str(date_value) + '.0']
            value = np.array(daily_value)

            df_daily['POINT_X'] = pointX
            df_daily['POINT_Y'] = pointY
            df_daily['value'] = value
            df_daily.to_csv(('E:/Userdata/yuy/downloads/CDFM/' + str(i) + '/time_series/' + filename),
                            index=False)