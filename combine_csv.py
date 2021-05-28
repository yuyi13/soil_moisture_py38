import pandas as pd
import os

for i in range(1,11):
    for j in range(1,18):
        path = 'E:/Userdata/yuy/downloads/test_set.v2/v' + str(i) + '/experiment' + str(j) + '/'
        output = 'E:/Userdata/yuy/downloads/test_set.v2/v' + str(i) + '.csv'
        for file in os.listdir(path):
            if file.endswith('.csv'):
                print(file)
                df = pd.read_csv((path + file), header=None)
                df = pd.DataFrame(df)
                df.to_csv(output, mode='a', index=False, header=False)
print("OK")