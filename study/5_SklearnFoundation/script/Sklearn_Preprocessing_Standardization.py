# coding: utf-8
'''
Created on Oct 31, 2017
@author:
    CaoZhen
@description:
    Sklearn Preprocessing Data - Standardization:
    mean removal & variance scaling
@reference:
    1. scikit-learn User Guide 4.3.1
'''

import numpy as np
from sklearn import preprocessing

X = np.array([[ 1., -1.,  2.],
              [ 2.,  0.,  0.],
              [ 0.,  1., -1.]])
      
print X

# 1. Standardization
# 1.1 scale
X_scaled = preprocessing.scale(X)
# Scaled data has zero mean and unit variance
print X_scaled.mean(axis=0)
print X_scaled.std(axis=0)
# scale func realization
print X_scaled
print (X - X.mean(axis=0)) / X.std(axis=0)

# 1.2 StandardScaler
scaler = preprocessing.StandardScaler().fit(X)
print scaler
print scaler.mean_
print scaler.scale_

print scaler.transform(X)

Xtest = [[-1., 1., 0.]]
print scaler.transform(Xtest)


# 1.3 scale to ranges
minmax_scaler = preprocessing.MinMaxScaler().fit(X)
print minmax_scaler.transform(X)
# min_max_scale func realization
# default: [0, 1]
min = 0
max = 1
m, n = np.shape(X)
X_minmax_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
X_minmax_scaled = X_minmax_std * (max - min) + min
print X_minmax_scaled


maxabs_scaler = preprocessing.MaxAbsScaler().fit(X)
print maxabs_scaler.transform(X)
# max_abs_scaler func realization
X_maxabs_scaled = X / np.abs(X.max(axis=0))
print X_maxabs_scaled


# 1.4 scale sparse data
# 1.5 scale data with outliers(异常值)
# robust_scale RobustScaler
