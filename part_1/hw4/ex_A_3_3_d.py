import cvxpy as cp

# Create two scalar optimization variables.
x = cp.Variable()
y = cp.Variable()
z = cp.Variable(2)
z1 = cp.Variable()
z2 = cp.Variable()

# Create two constraints.
constraints = [z[0] >= cp.maximum(x, 1), z[1] >= cp.maximum(y, 2), 
               cp.norm(z) <= 3 * x + y]

# Form objective.
obj = cp.Minimize((x - y + 2)**2)

# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value, y.value)

