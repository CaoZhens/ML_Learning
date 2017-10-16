# coding: utf-8
'''
Created  on Oct 16, 2017
@author:
    CaoZhen
@desc:
    Basic Usage of numpy.stack
@reference:
    
'''

import numpy as np

# ex1
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
print np.stack((a, b))
print np.stack((a, b), axis=-1)

# ex2
arrays = [np.arange(12).reshape(3, 4) for _ in range(10)]
print np.stack(arrays, axis=0).shape
print np.stack(arrays, axis=1).shape
print np.stack(arrays, axis=2).shape
print np.stack(arrays, axis=-1).shape