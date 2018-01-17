# 机器学习的数学基础[7] - 信息论基础2

## 相对熵／KL散度
相对熵用于衡量两个概率分布之间的差异性，即：
$$\mathbf{D}(p||q) = \sum_x{P(x)\log{\frac{P(x)}{Q(x)}}} = -\sum_x{P(x)\log{Q(x)}} - \left( -\sum_x{P(x)\log{P(x)}} \right)$$
其又被称为KL散度。

其中，上式的前半部分即**交叉熵**。

## 交叉熵
$$\mathbf{C}(p,q) = -\sum_x{P(x)\log{Q(x)}} $$