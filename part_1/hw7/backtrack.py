# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:09:02 2020

@author: Andrei
"""


import numpy as np
alpha = 0.3
beta = 0.8

f = lambda x: (x[0]**2 + 3*x[1]*x[0] + 12)
dfx1 = lambda x: (2*x[0] + 3*x[1])
dfx2 = lambda x: (3*x[0])

def gradf(x):
    return np.array([dfx1(x), dfx2(x)]).reshape([-1, 1])

t = 1
count = 1
x0 = np.array([2,3])
print('x0 = ', x0)
print('x0.shape = ', x0.shape)
# dx0 = np.array([.1, 0.05])


def backtrack(x0, dfx1, dfx2, t, alpha, beta, count):
    while (f(x0) - (f(x0 - t*np.array([dfx1(x0), dfx2(x0)])) 
                    + alpha * t * np.dot(np.array([dfx1(x0), dfx2(x0)]), 
                                         np.array([dfx1(x0), dfx2(x0)])))) < 0:
        t *= beta
        print("""

########################
###   iteration {}   ###
########################
""".format(count))
        print("Inequality: ",  f(x0) - (f(x0 - t*np.array([dfx1(x0), dfx2(x0)])) + alpha * t * np.dot(np.array([dfx1(x0), dfx2(x0)]), np.array([dfx1(x0), dfx2(x0)]))))
        count += 1
        
    return t

t = backtrack(x0, dfx1, dfx2, t, alpha, beta,count)

print("\nfinal step size :",  t)

def backtrack2(x, grad, alpha, beta):
    """
    Backtracking line search
    """    
    t = 1
    while True: 
        fx = f(x - t * grad)
        fxx = f(x) + alpha * t * np.dot(grad.T, grad)
        if np.isnan(fx) or np.isnan(fxx):
            print('backtrack: nan detected; multilying t: t = ', t)
            t *= beta
        elif fx > fxx:
            t *= beta
            print('backtrack: multiplying t: t = ', t)
        else: 
            print('backtrack: t found, returning: t = ', t)
            return t

x = x0.reshape([-1, 1])

t = backtrack2(x, gradf(x), alpha, beta)

