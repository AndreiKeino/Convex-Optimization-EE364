randn('state',0);
m = 50; n = 100;
% m = 5; n = 10;
A = randn(m,n); b = randn(m,1);
% \ell_1 heuristic
cvx_begin
variable x(n)
A*x <= b;
minimize(norm(x,1))
cvx_end
xell1 = x;
eps = 1e-4
nel1 = sum(abs(xell1) < eps)

% \ell_2 norm
cvx_begin
variable x(n)
A*x <= b;
minimize(sum(norms(reshape(x,5,20))))
cvx_end
xell2 = x;
nel2 = sum(abs(xell2) < eps)


% \ell_\infty norm
cvx_begin
variable x(n)
A*x <= b;
minimize(sum(norms(reshape(x,5,20),inf)))
cvx_end
xellinf = x;
nellinf = sum(abs(xellinf) < eps)

nel1
nel2
nellinf

