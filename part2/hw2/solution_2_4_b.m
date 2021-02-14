randn('state',6); % set state so problem is reproducable
% example is
% C:\! Convex_Optimization\ConvexOptimizationII\materials\lsocoee364b\02-subgrad_method_matlab\subgrad_method_pwl_speedup.m
% (2 points) Let J = 15, n = 10, m = 200 and  = 1
J = 15;
n = 10;
m = 200;

% tests
J = 5;
n = 2;
m = 4;

lambda = 1;

% Generate random matrices A1; : : : ;AJ in R^{mx n} with independent Gaussian entries 
% with mean 0 and variance 1/m
A = sqrt(1 / m) * randn([m, n, J]);
x = sqrt(1 / n) * randn([n, J]);
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

% optimal value after minimization
f_star = cvx_optval;
% solution variables
x_star = x_min;

% calculation using Polyak step length
f = [+Inf]; fbest = [+Inf];

MAX_ITERS = 1;
% initial value of x
x1 = zeros([n * J, 1]);

x = x1;
p = 0;

while p < MAX_ITERS 
  fprintf('p = ')
  p
  % objective values
  fval = 0.5 * norm(b - AA * x)^2;
  for s = 1:J 
    first = 1 + (s - 1) * n;
    last = first + n - 1;
    fprintf('size(x(first:last)) = ')
    size(x(first:last))
    fval = fval + norm(x(first:last));
  end
  fprintf('fval = ')
  fval
  f(end+1) = fval;
  fbest(end+1) = min( fval, fbest(end) );
    
    % gradient calculation
    g = zeros([n * J, 1]);   
    for s = 1:J 
        first = 1 + (s - 1) * n;
        last = first + n - 1;
        % calculate \sum(A_j * x_J)
        ss = zeros([m, 1]); 
        for r = 1:J
            firstJ = 1 + (r - 1) * n;
            lastJ = firstJ + n - 1;
            x_j = x(firstJ:lastJ);
            ss = ss + A(:, :, r) * x_j;
        end
        
        x_k = x(first:last);
        g_k = A(:, :, s)' * (- b + ss) + lambda * (x_k / norm(x_k));
        fprintf('s = '); s
        fprintf('ss = '); ss
        fprintf('g_k = '); g_k


        g(first:last) = g_k;
    end
    
    fprintf('g = '); g
    fprintf('size(g) = '); size(g)
    
    % calculate the Polyak step
    alpha = (f_star - fval) / (norm(g))^2;
    % update the x 
    x = x - alpha * g;
    p = p + 1;
end




