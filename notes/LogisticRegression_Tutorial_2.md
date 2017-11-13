# 逻辑回归（2）模型求解

## 回顾：线性回归模型求解的两种思路

思路一：  
基于MSE准则，定义损失函数$J(\theta)$并求
$$\theta = argmin_{\theta}J(\theta)$$可直接求解析解或利用梯度下降法求解

思路二：  
基于极大似然估计，构造似然函数
$$L(\theta) = P(\mathbf{y}|\mathbf{X};\theta)$$在高斯先验假设下写出$P(\mathbf{y}|\mathbf{X};\theta)$的具体定义式并求
$$\theta = argmax_{\theta}l(\theta)=argmax_{\theta}logL(\theta)$$

**特别地，在高斯先验假设条件下，极大似然估计与MSE准则等价！**

备注：如果对上述结论有疑惑，请复习线性回归的[第二节](LinearRegression_Tutorial_2.md)和[第三节](LinearRegression_Tutorial_3.md)

逻辑回归模型的求解仍然采用上述思路。

## 基于极大似然估计求解逻辑回归模型

### 伯努利分布先验假设

二分类问题满足伯努利分布，即：$y  \sim Bernoulli(\phi) $

其中，
$$p(y=1|\mathbf{x};\theta) = \phi  = h_\theta(\mathbf{x}) = g(\theta^T\mathbf{x}) = \frac{1}{1+e^{-\theta^T\mathbf{x}}}$$
$$ p(y=0|\mathbf{x};\theta) = 1-\phi $$

### 构造似然函数

基于伯努利分布先验假设条件，
$$p(y|\mathbf{x};\theta) = (h_\theta(\mathbf{x}))^{y^i}(1 - h_\theta(\mathbf{x}))^{1-y^i}$$
$$L(\theta) = P(\mathbf{y}|\mathbf{X};\theta) = \prod_{i=1}^m (h_\theta(\mathbf{x}^i))^{y^i}(1 - h_\theta(\mathbf{x}^i))^{1-y^i}$$

### 极大似然估计

基于极大似然估计求解。







