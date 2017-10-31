# coding: utf-8
'''
Created on Oct 26, 2017
@author:
    CaoZhen
@description:
    Decision Tree Source Code with CART algorithm
@reference:
    1. machinelearninginaction Ch09
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

'''
Binary Segmentation
'''
def binSplitDataSet(dataMat, featNum, value):
    subDataMat0 = dataMat[np.nonzero(dataMat[:, featNum] > value)[0], :]
    subDataMat1 = dataMat[np.nonzero(dataMat[:, featNum] <= value)[0], :]
    return subDataMat0, subDataMat1

'''
regTree - Calc Leaf Value
'''
def regLeaf(dataMat):
    return np.mean(dataMat[:, -1])

'''
regTree - Calc Error Function
'''
def regErr(dataMat):
    return np.var(dataMat[:, -1]) * np.shape(dataMat)[0]


def linearModel(dataMat):
    m, n = np.shape(dataMat)
    X = np.mat(np.ones(m, n))
    X[:,1:n] = dataMat[:,0:n-1]
    y = dataMat[:, -1]
    xTx = X.T * X
    if np.linalg.det(xTx) == 0.0:
        raise NameError('This matrix is singular. Cannot do inverse.')
    ws = xTx.I * (X.T * y)
    return ws, X, y

'''
modelTree - Calc Leaf Value
'''
def modelLeaf(dataMat):
    ws, X, y = linearModel(dataMat)
    return ws

'''
modelTree - Calc Error Function
'''
def modelErr(dataMat):
    ws, X, y = linearModel(dataMat)
    yhat = X * ws
    return np.sum(power(yhat - y, 2))

'''
Choose the Best feature in Regression Tree
'''
def chooseBestSplit(dataMat, leafFunc, errFunc, threholdOfM, threholdOfL):
    if len(set(dataMat[:, -1].T.tolist()[0])) == 1: 
        return None, leafFunc(dataMat)
    m, n = np.shape(dataMat)
    L = errFunc(dataMat)
    newL = np.inf
    bestL = np.inf
    bestIndex = 0
    bestVal = 0
    for featIndex in np.arange(n-1):
        for splitVal in set(np.asarray(dataMat[:, featIndex]).flatten()):
            subDataMat0, subDataMat1 = binSplitDataSet(dataMat, featIndex, splitVal)
            # if subData's m parameter < threholdofm continue
            if np.shape(subDataMat0)[0] < threholdOfM or np.shape(subDataMat1)[0] < threholdOfM:
                continue
            newL = errFunc(subDataMat0) + errFunc(subDataMat1)
            if newL < bestL:
                bestL = newL
                bestIndex = featIndex
                bestVal = splitVal
    
    # if error's change < threholdOfL
    if (L - newL) < threholdOfL:
        return None, leafFunc(dataMat)
    subDataMat0, subDataMat1 = binSplitDataSet(dataMat, bestIndex, bestVal)
    # 
    if np.shape(subDataMat0)[0] < threholdOfM or np.shape(subDataMat1)[0] < threholdOfM:
        return None, leafFunc(dataMat)
    return bestIndex, bestVal


'''
Create Tree
'''
def createTree(dataMat, leafFunc, errFunc, threholdOfM, threholdOfL):
    # choose the best split
    feat, val = chooseBestSplit(dataMat, leafFunc, errFunc, threholdOfM, threholdOfL)
    if feat == None:
        return val
    retTree = {}
    retTree['spFeat'] = feat
    retTree['spVal'] = val
    ldataMat, rdataMat = binSplitDataSet(dataMat, feat, val)
    retTree['left'] = createTree(ldataMat, leafFunc, errFunc, threholdOfM, threholdOfL)
    retTree['right'] = createTree(rdataMat, leafFunc, errFunc, threholdOfM, threholdOfL)
    return retTree


def isTree(obj):
    return (type(obj).__name__ == 'dict')

def getMean(tree):
    if isTree(tree['left']):
        tree['left'] = getMean(tree['left'])
    if isTree(tree['right']):
        tree['right'] = getMean(tree['right'])
    return (tree['left']+tree['right'])/2.0

'''
Post Pruning
'''
def postPrune(tree, testData):
    if np.shape(testData)[0] == 0:
        return getMean(tree)
    lSet, rSet = binSplitDataSet(testData, tree['spFeat'], tree['spVal'])
    if isTree(tree['left']):
        tree['left'] = postPrune(tree['left'], lSet)
    if isTree(tree['right']):
        tree['right'] = postPrune(tree['right'], rSet)

    if not isTree(tree['left']) and not isTree(tree['right']): # both left & right of tree is not tree (dict type)
        errorNoMerge = sum(np.power(lSet[:, -1]-tree['left'], 2)) + sum(np.power(rSet[:, -1]-tree['right'], 2))
        treeMean = (tree['left'] + tree['right']) / 2.0
        errorMerge = sum(np.power(testData[:, -1]-treeMean, 2))
        if errorMerge < errorNoMerge:
            print 'merging'
            return treeMean
        else:
            return tree
    else:
        return tree


'''
Calc the Depth of regTree
'''
# def getDepth(regTree):
#     maxDepth = 0
#     if isTree(regTree['left']):
#         thisDepth = 1 + getDepth(regTree['left'])
#     if isTree(regTree['right']):
#         thisDepth = 1 + getDepth(regTree['right'])
#     else:
#         thisDepth = 1
#     if thisDepth > maxDepth:
#         maxDepth = thisDepth
#     return maxDepth

if __name__ == '__main__':
    # test
    # dataMat = np.mat(np.eye(4))
    # print dataMat
    # mat0, mat1 = binSplitDataSet(dataMat, 1, 0.5)

    # print mat1


    data1 = loadDataSet('/Users/fanghan/mlproject/ML_Learning/datasets/decisionTree_ex1.txt')
    dataMat1 = np.mat(data1)
    print createTree(dataMat1, regLeaf, regErr, 4, 1)
    
    data3 = loadDataSet('/Users/fanghan/mlproject/ML_Learning/datasets/decisionTree_ex3.txt')
    dataMat3 = np.mat(data3)
    myTree3 = createTree(dataMat3, regLeaf, regErr, 4, 1)
    # when not defined newL: UnboundLocalError: local variable 'newL' referenced before assignment
    print myTree3

    # Post Pruning
    data3test = loadDataSet('/Users/fanghan/mlproject/ML_Learning/datasets/decisionTree_ex3test.txt')
    dataMat3test = np.mat(data3test)
    print postPrune(myTree3, dataMat3test)


    # print createTree(dataMat3, regLeaf, regErr, 4, 1)
    # print dataMat[np.nonzero(dataMat[:, 0] > 0.5)[0], :][0]
    # print set(dataMat[:, -1].T.tolist()[0])


