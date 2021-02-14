A1 = [1 3 2; 4 2 5; ]
A1
size(A1)

x1 = [1 1 2]'
x1
size(x1)

sprintf('A1 * x1 = ')
A1 * x1

A2 = [1 1 2; 4 3 5; ]
A2
size(A2)

x2 = [1 2 2]'
x2
size(x2)

sprintf('A2 * x2 = ')
A2 * x2

A = horzcat(A1, A2)
x = vertcat(x1, x2)

sprintf('A * x = ')
A * x
lambda = 1

J = 15;
n = 10;
m = 200;
lambda = 1;

A = sqrt(1 / m) * randn([m, n, J]);
x = sqrt(1 / n) * randn([n, J]);
fprintf('size A = '); size(A)
fprintf('size x = '); size(x)

AA = A(:, :, 1);
xx = x(:, 1);
for k = 2:J
    AA = horzcat(AA, A(:, :, k));
    xx = vertcat(xx, x(:, k));
end
% now AA * x will be equal to sum_j(A(:, :, j) * x(:, j))

b = AA * xx;

