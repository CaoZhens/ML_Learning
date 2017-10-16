# coding: utf-8
'''
Created  on Oct 16, 2017
@author:
    CaoZhen
@desc:
    Basic Usage of 
        numpy.chararray.flat
        numpy.chararray.flatten
        numpy.flatiter (class)
        numpy.ravel
@reference:
    
'''

import numpy as np

x = np.arange(1, 7).reshape(2, 3)

print x

try:
    print x[3]
except Exception,e:
    print e

print x.flat[3]

print x.T
print x.T.flat[3]
print type(x.flat)

# flatier
for item in x.flat:
    print item

print x.flat[2:4]


# flatten
a = np.array([[1,2], [3,4]])
print a
print a.flatten()
print a.flatten('F')

# np.ravel
a = np.array([[1,2,3],[4,5,6]])
print a
print a.ravel()
# ravel is equivalent to reshape(-1, order=order)
print a.reshape(-1)