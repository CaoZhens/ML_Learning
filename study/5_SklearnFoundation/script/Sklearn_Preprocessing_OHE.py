# coding: utf-8
'''
Created on Nov 01, 2017
@author:
    CaoZhen
@description:
    Sklearn Preprocessing Data - Encoding categorical features
@reference:
    1. scikit-learn User Guide 4.3.5
'''

from sklearn import preprocessing

data = [[0,0,3], [1,1,0], [0,2,1], [1,0,2]]
enc = preprocessing.OneHotEncoder()
enc.fit(data)
print enc.transform([[0,1,3]]).toarray()