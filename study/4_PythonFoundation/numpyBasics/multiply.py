# coding: utf-8
'''
Created on Nov 07, 2017
Updated on Nov 08, 2017 / Nov 14, 2017 / Nov 29, 2017
@author:
    CaoZhen
@description:
    1. multiply operation between ndarray & matrix
    2. np.dot / np.multiply / * / **
@reference:
    1. numpy.multiply in Dash
    2. numpy.dot      in Dash
    3. inner product (dot product) description in Baidu Baike [https://baike.baidu.com/item/%E7%82%B9%E7%A7%AF]
    2. http://blog.csdn.net/qq_18433441/article/details/54868889 !
'''

import numpy as np

# 1. np.dot
# Desc:
# a. for 1-D arrays, it is equivalent to inner product of vectors
# comment: inner product equivalent to dot product
print '\n==========1. scalars=========='
a = 2.0
b = 5.0
print 'a =', a, ', b =', b
print 'a * b =', a * b
print 'a ** 2 =', a ** 2
print 'a ** b =', a ** b
print 'np.dot(a, b) =', np.dot(a, b)
print 'np.multiply(a, b) =', np.multiply(a, b)

print '\n==========2. 1-D array=========='
a = np.arange(1, 5)
b = np.arange(2, 6)
print 'a =', a, 'b =', b
print 'a * b =', a * b
print 'a ** 2 =', a ** 2
print 'a ** b =', a ** b 
print 'np.dot(a, b) =', np.dot(a, b)
print 'np.multiply(a, b) =', np.multiply(a, b)
try:
    print 'np.mat(a) * np.mat(b) =', np.mat(a) * np.mat(b)
except Exception, e:
    print e
try:
    print 'np.mat(a) ** 2 =', np.mat(a) ** 2
except Exception, e:
    print e
try:
    print 'np.dot(np.mat(a), np.mat(b)) =', np.dot(np.mat(a), np.mat(b))
except Exception, e:
    print e
print 'np.multiply(np.mat(a), np.mat(b)) =', np.multiply(np.mat(a), np.mat(b))

# b. For 2-D arrays it is equivalent to matrix multiplication
print '\n==========3. 2-D array=========='
a = np.arange(1, 5).reshape(2, -1)
b = np.arange(2, 6).reshape(2, -1)
print 'a =\n', a
print 'b =\n', b
print 'a * b =\n', a * b
print 'a ** 2 =\n', a ** 2
print 'a ** b =\n', a ** b 
print 'np.dot(a, b) =', np.dot(a, b)
print 'np.mat(a) * np.mat(b) =', np.mat(a) * np.mat(b)
print 'np.mat(a) ** 2 =', np.mat(a) ** 2
try:
    print 'np.mat(a) ** np.mat(b) =', np.mat(a) ** np.mat(b)
except Exception, e:
    print e
print 'np.dot(np.mat(a), np.mat(b)) =', np.dot(np.mat(a), np.mat(b))
print 'np.multiply(np.mat(a), np.mat(b)) =', np.multiply(np.mat(a), np.mat(b))
# 2. np.multiply
# Desc    : <ufunc multiply> Multiply arguments element-wise.
# Notes   : Equivalent to x1 * x2 in terms of array broadcasting.
# Comment : ufunc - universal function