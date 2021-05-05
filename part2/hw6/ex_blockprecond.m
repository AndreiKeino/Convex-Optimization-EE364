%example: block precondioned pcg 
rand('state', 364);
m = 200; k = 20; n=m*k;
M = sparse(n, n);
for i = 1:k
    Asub = rand(m); Asub = 10*Asub*Asub';
    M(((i-1)*m+1):(i*m),((i-1)*m+1):(i*m)) = Asub;
end

density=5/(n);
A = -abs(sprandsym(n,density)); 
v = A*ones(n,1);
Sdiagonal = spdiags(v,0,n,n);
A = A - Sdiagonal + M;
%spy(A); 
clear M Sdiagonal Asub v

A_blk = sparse(n,n);
for i = 1:k
    A_blk(((i-1)*m+1):(i*m),((i-1)*m+1):(i*m)) = A(((i-1)*m+1):(i*m),((i-1)*m+1):(i*m));
end
b = 10*rand(n,1);