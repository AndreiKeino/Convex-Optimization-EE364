% number of variables n
n = 20;
%********************************************************************
% generate an example

%********************************************************************
rand('state',1)
c = 2*rand(n,1)-1;
% optimal solution
x_star = c;
f_star = 0;
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
    
% f and g at current x
f = norm(x-c);
g = (x-c)/f;
f_save = [f_save; f];
U = [U; min(f_save)];
% update PWL underestimator
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