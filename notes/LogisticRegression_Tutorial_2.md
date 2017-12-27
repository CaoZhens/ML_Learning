# 逻辑回归（2）模型求解

## 回顾：求解线性回归模型的两种思路

思路一：  
基于MSE准则，定义损失函数$J(\theta)$并求
$$\theta = \mathbf{argmin}_{\theta}J(\theta)$$可直接求解析解或利用梯度下降法求解

思路二：  
基于极大似然估计，构造似然函数
$$L(\theta) = P(\mathbf{y}|\mathbf{X};\theta)$$在高斯先验假设下写出$P(\mathbf{y}|\mathbf{X};\theta)$的具体定义式并求
$$\theta = \mathbf{argmax}_{\theta}l(\theta)=\mathbf{argmax}_{\theta}logL(\theta)$$

**特别地，在高斯先验假设条件下，极大似然估计与MSE准则等价！**

备注：如果对上述结论有疑惑，请复习线性回归的[第二节](LinearRegression_Tutorial_2.md)和[第三节](LinearRegression_Tutorial_3.md)

逻辑回归模型的求解仍然采用上述思路。

## 基于极大似然估计求解逻辑回归模型

### 伯努利分布先验假设

二分类问题（不妨假设 $y^i \in [0, 1]$ ）满足伯努利分布，即：$y^i  \sim \mathbf{Bernoulli}(\phi^i) $

其中，
$$ \phi^i = p(y^i=1|\mathbf{x}^i;\theta) = h_\theta(\mathbf{x}^i) = g(\theta^T\mathbf{x}^i) = \frac{1}{1+e^{-\theta^T\mathbf{x}^i}}$$
$$ p(y^i=0|\mathbf{x}^i;\theta) = 1-\phi^i $$

### 构造似然函数

基于伯努利分布先验假设条件，
$$p(y^i|\mathbf{x}^i;\theta) = (h_\theta(\mathbf{x}^i))^{y^i}(1 - h_\theta(\mathbf{x}^i))^{1-y^i}$$

构造似然函数
$$L(\theta) = P(\mathbf{y}|\mathbf{X};\theta) = \prod_{i=1}^m (h_\theta(\mathbf{x}^i))^{y^i}(1 - h_\theta(\mathbf{x}^i))^{1-y^i}$$

将$L(\theta)$转化为对数似然函数$l(\theta)$
$$l(\theta) = \log{L(\theta)} = \sum_{i=1}^m\left [ y^ilogh_{\theta}(\mathbf{x}^i) + (1-y^i)log(1-h_{\theta}(\mathbf{x}^i) \right ]$$

### 极大似然估计
基于极大似然估计求解逻辑回归模型：
$$\theta = \mathbf{argmax}_{\theta}l(\theta)$$

### 梯度下降法迭代求解
$l(\theta)$对$\theta_j$求偏导：
$$\frac{\partial{l(\theta)}}{\partial{\theta_j}} = \sum_i \left[ \frac{y^i}{h_{\theta}(\mathbf{x}^i)} - \frac{1-y^i}{1-h_{\theta}(\mathbf{x}^i)}\right]\frac{\partial{h_{\theta}(\mathbf{x}^i)}}{\partial{\theta_j}} $$

其中，
$$h_\theta(\mathbf{x}^i) = g(\theta^T\mathbf{x}^i)$$
$$\frac{\partial{h_{\theta}(\mathbf{x}^i)}}{\partial{\theta_j}} = \left[g(\theta^T\mathbf{x}^i)\left( 1-g(\theta^T\mathbf{x}^i) \right)\right]\frac{\partial{(\theta^T\mathbf{x}^i})}{\partial{\theta_j}} =  \left[g(\theta^T\mathbf{x}^i)\left( 1-g(\theta^T\mathbf{x}^i) \right)\right]\mathbf{x}_j^i$$
代回上式得：
$$\frac{\partial{l(\theta)}}{\partial{\theta_j}} = \sum_i \left[ \frac{y^i}{g(\theta^T\mathbf{x}^i)} - \frac{1-y^i}{1-g(\theta^T\mathbf{x}^i)}\right]g(\theta^T\mathbf{x}^i)\left( 1-g(\theta^T\mathbf{x}^i) \right)\mathbf{x}_j^i$$
化简得：
$$\frac{\partial{l(\theta)}}{\partial{\theta_j}} = \sum_i \left[ y^i - g(\theta^T\mathbf{x}^i)\right]\mathbf{x}_j^i$$
梯度下降法的参数学习规则是：
$$\theta_j := \theta_j + \alpha\frac{\partial{l(\theta)}}{\partial{\theta_j}} = \theta_j + \alpha\sum_i \left[ y^i - g(\theta^T\mathbf{x}^i)\right]\mathbf{x}_j^i $$