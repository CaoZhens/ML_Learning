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
> numpy.mean  
Compute the arithmetic mean along the specified axis.  
The arithmetic mean is the sum of the elements along the axis divided by the number of elements.

**方差**
> numpy.var  
Compute the variance along the specified axis.  
The variance is the average of the squared deviations from the mean, i.e., var = mean(abs(x - x.mean())**2).  
The mean is normally calculated as x.sum() / N, where N = len(x). If, however, ddof is specified, the divisor N - ddof is used instead. In standard statistical practice, ddof=1 provides an unbiased estimator of the variance of a hypothetical infinite population. ddof=0 provides a maximum likelihood estimate of the variance for normally distributed variables.

**标准差**
> numpy.std  
Compute the standard deviation along the specified axis.  
The standard deviation is the square root of the average of the squared deviations from the mean, i.e., std = sqrt(mean(abs(x - x.mean())**2)).  
The average squared deviation is normally calculated as x.sum() / N, where N = len(x). If, however, ddof is specified, the divisor N - ddof is used instead. In standard statistical practice, ddof=1 provides an unbiased estimator of the variance of the infinite population. ddof=0 provides a maximum likelihood estimate of the variance for normally distributed variables. The standard deviation computed in this function is the square root of the estimated variance, so even with ddof=1, it will not be an unbiased estimate of the standard deviation per se.

**协方差**
> numpy.cov  
Estimate a covariance matrix, given data and weights.  
Covariance indicates the level to which two variables vary together. If we examine N-dimensional samples, X = [x_1, x_2, ... x_N]^T, then the covariance matrix element C_{ij} is the covariance of x_i and x_j. The element C_{ii} is the variance of x_i.  

**相关系数**
> numpy.corrcoef  
Return Pearson product-moment correlation coefficients.

Please refer to the documentation for cov for more detail. The relationship between the correlation coefficient matrix, R, and the covariance matrix, C, is

R_{ij} = \frac{ C_{ij} } { \sqrt{ C_{ii} * C_{jj} } }

The values of R are between -1 and 1, inclusive.
