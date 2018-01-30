# coding: utf-8
'''
Created on Jan 30, 2018
@author:
    CaoZhen
@description:
    1. stacking
@reference:
    1. 
'''

import numpy as np
from sklearn import datasets
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cross_validation import StratifiedKFold
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier
from sklearn.metrics import roc_auc_score

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt

# create TrainSet
data, target = make_blobs(n_samples=50000, centers=2, random_state=0, cluster_std=0.6)
# plt.scatter(data[:,0], data[:,1], c=target, s=1.0)
# plt.show()

# Base models
clfs = [
    RandomForestClassifier(n_estimators=5, criterion="gini"),
    RandomForestClassifier(n_estimators=5, criterion="entropy"),
    ExtraTreesClassifier(n_estimators=5, criterion="gini"),
    ExtraTreesClassifier(n_estimators=5, criterion="entropy"),
    GradientBoostingClassifier(learning_rate=0.05, subsample=0.6, max_depth=5, n_estimators=5)
]

X, X_pre, y, y_pre = train_test_split(data, target, test_size=0.33, random_state=0)

stacking_train = np.zeros((X.shape[0], len(clfs)))
stacking_test = np.zeros((X_pre.shape[0], len(clfs)))

n_folds = 5
# print StratifiedKFold(y_train, n_folds)
skf = list(StratifiedKFold(y, n_folds, random_state=2018))

# for every base model
for j, clf in enumerate(clfs):
    # base model j's training procedure
    stacking_test_j = np.zeros((X_pre.shape[0], len(clfs)))
    for i, (train, test) in enumerate(skf):
        # cv - part i for predicting, and the other part to training
        X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
        clf.fit(X_train, y_train)
        y_clf_prob = clf.predict_proba(X_test)[:, 1]
        stacking_train[test, j] = y_clf_prob
        stacking_test_j[:, i] = clf.predict_proba(X_pre)[:, 1]
    # print stacking_test_j
    stacking_test[:, j] = stacking_test_j.mean(axis=1)
    print 'base model %d: testSet auc Score = %.6f' % (j,  roc_auc_score(y_pre, stacking_test[:, j]))

# stacking
model = LogisticRegression()
model.fit(stacking_train, y)
model_test_prob = model.predict_proba(stacking_test)[:, 1]
print model_test_prob
# print("Linear stretch of predictions to [0,1]")
# model_test_prob = (model_test_prob - model_test_prob.min()) / (model_test_prob.max() - model_test_prob.min())
# print model_test_prob
print 'stacking result: testSet auc Score = %.6f' % (roc_auc_score(y_pre, model_test_prob))