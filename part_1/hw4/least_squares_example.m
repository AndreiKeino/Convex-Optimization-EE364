rng('default');

m = 8; n = 4;
rng(1);
A = randn(m,n);
rng(2);
b = randn(m,1);

cvx_begin
    variable x(n)
    minimize( norm(A*x-b) )
cvx_end

fprintf('status:'); 
disp(cvx_status);

fprintf('optimal value:'); 
disp(cvx_optval )

fprintf('optimal variable:'); 
disp(x)

% analytical solution:

x_ls = A \ b;
fprintf('Analytical solution:'); 
disp(x_ls)

