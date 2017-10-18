# coding: utf-8
'''
Created  on Oct 10, 2017
Modified on Oct 11, 2017d
@author:
    CaoZhen
@description:
    LogisticRegression solved by Batch/Stochastic Gradient Descent
@reference:
    1. machinelearninginaction Ch05
'''

import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import animation
import matplotlib.ticker as mtick
from time import sleep

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

import copy
import json
import urllib2

'''
Load DataSet(2 targets)

'''
def loadDataSet(filename):
    x = []
    y = []
    with open(filename) as f:
        for line in f.readlines():
            lineArr = line.strip().split()
            x.append([1.0, float(lineArr[0]), float(lineArr[1])])
            y.append(int(lineArr[2]))
    return np.array(x), np.array(y)

'''
Load Iris(3 targets)
Args:
    null
Return:
    X - np.mat (m * 2)
    y - np.mat (n * 1)
'''
def loadIris():
    iris = load_iris()
    X = iris.data[:, :2]
    y = iris.target
    return X, y

'''
Sigmoid Function
'''
def Sigmoid(X, theta):
    return 1.0/(1 + np.exp(-X * theta))

'''
Loss Function

'''
def J(X, y, theta):
    m, n = np.shape(X)
    return float((1.0/(2*m)) * (X*theta - y).T * (X*theta - y))

'''
Log likelihood Function

'''
def l(X, y, theta):
    return float((y.T * (1.0 - Sigmoid(X, theta))) + ((y - 1.0).T * Sigmoid(X, theta)))

'''
Batch Gradient Descent

'''
def batchGD(X, y, alpha, maxCycles):
    m, n = np.shape(X)
    theta = np.ones((n,1))
    history_error = []
    history_theta = []
    for k in range(maxCycles):
        # h = X * theta
        h = Sigmoid(X, theta)
        theta_pre = copy.copy(theta)
        theta -= alpha * X.T * (h - y) / m
        # error = J(X, y, theta)
        error = l(X, y, theta)
        history_error.append(copy.copy(error))
        history_theta.append(copy.copy(theta))
        # if np.linalg.norm(theta - theta_pre) < 0.001:
        #     break
    return theta, history_error, history_theta

'''
Stochastic Gradient Descent
备注：
    1. 迭代式不再除以m 
    2.样本数较少时一次遍历可能不够 
    3. 为了保证迭代次数与BGD一致，暂时设置maxLoops=3（199个样本点）
'''
def stoGD(X, y, alpha, maxLoops):
    m, n = np.shape(X)
    theta = np.ones((n,1))
    history_error = []
    history_theta = []
    count = 0
    while count < maxLoops:
        count += 1
        for k in range(m):
            h = Sigmoid(X[k], theta)
            theta -= alpha * X[k].T * (h - y[k])
            error = l(X, y, theta)
            history_error.append(copy.copy(error))
            history_theta.append(copy.copy(theta))
    return theta, history_error, history_theta


# with animation
xArr, yArr = loadDataSet('/Users/fanghan/mlproject/ML_Learning/datasets/testSet.txt')
xMat = np.mat(xArr)
yMat = np.mat(yArr).T

theta, errors, thetas = batchGD(xMat, yMat, 0.1, 1000)
theta2, errors2, thetas2 = stoGD(xMat, yMat, 0.1, 10)
print np.shape(xMat)
print len(thetas)
print len(thetas2)
# print errors
# lstheta = leastSquareMethod(X, y)

# fitting Curve png
fC_2methods_png_fig = plt.figure()
ax = fC_2methods_png_fig.add_subplot(111)
# Plot also the training points
ax.scatter(xArr[:, 1], xArr[:, 2], c=yArr, edgecolors='k', cmap=mpl.colors.ListedColormap(['r', 'g', 'b']))
x = np.arange(-4.0, 4.0, 0.1)
# y_bgd = theta[0][0] + theta[1][0] * x
# y_sgd = theta2[0][0] + theta2[1][0] * x
y_bgd = -(theta[0][0] + theta[1][0] * x) / theta[2][0]
y_sgd = -(theta2[0][0] + theta2[1][0] * x) / theta2[2][0]
ax.plot(x, y_bgd, 'm', lw=1.0, label='fitting Curve by BGD')
ax.plot(x, y_sgd, 'g', lw=1.0, label='fitting Curve by SGD')
ax.legend()
plt.title('Logistic Regression')
# plt.grid(True)
# plt.show()
fC_2methods_png_fig.savefig("/Users/fanghan/Desktop/LogisticR_2methods_FittingCurve.png")
# 备注：用双引号就可以，单引号不行，为什么？
plt.close(fC_2methods_png_fig)


# fitting Curve gif
# bgd & sgd
fC_gd_gif_fig = plt.figure()
ax = fC_gd_gif_fig.add_subplot(111)
line1, = ax.plot([], [], 'r', lw=2.0, label='Batch Gradient Descent')
line2, = ax.plot([], [], 'g', lw=2.0, label='Stochastic Gradient Descent')
ax.legend()
plt.title('Logistic Regression solved by Gradient Descent')
plt.grid(True)

def drawLine1(theta):
    x = np.arange(-4.0, 4.0, 0.1)
    # y = theta[0][0] + theta[1][0] * x
    y = -(theta[0][0] + theta[1][0] * x) / theta[2][0]
    line1.set_data(x,y)
    return line1,

def drawLine2(theta):
    x = np.arange(-4.0, 4.0, 0.1)
    # y = theta[0][0] + theta[1][0] * x
    y = -(theta[0][0] + theta[1][0] * x) / theta[2][0]
    line2.set_data(x,y)
    return line2,

def init():
    m, n = np.shape(xMat)
    ax = fC_gd_gif_fig.add_subplot(111)
    # ax.scatter(X[:,1], y, s=30, c='b', alpha=0.5)
    ax.scatter(xArr[:, 1], xArr[:, 2], c=yArr, edgecolors='k', cmap=mpl.colors.ListedColormap(['r', 'g', 'b']))
    drawLine1(np.ones((n,1)))
    drawLine2(np.ones((n,1)))
    return

def animate(i):
    drawLine1(thetas[i])
    drawLine2(thetas2[i])
    return

anim = animation.FuncAnimation(fC_gd_gif_fig, animate, init_func=init,
                                frames=len(thetas),
                                interval=20,
                                repeat=True,
                                blit=False
                                )

# plt.show()
anim.save('/Users/fanghan/Desktop/LogisticR_GD_FittingCurve.gif', writer='imagemagick', fps=50)
plt.close(fC_gd_gif_fig)


# 绘制lossfunc曲线 
# 实际上是似然函数的导数
# ? 为什么一开始的几个数是负值？
lfC_gd_png_fig = plt.figure(figsize=(8,18))
ax1 = lfC_gd_png_fig.add_subplot(211)
ax1.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.4f'))
ax1.plot(range(len(errors)), errors, 'r', label='Batch Gradient Descent')
ax1.set_xlabel('Number of iterations')
ax1.set_ylabel('J')
ax1.grid(True)
ax2 = lfC_gd_png_fig.add_subplot(212)
ax2.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.4f'))
ax2.plot(range(len(errors2)), errors2, 'g', label='Stochastic Gradient Descent')
ax2.set_xlabel('Number of iterations')
ax2.set_ylabel('J')
ax2.grid(True)
plt.legend()
# plt.title('Loss Function')
plt.show()
# lfC_gd_png_fig.savefig("/Users/fanghan/Desktop/LinearR_GD_LossFunc.png")
# plt.close(lfC_gd_png_fig)


# 绘制lossfunc曲面
# size = 200
# theta0Vals = np.linspace(-4, 5, size)
# theta1Vals = np.linspace(-4, 5, size)
# JVals = np.zeros((size, size))
# for i in range(size):
#     for j in range(size):
#         col = np.mat([[theta0Vals[i]], [theta1Vals[j]]])
#         JVals[i, j] = J(X, y, col)
# # print JVals
# # print JVals.shape
# # print np.meshgrid(theta0Vals, theta1Vals)

# theta0Vals, theta1Vals = np.meshgrid(theta0Vals, theta1Vals)
# JVals = JVals.T

# lfS_gd_png_fig = plt.figure()
# ax = lfS_gd_png_fig.gca(projection='3d')
# ax.plot_surface(theta0Vals, theta1Vals, JVals,  rstride=2, cstride=2, alpha=0.3,
#                 cmap=cm.rainbow, linewidth=0, antialiased=False)
# ax.plot(theta[0], theta[1], 'bx', label='Solution by BGD')
# ax.plot(theta2[0], theta2[1], 'gs', label='Solution by SGD')
# ax.plot(lstheta[0], lstheta[1], 'ro', label='Solution by Least Square Method')
# ax.set_xlabel(r'$\theta_0$')
# ax.set_ylabel(r'$\theta_1$')
# ax.set_zlabel(r'$J(\theta)$')
# ax.legend(loc='best')
# plt.grid(True)
# # plt.show()
# lfS_gd_png_fig.savefig("/Users/fanghan/Desktop/LinearR_GD_LossFuncSurface.png")
# plt.close(lfS_gd_png_fig)


# 绘制lossfunc BGD gif
# lfS_gd_gif_fig = plt.figure()
# ax = Axes3D(lfS_gd_gif_fig)
# plt.grid(True)

# # create lossfunc Surf
# ax.plot_surface(theta0Vals, theta1Vals, JVals,
#     rstride=2, cstride=2, alpha=0.3, cmap=cm.rainbow, linewidth=0, antialiased=False)
# ax.plot(lstheta[0], lstheta[1], J(X, y, lstheta), 'ro', label='Best Solution by Least Square Method')

# # create the initial plot
# point1, = ax.plot(thetas[0][0], thetas[0][1], J(X, y, thetas[0]), 'b.', lw=0.5, label='BGD Solution per Iteration')
# point2, = ax.plot(thetas2[0][0], thetas2[0][1], J(X, y, thetas2[0]), 'g.', lw=0.5, label='SGD Solution per Iteration')
# ax.legend()

# # move the point position at every frame
# def animate(i, thetas, thetas2, point1, point2):
#     xVal1 = []
#     yVal1 = []
#     jVal1 = []
#     xVal2 = []
#     yVal2 = []
#     jVal2 = []
#     # 如何快速将list中的array写成np.array ?
#     for index in range(i+1):
#         xVal1.append(float(thetas[index][0]))
#         yVal1.append(float(thetas[index][1]))
#         jVal1.append(J(X, y, thetas[index]))
#         xVal2.append(float(thetas2[index][0]))
#         yVal2.append(float(thetas2[index][1]))
#         jVal2.append(J(X, y, thetas2[index]))
#     point1.set_data(np.array(xVal1), np.array(yVal1))
#     point1.set_3d_properties(np.array(jVal1), 'z')
#     point2.set_data(np.array(xVal2), np.array(yVal2))
#     point2.set_3d_properties(np.array(jVal2), 'z')
#     return point1, point2

# anim = animation.FuncAnimation(
#     lfS_gd_gif_fig,
#     animate,
#     frames=len(thetas)-1,
#     fargs=(thetas, thetas2, point1, point2),
#     interval=5,
#     repeat=True,
#     blit=False
#     )
# # plt.show()
# anim.save('/Users/fanghan/Desktop/LinearR_GD_LossFuncSurface.gif', writer='imagemagick', fps=20)
# plt.close(lfS_gd_gif_fig)

# 绘制能量轮廓
# contourFig = plt.figure()
# ax = contourFig.add_subplot(111)
# ax.set_xlabel(r'$\theta_0$')
# ax.set_ylabel(r'$\theta_1$')

# CS = ax.contour(theta0Vals, theta1Vals, JVals, np.logspace(-2,3,20))
# plt.clabel(CS, inline=1, fontsize=8)
# plt.show()
# if __name__ == '__main__':
#     trainData, trainLabel = loadDataSet('ex0.txt')
#     # print trainData
#     # print trainLabel

#     # !tuple& numpy

#     theta0 = standRegres(trainData, trainLabel)
#     # print theta0
#     # print theta[0][0], theta[1][0]

#     # print theta
#     # print realIterNum

#     # Draw
#     # mpl.rcParams['font.sans-serif'] = [u'SimHei']
#     # fig = plt.figure()
#     # ax = fig.add_subplot(111)
#     # ax.scatter(trainData[:, 1], trainLabel, s=10 * 2 ** 2, alpha=0.5)
#     # # if theta is not None:
#     # #     x = np.arange(0.0,1.1,0.1)
#     # #     y = theta[0][0] + theta[1][0] * x
#     # #     ax.plot(x,y,'r-',linewidth=2.0)
#     # ax.grid(b=True)
#     # plt.show()

#     # Draw
#     # x = np.arange(-1.0, 1.01, 0.01)
#     # mpl.rcParams['font.sans-serif'] = [u'SimHei']
#     # fig = plt.figure()
#     # ax = fig.add_subplot(111)
#     # ax.plot(x, gaussiKernel(x, 0.1), 'r-', linewidth=2.0, label='k = 0.1')
#     # ax.plot(x, gaussiKernel(x, 0.5), 'g-', linewidth=2.0, label='k = 0.5')
#     # ax.plot(x, gaussiKernel(x, 1.0), 'b-', linewidth=2.0, label='k = 1.0')
#     # ax.grid(b=True)
#     # ax.axis([-1,1,0,1])
#     # plt.title(u'高斯核函数')
#     # plt.legend()
#     # plt.show()

#     #lwlr
#     # yp1, x1 = lwlrTestPlot(trainData, trainLabel, 0.01)
#     # yp2, x2 = lwlrTestPlot(trainData, trainLabel, 0.003)
#     # print yp
#     # x is matrix / yp is ndarray
#     # convert mat to list
#     # print x[:, 1].tolist()

#     # convert mat to array
#     # print np.array(x[:, 1])
#     # print np.asarray(x[:, 1]).reshape(-1)

#     # attention: 浅拷贝&深拷贝 in function lwlrTestPlot
#     # Draw
#     # mpl.rcParams['font.sans-serif'] = [u'SimHei']
#     # print mpl.rcParams['figure.figsize'] # 8,6
#     # fig = plt.figure()
#     # ax1 = fig.add_subplot(111)
#     # ax1.scatter(trainData[:, 1], trainLabel, s=10 * 2 ** 2, alpha=0.5)
#     # ax1.plot(np.array(x1[:, 1]).reshape(-1), yp1, 'r-', label='k=0.01')
#     # ax1.grid(b=True)
#     # ax1.legend()
#     # ax2 = fig.add_subplot(111)
#     # ax2.scatter(trainData[:, 1], trainLabel, s=10 * 2 ** 2, alpha=0.5)
#     # ax2.plot(np.array(x2[:, 1]).reshape(-1), yp2, 'r-', label='k=0.003')
#     # ax2.grid(b=True)
#     # ax2.legend()
#     # plt.show()