# coding: utf-8
'''
Created on  Jan 04, 2018
@author:
    CaoZhen
@description:
    hyperopt's example 3
@reference:
    1. 
'''

from hyperopt import hp
space = hp.choice('a',
    [
        ('case 1', 1 + hp.lognormal('c1', 0, 1)),
        ('case 2', hp.uniform('c2', -10, 10))
    ])

# print space
import hyperopt.pyll.stochastic
print hyperopt.pyll.stochastic.sample(space)

def objectiveFunc(args):
    case, val = args
    if case == 'case 1':
        return val
    else:
        return val ** 2

from hyperopt import fmin, tpe
best = fmin(objectiveFunc, space, algo=tpe.suggest, max_evals=500)
print best
print hyperopt.space_eval(space, best)