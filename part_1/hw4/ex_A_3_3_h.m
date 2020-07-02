cvx_begin
    variable x;
    variable y;
    variable z;
    minimize(norm(x + y + z + 1));
    subject to
        x + z <= 1 + geo_mean([x, (y - quad_over_lin(z, x))])
        x >= 0;
        y >= 0;
cvx_end

fprintf('status:'); 
disp(cvx_status);

fprintf('optimal value:'); 
disp(cvx_optval )

fprintf('optimal x:\n'); 
disp(x)

fprintf('optimal y:\n'); 
disp(y)

fprintf('optimal z:\n'); 
disp(z)