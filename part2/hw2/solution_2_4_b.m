randn('state',6); % set state so problem is reproducable
% example is
% C:\! Convex_Optimization\ConvexOptimizationII\materials\lsocoee364b\02-subgrad_method_matlab\subgrad_method_pwl_speedup.m
% (2 points) Let J = 15, n = 10, m = 200 and  = 1
J = 15;
n = 10;
m = 200;
lambda = 1;

% Generate random matrices A1; : : : ;AJ in R^{mx n} with independent Gaussian entries 
% with mean 0 and variance 1/m
A = sqrt(1 / m) * randn([m, n, J]);
% x = sqrt(1 / n) * randn([n, J]);
x = sqrt(1 / n) * randn([n, J]);
% b = zeros([m,1])
fprintf('size A = '); size(A)
fprintf('size x = '); size(x)

AA = A(:, :, 1);
xx = x(:, 1);
for k = 2:J
    AA = horzcat(AA, A(:, :, k));
    xx = vertcat(xx, x(:, k));
end
% now AA * x will be equal to sum_j(A(:, :, j) * x(:, j))

b = AA * xx;

cvx_begin
    variable x_min(n * J)
    y_min = reshape(x_min, [n, J]);
    a1 = norm(y_min(:, 1), 2);
    for k = 2:J
        a1 = a1 + norm(y_min(:, k), 2);
    end   
    minimize(0.5 * pow_pos(norm(b - AA * x_min, 2), 2) + lambda * a1);    
cvx_end

f_star = cvx_optval

% calculation using Polyak step length
f = [+Inf]; fbest = [+Inf];

MAX_ITERS = 6;

k = 1;

while k < MAX_ITERS 
    % subgradient calculation
    
    
    k = k + 1;
end




