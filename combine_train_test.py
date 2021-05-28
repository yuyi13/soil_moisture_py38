import pandas as pd

for i in range(2017,2021):
    for j in range(1,13):
        df1 = pd.read_csv(('E:/Userdata/yuy/downloads/insitu_comparison/experiment8/test_set/test_'
                          + str(i) + '_' + str(j) + '.csv'))
        df2 = pd.read_csv(('E:/Userdata/yuy/downloads/insitu_comparison/experiment8/test_set/train_'
                          + str(i) + '_' + str(j) + '.csv'))
        df3 = pd.read_csv(('E:/Userdata/yuy/OneDrive_ANU/ML/downloads/train/'
                          + str(i) + '_' + str(j) + '.csv'), usecols=['POINTID', 'POINT_X', 'POINT_Y'])

        print(str(i) + '_' + str(j) + '.csv')
        df = df1.append(df2)
        df = df.sort_values(by=['Unnamed: 0'], ascending=True)
        df = df.drop(['SM_true'], axis=1)
        df = df.rename(columns={'Unnamed: 0': 'POINTID'})
        df = df.merge(df3, on=['POINTID'], how='left')
        df.to_csv(('E:/Userdata/yuy/downloads/insitu_comparison/experiment8/prediction_10km/'
                  + str(i) + '_' + str(j) + '.csv'), index=False)