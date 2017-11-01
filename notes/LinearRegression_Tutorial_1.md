# 线性回归（1）模型建立

## 基于单样本的建模

已知单个样本 $\{\mathbf{x}, y\}$，记特征个数为$n$，即：$$\mathbf{x} = (x_{0}, x_{1}, ... , x_{n})$$
线性回归模型为 $$h_\theta(\mathbf{x}) = \mathbf{\theta}^T \mathbf{x} = \theta_{0}x_{0}+\theta_{1}x_{1}+\cdots+\theta_{n}x_{n} = \hat{y}$$

## 基于多样本的建模

将样本个数从一个推广至$m$个，其中第$i$个样本记为$\{\mathbf{x}^i, y^i\}$

将上述向量表示推广至矩阵，样本矩阵可表示为：
$$\mathbf{X} = \left[
    \begin{matrix}
      \cdots & {\mathbf{x}^1}^T & \cdots \\  
      \cdots & {\mathbf{x}^2}^T & \cdots \\ 
       & \vdots &                        \\
      \cdots & {\mathbf{x}^m}^T & \cdots
    \end{matrix}
  \right],
  \mathbf{y} = \left[
    \begin{matrix}
      y^1 \\
      y^2 \\
      \vdots       \\
      y^m
    \end{matrix}  
  \right]$$

## 尝试求解
以单样本形式为例，目的是求解线性回归模型参数 $\theta$
假设m个样本，n个特征（一般地，m > n）
列出方程组
$$
  \begin {matrix}
    \theta^T\mathbf{x}^{(1)} = \theta_{0}{x_{0}}^{(1)}+\theta_{1}{x_{1}}^{(1)}+\cdots+\theta_{n}{x_{n}}^{(1)} = \mathbf{y}^{(1)} \\
    \theta^T\mathbf{x}^{(2)} = \theta_{0}{x_{0}}^{(2)}+\theta_{1}{x_{1}}^{(2)}+\cdots+\theta_{n}{x_{n}}^{(2)} = \mathbf{y}^{(2)} \\
    \vdots   \\
    \vdots   \\
    \theta^T\mathbf{x}^{(m)} = \theta_{0}{x_{0}}^{(m)}+\theta_{1}{x_{1}}^{(m)}+\cdots+\theta_{n}{x_{n}}^{(m)} = \mathbf{y}^{(m)}
  \end {matrix}
$$
方程组有m个方程，n+1个未知数
当m>n时，为超定方程组，该方程组无精确解
> 超定方程组是指方程个数大于未知量个数的方程组。对于方程组Ra=y，R为m×n矩阵，如果R列满秩，且m>n。则方程组没有精确解，此时称方程组为超定方程组。
超定方程组一般情况下，是通过定义损失函数，求取损失函数最小时对应的模型参数。

下一篇笔记将具体讨论线性回归模型的求解。