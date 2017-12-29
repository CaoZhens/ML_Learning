# 概率论的应用[2] - 组合数与信息熵
## 排列与组合
### 排列
排列是指给定$n$个元素，从中取出$m$个元素，**并考虑排序**，记为$A_n^m$。
$$A_n^m = n \cdot (n-1) \cdot (n-2) \cdots (n-m+1) = \frac{n!}{(n-m)!} $$
### 组合
组合是指给定$n$个元素，从中取出$m$个元素，**但不考虑排序**，记为$C_n^m$。
考虑$m$个元素排序，共有$A_m^m=m!$种可能性，**在组合中认为是同一种**。因此：
$$C_n^m = A_n^m / m! = \frac{n!}{(n-m)!m!}$$

## 装箱问题与组合数
> 把$n$个物品分成$k$组，每组的个数分别为$n_1,n_2,\cdots,n_k$,(其中$n = n_1+n_2+\cdots+n_k$),则不同的分组方法共有$\frac{n!}{n_1!n_2!\cdots n_k!}$种。

## 从组合数到信息熵
对于二进制系统而言，$n$比特可以表示$2^n$种可能性。那么$W$种可能性所需要的比特数即$\log_2{W}$。  
针对上面所描述的装箱问题，$n$个物品所需的比特数记为：
$$h = \log_2{\frac{n!}{n_1!n_2!\cdots n_k!}}$$
如果平摊到每一个物品，需要的比特数记为：
$$H = \frac1n\log_2{\frac{n!}{n_1!n_2!\cdots n_k!}}=\frac1n\left(\log_2{n!} - \sum_i\log_2{n_i!}\right)$$
下面对$H$求$n$趋近于无穷大时（$n_i$也趋近于无穷大）的值。**即：计算装箱问题时，保存每个物品的投放结果所需要的平均比特数目。**
$$H = \lim_{n \to \infty}\frac1n\left(\log_2{n!} - \sum_i\log_2{n_i!}\right)$$

根据[机器学习的数学基础[3] - 微积分在近似运算中的应用](./1_Mathematical_Tutorial_4.md)中的结论：  
> $\ln N! \approx N\ln{N}-N$

化简上式得：
$$H = \lim_{n \to \infty}\frac1n\left(\log_2{n!} - \sum_i\log_2{n_i!}\right) = \frac1n\left( n\log{n}-n - \sum_in_i\log{n_i}-n_i\right) = \frac1n\left( n\log{n} - \sum_in_i\log{n_i} -n +\sum_i{n_i}\right)$$
其中，$n = \sum_i{n_i}$
$$H = \frac1n\left( n\log{n} - \sum_in_i\log{n_i} \right) = \frac1n\left( \sum_i{n_i}\log{n} - \sum_in_i\log{n_i} \right) = \sum_i{\frac{n_i}{n}}\log{\frac{n}{n_i}} = -\sum_i{\frac{n_i}{n}}\log{\frac{n_i}{n}}$$
即：
$$H = -\sum_i{\frac{n_i}{n}}\log{\frac{n_i}{n}} = -\sum_i{p_i}\log{p_i}$$

**不失一般性，对于某离散概率分布，熵的意义是：该概率分布下，记录一次事件发生所需要的平均比特数目。**