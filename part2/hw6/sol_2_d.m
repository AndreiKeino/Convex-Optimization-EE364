%block preconditioning solution
clear all;
ex_blockprecond;
A_full = full(A);
fprintf('\nStarting dense direct solve ...\n');
time_start = cputime;
x_star_dense = A_full\b;
time_end = cputime;
relres_dense = norm(A*x_star_dense - b)/norm(b);
fprintf('Relative residual: %e\n', relres_dense);
fprintf('Dense direct solve done.\nTime taken: %e\n',...
time_end - time_start);
fprintf('\nStarting sparse direct solve ...\n');
time_start = cputime;
x_star_sparse = A\b;
time_end = cputime;
relres_sparse = norm(A*x_star_dense - b)/norm(b);
fprintf('Relative residual: %e\n', relres_sparse)
fprintf('Sparse direct solve done.\nTime taken: %e\n',...
time_end - time_start);
fprintf('\nStarting CG ...\n');

time_start = cputime;
[x,flag,relres,iter,resvec] = pcg(A,b,1e-4,200);
time_end = cputime;
fprintf('CG done. Status: %d\nTime taken: %e\n', flag,...
time_end - time_start);
figure; semilogy(resvec/norm(b), '.--'); hold on;
set(gca,'FontSize', 16, 'FontName', 'Times');
xlabel('cgiter'); ylabel('relres');
time_start = cputime;
L = chol(A_blk)';
time_end = cputime;
tchol = time_end - time_start;
fprintf('\nCholesky factorization. Time taken: %e\n', tchol);
fprintf('\nStarting CG with block preconditioning ...\n');
time_start = cputime;
[x,flag,relres,iter,resvec] = pcg(A,b,1e-8,200,L,L');
time_end = cputime;
fprintf('PCG done. Status: %d\nTime taken: %e\n', flag,...
time_end - time_start);
semilogy(resvec/norm(b), 'k.-'); hold off;
print('-depsc', 'ex_blockprecond_relres.eps');
fprintf('Total time block preconditioned PCG: %e\n',...
tchol+time_end - time_start);
    
