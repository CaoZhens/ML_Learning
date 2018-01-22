# coding: utf-8
'''
Created on Jan 19, 2018
@author:
    CaoZhen
@description:
    xgb origin model for hastie data - basic
@reference:
    1. http://blog.csdn.net/q383700092/article/details/53763328
'''

import xgboost as xgb
from sklearn.datasets import make_hastie_10_2
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time

start_time = time.time()
X, y = make_hastie_10_2(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# 为xgb矩阵赋值
xgb_train = xgb.DMatrix(X_train, label=y_train)
xgb_test = xgb.DMatrix(X_test, label=y_test)

# param
params = {
    'booster': 'gbtree',
    'eta': 0.008,
    'min_child_weight': 3,
    'max_depth': 6,
    'gamma': 0.1,
    'subsample': 0.7,
    'colsample_bytree': 0.7,
    'lambda': 2,
    'seed': 0,
    'silent': 1
}

watchlist = [(xgb_train, 'train'), (xgb_test, 'val')]
# model training
model = xgb.train(params, xgb_train, num_boost_round=100, evals=watchlist)

print 'best best_ntree_limit:', model.best_ntree_limit
y_prob = model.predict(xgb_test, ntree_limit=model.best_ntree_limit)
print y_prob

# print 'Accuracy: %.2f' % accuracy_score(y_test, y_pred)
# print len([1 for i in range(len(y_prob))])
# print len([1 for i in range(len(y_prob)) if int(y_prob[i] > 0.5) != y_test[i]])
# print sum([1 for i in range(len(y_prob)) if int(y_prob[i] > 0.5) != y_test[i]])
# print float(len(y_prob))

# attention: hastie dataset's y in {-1, 1} except {0, 1}
# given transform with y^ = 2 * y - 1
print 'error: %.2f' % (sum([1 for i in range(len(y_prob)) if (2* int(y_prob[i] > 0.5)-1) != y_test[i]]) / float(len(y_test)))
print 'xgb finished, cost time:',  time.time()-start_time, '(seconds)'