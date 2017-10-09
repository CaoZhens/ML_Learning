# coding: utf-8
'''
@author:
    CaoZhen
@desc:
    Basic Usage of sklearn.preprocessing.PolynomialFeatures
@reference:
    sklearn's UG - 1.1.16 & 4.3.7
'''
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

X = np.arange(6).reshape(3, 2)
print X

# Features of x have been transformed from [x1 x2] to [1 x1 x2 x1^2 x1x2 x2^2]
print PolynomialFeatures(degree=2).fit_transform(X)

# from [x1 x2] to [1 x1 x2 x1^2 x1x2 x2^2 x1^3 x1^2x2 x1x2^2 x2^3]
print PolynomialFeatures(degree=3).fit_transform(X)

print PolynomialFeatures(interaction_only=True).fit_transform(X)
print PolynomialFeatures(degree=3, interaction_only=True).fit_transform(X)

# In some cases, only interaction terms among features are required, 
# and it can be gotten with the setting interaction_only=True
X = np.arange(9).reshape(3, 3)
print X

print PolynomialFeatures(degree=2, interaction_only=True).fit_transform(X)
print PolynomialFeatures(degree=3, interaction_only=True).fit_transform(X)