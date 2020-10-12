res_alloc_stream_data;
% solution
cvx_begin
    variable x(n,P) % resource allocation
    variable t(J) % job traffic
    
    minimize (w'*pos(t_tar-t))
    subject to 
        t >= 0
        sum(x') <= x_tot'; % resource limits
        lambda = R*t; % process loads
        x >= x_min % minimum allowable resources for the processes
        lproc = inv_pos(sum(A.*x)-lambda')'; % process latencies
        ljob = R'*lproc; % job latencies
        ljob <= l_max; % job latency limit
cvx_end
cvx_optval
[t t_tar]
[ljob l_max]