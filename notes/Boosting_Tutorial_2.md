# XGBoost算法原理

## 回顾：损失函数
$$J(f_t) = \sum_{i=1}^mL(y^i,  \hat{y}_i^{(t-1)} + f_t(\mathbf{x}^i)) + \Omega(f_t) + Const$$

## 利用二阶泰勒展式改写损失函数

二阶泰勒展式：
$$f(x+\Delta{x}) \approx f(x) + f^{\prime}(x)\Delta{x} + \frac{1}{2}f^{\prime\prime}(x)\Delta{x}^2$$

**将$L(y^i,  \hat{y}_i^{(t-1)} + f_t(\mathbf{x}^i))$ 中的 $f_t(\mathbf{x}^i)$看作$\Delta{x}$,则：**
$$L(y^i,  \hat{y}_i^{(t-1)} + f_t(\mathbf{x}^i)) \approx L(y^i,  \hat{y}_i^{(t-1)}) + \frac{\partial L(y^i,  \hat{y}_i^{(t-1)})}{\partial\hat{y}_i^{(t-1)}}f_t(\mathbf{x}^i)+\frac12\frac{\partial^2 L(y^i,  \hat{y}_i^{(t-1)})}{\partial^2\hat{y}_i^{(t-1)}}f_t^2(\mathbf{x}^i)$$

不妨令：
$$g_i = \frac{\partial L(y^i,  \hat{y}_i^{(t-1)})}{\partial\hat{y}_i^{(t-1)}}, h_i = \frac{\partial^2 L(y^i,  \hat{y}_i^{(t-1)})}{\partial^2\hat{y}_i^{(t-1)}}$$

**$g_i$和$h_i$均是可计算的。**

综上，损失函数可改写为如下形式：
$$J(f_t) = \sum_{i=1}^m\left[L(y^i,  \hat{y}_i^{(t-1)}) + g_if_t(\mathbf{x}^i) + \frac12h_if_t^2(\mathbf{x}^i)\right] + \Omega(f_t) + Const$$

## 继续改写损失函数

### 回顾：决策树的两要素及函数本质

[决策树的两要素与函数本质](./DT_Tutorial_5.md)

>**决策树的本质是以$\mathbf{x}^i$为输入，$w_{q(\mathbf{x}^i)}$为输出的函数**，记为：
$$f(\mathbf{x}^i) = w_{q(\mathbf{x}^i)}$$

### 正则项的一种方式

$$\Omega(f_t) = \gamma T + \frac12\lambda\sum_{j=1}^Tw_j^2$$
其中，$T$为叶子数。
**上式的形象解释为：决策树的叶子数不应该过多，且每个叶子的权值不应该过大。**

### 子项$L(y^i,  \hat{y}_i^{(t-1)})$的讨论

$L(y^i,  \hat{y}_i^{(t-1)})$是常数，可以与常数项合并

### 综上，改写损失函数

$$J(f_t) = \sum_{i=1}^m\left[g_iw_{q(\mathbf{x}^i)} + \frac12h_iw_{q(\mathbf{x}^i)}^2\right] + \gamma T + \frac12\lambda\sum_{j=1}^Tw_j^2 + Const$$

根据[决策树的两要素与函数本质](./DT_Tutorial_5.md)  
>每一个数据样本$\mathbf{x}^i$经过决策树后都会被映射至某个叶子节点$j=q(\mathbf{x}^i)$，相应的叶子权值为$w_{q(\mathbf{x}^i)}$

因此，第一子项又可以改写为
$$\sum_{i=1}^m\left[g_i^iw_{q(\mathbf{x}^i)} + \frac12h_iw_{q(\mathbf{x}^i)}^2\right] = \sum_{j=1}^T\left[\left(\sum_{i \in I_j}g_i\right)w_{j} + \frac12\left(\sum_{i \in I_j}h_i\right)w_{j}^2\right]$$

损失函数：
$$J(f_t) = \sum_{j=1}^T\left[\left(\sum_{i \in I_j}g_i\right)w_{j} + \frac12\left(\sum_{i \in I_j}h_i\right)w_{j}^2\right] + \gamma T + \frac12\lambda\sum_{j=1}^Tw_j^2 + Const$$

不妨记：
$$G_j= \sum_{i \in I_j}g_i,H_j= \sum_{i \in I_j}h_i$$

### 损失函数的最终形式
$$J(f_t) = \sum_{j=1}^T\left[G_jw_{j} + \frac12\left(H_j+\lambda\right)w_{j}^2\right] + \gamma T  + Const$$

**即，损失函数被改写成关于$w_j$的函数。**

## 求解

$$\frac{\partial{J(f_t)}}{\partial{w_j}} = G_j + (H_j+\lambda)w_j = 0$$

解得：
$$w_j = - \frac{G_j}{H_j+\lambda}$$