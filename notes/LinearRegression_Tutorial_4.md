# 线性回归（4）极大似然估计与最小均方误差损失的等价性

## 回顾：线性回归模型的两个先验假设

1. 各样本独立同分布
2. 模型预测值与实际值之间的误差满足正态分布

详细描述请[看这里](LinearRegression_Tutorial_3.md)

即：**误差$\varepsilon^i$是独立同分布的，且服从均值为0，方差为$\sigma^2$的正态分布**

## 线性回归模型的似然函数

根据上述结论：
$$p(\varepsilon^i) = \frac{1}{\sqrt{2\pi}\sigma} \rm{exp}({-\frac{(\varepsilon^i)^2}{2\sigma^2}}) 
= \frac{1}{\sqrt{2\pi}\sigma} \rm{exp}({-\frac{(y^i - h_{\theta}(x^i))^2}{2\sigma^2}})
= p(y^i|x^i;\theta)$$

根据似然函数的定义
$$L(\theta) = P(\mathbf{y}|\mathbf{X};\Theta) 
= \prod_{i=1}^m P(y^i|x^i;\theta) = \prod_{i=1}^m \frac{1}{\sqrt{2\pi}\sigma} \rm{exp}({-\frac{(y^i - h_{\theta}(x^i))^2}{2\sigma^2}})$$

一般地，我们对两边取对数，即对数似然函数：
$$l(\theta) = logL(\theta) 
= log \prod_{i=1}^m \frac{1}{\sqrt{2\pi}\sigma} \rm{exp}({-\frac{(y^i - h_{\theta}(x^i))^2}{2\sigma^2}})
= \sum_{i=1}^m log(\frac{1}{\sqrt{2\pi}\sigma} \rm{exp}({-\frac{(y^i - h_{\theta}(x^i))^2}{2\sigma^2}})) = mlog \frac{1}{\sqrt{2\pi}\sigma } - \frac1{\sigma^2}\frac12\sum_{i=1}^m(y^i-h_{\theta}(x^i))^2$$

极大似然估计，即求
$$\theta = argmaxl(\theta)$$

等价于
$$\theta = argmin \frac12\sum_{i=1}^m(y^i-h_{\theta}(x^i))^2$$
**即最小均方误差损失**

**结论：线性回归模型的极大似然估计与最小均方误差损失是等价的**
