# 最优化算法[1] - 无约束优化问题的求解：梯度下降法，牛顿法
## 无约束优化问题
$$\theta^* = \mathbf{argmin}_{\theta}{f(\theta)}$$
## 梯度下降法 Gradient Descent Method
梯度下降是一种迭代方法：选取初值$\theta^0$，不断迭代，更新$\theta$的值，进行函数的极小化。
### 迭代公式
$$\theta^t = \theta^{t-1} + \Delta{\theta}$$
### 一阶泰勒展开
将函数$f(\theta)$在$\theta^{t-1}$处进行一阶泰勒展开：
$$f(\theta) = f(\theta^{t-1}+\Delta{\theta}) \approx f(\theta^{t-1}) + f^{\prime}(\theta^{t-1})\Delta{\theta}$$
### 函数极小化
要使得$f(\theta^t) < f(\theta^{t-1})$，$\Delta{\theta}$的一种可能取值是：
$$\Delta{\theta} = -\alpha f^{\prime}(\theta^{t-1})$$
**即：参数沿着负梯度方向前进一小段步长**。
### 总结
$$\theta^t = \theta^{t-1} - \alpha f^{\prime}(\theta^{t-1})$$
## 牛顿法 Newton's Method