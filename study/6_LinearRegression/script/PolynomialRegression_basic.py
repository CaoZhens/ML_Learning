# coding: utf-8
'''
Created on Oct 09, 2017
@author: 
    CaoZhen
@desc:
    PolynomialRegression's Basic Foundation including:
    1. PolynomialFeatures
    2. LinearRegression
    3. Pipeline
@reference:
    1. 
'''

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
import numpy as np

# Training Set
x = np.arange(5)
y = 3 - 2*x + x**2 - x**3

# Pipeline
model = Pipeline([('poly', PolynomialFeatures(degree=3)),
                  ('linear', LinearRegression(fit_intercept=False))])

print x
print y
print x.shape 
print np.newaxis
print x[:, np.newaxis]

model.fit(x[:, np.newaxis], y)
print model.named_steps['linear'].coef_

# In some cases it’s not necessary to include higher powers of any single feature, 
# but only the so-called interaction features that multiply together at most d distinct features. 
# These can be gotten from PolynomialFeatures with the setting interaction_only=True.

# For example, when dealing with boolean features, 
# x_i^n = x_i for all n and is therefore useless; 
# but x_i x_j represents the conjunction of two booleans. 
# This way, we can solve the XOR problem with a linear classifier

# Training Set
X = np.array([[0,0], [0,1], [1,0], [1,1]])
print X
# y = xor(x1,x2)
y = X[:, 0] ^ X[:, 1]
print y

# PolynomialFeatures with interaction_only=True

print PolynomialFeatures(interaction_only=True).fit_transform(X)