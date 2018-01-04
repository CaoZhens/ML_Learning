# coding: utf-8
'''
Created on  Jan 04, 2018
@author:
    CaoZhen
@description:
    hyperopt's example 4
@reference:
    1. https://github.com/hyperopt/hyperopt/wiki/FMin 1.3 The Trials Object
'''

import pickle
import time
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials

def objective(x):
    return {
        'loss': x ** 2,
        'status': STATUS_OK,
        'eval_time': time.time(),
        'other_stuff': {'type': None, 'value': [0, 1, 2]},
        'attachments': {'time_module': pickle.dumps(time.time)}
    }

trials = Trials()
best = fmin(objective,
            space = hp.uniform('x', -10, 10),
            algo = tpe.suggest,
            max_evals = 100,
            trials=trials)

print best
print trials.trials[0]
print trials.results[0]
print trials.losses()[0]
print trials.statuses()[0]