# -*- coding: utf-8 -*-

import numpy as np
import ex_9_30_test_hessian as h

f = h.f

np.random.seed(1)

m, n = 4, 2

a = np.random.random([m, n]).T
        

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


# t = h.backtrack(x, a, h.gradf(x, a), alpha, beta)
# print('t after backtrack = ', t)

# the Newton's method implementation
while True:
    
    print('iteration number ', iter_num)
    grad = h.gradf(x, a) #  gradient of f
    hess = h.hessf(x, a) #  hessian of f
    ihess = np.linalg. inv(hess) #  inverse hessian of f
    dx = - ihess @ grad #  Newton step
    lam_sq = grad.T @ (ihess @ grad) # Newton decrement

    print('lam_sq = %e' % lam_sq)
    if lam_sq / 2 <= nu_min:
        print("Newton's method: tolerance acieved, exiting...")
        print('iteration number ', iter_num)
        print('optimal value = %e' % f(x, a))
        print('optimal x = ', x)
        break
    #  Backtracking line search

    t = h.backtrack(x, a, grad, alpha, beta)
    step = t

    print('step =', step)
    
    print('grad = ', grad)
    
    x = x + step * dx
    
    print('new x = ', x)    
    iter_num += 1
    if iter_num >= max_iters:
        print("Newton's method: max_iters number exeeded")
        break
        
    
    
    


