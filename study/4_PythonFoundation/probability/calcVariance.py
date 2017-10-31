# coding: utf-8
'''
Created on Oct 31, 2017
@author:
    CaoZhen
@description:
    Calc Variance
@reference:
    1. machinelearninginaction Ch09 - regErr Func in regTree
'''

import numpy as np

'''
load DataSet
'''
def loadDataSet(fileName):
    data = []
    with open(fileName) as f:
        for line in f.readlines():
            curLine = line.strip().split('\t')
            fltLine = map(float, curLine)
            data.append(fltLine)
    return data

if __name__ == '__main__':
    data = loadDataSet('/Users/fanghan/mlproject/ML_Learning/datasets/decisionTree_ex1.txt')
    dataMat = np.mat(data)
    y = dataMat[:, -1]
    print np.shape(y)

    # Calc Mean Square Error - var
    print np.var(y)
    print np.mean(np.asarray(y - np.mean(y)) ** 2)

    # Calc Sum Square Error
    print np.var(y) * np.shape(y)[0]
    print np.sum(np.asarray(y - np.mean(y)) ** 2)