# -*- coding: utf-8 -*-

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.check_grad.html

# Convex optimization. gradient method.

import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

#  definition of some functions ->
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


def f(x, a):
    #  calculation of the function value
    if not np.all(a.T @ x < 1):
        return np.nan
    if not np.all(np.abs(x) <= 1):
        return np.nan
    ret1 = - np.sum(np.log(1 - a.T @ x))  
    ret2 =  - np.sum(np.log(1 - np.square(x)))
    return ret1 + ret2


def gradf(x, a):
    #  calculation of the function gradient

    if not np.all(a.T @ x < 1):
        return np.nan
    if not np.all(np.abs(x) <= 1):
        return np.nan
    print('x = ', x)
    
    ret1 = a @ (1 / (1 - a.T @ x))
    ret2 = 2 * x * (1 / (1 - x ** 2))
    return ret1 + ret2

def L2norm(x):
    return np.sqrt(np.sum(x ** 2))

def backtrack(x, grad, alpha, beta):
    """
    Backtracking line search
    https://stackoverflow.com/questions/52204231/implementing-backtracking-line-search-algorithm-for-unconstrained-optimization-p
    """    
    t = 1
    while True: 
        fx = f(x - t * grad, a)
        fxx = f(x, a) + alpha * t * np.dot(grad.T, grad)
        if np.isnan(fx) or np.isnan(fxx):
            #  print('backtrack: nan detected; multilying t: t = ', t)
            t *= beta
        elif fx > fxx:
            t *= beta
            #  print('backtrack: multilying t: t = ', t)
        else: 
            #  print('backtrack: t found, returning: t = ', t)
            return t
        
#  <- definition of some functions

np.random.seed(1)

m, n = 3, 2

a = np.random.random([m, n]).T
        
#  check the gradient calculation        

x_check = np.random.random([n, 1])

grad_err = check_grad(lambda x: f(x, a), lambda x: gradf(x, a), x_check)

assert grad_err < 1e-6, 'gradient calculation incorrect'

#  parameters for gradient descent method

nu_min = 1e-8 #  tolerance

step = 0.3

x_start = np.zeros([n, 1])

x = x_start


iter_num = 0

max_iters = 1000

max_line_search_iters = 1000

alpha = 0.4

beta = 0.4

print('x_start = ', x_start)
print('x_start.shape = ', x_start.shape)


t = backtrack(x, gradf(x, a), alpha, beta)
print('t after backtrack = ', t)

# the gradient descent implementation
while True:
    
    print('iteration number ', iter_num)
    grad = gradf(x, a)
    nu = L2norm(grad)
    print('nu = %e' % nu)
    if nu <= nu_min:
        print('gradient descent: tolerance acieved, exiting...')
        print('iteration number ', iter_num)
        print('optimal value = %e' % f(x, a))
        print('optimal x = ', x)
        break
    #  Backtracking line search

    t = backtrack(x, grad, alpha, beta)
    step = t

    print('step =', step)
    
    print('grad = ', grad)
    
    x = x - step * grad
    
    print('new x = ', x)    
    iter_num += 1
    if iter_num >= max_iters:
        print('gradient descent: max_iters number exeeded')
        break
        
def gradient_descent(alpha, beta):
    
    obj_func_arr = []
    step_arr = []
    iter_num = 0
    x = x_start
    
    while True:
        
        print('iteration number ', iter_num)
        obj_func_arr.append(f(x, a))
        grad = gradf(x, a)
        nu = L2norm(grad)
        print('nu = %e' % nu)
        if nu <= nu_min:
            print('gradient descent: tolerance acieved, exiting...')
            print('iteration number ', iter_num)
            print('optimal value = %e' % f(x, a))
            return np.abs(np.array(obj_func_arr) - f(x, a)), step_arr
            print('optimal x = ', x)
            break
        #  Backtracking line search
    
        t = backtrack(x, grad, alpha, beta)
        step = t
    
        print('step =', step)
        
        print('grad = ', grad)
        
        x = x - step * grad
        step_arr.append(step)
        
        print('new x = ', x)    
        iter_num += 1
        if iter_num >= max_iters:
            print('gradient descent: max_iters number exeeded')
            return None, None
            break
        
alpha_arr = [0.2, 0.4]

beta_arr = [0.2, 0.45]

plt.figure()

for alpha in  alpha_arr:
    for beta in beta_arr:
        print('alpha = ', alpha)
        print('beta = ', beta)
        obj_func, step =  gradient_descent(alpha, beta)
        x_plt = range(len(obj_func))
        plt.plot(x_plt, np.log10(obj_func), 
                 label='alpha = ' + str(alpha) + ' beta = ' + str(beta))

plt.title('logarithm of the objective function error vs iteration number')
plt.xlabel('logarithm of the objective function error')
plt.ylabel('iteration number')
plt.legend()
plt.show()


plt.figure()

for alpha in  alpha_arr:
    for beta in beta_arr:
        print('alpha = ', alpha)
        print('beta = ', beta)
        obj_func, step =  gradient_descent(alpha, beta)
        x_plt = range(len(step))
        plt.plot(x_plt, step, 
                 label='alpha = ' + str(alpha) + ' beta = ' + str(beta))

plt.title('step vs iteration number')
plt.xlabel('step')
plt.ylabel('iteration number')
plt.legend()
plt.show()