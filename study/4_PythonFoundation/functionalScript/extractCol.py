# coding: utf-8
'''
Created on Oct 20, 2017
@author:
    CaoZhen
@description:
    Comparation with extractCol & unique
@reference:
    1. 
'''

import numpy as np
import pandas as pd

data = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
dataArr = np.array(data)
df = pd.DataFrame(data, columns=['f1','f2','class'])

#1
print data
print dataArr
print df

#2
print np.shape(data)
print np.shape(dataArr)
print df.shape

# extract the col
def extractCol(data, featNum):
    # implementation by List Comprehension
    return [line[featNum] for line in data]

print extractCol(data, 0)
print extractCol(dataArr, 0)
print df['f1'].tolist()
# print df['f1'].toarray() # AttributeError: 'Series' object has no attribute 'toarray'

# unique
print set(extractCol(data, 0))
print set(extractCol(dataArr, 0))
print df['f1'].unique()