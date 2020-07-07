import cvxpy as cp

# Create two scalar optimization variables.
x = cp.Variable()
y = cp.Variable()
z = cp.Variable(2)

# Create two constraints.
constraints = [x >= cp.inv_pos(y), x >= 0, y >= 0]

# Form objective.
obj = cp.Minimize((x - y + 2)**2)

# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value, y.value)

