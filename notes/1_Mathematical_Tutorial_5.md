# 机器学习的数学基础[7] - 信息论基础1

为简化篇幅，以下均以离散变量为例；对连续变量，只需将求和变为积分即可。

## 信息熵

$$H(X) = -\sum_x P(x) \log{P(x)}$$

## 联合熵

$$H(X,Y) = -\sum_{x,y} P(x,y) \log{P(x,y)}$$

## 条件熵

$$H(Y|X) = H(X,Y) - H(X)$$
下面进一步推导条件熵表达式：
$$H(X,Y) - H(X) 
= -\sum_{x,y} P(x,y) \log{P(x,y)} + \sum_x P(x) \log{P(x)}$$
其中，$P(x)$可以表示为：
$$P(x) = \sum_{y}P(x,y)$$
代入原公式得：
$$H(X,Y) - H(X) 
= -\sum_{x,y} P(x,y) \log{P(x,y)} + \sum_x \left( \sum_{y}P(x,y) \right) \log{P(x)}
= -\sum_{x,y} P(x,y) \frac{\log{P(x,y)}}{\log{P(x)}} = -\sum_{x,y} P(x,y) \log{P(y|x)}$$
其中，$P(x,y)$又可以表示为：
$$P(x,y) = P(x)P(y|x)$$
再次代回原公式得：
$$H(X,Y) - H(X) = -\sum_{x,y} P(x,y) \log{P(y|x)} = -\sum_{x,y} \left( P(x)P(y|x) \right) \log{P(y|x)} = \sum_x P(x)H(Y|X=x)$$

**结论：**
$$H(Y|X) = H(X,Y) - H(X) = -\sum_{x,y} P(x,y) \log{P(y|x)}$$

$$H(Y|X) = H(X,Y) - H(X) = \sum_x P(x)H(Y|X=x)$$

## 互信息

互信息是指两个随机变量之间的关联程度。即给定一个随机变量后，另一个随机变量不确定性的削弱程度。  
根据上述定义，互信息表达式为：
$$I(X;Y) = H(X) - H(X|Y)$$

## 信息增益
$$\mathbf{G}(X,Y) = H(X) - H(X|Y)$$
信息增益即互信息。

## 信息增益比
$$\mathbf{G}_r(X,Y) = \mathbf{G}(X,Y)/H(Y)$$

## Gini系数

$${\rm Gini}(p) = \sum_{k=1}^K p_k(1-p_k) = 1-\sum_{k=1}^K{p_k}^2$$
特别地，对于二分类问题：
$${\rm Gini}(p) = p(1-p) + p(1-p) = 2p(1-p)$$

## 参考资料
1. [知乎专栏：通俗理解信息熵](https://zhuanlan.zhihu.com/p/26486223)
2. [知乎问题：如何通俗的解释交叉熵与相对熵?](https://www.zhihu.com/question/41252833)