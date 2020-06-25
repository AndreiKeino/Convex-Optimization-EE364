% http://web.cvxr.com/cvx/doc/quickstart.html

close all;
rng('default');

m = 16; n = 8;
rng(1);
A = randn(m,n);
rng(2);
b = randn(m,1);

rng(3);
bnds = randn(n,2);
l = min( bnds, [], 2 );
u = max( bnds, [], 2 );
%{
cvx_begin
    variable x(n)
    minimize( norm(A*x-b) )
    subject to
        l <= x <= u
cvx_end
%}

cvx_begin
    variable x(n);
    minimize( sum(huber(A*x-b)));
    subject to
        l <= x <= u    
cvx_end

fprintf('status:'); 
disp(cvx_status);

fprintf('optimal value:'); 
disp(cvx_optval )

fprintf('optimal variable:\n'); 
disp(x)


p = 4;
rng(3);
C = randn(p,n);
rng(4);
d = randn(p,1);

cvx_begin
    variable x(n);
    minimize( norm(A*x-b) );
    subject to
        C*x == d;
        norm(x,Inf) <= 1;
cvx_end

fprintf('status:'); 
disp(cvx_status);

fprintf('optimal value:'); 
disp(cvx_optval )

fprintf('optimal variable:\n'); 
disp(x)

% linear regression with regularization
gamma = logspace( -2, 2, 20 );

l2norm = zeros(size(gamma));
l1norm = zeros(size(gamma));
fprintf( 1, '   gamma       norm(x,1)    norm(A*x-b)\n' );
fprintf( 1, '---------------------------------------\n' );
for k = 1:length(gamma),
    fprintf( 1, '%8.4e', gamma(k) );
    cvx_begin
        variable x(n);
        minimize( norm(A*x-b)+gamma(k)*norm(x,1) );
    cvx_end
    l1norm(k) = norm(x,1);
    l2norm(k) = norm(A*x-b);
    fprintf( 1, '   %8.4e   %8.4e\n', l1norm(k), l2norm(k) );
end
figure;
plot( l1norm, l2norm );
xlabel( 'norm(x,1)' );
ylabel( 'norm(A*x-b)' );
grid on

