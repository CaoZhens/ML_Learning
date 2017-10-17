# coding: utf-8
'''
Created on Oct 17, 2017
@author:
    CaoZhen
@description:
    numpy.ndarray.shape (difference between np.array & np.mat)
@reference:
    1. numpy.ndarray.shape in Dash
'''

import numpy as np

a1Arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a1Mat = np.mat(a1Arr)

print a1Arr
print np.shape(a1Arr)

print a1Mat
print np.shape(a1Mat)

a2Arr = np.array([[0, 1, 2, 3, 4],[5, 6 ,7, 8, 9]])
a2Mat = np.mat(a2Arr)

print a2Arr
print np.shape(a2Arr)
print np.shape(a2Mat)

a3Arr = np.arange(10).reshape(2, -1)
a3Mat = np.mat(a2Arr)

print a3Arr
print np.shape(a3Arr)

print a3Mat
print np.shape(a3Mat)