# coding: utf-8
'''
Created on Dec 13, 2017
@author:
    CaoZhen
@description:
    1. Usage of pandas.DatetimeIndex
@reference:
    1. pandas.DatetimeIndex in Dash
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

# 调试Time_to_num函数
# 特别注意series与dataframe的切片区别
# 总结：slices：between series and dataframe
# da.loc[:, ictype['date'][0]]
# da.loc[:, ictype['date']]
das = da.loc[:, 'ListingInfo']
# print (das - das.min())[:3]
print (das - das.min())[:3].astype('timedelta64[D]')
tmp = pd.DatetimeIndex(das)
print das[:3]
print tmp[:3]
print tmp[:3].year
print tmp[:3].month
print tmp[:3].day
print tmp[:3].date
print tmp[:3].dayofweek
print tmp[:3].dayofyear

# print pd.DataFrame(dict(zip(*[["{}_{}".format(das.name, i) for i in ["DayDiff", "Year", "DayofYear", "DayofMonth", "DayofWeek"]], 
#                        [(das - das.min()).astype('timedelta64[D]').astype(int), tmp.year, tmp.dayofyear, tmp.day, tmp.dayofweek]])),
#                        index = das.index)
                       
# datime = pd.concat(map(lambda i: Time_to_num(dac.loc[:,i]), ictype['date']), axis = 1)