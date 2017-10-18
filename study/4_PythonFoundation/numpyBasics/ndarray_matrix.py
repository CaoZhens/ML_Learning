# coding: utf-8
'''
Created  on Oct 18, 2017
@author:
    CaoZhen
@description:
    Key Func's difference between numpy.ndarray & numpy.matrixlib.defmatrix.matrix
    1. np.shape
    2. np.sum
@reference:
    
'''

import numpy as np
import tensorflow.examples.tutorials.mnist.input_data as input_data


# Simple 1-D ndarray
xArr = np.arange(10)
yArr = np.ones(10)
print '----- Simple 1-D ndarray -----'
print 'type of xArr :', type(xArr), 'shape of xArr :', np.shape(xArr), 'xArr :\n', xArr
print 'type of yArr :', type(yArr), 'shape of yArr :', np.shape(yArr), 'yArr :\n', yArr
print 'type of xArr.T :', type(xArr.T), 'shape of xArr.T :', np.shape(xArr.T), 'xArr.T :\n', xArr.T
print 'type of yArr.T :', type(yArr.T), 'shape of yArr.T :', np.shape(yArr.T), 'yArr.T :\n', yArr.T
print np.sum(xArr)
print np.sum(xArr, axis=0)
# print np.sum(xArr, axis=1)



xMat = np.mat(xArr)
yMat = np.mat(yArr)
print '----- Simple 1-D mat -----'
print 'type of xMat :', type(xMat), 'shape of xMat :', np.shape(xMat), 'xMat :\n', xMat
print 'type of yMat :', type(yMat), 'shape of yMat :', np.shape(yMat), 'yMat :\n', yMat
print 'type of xMat.T :', type(xMat.T), 'shape of xMat.T :', np.shape(xMat.T), 'xArr.T :\n', xMat.T
print 'type of yMat.T :', type(yMat.T), 'shape of yMat.T :', np.shape(yMat.T), 'yArr.T :\n', yMat.T
print np.sum(xMat)
print np.sum(xMat, axis=0)
print np.sum(xMat, axis=1)

# Simple m-D ndarray
xArr = np.arange(10).reshape(2, -1)
print '----- Simple 2-D ndarray -----'
print 'type of xArr :', type(xArr), 'shape of xArr :', np.shape(xArr), 'xArr :\n', xArr
print 'type of xArr.T :', type(xArr.T), 'shape of xArr.T :', np.shape(xArr.T), 'xArr.T :\n', xArr.T
print np.sum(xArr)
print np.sum(xArr, axis=0)
print np.sum(xArr, axis=1)

xMat = np.mat(xArr)
print '----- Simple 2-D mat -----'
print 'type of xMat :', type(xMat), 'shape of xMat :', np.shape(xMat), 'xMat :\n', xMat
print 'type of xMat.T :', type(xMat.T), 'shape of xMat.T :', np.shape(xMat.T), 'xArr.T :\n', xMat.T
print np.sum(xMat)
print np.sum(xMat, axis=0)
print np.sum(xMat, axis=1)
