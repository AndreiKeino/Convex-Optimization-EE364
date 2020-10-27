# -*- coding: utf-8 -*-
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.check_grad.html

import numpy as np

def gradient_numerical(f, x0, delta = 1e-8):
    """
    function calculates the numerical gradient for function f in 
    the point x0
    """
    N = len(x0)
    grad_num = np.zeros([N, 1])
    for i in range(N):
        xi_plus = x0.copy()
        xi_plus[i] += delta

        xi_minus = x0.copy()
        xi_minus[i] -= delta
        
        grad_num[i] = (f(xi_plus) - f(xi_minus)) / (2 * delta)       
    return grad_num


def check_grad(f, gradf, x0, delta = 1e-8, verbose = True):
    grad = np.array(gradf(x0))
    grad_num = gradient_numerical(f, x0, delta)
    if (verbose):
        print('check_grad: precise gradient = ', grad)
        print('check_grad: approximate gradient = ', grad_num)
        print('check_grad: gradient error = ', grad - grad_num)        
        
    return np.sqrt(np.sum((grad - grad_num) ** 2))


np.random.seed(1)

m, n = 3, 2

a = np.random.random([m, n]).T

#  a = np.array([[-1, 0], [0.5, - 0.5], [0.5, 0]], dtype = np.float64).T

x0 = 0.5 * np.ones([n, 1]) 
x = np.array([-0.25, 0.75], dtype = np.float64).reshape(- 1, 1)



print('a.shape = ', a.shape)

def f(x, a):
    #  calculation of the function value
    if not np.all(a.T @ x < 1):
        return np.nan
    if not np.all(np.abs(x) <= 1):
        return np.nan
    ret1 = 0.0
    ret1 = - np.sum(np.log(1 - a.T @ x))  
    ret2 =  - np.sum(np.log(1 - np.square(x)))
    return ret1 + ret2

#  print('f(x, a) = ', f(x, a))

def gradf(x, a):
    #  calculation of the function gradient

    if not np.all(a.T @ x < 1):
        return np.nan
    if not np.all(np.abs(x) <= 1):
        return np.nan
    print('x = ', x)
    
    ret1 = a @ (1 / (1 - a.T @ x))
    # ret1 = 0.0
    ret2 = 2 * x * (1 / (1 - x ** 2))
    return ret1 + ret2

#  x = np.array([0.5, 0.75])

#x = np.array([-0.75, 0.5], dtype = np.float64).reshape(- 1, 1)

error1 = check_grad(lambda x: f(x, a), lambda x: gradf(x, a), x0)

print('gradient error1 = ', error1)

"""
def grad2(x):
    x1 = x[0]
    x2 = x[1]
    grad = [2 * x1 / (1 - x1 ** 2), 2 * x2 / (1 - x2 ** 2)]
    return np.array(grad).reshape([-1, 1])


error2 = check_grad(lambda x: f(x, a), grad2, x0)

print('gradient error2 = ', error2)

x0 = - 0.5 * np.ones([n, 1]) 
fl3 = lambda x: (x[0]**2 + 3*x[1]*x[0] + 12)

def f3(x):
    return (x[0]**2 + 3*x[1]*x[0] + 12)[0]

dfx1 = lambda x: (2*x[0] + 3*x[1])
dfx2 = lambda x: (3*x[0])

def gradf3(x):
    return np.array([dfx1(x), dfx2(x)]).reshape([-1, 1])


error3 = check_grad(f3, gradf3, x0)

print('gradient error3 = ', error3)
       
        
        
error4 = check_grad(f3, gradf3, x0)

print('gradient error4 = ', error4)
"""     
