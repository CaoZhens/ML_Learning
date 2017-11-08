# coding: utf-8
'''
Created on Nov 07, 2017
Updated on Nov 08, 2017
@author:
    CaoZhen
@description:
    1. multiply operation between ndarray & matrix
    2. np.dot / np.multiply / *
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
a = 2.0
b = 5.0
print 'a =', a, 'b =', b
print 'a * b =', a * b
print 'np.dot(a, b) =', np.dot(a, b)


a = np.arange(1, 5)
b = np.arange(2, 6)
print 'a =', a, 'b =', b
print 'a * b =', a * b
print 'np.dot(a, b) =', np.dot(a, b)
try:
    print 'np.mat(a) * np.mat(b) =', np.mat(a) * np.mat(b)
except Exception, e:
    print e
try:
    print 'np.dot(np.mat(a), np.mat(b)) =', np.dot(np.mat(a), np.mat(b))
except Exception, e:
    print e

# b. For 2-D arrays it is equivalent to matrix multiplication
a = np.arange(1, 5).reshape(2, -1)
b = np.arange(2, 6).reshape(2, -1)
print 'a =', a
print 'b =', b
print 'a * b =', a * b
print 'np.dot(a, b) =', np.dot(a, b)

print 'np.mat(a) * np.mat(b) =', np.mat(a) * np.mat(b)
print 'np.dot(np.mat(a), np.mat(b)) =', np.dot(np.mat(a), np.mat(b))
# 2. np.multiply
# Desc    : <ufunc multiply> Multiply arguments element-wise.
# Notes   : Equivalent to x1 * x2 in terms of array broadcasting.
# Comment : ufunc - universal function

a = np.arange(1, 5)
b = np.arange(2, 6)
print 'a =', a
print 'b =', b
print 'a * b =', a * b
print 'np.dot(a, b) =', np.dot(a, b)
print 'np.multiply(a, b) =', np.multiply(a, b)

try:
    print 'np.mat(a) * np.mat(b) =', np.mat(a) * np.mat(b)
except Exception, e:
    print e
try:
    print 'np.dot(np.mat(a), np.mat(b)) =', np.dot(np.mat(a), np.mat(b))
except Exception, e:
    print e

print 'np.multiply(np.mat(a), np.mat(b)) =', np.multiply(np.mat(a), np.mat(b))
# x1 = np.arange(9.0).reshape((3, 3))
# x2 = np.arange(3.0)
# print x1
# print x2
# # np.multiply(x1, x2)