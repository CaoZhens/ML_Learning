# coding: utf-8
'''
Created on Dec 14, 2017
@author:
    CaoZhen
@description:
    1. Example 1 of Code Reuse - Data Summary
@reference:
    1. 
'''

import numpy as np
import pandas as pd
filePath = '/Users/fanghan/mlproject/ML_Learning/datasets'


def stripString(xstr):
    xstr_strip = xstr.strip().strip(u'市').strip(u'省')
    if(xstr_strip == ''):
        xstr_strip = np.nan
    return(xstr_strip)

da = pd.read_csv('{}/pf_ld_ex2_from_PPD_FR_TrainSet_Master.csv'.format(filePath),\
        index_col=0, encoding='GB18030', parse_dates=['ListingInfo'], na_values = [-1], 
        converters = dict(zip(*[['UserInfo_{}'.format(i) for i in [2,4,7,8,9,19,20]], [stripString]*7]))
)

# 1. 明确处理单元： 行or列 单or多
# 2. 明确单元处理函数
def Value_counts(das, nhead = 5):
    tmp = pd.value_counts(das).reset_index().rename_axis({'index': das.name}, axis=1)
    value = pd.DataFrame(['value {}'.format(x+1) for x in np.arange(nhead)], index=np.arange(nhead)).join(tmp.iloc[:,0], how='left').set_index(0).T
    freq = pd.DataFrame(['freq {}'.format(x+1) for x in np.arange(nhead)], index=np.arange(nhead)).join(tmp.iloc[:,1], how='left').set_index(0).T
    nnull = das.isnull().sum()
    freqother = pd.DataFrame({das.name: [das.shape[0] - nnull - np.nansum(freq.values), nnull]}, index=['freq others', 'freq NA']).T
    op = pd.concat([value, freq, freqother], axis=1)
    return op

# 3. 单元处理函数调试
print '========单元处理函数调试========'
print Value_counts(da.iloc[:,0])

# 4. 思考处理顺序
print '\n========单元处理函数复用调试========'
print map(lambda i: Value_counts(da.loc[:,i]), da.columns[:2])

# 5. 整合
print '\n========整合调试========'
print pd.concat(map(lambda i: Value_counts(da.loc[:,i]), da.columns[:2]))