randn('state',0); n = 20;
Sigma = randn(n,n);
Sigma = Sigma'*Sigma+eye(n);
x = 0.5*diag(Sigma);
A = diag(ones(n,1)*0.25*sum(diag(Sigma).^2));
maxiters = 5000; U = inf; L = -inf; hist = []; feas = 0;
tol = 0.01;
for k = 1:maxiters
% find a subgradient
[val,ind] = min(x);
[V,d] = eig(diag(x)-Sigma);
if (val <= 0)
feas = 0;
g = zeros(n,1); g(ind) = -1;
elseif (max(diag(d)) >= 0)
feas = 0;
g = V(:,n).^2;
else
g = -ones(n,1);
feas = 1; D = diag(x);
U = min(U,-sum(x));
L = max(L,-sum(x)-sqrt(g'*A*g));
end
hist = [hist [k;feas;U;L]];
if (((U-L) < tol*sum(x)) && (feas == 1)) break; end;
% update the ellipsoid
g = g/sqrt(g'*A*g);

x = x-A*g/(n+1);
A = (n^2/(n^2-1))*(A-A*g*g'*A*(2/(n+1)));
end
cvx_begin
variable xopt(n)
Sigma-diag(xopt) == semidefinite(n);
xopt >= 0;
minimize(-sum(xopt))
cvx_end
figure;
set(gca,'Fontsize',16);
plot(hist(3,:),'k-'); hold on;
plot(hist(4,:),'k--');
plot(1:length(hist(3,:)),cvx_optval*ones(length(hist(3,:)),1),'k:');
xlabel('k'); ylabel('ul');
axis([0,2000,-120,-20]);
print('-depsc', 'ellipsoid_sdp.eps');