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
cvx_begin
    variable x_min(3, 2)
    y = reshape(x, [3, 2])
    
    y1 = x.^2
    y2 = sum(y1, 1)
    % y3 = y2.^(1/2) % (Consider POW_P, POW_POS, or POW_ABS instead.)
    % y3 = pow_p(y2, (1/2)) % (Consider POW_P, POW_POS, or POW_ABS instead.)
    % y3 = pow_pos(y2, (1/2)) % (Consider POW_P, POW_POS, or POW_ABS instead.)
    % y3 = pow_abs(y2, 0.5) % (Consider POW_P, POW_POS, or POW_ABS instead.)
    y3 = sqrt(y2)
    y4 = sum(y3)
    z = sum((sum((reshape(x, [3, 2])).^2, 1)).^(1/2))
    z = sum((sum((reshape(x, [3, 2])).^2, 1)).^(1/2))
    % t = y
    a1 = norm(x_min(:, 1) - 1, 2)
    for k = 1:2
        a1 = a1 + norm(x_min(:, 2) - k, 2)
    end
    
    minimize(lambda * a)
cvx_end

