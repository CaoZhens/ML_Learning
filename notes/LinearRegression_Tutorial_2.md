# 线性回归（2）模型求解——最小二乘法与梯度下降法

## 



  定义误差函数(Loss Function)为 $$J_m(\theta) = \frac{1}{2}\sum_{i=1}^{m}(\hat{\mathbf{y}}^i - \mathbf{y}^i)^2 = \frac{1}{2}\sum_{i=1}^{m}(\theta^T \mathbf{x} - \mathbf{y}^i)^2$$
基于最小均方误差准则（MLSE)，模型参数为$$\theta = argmin_{\theta}J_m(\theta)$$

即 $\mathbf{X}_{{m}\times{n}}$， $\mathbf{y}_{{m}\times{1}}$
线性回归模型为 $$h_\theta(\mathbf{X}) = \mathbf{X}_{{m}\times{n}} \mathbf{\theta}_{{n}\times{1}} = \hat{\mathbf{y}}_{{m}\times{1}}$$