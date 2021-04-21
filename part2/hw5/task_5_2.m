randn('state', 1091); rand('state', 1091); n = 40;
P = randn(n); P = 3*eye(n) + P'*P;

vals = [];
xold = 1/n*ones(n, 1);
Nmax = 16;
for i = 1:Nmax
cvx_begin
cvx_quiet(true);
variable x(n)
minimize(x'*P*x)
1 - 2*xold'*(x - xold) - xold'*xold <= 0;
cvx_end
disp(cvx_optval)
vals = [vals; cvx_optval];
xold = x;
end
figure(1); cla;
plot(vals); hold on;
plot([1 Nmax], min(eig(P))*[1 1], 'k--');
xlabel('x'); ylabel('y');
print -deps2 mineig.eps
