# sklearn调参实战——GBM算法
## 声明
本文档参考自[Analyticsvidhya：Complete Guide to Parameter Tuning in Gradient Boosting (GBM) in Python](https://www.analyticsvidhya.com/blog/2016/02/complete-guide-parameter-tuning-gradient-boosting-gbm-python/#)。  
主要对作者Aarshay Jain阐述的GBM调参方法进行了梳理与总结。  
原文中译版本[CSDN-寒小阳机器学习系列-Python中Gradient Boosting Machine(GBM）调参方法详解](http://blog.csdn.net/han_xiaoyang/article/details/52663170)  

## GBM模型参数总结

请参考文章

## GBM调参方法总结
备注：本文的调参结果和[原文](https://www.analyticsvidhya.com/blog/2016/02/complete-guide-parameter-tuning-gradient-boosting-gbm-python/#)有一定差异。重点放在思路与步骤，而不是调参结果上。

### GBM调参基本思路

>Approach for tackling the problem
>1. Run a Baseline Model.
>2. Decide a relatively higher value for learning rate and tune the number of estimators requried for that.
>3. Tune the tree specific parameters for that learning rate.
>4. Tune subsample.
>5. Lower learning rate as much as possible computationally and increase the number of estimators accordingly.

### GBM调参步骤
#### 1. Running a Baseline Model
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/10_FeatureEngineering/pic/GBM_TunPara_Baseline.png" alt="" data-canonical-src=""  />  

#### 2. Tunning the number of estimators(`n_estimator`) with a relatively high learning rate

>We will use the following benchmarks for parameters:
>1. min_samples_split = 500 :  ~0.5-1% of total values. Since this is imbalanced class problem, we'll take small value
>2. min_samples_leaf = 50 :  Just using for preventing overfitting. will be tuned later.
>3. max_depth = 8 :  since high number of observations and predictors, choose relatively high value
>4. max_features = 'sqrt' : general thumbrule to start with
>5. subsample = 0.8 :  typically used value (will be tuned later)

>0.1 is assumed to be a good learning rate to start with. Let's try to find the optimum number of estimators requried for this.

<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/10_FeatureEngineering/pic/GBM_TunPara_GS_n_estimator.png" alt="" data-canonical-src=""  />  

#### 3. Tune the tree-specific parameters
>1. Tune max_depth and num_samples_split
>2. Tune min_samples_leaf
>3. Tune max_features

##### 3.1 Tune `max_depth` and `num_samples_split`
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/10_FeatureEngineering/pic/GBM_TunPara_GS_3_1.png" alt="" data-canonical-src=""  />  

##### 3.2 Tune `min_samples_leaf`
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/10_FeatureEngineering/pic/GBM_TunPara_GS_3_2.png" alt="" data-canonical-src=""  />  

##### 3.3 Compare with Baseline Model
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/10_FeatureEngineering/pic/GBM_TunPara_Baseline.png" alt="" data-canonical-src=""  />  
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/10_FeatureEngineering/pic/GBM_TunPara_GS_3_3.png" alt="" data-canonical-src=""  />  

##### 3.4 Tune `max_features`
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/10_FeatureEngineering/pic/GBM_TunPara_GS_3_4.png" alt="" data-canonical-src=""  />  

#### 4. Tune `subsample` and Lower Learning Rate
##### 4.1 Tune `subsample`
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/10_FeatureEngineering/pic/GBM_TunPara_GS_4_1.png" alt="" data-canonical-src=""  />  

##### 4.2 Decrease the learning rate to half, with twice the number of trees.

**learning_rate=0.05, n_estimators=120**  
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/10_FeatureEngineering/pic/GBM_TunPara_GS_4_2_1.png" alt="" data-canonical-src=""  />  
**learning_rate=0.01, n_estimators=600**  
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/10_FeatureEngineering/pic/GBM_TunPara_GS_4_2_2.png" alt="" data-canonical-src=""  />  
**learning_rate=0.005, n_estimators=1200**  
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/10_FeatureEngineering/pic/GBM_TunPara_GS_4_2_3.png" alt="" data-canonical-src=""  />  
**learning_rate=0.005, n_estimators=1500**  
<img src="https://github.com/CaoZhens/ML_Learning/blob/master/study/10_FeatureEngineering/pic/GBM_TunPara_GS_4_2_4.png" alt="" data-canonical-src=""  />  