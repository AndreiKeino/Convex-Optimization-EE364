cvx_quiet(1);
% number of variables n and linear functions m
n = 20; m = 100;
%********************************************************************
% generate an example
%********************************************************************
randn('state',1)
A = randn(m,n);
b = randn(m,1);
%********************************************************************
% compute pwl optimal point using CVX
%********************************************************************
cvx_begin
variable x(n)
minimize max(A*x + b)
cvx_end
f_star = cvx_optval;
%********************************************************************
% cutting plane method
%********************************************************************
% number of iterations
niter = 40;
% initial localization polyhedron is the cube {x| norm(x, inf) <= R}
R = 1;
% initial point
x = zeros(n,1);
G = []; h = [];

f_save = []; L = []; U = [];
for i = 1:niter
% find active functions at current x
[f, idx] = max(A*x + b);
f_save = [f_save; f];
U = [U; min(f_save)];
% subgradient at current x
g = A(idx(1),:)';
G = [G; g'];
h = [h; f - g'*x];
cvx_begin
variable x(n)
minimize max(G*x + h)
norm(x, inf) <= 1
cvx_end
L = [L; cvx_optval];
end

%********************************************************************
% plots
%********************************************************************
figure
set(gca, 'FontSize',18);
plot(1:niter, f_save);
hold on;
plot(1:niter, L, 'r-.');
plot(1:niter, U, 'g--');
plot(1:niter, f_star*ones(1,niter),'k')
xlabel('k');
legend('f','L','U','pstar', 'Location','Southeast')

