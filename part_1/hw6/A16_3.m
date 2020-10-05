% solution for network utility problem
clear all;
net_util_data;
% let's find max utility with no delay constraint
cvx_begin
variable f(n)
maximize geo_mean(f)
    subject to
        R*f <= c
        f >= 0 % not needed; enforced by geomean domain
cvx_end
Umax=sum(log(f));

% let's find min latency with no utility constraint
% can be done analytically: just take f=0
Lmin = max(R'*(1./c));
% now let's do pareto curve
N = 20;
ds = 1.10*Lmin*logspace(0,1,N); % go from 10% above L
Uopt = [];
for d = ds
    cvx_begin
    variable f(n)
    maximize geo_mean(f);
        subject to
            R'*inv_pos(c-R*f) <= d*ones(n,1)
            f >= 0; % not needed; enforced by geomean domain
            R*f <= c; % not needed; enforced by inv_pos domain
    cvx_end
    Uopt = [Uopt n*log(cvx_optval)];
end
semilogx(ds,Uopt,'k-',[Lmin,ds],[Umax,ones(1,N)*Umax],...
'k--',[1,1]*Lmin,[Uopt(1),Umax],'k--')
% axis([ds(1), ds(N), -480, -340]);
xlabel('L'); ylabel('U');