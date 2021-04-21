bicommodity_data;

cvx_begin

variables x_star(n) y_star(n)
dual variables mu_star nu_star
minimize(sum((x_star+y_star).^2)+eps*(sum(x_star.^2+y_star.^2)))
subject to
mu_star: A*x_star+s==0;
nu_star: A*y_star+t==0;
x_star >= 0;
y_star >= 0;
cvx_end
f_min = cvx_optval;
% Dual decomposition
mu = zeros(p,1); nu = zeros(p,1);
x = zeros(n,1); y = zeros(n,1);
MAX_ITER = 200;
L = []; infeas1 = []; infeas2 = [];
for i = 1:MAX_ITER
% Potential differences
delta_mu = A'*mu; delta_nu = A'*nu;
% Update flows
for j = 1:n
[x(j),y(j)] = quad2_min(eps,delta_mu(j),delta_nu(j));
end
infeas1 = [infeas1 norm(A*x+s)];
infeas2 = [infeas2 norm(A*y+t)];
% Update lower bound
l = sum((x+y).^2)+eps*(sum(x.^2+y.^2))+mu'*(A*x+s)+nu'*(A*y+t);
L = [L l];
% Update potentials
alpha = .1;
mu = mu+alpha*(A*x+s);
nu = nu+alpha*(A*y+t);
end
figure
plot(1:MAX_ITER,L,'b-',[1 MAX_ITER],[f_min f_min],'r--')
legend('lb','opt')
xlabel('iter')
figure
semilogy(infeas1)
xlabel('iter')
ylabel('ninfeas1')
figure
semilogy(infeas2)
ylabel('ninfeas2')
xlabel('iter')