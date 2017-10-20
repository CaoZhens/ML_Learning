# coding: utf-8
'''
Created on Oct 20, 2017
@author:
    CaoZhen
@description:
    Comparation with valuecounts & sort
@reference:
    1. 
'''

import numpy as np
import pandas as pd
import operator

data = ['y', 'y', 'y', 'n', 'n', 'y']
dataArr = np.array(data)
df = pd.DataFrame(data, columns=['class'])

#1
print data
print dataArr
print df

#2
print np.shape(data)
print np.shape(dataArr)
print df.shape

# valuecounts func
# standard lib implementation 标准库实现
# input : list or ndarray
def calcLabelCounts(data):
    labelCounts = {}
    for label in data:
        if label not in labelCounts.keys():
            labelCounts[label] = 0
        labelCounts[label] += 1
    return labelCounts

print calcLabelCounts(data)
print calcLabelCounts(dataArr)
#orderby dict
sortedResult = sorted(calcLabelCounts(dataArr).iteritems(), key=operator.itemgetter(1), reverse=False)
print sortedResult

# pandas.Series.value_counts
print df.ix[:,0].value_counts()
# sort_values
print df.ix[:,0].value_counts().sort_values(ascending=True)