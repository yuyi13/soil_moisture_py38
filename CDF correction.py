import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import pytesmo
from pytesmo import scaling
import os

# quantiles = [0, 2.5, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 97.5, 100]

for i in ['CCI']:
    path1 = 'E:/Userdata/yuy/downloads/CDFM/' + str(i) + '/' + str(i) + '_time_series_T.csv'
    path2 = 'E:/Userdata/yuy/downloads/CDFM/SMAP/SMAP_time_series_T.csv'
    df1 = pd.read_csv(path1)
    df1.replace(-9999, np.nan, inplace=True)
    df2 = pd.read_csv(path2)
    df2.replace(-9999, np.nan, inplace=True)
    print('Dataframe prepared')

    # group = []
    # df = pd.DataFrame(group)
    # df['DATE'] = df1.iloc[:, 0]
    df = pd.read_csv('E:/Userdata/yuy/downloads/CDFM/CCI/time_dimension.csv')
    for j in range(0, 60291):  # full lengthis 0-60290
        src = df1[str(j)].dropna()
        ref = df2[str(j)].dropna()
        if len(~np.isnan(src)) > 100 and len(~np.isnan(ref)) > 100 and np.nanstd(df2[str(j)].values) > 0.0001:
            # src = src.fillna(src.mean()).values
            # not_nan_col = src[src == src]
            # src[np.isnan(src)] = not_nan_col.mean()
            print(j)
            src_cdfm = pytesmo.scaling.lin_cdf_match(src, ref, min_val=None, max_val=None,
                                                     percentiles=[0, 2.5, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 97.5, 100])
            src = pd.DataFrame(src)
            src = src.drop([str(j)], axis=1)
            src[str(j)] = src_cdfm
            src.index.name = 'DATE'
            # src['CDFM'] = src_cdfm
            # src.to_csv('E:/Userdata/yuy/downloads/CDFM/' + str(i) + '/rescaled_df/CCI_pixel_' + str(j) + '.csv')
            # df[str(j)] = src_cdfm
            df = df.merge(src, on=['DATE'], how='left')
    print(df)
    # df = df.T
    # df.columns = df.iloc[0]
    # df = df.drop(df.iloc[0].index.name)
    # print(df)
    # df3.loc[df3['FID'].isin(pointid)] # filter the value in a column using a np.array
    # df.insert(df.shape[1], 'd', 0)

'''
path = 'E:/Userdata/yuy/downloads/CDFM/CCI/rescaled_df/'

for filename in os.listdir(path):
    print(filename)
    pixel = filename.split('_')[-1].split('.')[0]
    df = pd.read_csv(path + filename)
    df = df.drop([str(pixel)], axis=1)
    df = df.rename(columns={'CDFM': str(pixel)})
    df_total = df_total.merge(df, on=['DATE'], how='left')

df_total.to_csv('E:/Userdata/yuy/downloads/CDFM/CCI/CCI_CDFM.csv', index=False)
'''




'''
            A_pdf, edges = np.histogram(A, bins=quantiles)
            A_cdf = np.cumsum(A_pdf) / len(A)
            B_pdf, edges = np.histogram(B, bins=quantiles)
            B_cdf = np.cumsum(B_pdf) / len(B)

            A_dist = stats.gamma(*stats.gamma.fit(A, floc=0))
            B_dist = stats.gamma(*stats.gamma.fit(B, floc=0))

            corrected_quantiles = B_dist.ppf(A_dist.cdf(quantiles[1:]))
            quantile_correction = corrected_quantiles - quantiles[1:]

            print('The above is ok')

            plt.figure()
            # Figure settings
            linewidth = 2
            markeredgewidth = 2
            # Plot sample CDFs
            plt.plot(quantiles[1:], A_cdf, 'x', c='r', markersize=8,
                     markeredgewidth=markeredgewidth, label='Sample A')
            plt.plot(quantiles[1:], B_cdf, '+', c='g', markersize=8,
                     markeredgewidth=markeredgewidth, label='Sample B')
            # Plot fitted CDFs
            plt.plot(quantiles[1:], A_dist.cdf(quantiles[1:]), '-', color='r',
                     linewidth=linewidth, label='Gamma approx. of A')
            plt.plot(quantiles[1:], B_dist.cdf(quantiles[1:]), '-', color='g',
                     linewidth=linewidth, label='Gamma approx. of B')
            # Plot arrows indicating CDF correction
            for q in range(len(quantiles[1:])):
                plt.arrow(quantiles[q + 1], A_dist.cdf(quantiles[q + 1]),
                          quantile_correction[q], 0, length_includes_head=True,
                          head_width=0.03, head_length=2, edgecolor='k', facecolor='k',
                          overhang=1)
            # Add legend, title, and labels
            plt.legend(loc='lower right')
            plt.title('CDF Matching - Making A Look Like B')
            plt.xlabel('Quantile Values (units of sample)')
            plt.ylabel('Probability Density')
            plt.show()
'''