cvx_begin
    variable x;
    variable y;
    variable z1;
    variable z2;
    minimize(norm(x + y + 1));
    subject to
        z1 >= max(x,1);
        z2 >=  max(y,2)
        norm([z1, z2]) <= 3*x + y;
cvx_end

fprintf('status:'); 
disp(cvx_status);

fprintf('optimal value:'); 
disp(cvx_optval )

fprintf('optimal x:\n'); 
disp(x)

fprintf('optimal y:\n'); 
disp(y)

