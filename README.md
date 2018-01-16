# 机器学习笔记
本项目用于记录学习笔记、代码及其它内容
## 访问之前
**机器学习概述**  
机器学习是一门跨学科领域，涉及高等数学、概率论与统计、信息论、最优化理论、计算机科学等多个领域。近年来，随着硬件成本的不断下降，以及大数据与分布式计算技术的发展完善，机器学习由理论时代进入了规模应用时代。  

**如何浏览笔记**  
由于笔记中包含大量LaTeX公式，而GitHub Flavored Markdown（GFM）不支持LaTeX，因此直接浏览会看到大量乱码。  
建议使用**Chrome浏览器**并安装扩展[**GitHub with MathJax**](https://chrome.google.com/webstore/detail/github-with-mathjax/ioemnmodlmafdkllaclgeombjnmnbima)，可以解决80%以上的乱码问题。其余乱码将随项目完善，逐渐解决。

## Machine Learning
### PART I 数学基础 Foundation of mathematics
[机器学习的数学基础[1] - 自然底数e](./notes/1_Mathematical_Tutorial_1.md)  
[机器学习的数学基础[2] - Gamma函数](./notes/1_Mathematical_Tutorial_2.md)  
[机器学习的数学基础[3] - 微积分在近似运算中的应用](./notes/1_Mathematical_Tutorial_4.md)  
[机器学习的数学基础[4] - Taylor公式及其应用](./notes/1_Mathematical_Tutorial_3.md)  
[机器学习的数学基础[5] - 概率论中的数字特征](./notes/Probability_Tutorial_2.md)  
[机器学习的数学基础[6] - 对协方差与皮尔逊相关系数的进一步讨论](./notes/Probability_Tutorial_1.md)  
[机器学习的数学基础[7] - 信息论基础](./notes/1_Mathematical_Tutorial_5.md)  

概率论的应用[1] - 生日悖论  
[概率论的应用[2] - 组合数与信息熵](./notes/Probability_Tutorial_3.md)  
概率论的应用[3] - taylor公式与Gini系数&信息熵  
概率论的应用[4] - taylor公式与泊松分布  
概率论的应用[5] - 本福特定律  

[最优化算法[1] - 求解无约束优化问题的方法：梯度下降法，牛顿法](./notes/Optimization_Tutorial_1.md)  

### PART II 模型 Model
#### 线性回归 Linear Regression
[线性回归[1] - 模型建立](./notes/LinearRegression_Tutorial_1.md)  
[线性回归[2] - 最小均方误差损失与模型求解(最小二乘法&梯度下降法)](./notes/LinearRegression_Tutorial_2.md)  
[线性回归[3] - 最大似然估计与线性回归模型的先验假设](./notes/LinearRegression_Tutorial_3.md)  
[线性回归[4] - 最大似然估计与最小均方误差损失的等价性](./notes/LinearRegression_Tutorial_4.md)  
线性回归的扩展[1] - 对特征做扩展 - 多项式回归Polynomial Regression  
线性回归的扩展[2] - 损失函数引入Normalization - Lasso/Ridge/ElasticNet  
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/6_LinearRegression/pic/LinearR_GD_FittingCurve.gif" alt="" data-canonical-src="" width="420" height="400" />
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/6_LinearRegression/pic/LinearR_GD_LossFuncSurface.gif" alt="" data-canonical-src="" width="420" height="400" />

#### 逻辑回归 Logistic Regression
**Logistic Regression - 二分类器**  
[逻辑回归[1] - 解决二分类问题的思路](./notes/LogisticRegression_Tutorial_1.md)  
[逻辑回归[2] - 模型求解](./notes/LogisticRegression_Tutorial_2.md)  
[逻辑回归[3] - 从损失函数的角度看逻辑回归](./notes/LogisticRegression_Tutorial_3.md)  
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/7_LogisticRegression/pic/LogisticR_GD_FittingCurve.gif" alt="" data-canonical-src="" width="420" height="400" />  
sklearn-LR参数详解  
**SoftMax Regression - 多分类器**  
逻辑回归与最大熵模型  

#### 广义线性模型 Generalized Linear Model,GLM
[GLM[1] - 指数分布族](./notes/GLM_Tutorial_1.md)  
[GLM[2] - 广义线性模型](./notes/GLM_Tutorial_2.md)

#### 决策树 Desicion Tree
[决策树概述](./notes/DT_Tutorial_1.md)   
[分类决策树的生成：ID3 / C4.5](./notes/DT_Tutorial_2.md)  
[分类回归树的生成：CART](./notes/DT_Tutorial_3.md)  
树剪枝：Pruning  
[决策树的两要素与函数本质](./notes/DT_Tutorial_5.md)  

#### 集成方法(Ensemble Methods)
Bootstrap与Bagging  
[Boosting概述之一：从参数空间到函数空间](./notes/Boosting_Tutorial_0.md)  
[Boosting概述之二：模型表达式](./notes/Boosting_Tutorial_1.md)   
[XGBoost算法原理](./notes/Boosting_Tutorial_2.md)  
Adaboost  
对比GBDT与XGboost  
sklearn-GBDT参数详解
... ...  

### PART III 工程化应用

#### 特征工程 Feature Engineering
[特征工程[1] - 数据摘要 Summary of dataSet](./notes/FeatureEngineering_1.md) [例1]() [例2](./study/10_FeatureEngineering/files/PPD_summary_da.csv)  
[特征工程[2] - 日期特征的处理](./notes/FeatureEngineering_2.md)  
[特征工程[3] - 逻辑特征的处理](./notes/FeatureEngineering_3.md)  
[特征工程[4] - 标准化处理：中心归一标准化(Z-Score)与正态标准化(Normalization)]()  
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/10_FeatureEngineering/pic/zscore_normalization_1.png" alt="" data-canonical-src=""  />  
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/10_FeatureEngineering/pic/zscore_normalization_2.png" alt="" data-canonical-src=""  />  

#### 代码复用 Code Reuse
[代码复用 - 概述与两种基本形式](./notes/CodeReuse_1.md)  
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/10_FeatureEngineering/pic/CodeReuse_pattern_1.png" alt="" data-canonical-src="" width="420"  />
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/10_FeatureEngineering/pic/CodeReuse_pattern_2.png" alt="" data-canonical-src="" width="420"  />  

#### 黑科技 Tricks
**模型调参**  
sklearn调参基础——模型概览  
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/10_FeatureEngineering/pic/TunPara_Tutorial.png" alt="" data-canonical-src=""  />  
sklearn调参实战——LR  
[sklearn调参实战——GBM算法](./notes/ParaTuning_GBM.md)  
sklearn调参实战——XGBoost  
[hyperopt: Distributed Asynchronous Hyperparameter Optimization in Python](http://hyperopt.github.io/hyperopt/)  

### PART IV 个人总结
[如何形式化描述机器学习问题？](./notes/Summary_Tutorial_1.md)  
[机器学习中的损失函数](./notes/Summary_Tutorial_2.md)  

## 附录A Python基础
### 重要的第三方库
#### [Numpy Basics](./study/4_PythonFoundation/numpyBasics/)
#### [Pandas Basics](./study/4_PythonFoundation/pandasBasics/)
#### [Scipy Basics](./study/4_PythonFoundation/scipyBasics/)
#### [Matplotlib Basics](./study/4_PythonFoundation/matplotlibBasics/)
#### [sklearn Basics](./study/5_SklearnFoundation/script/)

### 综合应用
[1 - 文件读取](./study/4_PythonFoundation/loadData/)  
[2 - Python多线程](./study/4_PythonFoundation/multiThreading/)

## 附录B 数据集

[1. 疝气病马存活情况数据集：Horse Colic Data Set](http://archive.ics.uci.edu/ml/datasets/Horse+Colic)  
*该数据集来自2010年1月11日的UCI机器学习数据库，原始数据包含368个样本和28个特征*  
**应用索引**  
[LogisticRegression with sklearn](./study/7_LogisticRegression/script/LogisticRegression_sklearn_HorseColic.py)