# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

plt.close('all')

def piecewise_linear_point(x, a, b):
    a = np.array(a, dtype = np.float).reshape(-1, 1)
    b = np.array(b, dtype = np.float).reshape(-1, 1)
    if a.shape[0] != b.shape[0]:
        raise ValueError('a.shape[0] != b.shape[0]')
    values= np.zeros_like(a)
    for i in range(len(a)):
        #values[i] = x * a[i] + b[i]
        values[i] = np.dot(a[i].T, x) + b[i]
    y = np.max(values)
    return y

def piecewise_linear_surface(x, a, b):
    y = np.zeros_like(x)
    for i in range(x.shape[0]):    
        y[i] = piecewise_linear_point(x[i], a, b)
    return y
          
x = np.linspace(-10, 10, 250).reshape(-1, 1)

a = [-1, 0, 1]
b = [1, 5, -1]

        
plt.figure()
plt.plot(x, piecewise_linear_surface(x, a, b))
plt.suptitle('a piecewize - linear function')
plt.show()

    

    
    


