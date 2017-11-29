# coding: utf-8
'''
Created on Nov 29, 2017
@author:
    CaoZhen
@description:
    numpy.corrcoef - Normalized covariance matrix
@reference:
    1. Dash - numpy.corrcoef
'''
import numpy as np

# corrcoef
# Return Pearson product-moment correlation coefficients.
# Please refer to the documentation for cov for more detail. The relationship between the correlation coefficient matrix, R, and the covariance matrix, C, is
# R_{ij} = \frac{ C_{ij} } { \sqrt{ C_{ii} * C_{jj} } }
# The values of R are between -1 and 1, inclusive.


x = np.array([0, 1, 2])
y = np.array([2, 1, 0])

print np.cov(x,y)
print np.corrcoef(x,y)