cvx_begin
variable x;
variable y;
minimize(norm(x + y + 1));
subject to
x >= inv_pos(y); 
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
