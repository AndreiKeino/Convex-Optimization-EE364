% https://www.mathworks.com/matlabcentral/answers/445798-outer-product-of-two-rectangular-matrices
A = [1, 2, 3]'
B = [2, 4, 1]'
sizeA = size(A)
o = zeros(length(A), length(B));

for i = 1:length(A)
    for j = 1:length(B)
        o(i, j) = A(i) * B(j);
    end
end
o


gamma = zeros(n, N);
for i = 1:n
    for j = 1:N
        gamma(i, j) = x(i) * cos(theta(j)) + y(i) * sin(theta(j));
    end
end
size(gamma)

