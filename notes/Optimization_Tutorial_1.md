# 最优化算法[1] - 求解无约束优化问题的方法：梯度下降法，牛顿法
## 无约束优化问题
$$\theta^* = \mathbf{argmin}_{\theta}{L(\theta)}$$
## 梯度下降法 Gradient Descent Method
梯度下降是一种迭代方法：选取初值$\theta^0$，不断迭代，更新$\theta$的值，进行函数的极小化。
### 迭代公式
$$\theta^t = \theta^{t-1} + \Delta{\theta}$$
### 一阶泰勒展开
将函数$L(\theta)$在$\theta^{t-1}$处进行一阶泰勒展开：
$$L(\theta) = L(\theta^{t-1}+\Delta{\theta}) \approx L(\theta^{t-1}) + L^{\prime}(\theta^{t-1})\Delta{\theta}$$
### 函数极小化
要使得$L(\theta^t) < L(\theta^{t-1})$，$\Delta{\theta}$的一种可能取值是：
$$\Delta{\theta} = -\alpha L^{\prime}(\theta^{t-1})$$
**即：参数沿着负梯度方向以步长$\alpha$前进**。
### 总结
$$\theta^t = \theta^{t-1} - \alpha L^{\prime}(\theta^{t-1})$$
## 牛顿法 Newton's Method
### 二阶泰勒展开
与梯度下降法类似，但对函数$L(\theta)$在$\theta^{t-1}$处进行二阶泰勒展开：
$$L(\theta) = L(\theta^{t-1}+\Delta{\theta}) \approx L(\theta^{t-1}) + L^{\prime}(\theta^{t-1})\Delta{\theta}+\frac12L^{\prime\prime}(\theta^{t-1}){\Delta{\theta}}^2$$
### $\theta$是标量时的函数极小化
为了简化分析过程，假设参数$\theta$是标量（一维），记一阶导数和二阶导数分别为$g$和$h$：
$$L(\theta) \approx L(\theta^{t-1}) + g\Delta{\theta}+\frac12h{\Delta{\theta}}^2$$
要使得$L(\theta)$极小，令
$$\frac{\partial{(g\Delta{\theta}+\frac12h{\Delta{\theta}}^2)}}{\partial{\Delta{\theta}}} = 0$$
即：
$$\Delta{\theta} = -\frac{g}{h}$$
即当$\theta$是标量时，牛顿法的迭代求解规则为：
$$\theta^t = \theta^{t-1} - \frac{g}{h}$$
### 将参数$\theta$推广至向量形式
$$\theta^t = \theta^{t-1} - H^{-1}g$$