# coding: utf-8

'''
Python 中心极限定理
@author ：CaoZhen
@date   ：2017/09/18
@comment：主要参考网络资料 & 小象学院4.1intro.py Section 6
'''

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import stats


# Fixing random state for reproducibility
np.random.seed(20170918)


# 1. Central Limit Theory's Validation - Uniform Distribution
# 1.1 Uniform Distribution's addition
# a = np.zeros(10000)
# for i in np.arange(1000):
#     a += np.random.uniform(-5, 5, 10000)
# a /= 1000
# plt.hist(a, bins=30, color='g', alpha=0.5, normed=True, label=u'Uniform Distribution\'s addition ')
# plt.legend(loc='best')
# plt.grid()
# plt.show()

# 1.2 其他分布的中心极限定理 - Poisson
# rvs - Random variates of given type
# pmf - Probability mass function at k of the given RV

p = stats.poisson(7)
y = p.rvs(size=1000)
plt.figure(figsize=(15, 8), facecolor='w')
plt.subplot(121)
plt.hist(y, bins=30, range=(0, 30), color='g', alpha=0.8, normed=True)
t = np.arange(0, 30+1)
plt.plot(t, p.pmf(t), 'ro-', lw=2)
plt.grid(True)

plt.subplot(122)
a = np.zeros(10000, dtype=np.float)
for i in np.arange(1000):
    a += stats.poisson(7).rvs(size=10000)
a /= 1000
plt.hist(a, bins=20, color='g', alpha=0.8, normed=True)
plt.grid(b=True)
plt.show()


# 2.1 Dice Game's Gif - Discrete Uniform Distribution
# randint - discrete uniform distribution

# indexArray = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])
# fig = plt.figure()
# ax = fig.add_subplot(111)
# plt.title('Dice Game')
# plt.grid(True)
#
# def init():
#     plt.grid(True)
#
# def animate(i):
#     plt.cla()
#     plt.hist(np.random.randint(1,7,6*indexArray[i]), bins=6, align='left', facecolor='b', alpha=0.7)
#     plt.annotate('n = %d'%(6*indexArray[i]), xy=(0.05, 0.95), xycoords='axes fraction')
#     plt.title('Dice Game')
#     plt.grid(True)
#
# anim = animation.FuncAnimation(fig, animate, init_func=init,
#                                 frames=len(indexArray),
#                                 interval=1500,
#                                 repeat=False,
#                                 blit=False
#                                 )
# plt.show()
# anim.save('/Users/fanghan/Desktop/DiceGame.gif', writer='imagemagick', fps=1)

# do Dice Game 1w counts
random_result = np.random.randint(1,7,10000)
# # print random_result.mean()
# # print random_result.std()
#
# # 均匀分布
# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# ax1.hist(random_result, bins=6, align='left', facecolor='b', alpha=0.7)
# plt.show()

def SampleAndSum(data, n):
    samples = []
    for i in range(0, 10000):
        sample = []
        for j in range(0, n):
            sample.append(data[int(np.random.random() * len(data))])
        sample_np = np.array(sample)
        samples.append(sample_np.sum())
    return samples

# 2.2 Dice Game's Gif - CentralLimitTheory Gif
# with animation
indexArray = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])
history_Samples = []
for i in indexArray:
    history_Samples.append(SampleAndSum(random_result, i))
print len(history_Samples)

# fig = plt.figure()
# ax = fig.add_subplot(111)
# plt.title('Validation of the Central Limit Theory')
# plt.grid(True)
#
# def init():
#     plt.hist(history_Samples[0], bins=6, align='left', facecolor='b', alpha=0.7)
#     plt.annotate('n = 1', xy=(0.05, 0.95), xycoords='axes fraction')
#     plt.grid(True)
#
# def animate(i):
#     plt.cla()
#     plt.hist(history_Samples[i], bins=(6*indexArray[i] if 6*indexArray[i]<512 else 512), align='left', facecolor='b', alpha=0.7)
#     plt.annotate('n = %d'%indexArray[i], xy=(0.05, 0.95), xycoords='axes fraction')
#     plt.title('Validation of the Central Limit Theory')
#     plt.grid(True)
#
# anim = animation.FuncAnimation(fig, animate, init_func=init,
#                                 frames=len(history_Samples),
#                                 interval=1500,
#                                 repeat=False,
#                                 blit=False
#                                 )
# plt.show()
# anim.save('/Users/fanghan/Desktop/CentralLimitTheory.gif', writer='imagemagick', fps=1)

