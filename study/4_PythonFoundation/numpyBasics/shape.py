# coding: utf-8
'''
Created on Oct 17, 2017
@author:
    CaoZhen
@description:
    1. numpy.ndarray.shape (difference between np.array & np.mat)
    2. review the usage of flatten()/ravel()/newaxis
@reference:
    1. numpy.ndarray.shape in Dash
'''

import numpy as np
aList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print '==========1. list: np.shape(XX) & XX.shape=========='
print aList
print np.shape(aList)
try:
    print aList.shape
except Exception, e:
    print Exception, ':', e

print '==========2. ndarray: np.shape(XX) & XX.shape=========='
a1Arr = np.array(aList)
print a1Arr
print np.shape(a1Arr)
print a1Arr.shape

print '==========3. ndarray(row to col): np.shape(XX) & XX.shape=========='
a1Arr_2 = a1Arr[:, np.newaxis]
print a1Arr_2
print np.shape(a1Arr_2)

print '==========4. ndarray(col to row): np.shape(XX) & XX.shape=========='
a1Arr_3 = a1Arr_2.flatten()
print a1Arr_3
print np.shape(a1Arr_3)

a1Arr_4 = a1Arr_2.ravel()
print a1Arr_4
print np.shape(a1Arr_4)


a1Mat = np.mat(a1Arr)
print 'a1Mat : ', a1Mat
print np.shape(a1Mat)

a1Mat_2 = a1Mat.T
print a1Mat_2
print np.shape(a1Mat_2)

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

# Conclusion
# list / ndarray / mat with1-D row: have different shape results