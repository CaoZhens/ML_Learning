# coding: utf-8
'''
Created  on Nov 07, 2017
@author:
    CaoZhen
@description:
    split selected feature by step
@reference:
    1. machinelearninginaction Ch07
'''
import numpy as np

def loadSimpleDataSet():
    dataSet = [[ 1. ,  2.1],
               [ 2. ,  1.1],
               [ 1.3,  1. ],
               [ 1. ,  1. ],
               [ 2. ,  1. ]]
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return dataSet, classLabels

if __name__ == '__main__':
    data, label = loadSimpleDataSet()
    dataMat = np.mat(data)
    m, n = np.shape(dataMat)
    
    # functional script
    stepNum = 10.0
    for i in np.arange(n):
        print 'feat Num : %d'%i
        rangeMin = dataMat[:, i].min()
        rangeMax = dataMat[:, i].max()
        step = (rangeMax - rangeMin) / stepNum
        print 'minVal=%f, maxVal=%f, step=%f'%(rangeMin, rangeMax, step)
        threshList = []
        for j in np.arange(-1, int(stepNum)+1):
            threshList.append(rangeMin + float(j)*step)
        print threshList