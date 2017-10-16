# coding: utf-8
'''
Created  on Oct 13, 2017
Modified on Oct 16, 2017
@author:
    CaoZhen
@description:
    scipy.sparse.csr_matrix Usage in Scipy
@reference:
    1. https://docs.scipy.org/doc/scipy-0.19.1/reference/generated/scipy.sparse.csr_matrix.html
'''

import numpy as np
from scipy.sparse import csr_matrix

# 1
print csr_matrix((3,4), dtype=np.int8).toarray()

# 2
row = np.array([0, 0, 1, 2, 2, 2])
col = np.array([0, 2, 2, 0, 1, 2])
data = np.array([1, 2, 3, 4, 5, 6])
print csr_matrix((data, (row, col)), shape=(3, 3)).toarray()

# 3! 没看懂
