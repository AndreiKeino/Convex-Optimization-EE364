import matplotlib.pyplot as plt
import numpy as np


plt.close('all')

def objective(x):
    return x**2 + 1

def constraint(x):
    return (x - 2) * (x - 4)

def lagrangian(x, lam):
    return objective(x) + lam * constraint(x)


x = np.linspace(0, 6, 100)


fig = plt.figure()
plt.plot(x, objective(x), label='objective')
plt.plot(x, constraint(x), label = 'constraint')
plt.plot(x, [0] * len(x) , label = 'zero level')

lam = 2
plt.plot(x, lagrangian(x, lam), label = 'Lagrangian, $\lambda$ = ' + str(lam))

lam = 4
plt.plot(x, lagrangian(x, lam), label = 'Lagrangian, $\lambda$ = ' + str(lam))

lam = 6
plt.plot(x, lagrangian(x, lam), label = 'Lagrangian, $\lambda$ = ' + str(lam))

axes = plt.gca()
y_min, y_max = axes.get_ylim()
y_space = np.linspace(y_min, y_max, len(x))

rect = plt.Rectangle((2, y_min), 2, y_max - y_min,
                     linewidth=1,edgecolor='b',facecolor='b', alpha = 0.2, 
                     label = 'feasible set')
axes.add_patch(rect)

plt.legend()
fig.suptitle('objective, feasible set, Lagrangian')
plt.xlabel('x')
plt.ylabel('objective')


plt.show()

#plt.savefig('5_1_b_1.png')

def objective_dual_0(lam):
    return (-lam**3 + 8 * lam ** 2 + 10 * lam + 1) / ((lam + 1) ** 2)

def objective_dual_2(lam):
    return - lam + 10 - 9 / (lam + 1)

lam = np.linspace(0, 6, 100)

fig = plt.figure()

#plt.plot(lam, objective_dual_0(lam), label = 'dual of $\lambda$')
plt.plot(lam, objective_dual_2(lam), label = 'dual  of $\lambda$')

plt.xlabel('$\lambda$')
plt.ylabel('dual objective')
plt.legend()
fig.suptitle('dual objective as a function of $\lambda$')

plt.show()

#plt.savefig('5_1_b_2.png')

def objective_u(u):
    y = np.zeros_like(u)
    for i in range(0, len(u)):
        if u[i] < - 1:
            y[i] = np.nan
        if u[i] >= 8:
            y[i] = 1
        else:
            y[i] = 11 - 6 * np.sqrt(1 + u[i]) + u[i]
    return y
            
        
u = np.linspace(-1, 10, 200)

fig = plt.figure()

plt.plot(u, objective_u(u), label = '$p^*(u)$')
plt.xlabel('$u$')
plt.ylabel('$p^*(u)$')
plt.legend()
fig.suptitle('objective as a function of $u$')

plt.show()

#plt.savefig('5_1_3.png')



