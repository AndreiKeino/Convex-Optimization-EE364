clear all; close all;
% data for problem instance
M = 20;
N = 20;
P = 20;
X = [
3.5674 4.1253 2.8535 5.1892 4.3273 3.8133 3.4117 ...
3.8636 5.0668 3.9044 4.2944 4.7143 3.3082 5.2540 ...
2.5590 3.6001 4.8156 5.2902 5.1908 3.9802 ;...
-2.9981 0.5178 2.1436 -0.0677 0.3144 1.3064 3.9297 ...
0.2051 0.1067 -1.4982 -2.4051 2.9224 1.5444 -2.8687 ...
1.0281 1.2420 1.2814 1.2035 -2.1644 -0.2821];

Y = [
-4.5665 -3.6904 -3.2881 -1.6491 -5.4731 -3.6170 -1.1876 ...
-1.0539 -1.3915 -2.0312 -1.9999 -0.2480 -1.3149 -0.8305 ...
-1.9355 -1.0898 -2.6040 -4.3602 -1.8105 0.3096; ...
2.4117 4.2642 2.8460 0.5250 1.9053 2.9831 4.7079 ...
0.9702 0.3854 1.9228 1.4914 -0.9984 3.4330 2.9246 ...
3.0833 1.5910 1.5266 1.6256 2.5037 1.4384];

Z = [
1.7451 2.6345 0.5937 -2.8217 3.0304 1.0917 -1.7793 ...
1.2422 2.1873 -2.3008 -3.3258 2.7617 0.9166 0.0601 ...
-2.6520 -3.3205 4.1229 -3.4085 -3.1594 -0.7311; ...
-3.2010 -4.9921 -3.7621 -4.7420 -4.1315 -3.9120 -4.5596 ...
-4.9499 -3.4310 -4.2656 -6.2023 -4.5186 -3.7659 -5.0039 ...
-4.3744 -5.0559 -3.9443 -4.0412 -5.3493 -3.0465];

cvx_begin
variables a1(2) a2(2) a3(2) b1 b2 b3
    minimize 0
    subject to 
        a1'*X-b1 >= max(a2'*X-b2,a3'*X-b3)+1;
        a2'*Y-b2 >= max(a1'*Y-b1,a3'*Y-b3)+1;
        a3'*Z-b3 >= max(a1'*Z-b1,a2'*Z-b2)+1;
        a1 + a2 + a3 == 0
        b1 + b2 + b3 == 0
cvx_end
a1
a2
a3
b1
b2
b3
% now let�s plot the three-way separation induced by
% a1,a2,a3,b1,b2,b3

% find maximally confusing point
p = [(a1-a2)';(a1-a3)']\[(b1-b2);(b1-b3)];
% plot
t = [-7:0.01:7];
u1 = a1-a2; u2 = a2-a3; u3 = a3-a1;
v1 = b1-b2; v2 = b2-b3; v3 = b3-b1;
line1 = (-t*u1(1)+v1)/u1(2); idx1 = find(u2'*[t;line1]-v2>0);
line2 = (-t*u2(1)+v2)/u2(2); idx2 = find(u3'*[t;line2]-v3>0);
line3 = (-t*u3(1)+v3)/u3(2); idx3 = find(u1'*[t;line3]-v1>0);
plot(X(1,:),X(2,:), '*',Y(1,:),Y(2,:),'ro',Z(1,:),Z(2,:),'g+',...
t(idx1),line1(idx1), 'k',t(idx2),line2(idx2),'k',t(idx3),line3(idx3),'k');
axis([-7 7 -7 7]);

% saveas(gcf,'additional_1_fig_1.png')

p = mfilename('fullpath')
[filepath,name,ext] = fileparts(p)
p
filepath

fname = strcat(filepath, '/additional_1_fig_1.png')
fname

saveas(gcf, fname)