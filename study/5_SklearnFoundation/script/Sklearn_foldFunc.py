# coding: utf-8
'''
Created on Jan 25, 2018
@author:
    CaoZhen
@description:
    Sklearn's Fold relevent Function
@reference:
'''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold, StratifiedKFold

def calcBalanceRate(y):
    df = pd.DataFrame(y, columns=['target'])
    return df.target.value_counts() / df.shape[0]

X = np.ones(12)
y = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# print len(X)
# print len(y)
print calcBalanceRate(y)

for i in range(10):
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=i)
    # 上式相当于nfold=3的cv
    # print '---------- Iter %d ----------' % i
    # print 'len of train:', len(y_train), y_train
    # print 'len of test: ', len(y_test), y_test
    # print calcBalanceRate(y_train)
    # print calcBalanceRate(y_test)

# 做实验少不了交叉验证，平时常用from sklearn.model_selection import train_test_split，
# 用train_test_split()函数将数据集分为训练集和测试集，但这样还不够。

# kfold
kf = KFold()
for train_index, test_index in kf.split(X):
    y_train = np.array(y)[train_index]
    y_test = np.array(y)[test_index]
    print 'len of train:', len(y_train), y_train
    print 'len of test: ', len(y_test), y_test
    print calcBalanceRate(y_train)
    print calcBalanceRate(y_test)

# 将样例划分为K份，其中默认为3折交叉验证，2/3作为训练集，1/3作为测试集。

# Stratified k-fold
skf = StratifiedKFold()
for train_index, test_index in skf.split(X, y):
    y_train = np.array(y)[train_index]
    y_test = np.array(y)[test_index]
    print 'len of train:', len(y_train), y_train
    print 'len of test: ', len(y_test), y_test
    print calcBalanceRate(y_train)
    print calcBalanceRate(y_test)
#StratifiedKFold()这个函数较常用，
# 比KFold的优势在于将k折数据按照百分比划分数据集，每个类别百分比在训练集和测试集中都是一样，
# 这样能保证不会有某个类别的数据在训练集中而测试集中没有这种情况，
# 同样不会在训练集中没有全在测试集中，这样会导致结果糟糕透顶。