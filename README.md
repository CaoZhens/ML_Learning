# 机器学习笔记
本项目用于记录学习笔记、代码及其它内容
## 访问之前
**如何浏览笔记**  
由于笔记中包含大量LaTeX公式，而GitHub Flavored Markdown（GFM）不支持LaTeX，因此直接浏览会看到大量乱码。  
建议使用**Chrome浏览器**并安装扩展[**GitHub with MathJax**](https://chrome.google.com/webstore/detail/github-with-mathjax/ioemnmodlmafdkllaclgeombjnmnbima)，可以解决80%以上的乱码问题。  
其余乱码将随项目完善，逐渐解决。

## Machine Learning
### PART I 数学基础
[机器学习的数学基础[1] - 自然底数e](./notes/1_Mathematical_Tutorial_1.md)  
[机器学习的数学基础[2] - Gamma函数](./notes/1_Mathematical_Tutorial_2.md)  
机器学习的数学基础[3] - 微积分在运算中的应用   
[机器学习的数学基础[4] - Taylor公式及其应用](./notes/1_Mathematical_Tutorial_3.md)  
[机器学习的数学基础[5] - 信息论基础](./notes/1_Mathematical_Tutorial_5.md)  
概率论的应用[1] - 生日悖论  
概率论的应用[2] - 组合数与信息熵  
概率论的应用[3] - taylor公式与Gini系数&信息熵  
概率论的应用[4] - taylor公式与泊松分布  
概率论的应用[5] - 本福特定律  

### PART II 模型
#### 线性回归
[线性回归[1] - 模型建立](./notes/LinearRegression_Tutorial_1.md)  
[线性回归[2] - 模型求解：最小二乘法与梯度下降法](./notes/LinearRegression_Tutorial_2.md)  
[线性回归[3] - 最大似然估计与线性回归模型的先验假设](./notes/LinearRegression_Tutorial_3.md)  
[线性回归[4] - 最大似然估计与最小二乘法的等价性](./notes/LinearRegression_Tutorial_4.md)  
线性回归的扩展[1] - 对特征做扩展 - 多项式回归Polynomial Regression  
线性回归的扩展[2] - 损失函数引入Normalization - Lasso/Ridge/ElasticNet  
附：梯度下降法 —— 批梯度下降与随机梯度下降  
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/6_LinearRegression/pic/LinearR_GD_FittingCurve.gif" alt="" data-canonical-src="" width="400" height="400" />
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/6_LinearRegression/pic/LinearR_GD_LossFuncSurface.gif" alt="" data-canonical-src="" width="400" height="400" />

#### Logistic回归
**Logistic Regression - 二分类器**  
[逻辑回归[1] - 解决二分类问题的思路](./notes/LogisticRegression_Tutorial_1.md)  
[逻辑回归[2] - 模型求解](./notes/LogisticRegression_Tutorial_2.md)  
[逻辑回归[3] - 从损失函数的角度看逻辑回归](./notes/LogisticRegression_Tutorial_3.md)  
**SoftMax Regression - 多分类器**  
逻辑回归与最大熵模型  

#### 广义线性模型
**从线性回归、逻辑回归到广义线性模型**  

##### 算法篇

![image](https://github.com/CaoZhens/ML_Learning/blob/master/study/7_LogisticRegression/pic/LogisticR_GD_FittingCurve.gif) 

#### 决策树
[决策树概述](./notes/DT_Tutorial_1.md)   
分类决策树：ID3 / C4.5  
分类回归树：CART树  
树剪枝：Pruning  

#### 集成方法(Ensemble Methods)
Bootstrap与Bagging  
提升：Boosting  
&emsp;Adaboost  
对比GBDT与XGboost  
... ...  


## 附录A Python基础

### 重要的第三方库

#### Numpy Basics
[list、ndarray、matrix的相互转换](./study/4_PythonFoundation/numpyBasics/convert_list_ndarray_matrix.py)  
1.2 Key Functions

&emsp;&emsp;[1.2.1 shape](./study/4_PythonFoundation/numpyBasics/shape.py)

&emsp;&emsp;[1.2.2 slices](./study/4_PythonFoundation/numpyBasics/slices.py)

#### [Scipy Basics](./study/4_PythonFoundation/scipyBasics/)

####[Matplotlib Basics](./study/4_PythonFoundation/matplotlibBasics/)

#### [scikit-learn Basics](./study/5_SklearnFoundation/script/)

### 综合应用
[1 - 文件读取](./study/4_PythonFoundation/loadData/)  
[2 - Python多线程](./study/4_PythonFoundation/multiThreading/)

## 附录B 数据集

[1. 疝气病马存活情况数据集：Horse Colic Data Set](http://archive.ics.uci.edu/ml/datasets/Horse+Colic)
*该数据集来自2010年1月11日的UCI机器学习数据库，原始数据包含368个样本和28个特征*
**应用索引**
[LogisticRegression with sklearn](./study/7_LogisticRegression/script/LogisticRegression_sklearn_HorseColic.py)