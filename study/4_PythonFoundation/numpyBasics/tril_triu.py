# coding: utf-8
'''
Created on  Dec 07, 2017
@author:
    CaoZhen
@description:
    numpy.tril & numpy.triu
@reference:
    1. Dash
'''

import numpy as np

'''
numpy.tril(m, k=0)
Lower triangle of an array.
Return a copy of an array with elements above the k-th diagonal zeroed.

Parameters:	
m : array_like, shape (M, N)
Input array.
k : int, optional
Diagonal above which to zero elements. 
k = 0 (the default) is the main diagonal, 
k < 0 is below it and k > 0 is above.

Returns:	
tril : ndarray, shape (M, N)
Lower triangle of m, of same shape and data-type as m.
'''

arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print arr
print np.tril(arr, k=0)
print np.tril(arr, k=-1)