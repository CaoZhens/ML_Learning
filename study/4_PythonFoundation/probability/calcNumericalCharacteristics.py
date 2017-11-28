# coding: utf-8
'''
Created on Oct 31, 2017
Updated on Nov 28, 2017
@author:
    CaoZhen
@description:
    Numerical Characteristics of Random Variables - 随机变量的数字特征
@reference:
    1. machinelearninginaction Ch09 - regErr Func in regTree
'''

import numpy as np
from scipy import stats

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
    print type(y), np.shape(y)

    # 数字特征
    # Calc Mean
    print np.sum(y) / np.shape(y)[0]
    print np.mean(y)

    # Calc Mean Square Error - var
    print np.mean(y.A1**2) - np.mean(y)**2
    print np.mean(np.asarray(y - np.mean(y)) ** 2)
    print np.var(y)

    # Calc std
    print np.sqrt(np.var(y))
    print np.std(y)

    # Calc Sum Square Error
    print np.var(y) * np.shape(y)[0]
    print np.sum(np.asarray(y - np.mean(y)) ** 2)

    # 以上讨论的是单个随机变量
    # 下面讨论多个随机变量（2个）
    N = 10
    x = np.random.rand(N)
    y = 2 * x + np.random.randn(N)
    print x
    print y
    # cov
    print np.mean((x - np.mean(x)) * (y - np.mean(y)))
    print np.cov(x, y, bias=True)[0,1]

    # pearson
    # self defined func
    def calcPearson(x, y):
        std_x = np.std(x)
        std_y = np.std(y)
        cov = np.cov(x, y, bias=True)[0, 1]
        return cov / (std_x * std_y)

    print calcPearson(x, y)
    print stats.pearsonr(x, y)[0]