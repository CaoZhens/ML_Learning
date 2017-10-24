# coding: utf-8
'''
Created on Oct 24, 2017
@author:
    CaoZhen
@description:
    Basic annotation
@reference:
    1. 
'''

import numpy as np
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
line, = ax.plot(t, s, lw=2)
ax.set_ylim(-2, 2)

# basic annotation
ax.annotate('local max 1', xy=(2,1), xytext=(3,1.5),
    arrowprops=dict(facecolor='black', shrink=0.05),)

ax.annotate('local max 2', xy=(2,1), xytext=(0.8,0.8), textcoords='axes fraction',
    arrowprops=dict(facecolor='black', shrink=0.05),)

ax.annotate('local max 3', xy=(2,1), xytext=(0.8,0.8), textcoords='figure fraction',
    arrowprops=dict(facecolor='black', shrink=0.05),)
    
plt.show()