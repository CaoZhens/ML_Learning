# 机器学习的数学基础[5] - 信息论基础

为简化记录，以下均以离散变量为例；对连续变量，只需将求和变为积分即可。

## 信息熵

$$H(X) = -\sum_x P(x) \log{P(x)}$$

## 联合熵

$$H(X,Y) = -\sum_{x,y} P(x,y) \log{P(x,y)}$$

## 条件熵

$$H(Y|X) = H(X,Y) - H(X)$$
下面进一步推导其表达式：
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

## 交叉熵

## 互信息