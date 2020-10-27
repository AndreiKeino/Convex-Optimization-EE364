# -*- coding: utf-8 -*-
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.check_grad.html

import numpy as np

def backtrack(x, a, grad, alpha, beta):
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
        

def backtrack_2(x, a, grad, ihess, alpha, beta):
    """
    Backtracking line search
    https://stackoverflow.com/questions/52204231/implementing-backtracking-line-search-algorithm-for-unconstrained-optimization-p
    """
    """    
    print('grad.shape = ', grad.shape)
    print('grad = ', grad)
    print('ihess.shape = ', ihess.shape)
    print('ihess = ', ihess)
    """
    gh = grad.T @ ihess
    #  print('grad.T @ ihess = ', gh)

    
    t = 1
    while True: 
        #  print('x = ', x)
        #  print('gh = ', gh)
        
        fx = f(x - t * gh , a)
        
        fxx = f(x, a) + alpha * t * np.sum(gh ** 2)
        #  fxx = f(x, a) + alpha * t * np.dot(gh, gh.T) #  the same as f(x, a) + alpha * t * np.sum(gh ** 2)
        
        if np.isnan(fx) or np.isnan(fxx):
            #  print('backtrack: nan detected; multilying t: t = ', t)
            t *= beta
        elif fx > fxx:
            t *= beta
            #  print('backtrack: multilying t: t = ', t)
        else: 
            #  print('backtrack: t found, returning: t = ', t)
            return t

def L2norm(x):
    return np.sqrt(np.sum(x ** 2))


def derivative_numerical(f, x0, i, delta = 1e-8):
    xi_plus = x0.copy()
    xi_plus[i] += delta

    xi_minus = x0.copy()
    xi_minus[i] -= delta
    return (f(xi_plus) - f(xi_minus)) / (2 * delta)



def gradient_numerical(f, x0, delta = 1e-8):
    """
    function calculates the numerical gradient for function f in 
    the point x0
    """
    N = len(x0)
    grad_num = np.zeros([N, 1])
    for i in range(N):
        grad_num[i] = derivative_numerical(f, x0, i, delta)
    return grad_num


def check_grad(f, gradf, x0, delta = 1e-8, verbose = True):
    grad = np.array(gradf(x0))
    grad_num = gradient_numerical(f, x0, delta)
    if (verbose):
        print('check_grad: precise gradient = ', grad)
        print('check_grad: approximate gradient = ', grad_num)
        print('check_grad: gradient error = ', grad - grad_num)        
        
    return np.sqrt(np.sum((grad - grad_num) ** 2))

def second_derivative_numerical(f, x0, i, k, delta = 1e-5):
    """
	function calculates second derivative
    returns d^2f/(dx_k dx_i)
    """
    xk_plus = x0.copy()
    xk_plus[k] += delta

    xk_minus = x0.copy()
    xk_minus[k] -= delta
    
    dfi_plus = derivative_numerical(f, xk_plus, i, delta)
    dfi_minus = derivative_numerical(f, xk_minus, i, delta)
    
    return (dfi_plus - dfi_minus) / (2 * delta)

def hessian_numerical(f, x0, delta = 1e-5):
    """
	#  function calculates the hessian matrix
    """
    assert x.shape[1] == 1, 'hessian_numerical: input array should have shape [N, 1]'
        
    N = len(x)
    hessian = np.zeros([N, N], dtype = np.float64)
    for i in range(N):
        for k in range(i, N):
            hessian[i, k] = second_derivative_numerical(f, x0, i, k, delta)
            if i != k:
                hessian[k, i] = hessian[i, k]
    return hessian

def check_hessian(f, hess_analytical, x0, delta = 1e-5, verbose = True):
    """
	function checks he hessian matrix
    """
    hessian_analytical = np.array(hess_analytical)
    hessian_num = hessian_numerical(f, x0, delta)
    if verbose:
        print('check_hessian: hessian_analytical = ', hessian_analytical)
        print('check_hessian: hessian_num = ', hessian_num)
        print('check_hessian: hessian difference = ', 
              hessian_analytical - hessian_num)
        
    return np.sqrt(np.sum((hessian_analytical - hessian_num) ** 2))

#%%
# definitions for the function, gradient and hessian

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
    #  print('x = ', x)
    
    ret1 = 0.0    
    ret1 = a @ (1 / (1 - a.T @ x))
    ret2 = 2 * x * (1 / (1 - x ** 2))
    return ret1 + ret2

def hessf(x, a):
    if not np.all(a.T @ x < 1):
        return np.nan
    if not np.all(np.abs(x) <= 1):
        return np.nan
    ret1 = 0
    ret1 = a @ (a.T * (1 / (1 - a.T @ x) ** 2))
    ret2 = 2 * (1 + x ** 2) / ((1 - x ** 2) ** 2)
    ret2 = np.diagflat(ret2)
    
    return ret1 + ret2


if __name__ == "__main__":
    
    np.random.seed(1)
    
    m, n = 3, 2
    
    a = np.random.random([m, n]).T
    
    #  a = np.array([[-1, 0], [0.5, - 0.5], [0.5, 0]], dtype = np.float64).T
    
    x0 = 0.5 * np.ones([n, 1]) 
    x = np.array([-0.25, 0.75], dtype = np.float64).reshape(- 1, 1)
    
    
    
    print('a.shape = ', a.shape)
    
    
    #  x = np.array([0.5, 0.75])
    
    #x = np.array([-0.75, 0.5], dtype = np.float64).reshape(- 1, 1)
    
    error1 = check_grad(lambda x: f(x, a), lambda x: gradf(x, a), x0)
    
    assert error1 < 1e-6, 'error1 too big'
    
    print('gradient error1 = ', error1)
    
    
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
           
    assert error3 < 1e-6, 'error3 too big'
            
    error4 = check_grad(f3, gradf3, x0)
    
    print('gradient error4 = ', error4)
    
    assert error4 < 1e-6, 'error4 too big'
    
    #%%
    # test function for hessian 
    
    def fh(z):
        assert z.shape[0] == 2 and z.shape[1] == 1, 'fh(x): incorrect input shape'
    
        x = z[0]
        y = z[1]
        
        return x**2 + 0.5 * y**2 + 2 * x * y + 3 * x + 4 * x**2 * y**2 + 5 * y * x**2
    
    def fh_hessian(z):
        assert z.shape[0] == 2 and z.shape[1] == 1, 'fh_hessian(x): incorrect input shape'
    
        x = z[0]
        y = z[1]
        
        hessian = np.zeros([2, 2], dtype = np.float64)
        print('')
        hessian[0, 0] = 2 + 8 * y**2 + 10 * y
        hessian[0, 1] = 2 + 16 * x * y + 10 * x
        hessian[1, 0] = hessian[0, 1]
        hessian[1, 1] = 1 + 8 * x ** 2
        return hessian
    
    #%%
    
    
    #  test check_hessian function:
    
    x0 = np.array([0.5, 8], dtype=np.float64).reshape(-1, 1)
    
    #  x0 = np.array([0, 0], dtype=np.float64).reshape(-1, 1)
    
    #  x0 = np.array([1, 1], dtype=np.float64).reshape(-1, 1)
    
    hess_analytical = fh_hessian(x0)
    
      
    hd = check_hessian(fh, hess_analytical, x0, delta = 1e-5, verbose = True)
    
    print('test of check_hessian, diff = %e' % hd)
    
    # x0 = np.array([0.5, -0.25], dtype=np.float64).reshape(-1, 1)    
    x0 = np.array([-0.5, -0.75], dtype=np.float64).reshape(-1, 1)    
   
    v_hess_analytical = hessf(x0, a)
    
    print('v_hess_analytical = ', v_hess_analytical)
    
    
    v_hess_num = hessian_numerical(lambda x: f(x, a), x0)
    
    print('v_hess_num = ', v_hess_num)

    hc = check_hessian(lambda x: f(x, a), v_hess_analytical, x0)
    print('hc = ', hc)
    
    assert hc < 1e-4, 'hessian seems to be incorrect'
    
    grad = np.array([[3.26697727], [4.08950456]])    
    ihess = np.array([[ 0.31264018, -0.13959122],  [-0.13959122,  0.28763308]])
    print('grad.shape = ', grad.shape)
    print('ihess.shape = ', ihess.shape)
    y = grad.T @ ihess
    print('y = ', y)
    print('y.shape = ', y.shape)
    
    
    print(np.sum(y**2))