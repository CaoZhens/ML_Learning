# coding: utf-8
'''
Created on Dec 14, 2017
@author:
    CaoZhen
@desc:
    Basic Usage of numpy.stack & numpy.vstack
@reference:
    
'''

import numpy as np
import pandas as pd


filePath = '/Users/fanghan/mlproject/ML_Learning/datasets'
# df = pd.read_table('{}/pf_ld_ex3_from_Woplus_talklen.txt'.format(filePath), sep='|')
# print df.head()

# DataFrame.pivot
# DataFrame.pivot(index=None, columns=None, values=None)[source]
# Reshape data (produce a “pivot” table) based on column values. Uses unique values from index / columns to form axes of the resulting DataFrame.

# Parameters:	
# index : string or object, optional
# Column name to use to make new frame’s index. If None, uses existing index.
# columns : string or object
# Column name to use to make new frame’s columns
# values : string or object, optional
# Column name to use for populating new frame’s values. If not specified, all remaining columns will be used and the result will have hierarchically indexed columns
# Returns:	
# pivoted : DataFrame
# print df.pivot(index='imsi', columns='mon').head()

# Basic Example
# 1. pivot
# Pivot a table based on column values.
df1 = pd.DataFrame({'foo': ['one','one','one','two','two','two'],
                       'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                       'baz': [1, 2, 3, 4, 5, 6]})
print 'df1:\n', df1
print 'df1.pivot(index=\'foo\', columns=\'bar\'):\n', df1.pivot(index='foo', columns='bar')
print 'df1.pivot(index=\'foo\', columns=\'bar\'):\n', df1.pivot(index='foo', columns='bar', values='baz')
print 'df1.pivot(index=\'foo\', columns=\'bar\')[\'baz\']:\n', df1.pivot(index='foo', columns='bar')['baz']
# pivot的特点 pivot without aggregation that can handle non-numeric data
# 不能做aggregation，因此行数据必须具有唯一性
# index和column参数仅支持单一取值，不支持多取值
# 可以handle non-numeric data

# 2. pivot_table
# generalization of pivot that can handle duplicate values for one index/column pair
df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                          "bar", "bar", "bar", "bar"],
                    "B": ["one", "one", "one", "two", "two",
                          "one", "one", "two", "two"],
                    "C": ["small", "large", "large", "small",
                          "small", "large", "small", "small",
                          "large"],
                    "D": [1, 2, 2, 3, 3, 4, 5, 6, 7]})
print 'df:\n', df
print df.pivot_table(values='D', index=['A','B'], columns=['C'], aggfunc=np.sum)
print df.pivot_table(values='D', index=['A','B'], columns=['C'], aggfunc=np.sum, fill_value=0)
# pivot_table的特点：
# 可以handle duplicate values for index/columns pair，即不要求行数据具有唯一性
# 根据上一条，肯定支持数据聚合 aggregation
# 支持multi-index

# 3. unstack
# pivot based on the index values instead of a column
print df1
print df1.set_index(['foo','bar'])
print df1.set_index(['foo','bar']).unstack()
print df1.set_index(['foo','bar']).unstack(level=-1)
print df1.set_index(['foo','bar']).unstack(level=0)
# unstack的特点
# pivot based on the index values instead of a column
# 默认level=-1即最后一个index

# pivot与unstack的对比
# pivot／pivot_table是将column分别安置于index／column／value
# unstack是将index做pivot处理