# sklearn调参基础——以GBM算法为例
## 声明
本文档参考自[Analyticsvidhya:Complete Guide to Parameter Tuning in Gradient Boosting (GBM) in Python](https://www.analyticsvidhya.com/blog/2016/02/complete-guide-parameter-tuning-gradient-boosting-gbm-python/#)。主要对作者Aarshay Jain阐述的GBM调参方法进行了梳理与总结。  
原文中译版本[CSDN:寒小阳机器学习系列:Python中Gradient Boosting Machine(GBM）调参方法详解](http://blog.csdn.net/han_xiaoyang/article/details/52663170)  

## GBM模型参数总结

请参考文章

## GBM调参方法总结

### GBM调参基本思路

>Approach for tackling the problem
>1. Run a Baseline Model for Comparison.
>2. Decide a relatively higher value for learning rate and tune the number of estimators requried for that.
>3. Tune the tree specific parameters for that learning rate.
>4. Tune subsample.
>5. Lower learning rate as much as possible computationally and increase the number of estimators accordingly.

### GBM调参步骤
1. Running a Baseline Model
<img src="https://github.com/CaoZhens/ML_Learning/tree/master/study/10_FeatureEngineering/pic/GBM_TunPara_Baseline.png" alt="" data-canonical-src=""  />

2. Tunning the number of estimators(`n_estimator`) for a relatively high learning rate

>We will use the following benchmarks for parameters:
>1. min_samples_split = 500 :  ~0.5-1% of total values. Since this is imbalanced class problem, we'll take small value
>2. min_samples_leaf = 50 :  Just using for preventing overfitting. will be tuned later.
>3. max_depth = 8 :  since high number of observations and predictors, choose relatively high value
>4. max_features = 'sqrt' : general thumbrule to start with
>5. subsample = 0.8 :  typically used value (will be tuned later)

>0.1 is assumed to be a good learning rate to start with. Let's try to find the optimum number of estimators requried for this.

<img src="https://github.com/CaoZhens/ML_Learning/tree/master/study/10_FeatureEngineering/pic/GBM_TunPara_GS_n_estimator.png" alt="" data-canonical-src=""  />  