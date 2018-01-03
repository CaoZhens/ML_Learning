# Boosting概述之一：从参数空间到函数空间
## 从参数空间到函数空间
### 从Gradient Descent到Gradient Boosting
#### Gradient Descent
$$\theta^t = \theta^{t-1} + \theta_t = \theta^{t-1} - \alpha L^{\prime}(\theta^{t-1})$$
即参数迭代更新的方向为负梯度方向；最终参数等于每次迭代增量的累加和，即：
$$\theta = \sum_{t=0}^T\theta_t$$
#### Gradient Boosting
考虑函数空间而不是参数空间：
$$f^t(x) = f^{t-1}(x) + f_t(x)$$
其中，
$$f_t(x) = -\alpha \frac{\partial{f}}{\partial{x}}|_{f=f^{t-1}}$$
最终函数等于每次迭代增量的累加和，即：
$$F(x) = \sum_{t=0}^T{f_t(x)}$$
### 从Newton's Method到Newton's Boosting
#### Newton's Method
牛顿法与梯度下降法唯一的不同就是参数增量：
$$\theta^t = \theta^{t-1} + \theta_t = \theta^{t-1} - \alpha H^{-1}g$$
$$\theta = \sum_{t=0}^T\theta_t$$
#### Newton's Boosting
考虑函数空间而不是参数空间：
$$f^t(x) = f^{t-1}(x) + f_t(x)$$
其中，
$$f_t(x) = -\frac{g_t(x)}{h_t(x)}$$
其中，
$$g_t(x)=\frac{\partial{f}}{\partial{x}}|_{f=f^{t-1}}, h_t(x) = \frac{\partial^2{f}}{\partial^2{x}}|_{f=f^{t-1}}$$
最终函数等于每次迭代增量的累加和，即：
$$F(x) = \sum_{t=0}^T{f_t(x)}$$
## Boosting
* Boosting是一种加法模型
* GBDT是在函数空间中利用梯度下降方法迭代求最优模型，即Gradient Boosting。
* XGBoost是在函数空间中利用牛顿法迭代求最优模型，即Newton's Boosting。