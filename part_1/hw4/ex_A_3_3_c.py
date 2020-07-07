import cvxpy as cp

# Create two scalar optimization variables.
x = cp.Variable()
y = cp.Variable()

# Create two constraints.
constraints = [cp.inv_pos(x) + cp.inv_pos(y) <= 1]
#constraints = [x + y >= 0]

# Form objective.
obj = cp.Minimize((x - y + 2)**2)

# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value, y.value)

