# -*- coding: utf-8 -*-
import numpy as np

N = 7
p = np.random.rand(N)
q = np.random.rand(N)

p = np.array(np.abs(p))
q = np.array(np.abs(q))

p = p / np.sum(p)
q = q / np.sum(q)

print('p = ', p)
print('q = ', q)

print('p.sum() = ', np.sum(p))
print('q.sum() = ', np.sum(q))
print('np.abs(p - q) = ', np.abs(p - q))
print('np.sum(np.abs(p - q)) = ', np.sum(np.abs(p - q)))
print('np.max(np.abs(p - q)) = ', np.max(np.abs(p - q))) 

ret = np.sum(np.abs(p - q)) / np.max(np.abs(p - q))

print('np.sum(np.abs(p - q)) / np.max(np.abs(p - q)) = ', ret)     

