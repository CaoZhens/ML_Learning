# coding: utf-8
'''
Created on  Jan 04, 2018
@author:
    CaoZhen
@description:
    hyperopt's simplest example
@reference:
    1. https://github.com/hyperopt/hyperopt/wiki/FMin 1.1 The Simplest Case
'''

from hyperopt import fmin, tpe, hp
best = fmin(fn = lambda x: x ** 2,
            space = hp.uniform('x', -5, 5),
            algo = tpe.suggest,
            max_evals = 100)
print best