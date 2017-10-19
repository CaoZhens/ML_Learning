# coding: utf-8

a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
# print a


a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
# print a

# test the splitDataSet(dataset, axis, value) in 8_DecisionTree
a = [1, 2, 3]
b = [4, 5, 6]
dataSet = [a, b]
axis = 0
value = 1
retDataSet = []
for featVec in dataSet: # featVec is 1-D
    print featVec[axis]
    if featVec[axis] == value:
        reducedFeatVec = featVec[:axis] # 前闭后开区间
        print reducedFeatVec
        reducedFeatVec.extend(featVec[axis+1:])
        retDataSet.append(reducedFeatVec)
print retDataSet

# test the chooseBestFeatureToSplit in 8_DecisionTree
numFeatures = len(dataSet[0]) - 1
for i in range(numFeatures):         # iterate over all the features
    featList = [example[i] for example in dataSet]
    print featList
