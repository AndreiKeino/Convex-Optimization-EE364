n = 3; % variable size
m = 3; % number of inequalities
noise = 0.1; % amount of uncertainty
Abar = [ 1 0 0;
1 1/2 0;
1 1 1/2];
bbar = [9/10; 1; 9/10];

%********************************************************************
% maximum margin heuristic: minimize max_i E(b) - E(A)x
%********************************************************************
cvx_begin
variable x_mm(n)
minimize( max( bbar - Abar*x_mm ) )
subject to
norm( x_mm, inf ) <= 1;
cvx_end

%********************************************************************
% direct solution of sampled problem:
%
% minimize 1/M sum_i ( max(b^{i} - A^{i}x)_+ )
% subject to ||x||_inf <= 1
%********************************************************************
M = 100;
Amtx = repmat(Abar,M,1) + 2*noise*rand(M*m,n) - noise;
bmtx = repmat(bbar,M,1) + 2*noise*rand(M*m,1) - noise;
cvx_begin
variable x_ds(n)

minimize( 1/M*sum( max( pos( reshape(bmtx - Amtx*x_ds,m,M) ) ) ) )
subject to
norm( x_ds, inf ) <= 1;
cvx_end


%********************************************************************
% stochastic subgradient method with 1/k step size and a single sample
% used to compute a noisy (unbiased) subgradient
%********************************************************************
MAX_ITERS = 5000;
% run subgradient method with 1/k step size
f = [+Inf]; fbest = [+Inf];
iter = 1;
x = zeros(n,1); % initial point
xhist = [x];
while iter < MAX_ITERS
% fprintf(1,’iter = %d\n’,iter);
% noisy subgradient calculation
M = 1;
% generate a random realization of the data A and b
A = repmat(Abar,M,1) + 2*noise*rand(M*m,n) - noise;
b = repmat(bbar,M,1) + 2*noise*rand(M*m,1) - noise;
% compute max and obtain a noisy subgradient
% [fval, ind] = max(pos(b - A*x));
% ??????, ??? ???????? ????????? max
[fval, ind] = max(pos(b - A*x));
fprintf('iter = ');
iter

fprintf('fval = ');
fval

if( fval > 0 )
g = -A(ind,:);
else
g = zeros(n,1);
end
% step size selection
alpha = 1/iter;
% store objective values
f(end+1) = fval;
fbest(end+1) = min( fval, fbest(end) );
% subgradient update

x = x - alpha*g;
% project back onto feasible set
x = max( min( x, 1), -1 );
% iteration counter
iter = iter + 1; xhist = [xhist, x];
end
x_stoch = x; % keep the last solution as the best one
%********************************************************************
% generate histograms of max(b-Ax)_+ for the three solutions
%********************************************************************
NSAMPLES = 1000;
Amtx = repmat(Abar,NSAMPLES,1) + 2*noise*rand(NSAMPLES*m,n) - noise;
bmtx = repmat(bbar,NSAMPLES,1) + 2*noise*rand(NSAMPLES*m,1) - noise;
fvals_stoch = max( reshape(bmtx - Amtx*x_stoch,m,NSAMPLES) );
fvals_mm = max( reshape(bmtx - Amtx*x_mm,m,NSAMPLES) );
fvals_ds = max( reshape(bmtx - Amtx*x_ds,m,NSAMPLES) );
fpvals_stoch = max( pos( reshape(bmtx - Amtx*x_stoch,m,NSAMPLES) ) );
fpvals_mm = max( pos( reshape(bmtx - Amtx*x_mm,m,NSAMPLES) ) );
fpvals_ds = max( pos( reshape(bmtx - Amtx*x_ds,m,NSAMPLES) ) );
fprintf("Estimated obj value for x_stoch %3.5f\n",mean(fpvals_stoch));
fprintf("Estimated obj value for x_mm %3.5f\n",mean(fpvals_mm));
fprintf("Estimated obj value for x_ds %3.5f\n",mean(fpvals_ds));
%********************************************************************
% histogram plots
%********************************************************************
figure(1), clf
edges = linspace(-0.4,0.4,40);
[count_1] = histc( fvals_stoch, edges );
[count_2] = histc( fvals_mm, edges );
[count_3] = histc( fvals_ds, edges );
% stochastic subgradient solution
subplot(3,1,1), bar( edges, count_1, 'histc' )
title('stoch subgrad')

% maximum margin solution
subplot(3,1,2), bar( edges, count_2, 'histc' )
title('maximum margin')
% direct solution of sampled problem
subplot(3,1,3), bar( edges, count_3, 'histc')
title('direct solution')
