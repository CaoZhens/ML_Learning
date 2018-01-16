# 线性回归（2）最小均方误差损失与模型求解(最小二乘法&梯度下降法)

## MSE准则

基于MSE准则，定义损失函数(Loss Function)： 
$$
J_m(\theta) = \frac{1}{2}\sum_{i=1}^{m}(\hat{y}^i - y^i)^2 = \frac{1}{2}\sum_{i=1}^{m}(\theta^T \mathbf{x}^i - y^i)^2
$$

模型目标为：
$$
\theta = argmin_{\theta}J_m(\theta)
$$

## 直接求解析解：最小二乘法

将样本表示为矩阵，即 $\mathbf{X}_{{m}\times{n}}$， $\mathbf{y}_{{m}\times{1}}$

将参数表示为矩阵，即 $\theta_{{n}\times{1}}$

误差函数记为
$$
J_m(\theta) = \frac{1}{2}\sum_{i=1}^{m}(\theta^T \mathbf{x}^i - y^i)^2 = \frac12 \left( \theta\mathbf{X} - \mathbf{y}\right)^T\left( \theta\mathbf{X} - \mathbf{y}\right) = J(\theta)
$$

求误差函数的最小值，等价于令误差函数的偏导为0，即：
$$
\nabla_\theta{J(\theta)} = ... = \mathbf{X}^T\mathbf{X}\theta - \mathbf{X}^T\mathbf{y}  \to 0
$$

当$\mathbf{X}^T\mathbf{X}$可逆时
$$
\theta = \left( \mathbf{X}^T\mathbf{X} \right)^{-1}\left( \mathbf{X}^T\mathbf{y}\right)
$$

## 梯度下降法求解