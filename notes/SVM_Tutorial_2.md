# SVM[2] - 线性可分SVM的原始问题和对偶问题
## 回顾：线性可分SVM的目标函数
$$\min{\frac12{||w||}^2}, s.t. y^i(w^Tx^i+b)>=1$$
此目标函数即求解带不等式约束的极值问题，使用拉格朗日乘子法求解。
## 拉格朗日乘子法
### 拉格朗日公式
$$L(w, b, \alpha) = \frac12{||w||}^2 - \sum_i{\alpha^i\left[y^i(w^Tx^i+b-1)\right]}$$
### 原始问题（Primal)
$$p^* = \min_{w,b}\max_{\alpha^i>=0}{L(w, b, \alpha)}$$
### 对偶问题（Dual）
$$d^* = \max_{\alpha^i>=0}\min_{w,b}{L(w, b, \alpha)}$$
### 原始问题与对偶问题的等价条件
假设f和g都是凸函数，h是仿射的（affine，clip_image038[6]）。并且存在w使得对于所有的i，clip_image040[10]。在这种假设下，一定存在clip_image042[14]使得clip_image044[14]是原问题的解，clip_image046[6]是对偶问题的解。还有clip_image047[6]另外，clip_image042[15]满足库恩-塔克条件（Karush-Kuhn-Tucker, KKT condition），该条件如下：
$$\frac{\partial}{\partial w}{L(w, b, \alpha)} = 0$$
$${\alpha_i}^*g_i(w^*) = 0$$
$$g_i(w^*) <= 0$$
$${\alpha_i}^* >= 0$$
### 求解对偶问题
求解对偶问题分为三个步骤：
1. $L(w, b, \alpha)$关于w,b最小化
2. 
3. 
#### 步骤一
对w求偏导数：
$$w - \sum_i{\alpha_iy^ix^i} = 0$$
对b求偏导：
$$\sum_i{\alpha_iy^i} = 0$$
#### 步骤二
将步骤一中对w求偏导数的结果带回得到：
$$L(w, b, \alpha) = \sum_i{\alpha_i} - \frac12\sum_{i,j}{y^iy^j\alpha_i\alpha_j(x^i)^Tx^j} - b\sum_i{\alpha_iy^i}$$