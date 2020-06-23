# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 17:12:33 2020

@author: Andrei
"""


from scipy.stats import iqr
import numpy as np

def qantile(x, q):
    return np.quantile(x, q, interpolation='higher')

def stm(x):
    s = 0
    for i in range(9):
        q = (i + 1) / 10
        print('i = ', i, ' q = ', q)
        print('qantile(x, q) = ', qantile(x, q))
        s = s + qantile(x, q)
    return s / (0.8 * len(x) + 1)

x1 = np.array([0] * 20)
x1[0] = 1
#x1[1] = 1
x2 = np.array([0] * 20)
x2[1] = 1
#x2[2] = 1

print("stm(x1) = ", stm(x1))
print("stm(x2) = ", stm(x2))
print('mean of stm(x1), stm(x2) = ', (stm(x1) + stm(x2)) / 2)
print('stm of mean of x1, x2 = ', stm(x1 + x2) / 2)

'''
x1 = np.array([0] * 20)
x1[0] = 17
#x1[1] = 17
x2 = np.array([0] * 20)
x2[0] = - 17
#x2[2] = - 17

print("stm(x1) = ", stm(x1))
print("stm(x2) = ", stm(x2))
print('mean of stm(x1), stm(x2) = ', (stm(x1) + stm(x2)) / 2)
print('stm of mean of x1, x2 = ', stm(x1 + x2) / 2)
'''