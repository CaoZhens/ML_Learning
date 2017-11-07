# coding: utf-8
'''
Created  on Nov 06, 2017
@author:
    CaoZhen
@description:
    Adaptive Boosting 
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
    return np.array(dataSet), np.array(classLabels)

# def loadDataSet(fileName):      #general function to parse tab -delimited floats
#     numFeat = len(open(fileName).readline().split('\t')) #get number of fields 
#     dataMat = []; labelMat = []
#     fr = open(fileName)
#     for line in fr.readlines():
#         lineArr =[]
#         curLine = line.strip().split('\t')
#         for i in range(numFeat-1):
#             lineArr.append(float(curLine[i]))
#         dataMat.append(lineArr)
#         labelMat.append(float(curLine[-1]))
#     return dataMat,labelMat

'''
Generate Stump's subFunc: Stump Classify
'''
def stumpClassify(dataMat, dimen, threshVal, threshIneq):
    retMat = np.ones((np.shape(dataMat)[0], 1))
    if threshIneq == 'lt':
        retMat[dataMat[:,dimen] <= threshVal] = -1.0
    else:
        retMat[dataMat[:,dimen] > threshVal] = -1.0
    return retMat

'''
Generate Stump
'''
def buildStump(dataMat, classLabels, D):
    m, n = np.shape(dataMat)
    numSteps = 10.0
    bestStump = {}
    bestClassEst = np.mat(np.zeros((m, 1)))
    minError = np.inf   # init error sum, to +infinity
    for i in np.arange(n):
        rangeMin = dataMat[:, i].min()
        rangeMax = dataMat[:, i].max()
        stepSize = (rangeMax - rangeMin) / numSteps
        for j in np.arange(-1, int(numSteps)+1):  # loop over all range in current dimension
            for inequal in ['lt', 'gt']: # go over less than and greater than
                threshVal = (rangeMin + float(j) * stepSize)
                predictedVals = stumpClassify(dataMat, i, threshVal, inequal) # call stump classify with i, j, lessThan
                error = np.mat(np.ones((m, 1)))
                error[predictedVals == np.mat(classLabels).T] = 0
                weightedError = D.T * error  #calc total error multiplied by D
                # print "split: featNum %d, thresh %.2f, thresh ineqal: %s, the weighted error is %.3f" % (i, threshVal, inequal, weightedError)
                if weightedError < minError:
                    minError = weightedError
                    bestClassEst = predictedVals.copy()
                    bestStump['featNum'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump, minError, bestClassEst

'''
AdaBoost with Decision Stump
'''
def adaBoostWithDS(dataMat, classLabels, numIt=40):
    weakClassArr = []
    m = np.shape(dataMat)[0]
    D = np.mat(np.ones((m, 1)) / m)                                      # init D to all equal
    aggClassEst = np.mat(np.zeros((m, 1)))
    for i in np.arange(numIt):
        bestStump, error, classEst = buildStump(dataMat, classLabels, D)
        # print "D:",D.T
        alpha = float(0.5 * np.log((1.0 - error) / max(error, 1e-16)))   # calc alpha, throw in max(error,eps) to account for error=0
        bestStump['alpha'] = alpha
        weakClassArr.append(bestStump)                                   # store Stump Params in Array
        # print "classLabel: ", classLabels
        # print "classEst: ",classEst.T
        classEstComp = np.multiply(np.mat(classLabels).T, classEst)      # corr:positive, incorr:negative
        # print classEstComp
        expon = -1 * alpha * classEstComp                                # exponent for D calc, getting messy
        D = np.multiply(D, np.exp(expon))                                   # Calc New D for next iteration
        D = D / D.sum()
        # calc training error of all classifiers, if this is 0 quit for loop early (use break)
        aggClassEst += alpha * classEst
        # print "aggClassEst: ",aggClassEst.T
        # print np.sign(aggClassEst) != np.mat(classLabels).T
        aggErrors = np.multiply(np.sign(aggClassEst) != np.mat(classLabels).T, np.ones((m,1)))
        # print aggErrors
        errorRate = aggErrors.sum()/m
        print "total error: ",errorRate
        if errorRate == 0.0: 
            break
    return weakClassArr

# def adaClassify(datToClass,classifierArr):
#     dataMatrix = mat(datToClass)#do stuff similar to last aggClassEst in adaBoostTrainDS
#     m = shape(dataMatrix)[0]
#     aggClassEst = mat(zeros((m,1)))
#     for i in range(len(classifierArr)):
#         classEst = stumpClassify(dataMatrix, classifierArr[i]['dim'],\
#                                  classifierArr[i]['thresh'],\
#                                  classifierArr[i]['ineq'])#call stump classify
#         aggClassEst += classifierArr[i]['alpha']*classEst
#         print aggClassEst
#     return sign(aggClassEst)

# def plotROC(predStrengths, classLabels):
#     import matplotlib.pyplot as plt
#     cur = (1.0,1.0) #cursor
#     ySum = 0.0 #variable to calculate AUC
#     numPosClas = sum(array(classLabels)==1.0)
#     yStep = 1/float(numPosClas); xStep = 1/float(len(classLabels)-numPosClas)
#     sortedIndicies = predStrengths.argsort()#get sorted index, it's reverse
#     fig = plt.figure()
#     fig.clf()
#     ax = plt.subplot(111)
#     #loop through all the values, drawing a line segment at each point
#     for index in sortedIndicies.tolist()[0]:
#         if classLabels[index] == 1.0:
#             delX = 0; delY = yStep
#         else:
#             delX = xStep; delY = 0
#             ySum += cur[1]
#         #draw line from cur to (cur[0]-delX,cur[1]-delY)
#         ax.plot([cur[0],cur[0]-delX],[cur[1],cur[1]-delY], c='b')
#         cur = (cur[0]-delX,cur[1]-delY)
#     ax.plot([0,1],[0,1],'b--')
#     plt.xlabel('False positive rate'); plt.ylabel('True positive rate')
#     plt.title('ROC curve for AdaBoost horse colic detection system')
#     ax.axis([0,1,0,1])
#     plt.show()
#     print "the Area Under the Curve is: ",ySum*xStep

if __name__ == '__main__':
    data, label = loadSimpleDataSet()
    dataMat = np.mat(data)
    m, n = np.shape(dataMat)
    print m, n

    # retArr = np.ones(m)
    # print retArr

    # print retArr[dataMat[:, 0] <= 0.5]

    # D = np.mat(np.ones((m, 1))/5)
    # attention the difference
    # np.ones(m)
    # np.ones((m, 1))
    # buildStump(dataMat, label, D)
    adaBoostWithDS(dataMat, label)