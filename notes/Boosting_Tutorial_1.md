# Boosting概述

## 引言

前面介绍的内容，都是使用单一模型进行机器学习的过程。然而有时，单模型往往不能取得很好的结果。  
**思路是：利用多个模型组合进行机器学习，使多个单一的弱模型组合成为比较强大的模型。**   
一般有以下两种方式：
* 数据样本加权：本次预测错误的样本，下一次权重升高
* 模型加权：多个模型加权进行预测

## 回顾

回顾：[如何形式化描述机器学习问题？](./Summary_Tutorial_1.md)  
> 已知$m$个样本，其中第$i$个样本记为$\{\mathbf{x}^i, y^i\}$  
待建立的模型记为$Model(\mathbf{x}, \theta)$  
为了下面公式表达方便，也可记为$F(\mathbf{x}, \theta)$  
建立损失函数
$$L(F(\mathbf{x}, \theta), y)$$
待求解参数
$$\theta = argmin_{\theta}L(F(\mathbf{x}, \theta), y)$$

损失函数是关于$\theta$的函数。

## Boosting

### 换一个角度看待损失函数
不再把损失函数看成关于$\theta$的函数，**而是看成关于模型$F$的函数。** 

### 重新对机器学习问题进行描述
已知$m$个样本，其中第$i$个样本记为$\{\mathbf{x}^i, y^i\}$  
待建立的模型记为$Model(\mathbf{x})$  
为了下面公式表达方便，也可记为$F(\mathbf{x})$  
建立损失函数
$$L(F(\mathbf{x}), y)$$
待求解的最优模型是使得损失函数期望最小的模型，即：
$$F^* = argminE_{\{x,y\}}\left(L(F(\mathbf{x}), y)\right)$$

###  换一个角度看待模型
将模型$F(\mathbf{x})$看成一组基模型$f_i(\mathbf{x})$的加权和，即：
$$F(\mathbf{x}) = \sum_{i=1}^M \gamma_i f_i(\mathbf{x}) + const$$
**即：求解模型$F$转化为求解每一个基模型$f_i$及相应的权值$\gamma_i$**  
备注：实际上，权值$\gamma_i$也可以看作$f_i$的一部分，因此后续推导过程不再考虑$\gamma_i$，上式可改写为：
$$F(\mathbf{x}) = \sum_{i=1}^M f_i(\mathbf{x}) + const$$

### 基于贪心法的模型表达式
利用贪心法的思路，逐次求解每一个基模型$f_i$：
1. 假设初始基模型为**常函数**，即$f_0(\mathbf{x})=C$，此时：
$$F_0(\mathbf{x}) = f_0(\mathbf{x}) = C_0$$
$F_0(\mathbf{x})$的最优解为
$$F_0^* = argmin_{C_0} L(y, C_0)$$

2. 利用贪心思路扩展得到后续模型：
$$F_m(\mathbf{x}) = F_{m-1}(\mathbf{x}) + argmin_f \sum_{i=1}^m L(y^i, F_{m-1}(\mathbf{x}^i) + f(\mathbf{x}^i))$$

### 损失函数

根据上一节可知，每次求解基模型$f_i$即可。不妨定义：
已知$f_0, f_1, ... f_{t-1}$，求$f_t$  
其中，前t个基函数加权构成
$$F_{t-1}(\mathbf{x}) = f_0(\mathbf{x})+f_1(\mathbf{x})+...+f_{t-1}(\mathbf{x})$$
记前t个基函数对第i个数据样本的预测值为：
$$F_{t-1}(\mathbf{x}^i) = \hat{y}_i^{(t-1)}$$

定义损失函数(带正则项)：
$$J(f_t) = \sum_{i=1}^mL(y^i,  \hat{y}_i^{(t-1)} + f_t(\mathbf{x}^i)) + \Omega(f_t) + Const$$









