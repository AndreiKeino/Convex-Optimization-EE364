m = 200;
n = 100;
A = randn(m,n);
b = randn(m,1);
b = b/(1.01*max(abs(b)));

x = A \ b;

hist(A*x-b,m/2);
saveas(gcf,'C:/! Convex_Optimization/homework_solutions/part_1/hw5/A_5_4_a.png')