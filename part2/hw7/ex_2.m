close all;
clear all;

% Generate a random example.
randn('state', 109)
n = 100;

W = randn(n); W = W + W';
% Set x_1 to 1 without loss of generality.
fixedind = [1]; fixedvals = [1];
% Evaluate and display the bounds at the root node.
[v, lower, upper] = bbsdp(n, W, fixedind, fixedvals);
disp([lower upper]);
% Choose which node to split.
[y, i] = min(abs(v)); fixedind = [fixedind i];
% Solve new problems and display bounds.
[v, lower, upper] = bbsdp(n, W, fixedind, [fixedvals -1]);
disp([i -1]); disp([lower upper]);
[v, lower, upper] = bbsdp(n, W, fixedind, [fixedvals 1]);
disp([i 1]); disp([lower upper]);
% We will split with x_40 == -1.
fixedvals = [fixedvals -1];
% Find the node to split next time.
[y, i] = min(abs(v)); fixedind = [fixedind i];
% Solve new problems and display bounds.
[v, lower, upper] = bbsdp(n, W, fixedind, [fixedvals -1]);
disp([i -1]); disp([lower upper]);
[v, lower, upper] = bbsdp(n, W, fixedind, [fixedvals 1]);
disp([i 1]); disp([lower upper]);
% We will split with x_26 == 1.
fixedvals = [fixedvals 1];
% Find the node to split next time.
[y, i] = min(abs(v)); fixedind = [fixedind i];
% Solve new problems and display bounds.
[v, lower, upper] = bbsdp(n, W, fixedind, [fixedvals -1]);
disp([i -1]); disp([lower upper]);
[v, lower, upper] = bbsdp(n, W, fixedind, [fixedvals 1]);
disp([i 1]); disp([lower upper]);