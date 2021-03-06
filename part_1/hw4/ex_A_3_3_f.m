cvx_begin
    variable x;
    variable y;
    minimize(norm(x + y + 1));
    subject to
        quad_over_lin((x + y), sqrt(y)) <= x - y + 5;
        y >= 0;
        x >= y - 5;
cvx_end

fprintf('status:'); 
disp(cvx_status);

fprintf('optimal value:'); 
disp(cvx_optval )

fprintf('optimal x:\n'); 
disp(x)

fprintf('optimal y:\n'); 
disp(y)

