% radiation treatment planning
treatment_planning_data;
cvx_begin
    variable b(n); % beam intensities
    minimize (sum(square_pos(Aother*b-Dother))) % minimize square excess dose delivered to others
    subject to 
        0 <= b;
        b <= Bmax;
        Atarget*b >= Dtarget % deliver minimum does to tumor voxels
cvx_end

subplot(2,1,1);
hist(Atarget*b);
axis([0 2 0 60]);
hold on; plot([Dtarget Dtarget],[0 60],'r')
title('Tumor voxel dose histogram')
subplot(2,1,2);
hist(Aother*b);
axis([0 2 0 150]);
hold on; plot([Dother Dother],[0 150],'r')
title('Other voxel dose histogram')
xlabel('Dosage')
print -depsc dose_histos