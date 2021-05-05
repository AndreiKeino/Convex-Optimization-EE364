randn('state',0);
n = 50; p = 10; q = 10;
A = zeros(p,q,n); A0 = randn(p,q);
for i = 1:n A(:,:,i) = randn(p,q); end;
cvx_begin
variable x(n)
obj = A0;
for i = 1:n obj = obj+x(i)*A(:,:,i); end;
minimize(norm_nuc(obj))
cvx_end

B = obj;
sig = svd(B)

