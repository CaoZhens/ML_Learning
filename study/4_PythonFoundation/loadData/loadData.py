# coding: utf-8
'''
Created on Oct 27, 2017
@author:
    CaoZhen
@description:
    1. Load Data Difference between Python Standard Library / Numpy / Pandas 
@reference:
    1. 
'''

import numpy as np
import pandas as pd

filePath = '/Users/fanghan/mlproject/ML_Learning/datasets/pf_ld_ex1.txt'

# PSL
data = []
with open(filePath) as f:
    for line in f.readlines():
        curLine = line.strip().split(',')
        data.append(curLine)

print data

# Numpy ndarray
print np.array(data)

# Pandas DataFrame
df = pd.read_table(filePath, header=None, sep=',')
print df