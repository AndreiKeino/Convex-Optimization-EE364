sp_bayesnet_data;
Y = (Ys*Ys')./N; lambda = 0.025;
cvx_begin sdp
variable S(n,n) symmetric
maximize(log_det(S)-trace(S*Y)-lambda*sum(norms(S,1)))
S >= 0;
cvx_end
S(find(abs(S) < 1e-4)) = 0;
figure;
subplot(121);
spy(Siginv);

title('Inverse of true covariance matrix')
subplot(122);
spy(S);
title('Inverse of estimated covariance matrix');
print('-depsc','sp_bayesnet.eps');