# coding: utf-8
'''
Created on Dec 12, 2017
@author:
    CaoZhen
@description:
    1. Z-Score & Normalization
@reference:
    1. 
'''
import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt

obj = pd.Series([7,-5,7,4,2,0,4], name='testList')

fig = plt.figure(figsize=(12,4))
# fig.set(alpha = 1)

plt.subplot2grid((1,3),(0,0))
obj.plot(kind='kde')
plt.legend(['{} origin'.format(obj.name)], loc='best')
plt.grid()
plt.title('Origin pdf Curve')
obj_zscore = (obj - obj.mean())/obj.std()
obj_norm = (obj.rank(pct=True) - 0.5/obj.shape[0]).apply(st.norm.ppf)

plt.subplot2grid((1,3),(0,1),colspan=2)
obj_zscore.plot(kind='kde')
obj_norm.plot(kind='kde')
plt.legend(['{} Z-Score'.format(obj.name),'{} norm'.format(obj.name)], loc='best')
plt.grid()
plt.title('Z-Score & Normalization pdf Curve')
# plt.show()
fig.savefig("/Users/fanghan/Desktop/zscore_normalization_1.png")