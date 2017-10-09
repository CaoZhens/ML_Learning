# coding:utf-8

'''
Created on Sep 30, 2017
@author:
    CaoZhen
@desc:
    Distribution Generation
    1. Uniform Distribution
    2. Standard Normal Distribution
    3. Gaussian Distribution

@reference:
    4.1.intro.py Section 6
'''
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


'''
1. Uniform Distribution 均匀分布
rand - uniform distribution over [0, 1)
'''
x = np.random.rand(10000)
fig = plt.figure(figsize=(14,6))
plt.title('Uniform Distribution')
ax1 = fig.add_subplot(121)
ax1.hist(x, 20, color='b', alpha=0.5)
# ax1.axis([0.0, 1.0, 0, 500])
# 两个子图如何处理坐标轴的显示
ax1.grid(True)

ax2 = fig.add_subplot(122)
ax2.plot(np.arange(len(x)), x)
# ax2.axis([0, 10000, 0.0, 1.0])
ax2.grid(True)
plt.show()

'''
2. Standard Normal Distribution 标准正态分布
randn - univariate “normal” (Gaussian) distribution of mean 0 and variance 1
'''
x = np.random.randn(10000)
label = u'$\mu$=%d, $\sigma^2$=%d' % (np.mean(x), np.var(x))

fig = plt.figure(figsize=(14,6))
plt.title('Standard Normal Distribution')
ax1 = fig.add_subplot(121)
ax1.hist(x, 20, color='b', alpha=0.5, label=label)
ax1.legend(loc='best')
# ax1.axis([0.0, 1.0, 0, 500])
# 两个子图如何处理坐标轴的显示
ax1.grid(True)

ax2 = fig.add_subplot(122)
ax2.plot(np.arange(len(x)), x, label=label)
ax2.legend(loc='best')
# ax2.axis([0, 10000, 0.0, 1.0])
ax2.grid(True)
plt.show()

'''
3. Gaussian Distribution 高斯分布
For random samples from N(\mu, \sigma^2), use: sigma * np.random.randn(...) + mu
'''

x = np.sqrt(2) * np.random.randn(10000) + 3
label = u'$\mu$=%.f, $\sigma^2$=%.f' % (np.mean(x), np.var(x))

fig = plt.figure(figsize=(14,6))
plt.title(u'Gaussian Distribution')
ax1 = fig.add_subplot(121)
ax1.hist(x, 20, color='b', alpha=0.5, label=label)
ax1.legend(loc='best')
# ax1.axis([0.0, 1.0, 0, 500])
# 两个子图如何处理坐标轴的显示
ax1.grid(True)

ax2 = fig.add_subplot(122)
ax2.plot(np.arange(len(x)), x, label=label)
ax2.legend(loc='best')
# ax2.axis([0, 10000, 0.0, 1.0])
ax2.grid(True)
plt.show()

'''
4. Poisson
'''

# 注意normed的用法
x = np.random.poisson(lam=5, size=10000)
# a = plt.hist(x, bins=15, normed=True, range=[0, 15], color='g', alpha=0.5)
a = plt.hist(x, bins=15, range=[0, 15], color='g', alpha=0.5)
plt.grid()
plt.show()
# print a
# print a[0].sum()