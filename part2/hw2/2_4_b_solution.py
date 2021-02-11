# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 19:14:16 2021

@author: Andrei
"""

import numpy as np

"""
Let J = 15, n = 10, m = 200 and  = 1. Generate random matrices
A1; : : : ;AJ 2 Rmn with independent Gaussian entries with mean 0 and variance
1=m, and, random vectors x1; : : : ; xJ 2 Rn with independent Gaussian with mean
0 and variance 1=n, then set b =
PJ
j=1 Axj .
"""

J = 15
n = 10
m = 200
# https://numpy.org/doc/stable/user/basics.broadcasting.html
# A = np.random.normal(loc=0, scale=1 / np.sqrt(m), size=(m, n, J)) / np.sqrt(m)
# x = np.random.normal(loc=0, scale=1 / np.sqrt(n), size=(n, J)) / np.sqrt(m)

# https://stackoverflow.com/questions/35894631/multiply-array-of-vectors-with-array-of-matrices-return-array-of-vectors

A = np.random.normal(loc=0, scale=1 / np.sqrt(m), size=(J, m, n)) / np.sqrt(m)
x = np.random.normal(loc=0, scale=1 / np.sqrt(n), size=(J, n, 1)) / np.sqrt(m)

# https://numpy.org/doc/stable/reference/generated/numpy.matmul.html

b = np.matmul(A, x).sum(axis=0)
print('b.shape = ', b.shape)

