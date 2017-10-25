# coding: utf-8
'''
Created on Oct 24, 2017
@author:
    CaoZhen
@description:
    Basic annotation of matplotlib
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
# 1. xy / xytext / xycoords / textcoords / arrowprops
ax.plot(1, 1, 'ro')
ax.annotate('local max 1', xy=(1,1), xytext=(2,1.5),
    arrowprops=dict(facecolor='black', shrink=0.05),)

ax.annotate('local max 2', xy=(2,1), xytext=(0.8,0.8), textcoords='axes fraction',
    arrowprops=dict(facecolor='black', arrowstyle='<-'),)

ax.annotate('local max 3', xy=(3,1), xytext=(0.8,0.8), textcoords='figure fraction',
    arrowprops=dict(facecolor='black', arrowstyle='->'),)

# advanced annotation
# 1. add the box of text (bbox)
ax.annotate('local max 4', xy=(4,1), xytext=(4,-1),
    arrowprops=dict(facecolor='black', shrink=0.05),
    bbox=dict(boxstyle='sawtooth'))

plt.show()