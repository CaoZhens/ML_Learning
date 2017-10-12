# coding: utf-8
'''
Created on Oct 09, 2017
@author: 
    CaoZhen
@desc:
    1. PolynomialRegression's Example (LinearRegression)
    2. xSS —— coefficents of Determination
@reference:
    1. 9.3.ElasticNet.py
'''

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.exceptions import ConvergenceWarning
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import warnings

''' 
  R2 - coefficient of determination 决定系数
  与均值相比的优秀程度，介于[0~1]。0表示不如均值。1表示完美预测.这个版本的实现是参考scikit-learn官网文档 
  备注：上一行描述抄自网络，描述有误

  Returns the coefficient of determination R^2 of the prediction.
  
  The coefficient R^2 is defined as (1 - u/v), 
  where u is the residual sum of squares ((y_true - y_pred) ** 2).sum() 
  and v is the total sum of squares ((y_true - y_true.mean()) ** 2).sum(). 
  
  The best possible score is 1.0,
  
  and it can be negative (because the model can be arbitrarily worse). 
  
  A constant model that always predicts the expected value of y, disregarding the input features, 
  would get a R^2 score of 0.0.
'''
def R2(y_test, y_true):
    return float(1.0 - ((y_test - y_true)**2).sum() / ((y_true - y_true.mean())**2).sum())
'''
coefficients of determination in Machine Learning
    TSS = SUM[(y - y.mean) ** 2]
    RSS = SUM[(y - yhat) ** 2]
    R^2 = 1 - RSS/TSS
    ESS = SUM[(yhat - y.mean) ** 2]

    TSS >= RSS + ESS

'''
def xSS(y, y_hat):
    y = y.ravel()
    y_hat = y_hat.ravel()
    # print (y - np.mean(y)) ** 2
    # print y_hat
    # Version 1
    TSS = ((y - np.mean(y)) ** 2).sum()     # Total Sum of Squares 
    RSS = ((y_hat - y) ** 2).sum()          # Residual Sum of Squares
    ESS = ((y_hat - np.mean(y)) ** 2).sum() # Explained Sum of Squares
    R2 = 1 - RSS / TSS
    print 'TSS: ', TSS
    print 'RSS: ', RSS
    print 'ESS: ', ESS
    print 'RSS + ESS: ', RSS + ESS
    tssList.append(TSS)
    rssList.append(RSS)
    essList.append(ESS)
    rssessList.append(RSS + ESS)
    # Version 2
    # tss = np.var(y)
    # rss = np.average((y_hat - y) ** 2)
    # r2 = 1 - rss / tss
    # corr_coef = np.corrcoef(y, y_hat)[0, 1]
    return R2


if __name__ == "__main__":
    warnings.filterwarnings(action='ignore', category=ConvergenceWarning) # 不在console显示warning信息
    np.set_printoptions(linewidth=300)
    matplotlib.rcParams['font.sans-serif'] = [u'simHei'] #用来正常显示中文标签
    matplotlib.rcParams['axes.unicode_minus'] = False #用来正常显示负号
    np.set_printoptions(suppress=True)
    
    # Generate Data
    np.random.seed(0)
    N = 9
    x = np.linspace(0, 6, N) + np.random.randn(N)
    x = np.sort(x)
    y = x**2 - 4*x - 3 + np.random.randn(N)
    x.shape = -1, 1
    y.shape = -1, 1
    # print x.ravel()
    # print y.ravel()

    # LinearRegression
    linearR = Pipeline([
        ('poly', PolynomialFeatures()),
        ('linear', LinearRegression(fit_intercept=False))
    ])

    # 阶数
    d_pool = np.arange(1, N, 1)
    m = d_pool.size

    # 图片参数
    clrs = []
    for c in np.linspace(16711680, 255, m):
        clrs.append('#%06x' % c)
    # line_width = np.linspace(5, 2, m)

    # fitting Curve
    fC_PLinearR_png_fig = plt.figure()
    ax = fC_PLinearR_png_fig.add_subplot(111)
    ax.plot(x, y, 'ro', ms=10, zorder=N)
    tssList = []
    rssList = []
    essList = []
    rssessList = []
    for i, d in enumerate(d_pool):
        linearR.set_params(poly__degree = d)
        linearR.fit(x, y.ravel())
        lin = linearR.get_params('linear')['linear']
        output = u'%d阶，系数为：' % (d)
        if hasattr(lin, 'alpha_'):
            idx = output.find(u'系数')
            output = output[:idx] + (u'alpha=%.6f，' % lin.alpha_) + output[idx:]
        if hasattr(lin, 'l1_ratio_'):   # 根据交叉验证结果，从输入l1_ratio(list)中选择的最优l1_ratio_(float)
            idx = output.find(u'系数')
            output = output[:idx] + (u'l1_ratio=%.6f，' % lin.l1_ratio_) + output[idx:]
        print output, lin.coef_.ravel()
        x_hat = np.linspace(x.min(), x.max(), num=100)
        x_hat.shape = -1, 1
        y_hat = linearR.predict(x_hat)
        s = linearR.score(x, y)
        R2 = xSS(y, linearR.predict(x))
        print 'R2和相关系数：', R2
        # print 'R2：', s, '\n'
        z = N - 1 if (d == 2) else 0
        label = u'%d Degree, $R^2$=%.3f' % (d, s)
        ax.plot(x_hat, y_hat, color=clrs[i], lw=2, alpha=0.75, label=label, zorder=z)
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.title('Polynomial Regression', fontsize=14)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.tight_layout(1, rect=(0, 0, 1, 0.95))
    # plt.show()
    fC_PLinearR_png_fig.savefig("/Users/fanghan/Desktop/PolyR_LinearR_fittingCurve.png")
    plt.close(fC_PLinearR_png_fig)


    # xSS Curve
    xSSC_PLinearR_png_fig = plt.figure(facecolor='w')
    t = np.arange(len(tssList))
    plt.plot(t, tssList, 'ro-', lw=2, label=u'TSS(Total Sum of Squares)')
    plt.plot(t, essList, 'mo-', lw=1, label=u'ESS(Explained Sum of Squares)')
    plt.plot(t, rssList, 'bo-', lw=1, label=u'RSS(Residual Sum of Squares)')
    plt.plot(t, rssessList, 'go-', lw=2, label=u'RSS+ESS')
    plt.ylim((0, max(max(tssList), max(rssessList)) * 1.05))
    plt.legend(loc='center right')
    plt.xlabel(u'PolynomialRegression\'s degree')
    plt.ylabel(u'xSS')
    plt.title(u'xSS —— coefficients of Determination', fontsize=14)
    plt.grid(True)
    # plt.show()
    xSSC_PLinearR_png_fig.savefig("/Users/fanghan/Desktop/PolyR_LinearR_xSSCurve.png")
    plt.close(xSSC_PLinearR_png_fig)