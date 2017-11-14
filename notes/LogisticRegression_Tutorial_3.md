# 逻辑回归（3）从损失函数的角度看逻辑回归

## 回顾：逻辑回归的似然函数
当$y \in [0,1]$时，逻辑回归的似然函数为：
$$L(\theta) = \prod_{i=1}^m (h_\theta(\mathbf{x}^i))^{y^i}(1 - h_\theta(\mathbf{x}^i))^{1-y^i}$$

$$l(\theta) = \sum_{i=1}^m\left [ y^ilogh_{\theta}(\mathbf{x}^i) + (1-y^i)log(1-h_{\theta}(\mathbf{x}^i) \right ]$$
将
$$h_{\theta}(\mathbf{x}^i) = \frac{1}{1+e^{-\theta^T\mathbf{x}^i}}$$代入对数似然函数：
$$l(\theta) = \sum_{i=1}^m\left [ y^ilog\frac{1}{1+e^{-\theta^T\mathbf{x}^i}} + (1-y^i)log(1-\frac{1}{1+e^{-\theta^T\mathbf{x}^i}}) \right ]$$
根据sigmoid函数性质2：
$$l(\theta) = \sum_{i=1}^m\left [ y^ilog\frac{1}{1+e^{-\theta^T\mathbf{x}^i}} + (1-y^i)log\frac{1}{1+e^{\theta^T\mathbf{x}^i}} \right ]$$
继续化简得到：
$$l(\theta) = -\sum_{i=1}^m\left [ y^ilog(1+e^{-\theta^T\mathbf{x}^i}) + (1-y^i)log(1+e^{\theta^T\mathbf{x}^i}) \right ]$$

## 逻辑回归的损失函数
$$LossFunc = -l(\theta) = \sum_{i=1}^m\left [ y^ilog(1+e^{-\theta^T\mathbf{x}^i}) + (1-y^i)log(1+e^{\theta^T\mathbf{x}^i}) \right ]$$

## 另外一种表示方法
上面的推导过程是基于$y \in [0,1]$的，我们也可以换一种表示方法：
不妨设$y \in [-1, +1]$，此时逻辑回归的似然函数形式为：
$$L(\theta) = \prod_{i=1}^m (h_\theta(\mathbf{x}^i))^{\frac{y^i+1}{2}}(1 - h_\theta(\mathbf{x}^i))^{-\frac{y^i-1}{2}}$$
化简对数似然函数得到：
$$l(\theta) = -\sum_{i=1}^m\left [ \frac12(y^i+1)log(1+e^{-\theta^T\mathbf{x}^i}) - \frac12(-y^i-1)log(1+e^{\theta^T\mathbf{x}^i}) \right ]$$
损失函数为：
$$LossFunc = -l(\theta) = \sum_{i=1}^m\left [ \frac12(y^i+1)log(1+e^{-\theta^T\mathbf{x}^i}) - \frac12(-y^i-1)log(1+e^{\theta^T\mathbf{x}^i}) \right ]$$
$$ LossFunc = \begin{cases} \sum_{i=1}^m log(1+e^{-\theta^T\mathbf{x}^i}), & \text {if $y^i = +1$} \\ \sum_{i=1}^m log(1+e^{\theta^T\mathbf{x}^i}), & \text{if $y^i=-1$} \end{cases} $$
即：
$$LossFunc = \sum_{i=1}^m log(1+e^{y^i(-\theta^T\mathbf{x}^i)})$$