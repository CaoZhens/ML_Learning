# coding: utf-8
'''
Created on  Oct 27, 2017
Modified on Oct 30, 2017
@author:
    CaoZhen
@description:
    1. Convert between list / ndarray / matrix
@reference:
    1. 
'''

import numpy as np

aList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1. list to ndarray / matrix
print '==========1. list to ndarray/matrix=========='
aArr = np.array(aList)
aMat = np.mat(aList)
print 'list:\t', aList
print 'ndarr:\t', aArr
print 'matrix:\t', aMat

# 2. matrix to ndarray
print '==========2. matrix to ndarray=========='
try:
    print aMat.toarray()
except Exception, e:
    print e
print np.asarray(aMat)
print np.array(aMat)

# 3. matrix to list
print '==========3. matrix to list=========='
print aMat.tolist()
print aMat.T.tolist()

# 4. ndarray/matrix - row to col
print '==========4. ndarray/matrix - row to col=========='
aArr2 = aArr[:, np.newaxis]
aMat2 = np.mat(aArr2)
print aArr2, type(aArr2)
print aMat[:, np.newaxis], type(aMat[:, np.newaxis])

# 5. ndarray - col to row
print '==========5. ndarray - col to row=========='
# Convert ndarray with 1 column to an array with M elements
print np.squeeze(aArr2)
print aArr2.reshape(-1)
print aArr2.flatten()
print aArr2.ravel()

# 6. matrix - col to row directly
print '==========6. matrix - col to row directly=========='
print aMat2.A1

# Conclusion
# mat have tolist() , don't have toarray(), use np.asarray() or np.array()