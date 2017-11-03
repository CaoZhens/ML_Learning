# coding: utf-8
'''
Created on  Nov 03, 2017
@author:
    CaoZhen
@description:
    Key Func's difference between numpy.ndarray & numpy.matrixlib.defmatrix.matrix
    1. slices
@reference:
    1.  
'''

import numpy as np

print '==========1. 1-D slices=========='
x1Arr = np.random.rand(50)
print x1Arr
print x1Arr[:2]

x1Mat = np.mat(x1Arr)
print x1Mat
print x1Mat[:, :2]

print '==========2. 2-D slices=========='
x2Arr = np.random.rand(50).reshape(10, -1)
print x2Arr[:, 2]
print x2Arr[:, 2:4]

x2Mat = np.mat(x2Arr)
print x2Mat[:, 2]
print x2Mat[:, 2:4]

print '==========3. slices & index=========='
print x2Arr[:, 2] >= 0.5
print np.nonzero(x2Arr[:, 2] >= 0.5)
print np.nonzero(x2Arr[:, 2] >= 0.5)[0]
print x2Arr[np.nonzero(x2Arr[:, 2] >= 0.5)[0]]

print x2Mat[:, 2] >= 0.5
print np.nonzero(x2Mat[:, 2] >= 0.5)
print np.nonzero(x2Mat[:, 2] >= 0.5)[0]
print x2Mat[np.nonzero(x2Mat[:, 2] >= 0.5)[0]]