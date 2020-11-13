% solves standard form LP for two problem instances
clear all;
m = 100;
n = 500;

% infeasible problem instance
rand('seed',0);
randn('seed',0);

% feasible problem instance
A = [randn(m-1,n); ones(1,n)];
v = rand(n,1) + 0.1;
b = A*v;
c = randn(n,1);
[x_star,p_star,gap,status,nsteps] = lp_solve_plot(A,b,c);

fprintf('\n\nOptimal value found by barrier method:\n');
p_star

fprintf('Duality gap from barrier method:\n');
gap

% solve Ax = b for b == 0

return
% solve LP using cvx for comparison
cvx_begin
variable x(n)
minimize(c'*x)
subject to
A*x == b
x >= 0
cvx_end
fprintf('\n\nOptimal value found by barrier method:\n');
p_star
fprintf('Optimal value found by CVX:\n');
cvx_optval
fprintf('Duality gap from barrier method:\n');
gap

