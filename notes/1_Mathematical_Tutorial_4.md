# 微积分在近似运算中的应用

## 应用1 大数的阶乘取对数

上一节（[机器学习的数学基础[2] - Gamma函数](./1_Mathmatical_Tutorial_2.md)）介绍了Gamma函数，**Gamma函数的代数意义是：阶乘在实数域上的推广！**  
下面继续讨论阶乘，**问题：如果一个对一个大数的阶乘取对数，大概会是什么量级？**
$$\log{N!} = \sum_{i=1}^N \log{i}$$
**求和可以近似成积分运算，即：**
$$\sum_{i=1}^N \log{i} \approx \int_1^N {\log{x}} \,{\rm d}x$$
对上面的积分式作分步积分，得：
$$\int_1^N {\log{x}} \,{\rm d}x = \left. {x\log{x}} \right| _1^N -  \int_1^N x {\rm d}{\log{x}} = N \log{N} -  \int_1^N x\frac1x {\rm d}{x} = N\log{N} - (N-1)$$

**即：$\log{N!}$的数量级为$N(\log{N}-1)$**