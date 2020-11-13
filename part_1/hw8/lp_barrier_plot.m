function [x_star, history, gap] = lp_barrier(A,b,c,x_0)
% solves standard form LP
% minimize c^T x
% subject to Ax = b, x >=0;
% using barrier method, given strictly feasible x0
% uses function std_form_LP_acent() to carry out centering steps
% returns:
% - primal optimal point x_star
% - history, a 2xk matrix that returns number of newton steps
% in each centering step (top row) and duality gap (bottom row)
% (k is total number of centering steps)
% - gap, optimal duality gap
% barrier method parameters
T_0 = 1;
MU = 20;
EPSILON = 1e-3; % duality gap stopping criterion
n = length(x_0);
t = T_0;
x = x_0;
history = [];

plotted = false;
while(1)
    [x_star, nu_star, lambda_hist] = lp_acent_plot(A,b,t*c,x);
    x = x_star;
    gap = n/t;
    history = [history [length(lambda_hist); gap]];
    fprintf('lp_barrier_plot: history:')
    history
    
    fprintf('lp_barrier_plot: lambda_hist:')
    lambda_hist
    
    if plotted == false
        figure()
        plot([1:length(lambda_hist)], log(lambda_hist))
        title('Dependency of \lambda ^2 / 2 vs newton step')
        xlabel('step count') 
        ylabel('\lambda ^2 / 2') 
        plotted = true;
    end
    
    if gap < EPSILON break; end
    t = MU*t;
end

