# coding: utf-8
'''
Created on Oct 27, 2017
Updated on Dec 11, 2017
@author:
    CaoZhen
@description:
    1. Load Data Difference between Python Built-in Function / Numpy / Pandas 
    2. Advanced Usage of Pandas read_csv/read_table
@reference:
    1. 
'''

import numpy as np
import pandas as pd

filePath = '/Users/fanghan/mlproject/ML_Learning/datasets'

# Python Built-in Function
print '========1. Load Data with Python Built-in Function========'
data = []
with open('{}/pf_ld_ex1.txt'.format(filePath)) as f:
    for line in f.readlines():
        curLine = line.strip().split(',')
        data.append(curLine)
print data

# Numpy ndarray
print '\n========2. Load Data with Numpy========'
print np.array(data)

# Pandas DataFrame
print '\n========3. Load Data with Pandas========'
df = pd.read_table('{}/pf_ld_ex1.txt'.format(filePath), header=None, sep=',')
print df

print '\n========4. Advanced Usage of Pandas read_csv/read_table========'

'''
index_col
encoding
parse_dates
na_values
converters
'''

def stripString(xstr):
    xstr_strip = xstr.strip().strip(u'市').strip(u'省')
    if(xstr_strip == ''):
        xstr_strip = np.nan
    return(xstr_strip)

df2 = pd.read_csv('{}/pf_ld_ex2_from_PPD_FR_TrainSet_Master.csv'.format(filePath),\
        index_col=0, encoding='GB18030', parse_dates=['ListingInfo'], na_values = [-1], 
        converters = dict(zip(*[['UserInfo_{}'.format(i) for i in [2,4,7,8,9,19,20]], [stripString]*7]))
)
print df2.head()