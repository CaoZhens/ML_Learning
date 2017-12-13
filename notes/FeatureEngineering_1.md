# 数据摘要

## 内容
对数据的每个特征（列），分析以下内容：
* 类型 `dtypes`
* 基础统计量（均值、方差、四分位数含最值）`describe()`
* 空值／非空值个数 `isnull().sum()` `notnull().sum()`
* 出现频数TOP-n的值与数量，及其它所有非空值数量 [`pandas.Series.value_counts`](../study/4_PythonFoundation/pandasBasics/value_counts.py)

## API
```python
def Value_counts(das, nhead = 5):
    tmp = pd.value_counts(das).reset_index().rename_axis({'index': das.name}, axis = 1)
    value = pd.DataFrame(['value {}'.format(x+1) for x in range(nhead)], index = np.arange(nhead)).join(tmp.iloc[:,0], how = 'left').set_index(0).T
    freq = pd.DataFrame(['freq {}'.format(x+1) for x in range(nhead)], index = np.arange(nhead)).join(tmp.iloc[:,1], how = 'left').set_index(0).T
    nnull = das.isnull().sum()
    freqother = pd.DataFrame({das.name: [das.shape[0]-nnull-np.nansum(freq.values), nnull]}, index = ['freq others', 'NA']).T
    op = pd.concat([value, freq, freqother], axis = 1)
    return(op)

def Summary(da):
    op = pd.concat([pd.DataFrame({'type': da.dtypes, 'non-NA': da.notnull().sum(axis = 0)}), 
                    da.describe().T.iloc[:,1:], 
                    pd.concat(map(lambda i: Value_counts(da.loc[:,i]), da.columns))], axis = 1).loc[da.columns]
    op.index.name = 'Columns'
    return(op)
```