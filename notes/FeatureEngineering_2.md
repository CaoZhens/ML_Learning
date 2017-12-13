# 日期特征工程

## 内容
对日期特征，分析以下内容：
* 年 `DatetimeIndex.year #The year of the datetime`
* 月 `DatetimeIndex.month #The month as January=1, December=12`
* 日 `DatetimeIndex.day`
* 每周第几天 `DatetimeIndex.dayofweek #The day of the week with Monday=0, Sunday=6`
* 每年第几天 `DatetimeIndex.dayofyear #The ordinal day of the year`
* 与最早时间的天数差 `(d1-d2).astype('timedelta64[D]')`