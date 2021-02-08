randn('state',6); % set state so problem is reproducable
% example is
% C:\! Convex_Optimization\ConvexOptimizationII\materials\lsocoee364b\02-subgrad_method_matlab\subgrad_method_pwl_speedup.m
% (2 points) Let J = 15, n = 10, m = 200 and  = 1
J = 15;
n = 10;
m = 200;
lambda = 1;

% Generate random matrices A1; : : : ;AJ in R^{mx n} with independent Gaussian entries 
% with mean 0 and variance1/m
A = sqrt(1 / m) * randn([m, n, J]);
% x = sqrt(1 / n) * randn([n, J]);
x = sqrt(1 / n) * randn([n, J]);
% b = zeros([m,1])
fprintf('size A = '); size(A)
fprintf('size x = '); size(x)

A1 = A(:, :, 1);
x1 = x(:, 1);
s = A1 * x1
fprintf('size of s = ')
size(s)

% https://www.mathworks.com/help/matlab/ref/arrayfun.html

% https://www.mathworks.com/help/matlab/matlab_prog/compatible-array-sizes-for-basic-operations.html
% https://www.mathworks.com/help/matlab/ref/times.html


% https://stackoverflow.com/questions/6580656/matlab-how-to-vector-multiply-two-arrays-of-matrices?lq=1

% https://www.mathworks.com/matlabcentral/answers/120162-multiply-a-stack-of-matrices-with-a-stack-of-vectors
fh = @(k) A(:,:,k) * x(:,k);
C = (arrayfun(fh,1:J,'UniformOutput',false))';
b = cat(3,C{:})
b = sum(b, 3)
fprintf('size b is')
size(b)

% https://stackoverflow.com/questions/6580656/matlab-how-to-vector-multiply-two-arrays-of-matrices?lq=1

% b = A.*x

% C = cellfun(@mtimes, A, x, 'UniformOutput', false);

%********************************************************************
% compute optimal value by solving a linear program (use CVX)
%********************************************************************
%cvx_begin
 %variable x_min(n, 1)
 %minimize( max(A(1)*x_min + b) )
%cvx_end


%cvx_begin
 % variable x_min(n)
  %minimize( max(A*x_min + b) )
%cvx_end


