# 机器学习笔记

本项目用于记录学习笔记、代码及其它内容

## 访问之前

**如何浏览笔记**

由于笔记中包含大量LaTeX公式，而GitHub Flavored Markdown（GFM）不支持LaTeX，因此直接浏览会看到大量乱码；
建议使用**Chrome浏览器**并安装扩展**GitHub with MathJax**，可以解决80%以上的乱码问题，其余乱码将随项目完善，逐渐进行解决

## 主要内容

### Machine Learning

#### 1. 机器学习的数学基础

[机器学习的数学基础[1] - 自然底数e](./notes/1_Mathematical_Tutorial_1.md)

[机器学习的数学基础[2] - Gamma函数](./notes/1_Mathematical_Tutorial_2.md)

机器学习的数学基础[3] - 微积分在运算中的应用 

[机器学习的数学基础[4] - Taylor公式及其应用](./notes/1_Mathematical_Tutorial_3.md)

概率论的应用[1] - 生日悖论

概率论的应用[2] - 组合数与信息熵

概率论的应用[3] - taylor公式与Gini系数&信息熵

概率论的应用[4] - taylor公式与泊松分布

概率论的应用[5] - 本福特定律

#### 2. 线性回归／最小二乘法／梯度下降法

##### 模型篇

[线性回归[1] - 模型建立](./notes/LinearRegression_Tutorial_1.md)

[线性回归[2] - 模型求解：最小二乘法与梯度下降法](./notes/LinearRegression_Tutorial_2.md)

[线性回归[3] - 最大似然估计与线性回归模型的先验假设](./notes/LinearRegression_Tutorial_3.md)

[线性回归[4] - 最大似然估计与最小二乘法的等价性](./notes/LinearRegression_Tutorial_4.md)

线性回归的扩展[1] - 对特征做扩展 - 多项式回归Polynomial Regression

线性回归的扩展[2] - 损失函数引入Normalization - Lasso/Ridge/ElasticNet


##### 算法篇

批梯度下降与随机梯度下降

<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/6_LinearRegression/pic/LinearR_GD_FittingCurve.gif" alt="" data-canonical-src="" width="400" height="400" /> <img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/6_LinearRegression/pic/LinearR_GD_LossFuncSurface.gif" alt="" data-canonical-src="" width="400" height="400" />

#### 3. Logistic回归与SoftMax回归

##### 模型篇

**Logistic Regression - 二分类器**

[逻辑回归[1] 解决二分类问题的思路](./notes/LogisticRegression_Tutorial_1.md)

[逻辑回归[2] 模型求解](./notes/LogisticRegression_Tutorial_2.md)

SoftMax Regression - 多分类器

逻辑回归与最大熵模型

一般线性模型：再谈数据先验分布与极大似然估计

##### 算法篇

![image](https://github.com/CaoZhens/ML_Learning/blob/master/study/7_LogisticRegression/pic/LogisticR_GD_FittingCurve.gif) 

#### 4. 决策树

分类决策树：ID3 / C4.5

分类回归树：CART树

树剪枝：Pruning

#### 5. 集成方法：Ensemble

Bootstrap与Bagging

提升：Boosting

&emsp;Adaboost

对比GBDT与XGboost

#### 6. SVM

... ...


### 附录 Python基础

####  Package篇

1 - Numpy Basics

&emsp;[1.1 list / ndarray / matrix的相互转换](./study/4_PythonFoundation/numpyBasics/convert_list_ndarray_matrix.py)

&emsp;1.2 Key Functions

&emsp;&emsp;[1.2.1 shape](./study/4_PythonFoundation/numpyBasics/shape.py)

&emsp;&emsp;[1.2.2 slices](./study/4_PythonFoundation/numpyBasics/slices.py)

[2 - Scipy Basics](./study/4_PythonFoundation/scipyBasics/)

[3 - Matplotlib Basics](./study/4_PythonFoundation/matplotlibBasics/)

[4 - scikit-learn Basics](./study/5_SklearnFoundation/script/)

#### 综合篇

[1 - Python 文件读取](./study/4_PythonFoundation/loadData/)

[2 - Python 多线程](./study/4_PythonFoundation/multiThreading/)