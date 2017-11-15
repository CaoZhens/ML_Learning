# coding: utf-8
'''
Created on Nov 15, 2017
@author:
    CaoZhen
@description:
    LogisticRegression examples with Horse Colic DataSet in sklearn 
@reference:
    1. 
'''
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report

def loadHorseColic(trainFile, testFile):
    xTrain = []
    yTrain = []
    xTest = []
    yTest = []
    # load Trainning Set
    with open(trainFile) as f:
        for line in f.readlines():
            currLine = line.strip().split('\t')
            lineArr = []
            for i in np.arange(len(currLine)-1):
                lineArr.append(float(currLine[i]))
            xTrain.append(lineArr)
            yTrain.append(float(currLine[-1]))
    # load Test Set
    with open(testFile) as f:
        for line in f.readlines():
            currLine = line.strip().split('\t')
            lineArr = []
            for i in np.arange(len(currLine)-1):
                lineArr.append(float(currLine[i]))
            xTest.append(lineArr)
            yTest.append(float(currLine[-1]))
    return np.array(xTrain), np.array(yTrain), np.array(xTest), np.array(yTest)

if __name__ == '__main__':
    xTrain, yTrain, xTest, yTest = loadHorseColic('/Users/fanghan/mlproject/ML_Learning/datasets/horseColicTraining.txt', '/Users/fanghan/mlproject/ML_Learning/datasets/horseColicTest.txt')
    # print np.shape(xTrain), np.shape(yTrain), np.shape(xTest), np.shape(yTest)
    # dfxTrain = pd.DataFrame(xTrain)
    # print dfxTrain.describe()

    # 1.
    lr1 = LogisticRegression()
    lr1.fit(xTrain, yTrain)
    yHat = lr1.predict(xTrain)
    yHatProb = lr1.predict_proba(xTrain)
    print u'算法1：'
    # print lr1
    print u'训练集准确度：%.2f, %.2f' % (np.mean(yHat == yTrain), lr1.score(xTrain, yTrain))
    print u'测试集准确度：%.2f' % (np.mean(lr1.predict(xTest) == yTest))

    # 2.
    lr2 = Pipeline([
        ('sc', StandardScaler()),
        ('LR', LogisticRegression())
    ])
    lr2.fit(xTrain, yTrain)
    yHat = lr2.predict(xTrain)
    yHatProb = lr2.predict_proba(xTrain)
    print u'\n算法2：'
    # print lr2
    print u'训练集准确度：%.2f' % (np.mean(yHat == yTrain))
    print u'测试集准确度：%.2f, %.2f' % (np.mean(lr2.predict(xTest) == yTest), lr2.score(xTest, yTest))

    # 3.
    XTr, XTe, yTr, yTe = train_test_split(xTrain, yTrain, test_size=0.3, random_state=0)
    lr3 = Pipeline([
        ('sc', StandardScaler()),
        ('LR', LogisticRegression())
    ])
    lr3.fit(XTr, yTr)
    yHat = lr3.predict(XTr)
    print u'\n算法3：'
    # print lr3
    print u'训练集准确度：%.2f' % (np.mean(yHat == yTr)) 
    print u'验证集准确度：%.2f' % (np.mean(lr3.predict(XTe) == yTe)) 
    print u'测试集准确度：%.2f' % (np.mean(lr3.predict(xTest) == yTest))
    # report = classification_report(yTe, yHat)
    # print(report)

    # 4.
    lr4 = Pipeline([
        ('sc', StandardScaler()),
        ('LR', LogisticRegression())
    ])
    parameters = {'LR__C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}

    cv = GridSearchCV(lr4, param_grid=parameters)
    cv.fit(XTr, yTr)
    print u'\n算法4：'
    print cv.best_params_
    print u'训练集准确度：%.2f' % (np.mean(cv.predict(XTr) == yTr)) 
    print u'验证集准确度：%.2f' % (np.mean(cv.predict(XTe) == yTe)) 
    print u'测试集准确度：%.2f' % (np.mean(cv.predict(xTest) == yTest))