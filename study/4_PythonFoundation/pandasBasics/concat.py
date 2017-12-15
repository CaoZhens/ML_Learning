# coding: utf-8
'''
Created on Dec 15, 2017
@author:
    CaoZhen
@description:
    1. Usage of concat
@reference:
    1. pandas.concat in Dash
'''

import numpy as np
import pandas as pd

# example 1: combine two Series
s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])
print s1
print s2
print pd.concat([s1, s2])

# Clear the existing index and reset it in the result by setting the ignore_index option to True.
print pd.concat([s1, s2], ignore_index=True)

# Add a hierarchical index at the outermost level of the data with the keys option.
print pd.concat([s1, s2], keys=['s1', 's2'])

# Label the index keys you create with the names option.
print pd.concat([s1, s2], keys=['s1', 's2'], names=['Series name', 'Row ID'])

# example 2: combine two dataframe with identical columns
df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
df2 = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])
print pd.concat([df1, df2])
print pd.concat([df1, df2], ignore_index=True)

# Combine DataFrame objects with overlapping columns and return everything. Columns outside the intersection will be filled with NaN values.
df3 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']], columns=['letter', 'number', 'animal'])
print pd.concat([df1, df3])

# Combine DataFrame objects with overlapping columns and return only those that are shared by passing inner to the join keyword argument.
print pd.concat([df1, df3], join='inner')

# Combine DataFrame objects horizontally along the x axis by passing in axis=1.
df4 = pd.DataFrame([['bird', 'polly'], ['monkey', 'george']], columns=['animal', 'name'])
print pd.concat([df1, df4], axis=1)
print pd.concat([df1, df3], axis=1)
print pd.concat([df1, df3], axis=1, ignore_index=True)

# Prevent the result from including duplicate index values with the verify_integrity option.
# print pd.concat([df1, df3], axis=1, verify_integrity=True)
print pd.concat([df1, df3], verify_integrity=True)