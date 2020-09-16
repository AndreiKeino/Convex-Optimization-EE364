# -*- coding: utf-8 -*-
import numpy as np


N = 3

p = np.random.rand(N)
q = np.random.rand(N)

p = np.abs(p)
q = np.abs(q)

p = p / p.sum()
q = q / q.sum()

print('p = ', p)
print('q = ', q)

P_diff = np.zeros((N, N), dtype=np.double)

for i in range(N):
    for k in range(N):
        P_diff[i, k] = np.abs(p[i] - q[k])

print('P_diff = ', P_diff)
d_mp = np.max(P_diff)

print('d_mp = ', d_mp)

diff_norm = np.sum(np.abs(p - q))

print('diff_norm = %f'% diff_norm)

print('diff_norm / d_mp = ', diff_norm / d_mp)