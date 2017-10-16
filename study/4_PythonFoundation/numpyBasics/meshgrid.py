# coding: utf-8
'''
Created  on Oct 16, 2017
@author:
    CaoZhen
@desc:
    Basic Usage of numpy meshgrid
@reference:
    
'''
import numpy as np
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

x = np.linspace(0, 1, 3)
y = np.linspace(0, 1, 2)
# print x
# print y

# indexing = 'xy' (default)
xv, yv = np.meshgrid(x, y)
# print xv
# print yv

# indexing = 'ij'
xv2, yv2 = np.meshgrid(x, y, indexing='ij')
# print xv2
# print yv2

# sparse = True
xv3, yv3 = np.meshgrid(x, y, sparse=True)
# print xv3
# print yv3

xv4, yv4 = np.meshgrid(x, y, indexing='ij', sparse=True)
# print xv4
# print yv4

# meshgrid is useful to evaluate functions on a grid.
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
xx, yy = np.meshgrid(x, y, sparse=True)
# xx + yy as broadcast
z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
plt.contourf(x, y, z)
# plt.show()

# usage in LogisticRegression_sklearn.py
# Simple ex
t1 = np.linspace(10, 60, 6)
t2 = np.linspace(1, 6, 6)
print t1
print t2
x1, x2 = np.meshgrid(t1, t2)
print x1
print x2
print np.stack((x1.flat, x2.flat), axis=1)   # 测试点

# h = .2 # step size in the mesh
iris = load_iris()
X = iris.data
y = iris.target
X = X[:, :2]
x1_min, x1_max = X[:, 0].min() - .5, X[:, 0].max() + .5
x2_min, x2_max = X[:, 1].min() - .5, X[:, 1].max() + .5
t1 = np.linspace(x1_min, x1_max, 500)
t2 = np.linspace(x2_min, x2_max, 500)
x1, x2 = np.meshgrid(t1, t2)
x_test = np.stack((x1.flat, x2.flat), axis=1)   # 测试点
# print x_test