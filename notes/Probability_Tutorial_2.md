# 概率论中的数字特征

## 什么是数字特征？

### 特性与特征

任一客体或任一组客体都具有众多特性。  
人们根据客体共有的特性，抽象出某个概念，这个概念就成为了特征。

### 数字特征

数字特征是对数字的抽象。  
不同的抽象方式代表不同的数字特征，如：均值表示数字的平均水平、方差表示数字的离散程度。  
**从信息论的角度说，特征化是对信息的一种压缩方式。**
> 举个简单的例子，校长去调查某个班级学生的学习水平，他不太可能去查看询问每个人的成绩。所以我们将班级的成绩信息进行抽象（均值，众数，标准差等），以此为校长提供其所关心的平均水平，成绩差异程度等。

## 概率论中的常用数字特征

**期望**
数学期望反映了随机变量的**平均水平**。
$$E(X) = \sum_k x_k p_k$$
> numpy.mean  
Compute the arithmetic mean along the specified axis.  
The arithmetic mean is the sum of the elements along the axis divided by the number of elements.

**方差**
方差反映了随机变量相对其数学期望的**偏离程度**。
$$D(X) = E\{[X-E(X)]^2\}=E\{[X^2-2XE(X)+{E(X)}^2]\}=E(X^2)-\{E(X)\}^2$$
> numpy.var  
Compute the variance along the specified axis.  
The variance is the average of the squared deviations from the mean, i.e., var = mean(abs(x - x.mean())**2).  
The mean is normally calculated as x.sum() / N, where N = len(x). If, however, ddof is specified, the divisor N - ddof is used instead. In standard statistical practice, ddof=1 provides an unbiased estimator of the variance of a hypothetical infinite population. ddof=0 provides a maximum likelihood estimate of the variance for normally distributed variables.

**标准差**
$$\sigma_X = \sqrt{D(X)}$$
已经有方差，为什么还需要标准差？  
标准差和均值的量纲（单位）是一致的，在描述一个波动范围时标准差比方差更方便。  
> 比如一个班男生的平均身高是170cm,标准差是10cm,那么方差就是100cm^2。可以进行的比较简便的描述是本班男生身高分布是170±10cm，方差就无法做到这点。  
再举个例子，从正态分布中抽出的一个样本落在[μ-3σ, μ+3σ]这个范围内的概率是99.7%，也可以称为“正负3个标准差”。如果没有标准差这个概念，我们使用方差来描述这个范围就略微绕了一点。万一这个分布是有实际背景的，这个范围描述还要加上一个单位，这时候为了方便，人们就自然而然地将这个量单独提取出来了。

> numpy.std  
Compute the standard deviation along the specified axis.  
The standard deviation is the square root of the average of the squared deviations from the mean, i.e., std = sqrt(mean(abs(x - x.mean())**2)).  
The average squared deviation is normally calculated as x.sum() / N, where N = len(x). If, however, ddof is specified, the divisor N - ddof is used instead. In standard statistical practice, ddof=1 provides an unbiased estimator of the variance of the infinite population. ddof=0 provides a maximum likelihood estimate of the variance for normally distributed variables. The standard deviation computed in this function is the square root of the estimated variance, so even with ddof=1, it will not be an unbiased estimate of the standard deviation per se.

**协方差**
$$Cov(X,Y) = E\{[X-E(X)][Y-E(Y)]\} = E(XY) - E(X)E(Y)$$
> numpy.cov  
Estimate a covariance matrix, given data and weights.  
Covariance indicates the level to which two variables vary together. If we examine N-dimensional samples, X = [x_1, x_2, ... x_N]^T, then the covariance matrix element C_{ij} is the covariance of x_i and x_j. The element C_{ii} is the variance of x_i.  

**相关系数**
$$\rho_{XY} = \frac{Cov(X,Y)}{\sigma_X \sigma_Y}$$
> numpy.corrcoef  
Return Pearson product-moment correlation coefficients.

Please refer to the documentation for cov for more detail. The relationship between the correlation coefficient matrix, R, and the covariance matrix, C, is

R_{ij} = \frac{ C_{ij} } { \sqrt{ C_{ii} * C_{jj} } }

The values of R are between -1 and 1, inclusive.