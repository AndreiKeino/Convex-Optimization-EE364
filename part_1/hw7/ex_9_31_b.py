# -*- coding: utf-8 -*-

import numpy as np
import ex_9_30_test_hessian as h
import matplotlib.pyplot as plt
plt.close('all')

f = h.f

np.random.seed(3)

m, n = 18, 10

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


# the Newton's method implementation
while True:
    
    print('iteration number ', iter_num)
    grad = h.gradf(x, a) #  gradient of f
    hess = h.hessf(x, a) #  hessian of f
    # Diagonal approximation. We replace the Hessian by its diagonal
    ihess = np.diag(1 / np.diagonal(hess))
    # ihess = np.linalg. inv(hess) #  inverse hessian of f
    dx = - ihess @ grad #  Newton step
    lam_sq = grad.T @ (ihess @ grad) # Newton decrement

    print('lam_sq = %e' % lam_sq)
    if np.sqrt(lam_sq / 2) <= nu_min:
        print("Newton's method: tolerance achieved, exiting...")
        print('iteration number ', iter_num)
        #  print('a = ', a)
        print('optimal value = %e' % f(x, a))
        print('optimal x = ', x)
        break
    #  Backtracking line search

    t = h.backtrack_2(x, a, grad, ihess, alpha, beta)
    step = t
    # step = 1

    print('step =', step)
    
    x = x + step * dx
    
    print('new x = ', x)    
    iter_num += 1
    if iter_num >= max_iters:
        print("Newton's method: max_iters number exeeded")
        break
    
def newton_method(alpha, beta):
    
    obj_func_arr = []
    step_arr = []
    iter_num = 0
    x = x_start

    
    while True:
        
        print('iteration number ', iter_num)
        obj_func_arr.append(f(x, a))
        grad = h.gradf(x, a) #  gradient of f
        hess = h.hessf(x, a) #  hessian of f
        # Diagonal approximation. We replace the Hessian by its diagonal
        ihess = np.diag(1 / np.diagonal(hess))

        dx = - ihess @ grad #  Newton step
        lam_sq = grad.T @ (ihess @ grad) # Newton decrement
    
        print('lam_sq = %e' % lam_sq)
        if np.sqrt(lam_sq / 2) <= nu_min:
            print("Newton's method: tolerance achieved, exiting...")
            print('iteration number ', iter_num)
            #  print('a = ', a)
            print('optimal value = %e' % f(x, a))
            print('optimal x = ', x)
            return np.array(obj_func_arr) - f(x, a), step_arr
            break
        #  Backtracking line search
    
        t = h.backtrack_2(x, a, grad, ihess, alpha, beta)
        step = t
        step_arr.append(step)
    
        print('step =', step)
        
        x = x + step * dx
        
        print('new x = ', x)    
        iter_num += 1
        if iter_num >= max_iters:
            print("Newton's method: max_iters number exeeded")
            break

# plot the graphs        
alpha_arr = [0.2, 0.4]

beta_arr = [0.2, 0.45]

plt.figure()

for alpha in  alpha_arr:
    for beta in beta_arr:
        print('alpha = ', alpha)
        print('beta = ', beta)
        obj_func, step =  newton_method(alpha, beta)
        x_plt = range(len(obj_func))
        plt.plot(x_plt, np.log10(obj_func), 
                 label='alpha = ' + str(alpha) + ' beta = ' + str(beta))

plt.title('logarithm of the objective function error vs iteration number')
plt.ylabel('logarithm of the objective function error')
plt.xlabel('iteration number')
plt.legend()
plt.show()

plt.savefig('9_31_b_obj_func.png', bbox_inches='tight')


plt.figure()

for alpha in  alpha_arr:
    for beta in beta_arr:
        print('alpha = ', alpha)
        print('beta = ', beta)
        obj_func, step =  newton_method(alpha, beta)
        x_plt = range(len(step))
        plt.plot(x_plt, step, 
                 label='alpha = ' + str(alpha) + ' beta = ' + str(beta))

plt.title('step vs iteration number')
plt.ylabel('step')
plt.xlabel('iteration number')
plt.legend()
plt.show()

plt.savefig('9_31_b_step.png', bbox_inches='tight')
    
        
    


              
              
