# coding: utf-8
'''
Created  on Oct 19, 2017
Modified on Oct 30, 2017
@author:
    CaoZhen
@description:
    Decision Tree Source Code with ID3 algorithm
@reference:
    1. machinelearninginaction Ch03
'''

from math import log
import operator
import copy

'''
Create Simple DataSet
'''
def createSimpleDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    # feature's label
    labels = ['no surfacing','flippers']
    # change to discrete values
    return dataSet, labels

'''
Calc Shannon Entropy of the DataSet's Label
'''
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet: #the the number of unique elements and their occurance
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    # print labelCounts
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2) #log base 2
    return shannonEnt

'''
Split DataSet with the selected feature
'''
def splitDataSet(dataSet, feaNum, value):
    retDataSet = []
    for line in dataSet:
        if line[feaNum] == value:
            reducedLine = line[:feaNum]     #chop out axis used for splitting # sel the begin : axis
            reducedLine.extend(line[feaNum+1:]) # sel the axis+1:
            retDataSet.append(reducedLine)
    return retDataSet
    
'''
Calc I(Y,Xn) & Choose the best feature split
'''
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1      # the last column is used for the labels
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):         # iterate over all the features
        featList = [line[i] for line in dataSet] # create a list of all the examples of this feature 实际是取列  
        uniqueVals = set(featList)       # get a set of unique values
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet)) # prob of each value of uniqueVals
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy   # calculate the info gain; ie reduction in entropy
        if (infoGain > bestInfoGain):         # compare this to the best gain so far
            bestInfoGain = infoGain           # if better than current best, set to best
            bestFeature = i
    return bestFeature

'''
Vote to the maximum value of yLabel
'''
def majorityCnt(yList):
    valueCount = {}
    for y in yList:
        if y not in valueCount.keys():
            valueCount[y] = 0
        valueCount[y] += 1
    sortedValueCount = sorted(valueCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedValueCount[0][0]

'''
Decision Tree Generation
'''
def createTree(dataSet, labels):
    yList = [line[-1] for line in dataSet]
    if yList.count(yList[0]) == len(yList):
        return yList[0]            # stop splitting when all of the classes are equal
    if len(dataSet[0]) == 1:       # stop splitting when there are no more features in dataSet
        return majorityCnt(yList)
    featLabels = copy.copy(labels) # deep copy
    bestFeatNum = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = featLabels[bestFeatNum]
    myTree = {bestFeatLabel : {}}
    del(featLabels[bestFeatNum])
    featValues = [line[bestFeatNum] for line in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = featLabels[:]  # copy all of labels, so trees don't mess up existing labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeatNum, value),subLabels)
    return myTree

'''
Using DT to Classify TestSet
'''
def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict):
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else: 
        classLabel = valueOfFeat
    return classLabel

def storeTree(inputTree,filename):
    import pickle
    fw = open(filename,'w')
    pickle.dump(inputTree,fw)
    fw.close()
  
def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)

if __name__ == '__main__':
    data, label = createSimpleDataSet()
    trainTree = createTree(data, label)
    print trainTree
    print label
    print classify(trainTree, label, [1, 0])