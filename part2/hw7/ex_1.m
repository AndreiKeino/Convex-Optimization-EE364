close all;
clear all;
cvx_quiet(1);
n = 3; m = 1;
A = [1,1,0;0,1,1;0,0,1]; B = [0;0.5;1]; C = [-1,0,1];
Umax = 0.1; T = 100;
ydes = zeros(150,1); ydes(1:30) = 0;
ydes(31:70) = 10; ydes(71:150) = 0;

% optimal
cvx_begin
variables X(n,T+1) U(m,T)
max(U') <= Umax; min(U') >= -Umax;
X(:,2:T+1) == A*X(:,1:T)+B*U;
X(:,1) == 0;
minimize (sum(sum_square(C*X-ydes(1:T+1)')))
cvx_end
Jopt = cvx_optval;
tvec = 0:1:T;
plot(tvec,ydes(1:T+1)); hold on;
plot(C*X,'r');

'problem 1 solved'
% mpc
hor = 8; Xmpc = zeros(n,T+1);
x = zeros(n,1);
for t = 1:T
        fprintf('problem 2, iteration %d of %d\n', t, T)
cvx_begin
variables X(n,hor+1) U(m,hor)
max(U') <= Umax; min(U') >= -Umax;
X(:,2:hor+1) == A*X(:,1:hor)+B*U;
X(:,1) == x;
minimize (sum(sum_square(C*X-ydes(t:t+hor)')))
cvx_end
x = X(:,2); Xmpc(:,t+1) = x;
end

'problem 2 solved'

J8 = sum(sum_square(C*Xmpc-ydes(1:T+1)'));
plot(C*Xmpc,'g');
hor = 10; Xmpc = zeros(n,T+1);
x = zeros(n,1);
for t = 1:T
    fprintf('problem 3, iteration %d of %d\n', t, T)
cvx_begin
variables X(n,hor+1) U(m,hor)

max(U') <= Umax; min(U') >= -Umax;
X(:,2:hor+1) == A*X(:,1:hor)+B*U;
X(:,1) == x;
minimize (sum(sum_square(C*X-ydes(t:t+hor)')))
cvx_end
x = X(:,2); Xmpc(:,t+1) = x;
end
J10 = sum(sum_square(C*Xmpc-ydes(1:T+1)'));
plot(C*Xmpc,'k');

'problem 3 solved'
hor = 12; Xmpc = zeros(n,T+1);
x = zeros(n,1);
for t = 1:T
    fprintf('problem 4, iteration %d of %d\n', t, T)
cvx_begin
variables X(n,hor+1) U(m,hor)
max(U') <= Umax; min(U') >= -Umax;
X(:,2:hor+1) == A*X(:,1:hor)+B*U;
X(:,1) == x;
minimize (sum(sum_square(C*X-ydes(t:t+hor)')))
cvx_end
x = X(:,2); Xmpc(:,t+1) = x;
end
J12 = sum(sum_square(C*Xmpc-ydes(1:T+1)'));

'problem 4 solved'

plot(C*Xmpc,'m');
axis([0,100,-5,15]);
xlabel('t'); ylabel('y');

legend('ideal', 'optimal', 'Rolling look-ahead N=8', 'Rolling look-ahead N=10', 'Rolling look-ahead N=12')

print('-depsc','mpc_track.eps');

