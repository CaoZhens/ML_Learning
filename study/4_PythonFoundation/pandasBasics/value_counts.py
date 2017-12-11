# coding: utf-8
'''
Created on Dec 11, 2017
@author:
    CaoZhen
@description:
    1. Usage of pandas.Series.value_counts
@reference:
    1. pandas.Series.value_counts in Dash
'''

import numpy as np
import pandas as pd
filePath = '/Users/fanghan/mlproject/ML_Learning/datasets'

def stripString(xstr):
    xstr_strip = xstr.strip().strip(u'市').strip(u'省')
    if(xstr_strip == ''):
        xstr_strip = np.nan
    return(xstr_strip)

print 'Attention: pandas.Series.value_counts'
da = pd.read_csv('{}/pf_ld_ex2_from_PPD_FR_TrainSet_Master.csv'.format(filePath),\
        index_col=0, encoding='GB18030', parse_dates=['ListingInfo'], na_values = [-1], 
        converters = dict(zip(*[['UserInfo_{}'.format(i) for i in [2,4,7,8,9,19,20]], [stripString]*7]))
)


dac = da.iloc[:,0]
print '\n========{}========'.format(dac.name)
print pd.value_counts(dac).head()
print pd.value_counts(dac).reset_index().head()
print pd.value_counts(dac).reset_index().rename_axis({'index':dac.name}, axis=0).head()
print pd.value_counts(dac).reset_index().rename_axis({'index':dac.name}, axis=1).head()


dac = da.iloc[:,3]
print '\n========{}========'.format(dac.name)
print pd.value_counts(dac).head()
print pd.value_counts(dac).reset_index().head()
print pd.value_counts(dac).reset_index().rename_axis({'index':dac.name}, axis=0).head()
print pd.value_counts(dac).reset_index().rename_axis({'index':dac.name}, axis=1).head()