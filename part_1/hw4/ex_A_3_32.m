cd 'C:/! Convex_Optimization/homework_solutions/part_1/hw4\'
satisfy_some_constraints_data;

cvx_begin
    variable x(n);
    variable y;
    minimize (c.' * x);
    subject to
        sum(pos(y +  A * x - b)) <= (m - k) * y;
        y > 0;
cvx_end

fprintf('status = '); 
disp(cvx_status);

fprintf('optimal value = '); 
disp(cvx_optval )

fprintf('optimal x = \n'); 
disp(x)

fprintf('optimal lambda = '); 
disp(1 / y)

e_feas = 1e-5;
fprintf('actual constraints safisfied = ')
disp(sum(A * x - b <= e_feas))

% get inedxes of k firt minimal 
[~, idx] = (sort(A * x - b));
min_idx = idx(1:k);
% get the rows of A corresponding these minimal indexes
A_min = A(min_idx, :);
% get the elements of b corresponding these minimal indexes
b_min = b(min_idx);

cvx_begin
    variable x(n);
    minimize (c.' * x);
    subject to
        A_min * x <= b_min;
cvx_end

fprintf('final objective value = %f', cvx_optval)

