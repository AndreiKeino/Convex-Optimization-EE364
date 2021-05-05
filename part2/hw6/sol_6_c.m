% better lower bound
Gamma = 1/B;
U = [];
for i=1:n
cvx_begin
variable x(n)
maximize x(i)
quad_form(x,Sigma) <= std_l1^2
x>=0
mu'*x>=Rmin
sum(x) + Beta*Gamma*sum(x) + Alpha'*x <= B
cvx_end
U = [U; cvx_optval];
end
cvx_begin
variable x(n)
minimize quad_form(x,Sigma)
x>=0
mu'*x>=Rmin
sum(x) + Beta*(1./U)'*x+ Alpha'*x <= B
cvx_end
std_lb2 = sqrt(cvx_optval)

