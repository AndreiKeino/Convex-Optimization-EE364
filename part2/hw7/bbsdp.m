% bbsdp.m: Solves an SDP relaxation for a branch and bound two-way partitioning
% problem.
function [v, lower, upper] = bbsdp(n, W, fixedind, fixedvals)
cvx_begin
cvx_quiet(true);
variable x(n);

variable X(n, n) symmetric;
minimize(trace(W*X))
[X x; x' 1] == semidefinite(n + 1);
diag(X) == 1;
x(fixedind) == fixedvals';
cvx_end
lower = cvx_optval;
% Find a feasible point.
[V, D] = eig([X x; x' 1]);
v = V(:,end);
v = v(1:end-1) * sign(v(end) + 1e-5);
xstar = sign(v);
upper = xstar'*W*xstar;