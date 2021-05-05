Gamma = 1/B;
cvx_begin
variable x(n)
minimize quad_form(x,Sigma)
x>=0
mu'*x>=Rmin
sum(x) + Beta*Gamma*sum(x) + Alpha'*x <= B
cvx_end
std_lb1 = sqrt(cvx_optval)
