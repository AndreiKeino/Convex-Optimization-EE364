% generate the problem data
randn('state',0);
n = 4; m = 10; maxiter = 1000; eps = 1e-6;
A = randn(m,m,n); B = randn(m,m); B = B*B'; c = randn(n,1);
for j = 1:n A(:,:,j) = A(:,:,j)+A(:,:,j'); end;
% solve using subgradient method
x = zeros(n,1); g = zeros(n,1); fbest = (c'*x)*ones(maxiter,1);
for k = 1:maxiter
    F = -B;
    for j = 1:n F = F+x(j)*A(:,:,j); end;
        [V,D] = eig(F);
        if (D(m,m) > 0)
            for j = 1:n g(j) = V(:,m)'*A(:,:,j)*V(:,m); end;

            x = x-((D(m,m)+eps)/(g'*g))*g;
        else
            if (c'*x < fbest(k))
            fbest(k:end) = c'*x;
    end
    x = x-(1/k)*c;
    end
end
x_subg = x;
% check solution using CVX
cvx_begin sdp
variable x(n)
F = -B;
for j = 1:n
F = F+x(j)*A(:,:,j);
end
subject to
    F <= 0;
minimize (c'*x)
cvx_end

x_cvx = x;
set(gca,'Fontsize', 16);
semilogy(fbest-cvx_optval);
xlabel('k'); ylabel('fbestmf');
print('-depsc', 'subgrad_sdp.eps');