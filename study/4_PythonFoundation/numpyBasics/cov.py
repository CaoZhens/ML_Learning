# coding: utf-8
'''
Created on Nov 29, 2017
@author:
    CaoZhen
@description:
    numpy.cov - Estimate a covariance matrix, given data and weights.
@reference:
    1. Dash - numpy.cov
'''
import numpy as np

# cov

# Covariance indicates the level to which two variables vary together. 
# If we examine N-dimensional samples, X = [x_1, x_2, ... x_N]^T, 
# then the covariance matrix element C_{ij} is the covariance of x_i and x_j. 
# The element C_{ii} is the variance of x_i.

# ex1 : Consider two variables, x_0 and x_1, which correlate perfectly, but in opposite directions:
# m : array_like
# A 1-D or 2-D array containing multiple variables and observations. 
# Each row of m represents a variable, 
# and each column a single observation of all those variables. Also see rowvar below.
    
print '========np.cov example 1========'
x = np.array([0, 1, 2])
y = np.array([2, 1, 0])
print 'x:', x
print 'y:', y
print 'np.cov(x, y):\n', np.cov(x, y)

print '\n========np.cov example 2========'
X = np.array([[0, 2], [1, 1], [2, 0]]).T
print 'X:\n', X
print 'np.cov(X):\n', np.cov(X)