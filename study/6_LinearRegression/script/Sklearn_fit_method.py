# coding: utf-8
'''
Created on Oct 09, 2017
@author: 
    CaoZhen
@description:
    Sklearn fit method Foundation exampled by LinearRegression
@reference:
'''

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
import numpy as np 


# Training Set - type1 - ndarray
x = np.arange(10)
y = 3 - 2*x
print x
print y

# method 0
# error
try:
    print LinearRegression(fit_intercept=False).fit(x, y).coef_
except Exception, e:
    print Exception, ':', e

# method 1
x = np.arange(10)
y = 3 - 2*x
x.shape = -1, 1
print LinearRegression(fit_intercept=False).fit(x, y).coef_
print LinearRegression(fit_intercept=False).fit(x, y).intercept_

print LinearRegression(fit_intercept=True).fit(x, y).coef_
print LinearRegression(fit_intercept=True).fit(x, y).intercept_

# method 2
# Use x.shape = -1,1 to transform x
# Use PolynomialFeatures to add bias feature
x = np.arange(10)
y = 3 - 2*x
x.shape = -1, 1
X2 = PolynomialFeatures(degree=1).fit_transform(x)
print LinearRegression(fit_intercept=False).fit(X2, y).coef_
'''
    Fit to data, then transform it.
    Fits transformer to X and y with optional parameters fit_params
    and returns a transformed version of X.
        
    Parameters
    ----------
        X : numpy array of shape [n_samples, n_features]
            Training set.
        y : numpy array of shape [n_samples]
            Target values.
    Returns
    -------
        X_new : numpy array of shape [n_samples, n_features_new]
            Transformed array.
'''

# method 3
# Use x,y.shape = -1,1 to transform x,y
# Use PolynomialFeatures to add bias feature
# Use y.ravel()
x = np.arange(10)
y = 3 - 2*x
x.shape = -1, 1
y.shape = -1, 1
X3 = PolynomialFeatures(degree=1).fit_transform(x)
print LinearRegression(fit_intercept=False).fit(X3, y.ravel()).coef_
'''
Fit linear model.
    Parameters
    ----------
        X : numpy array or sparse matrix of shape [n_samples,n_features]
            Training data
        y : numpy array of shape [n_samples, n_targets]
            Target values. Will be cast to X's dtype if necessary
        sample_weight : numpy array of shape [n_samples]
            Individual weights for each sample
            .. versionadded:: 0.17
               parameter *sample_weight* support to LinearRegression.
    Returns
    -------
        self : returns an instance of self.
'''

# method 4
# Use x[:, np.newaxis] to transform x
# Use PolynomialFeatures to add bias feature
x = np.arange(10)
y = 3 - 2*x
X4 = PolynomialFeatures(degree=1).fit_transform(x[:, np.newaxis])
print LinearRegression(fit_intercept=False).fit(X4, y).coef_

# method 5
# Use Pipeline
x = np.arange(10)
y = 3 - 2*x
model = Pipeline([('poly', PolynomialFeatures(degree=1)),
                  ('linear', LinearRegression(fit_intercept=False))])
print model.fit(x[:, np.newaxis], y).named_steps['linear'].coef_