clear all
rand('state',0);
%N= 10; %400;
%n = 2;%40;
N = 400;
n = 40;
x = 30 * rand(n,1);
y = 30 * rand(n,1);
X = [x'; y'];

beamwidth = 15*pi/180;
theta_tar=15*pi/180;
theta = linspace(theta_tar+beamwidth, 2*pi+theta_tar-beamwidth, N)';
A = exp(i * [cos(theta), sin(theta)] * X);
Atar = exp(i * [cos(theta_tar), sin(theta_tar)] * X);

cvx_begin
    variable w(n) complex
    minimize(max(abs(A*w)))
    subject to
    Atar*w == 1;
cvx_end

gamma = zeros(n, N);
for i = 1:n
    for j = 1:N
        gamma(i, j) = x(i) * cos(theta(j)) + y(i) * sin(theta(j));
    end
end
size(gamma)

G = zeros(N, 1);

for i = 1:N
    for j = 1:n
        omega = w(j);
        rw = real(omega);
        iw = imag(omega);
        g = gamma(j, i);
        G(i) = G(i) + complex(rw * cos(g) - iw * sin(g), (rw * sin(g) + iw * cos(g)));
    end
end

abs_G = abs(G)

plot(theta, abs(G))

%saveas(gcf,'C:/! Convex_Optimization/homework_solutions/part_1/hw5/A_5_12.png')