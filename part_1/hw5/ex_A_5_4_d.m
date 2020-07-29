m = 200;
n = 100;
A = randn(m,n);
b = randn(m,1);
b = b/(1.01*max(abs(b)));

cvx_begin
    variable x(n);
    minimize sum(max([zeros(m), abs(A * x - b) - 0.2, 2 * abs(A * x - b) - 0.5]))
cvx_end

hist(A*x-b,m/2);
saveas(gcf,'C:/! Convex_Optimization/homework_solutions/part_1/hw5/A_5_4_d.png')