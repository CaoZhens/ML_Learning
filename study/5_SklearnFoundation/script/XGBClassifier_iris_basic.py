# coding: utf-8
'''
Created on Jan 19, 2018
@author:
    CaoZhen
@description:
    XGBClassifier for Iris data - basic
@reference:
    1. http://blog.csdn.net/q383700092/article/details/53763328
'''

import pandas as pd
import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=0)
model = xgb.XGBClassifier(
    learning_rate=0.1,
    n_estimators=1000,
    max_depth=5,
    gamma=0,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="binary:logistic",
    seed=0
)
model.fit(X_train, y_train)
test = model.predict(X_test)
print 'Accuracy: %.2f' % accuracy_score(y_test, test)

# feat_importance
feat_imp = pd.Series(model.booster().get_fscore()).sort_values(ascending=False)
print feat_imp

feat_imp.plot(kind='bar', title='Feature Importance')
plt.show()