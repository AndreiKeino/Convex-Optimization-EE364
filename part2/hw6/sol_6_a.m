close all;
clear all;
l1_heuristic_portfolio_data;

cvx_quiet(1);
l1_heuristic_portfolio_data;
% l1 heuristic
gammas = linspace(0,25,50);
stds = [];
cards = [];
xs = [];
for i=1:length(gammas)
    % replace card(x) with gamma*||x||_1 = gamma*1’*x
    cvx_begin
    variable x(n)
    minimize quad_form(x,Sigma)
    subject to
        x>=0
        mu'*x>=Rmin
        sum(x) + Beta*gammas(i)*sum(x) + Alpha'*x <= B
    cvx_end
    % polishing
    idx = find(x<1e-3);
    card = n-length(idx);
    cards = [cards card];
    cvx_begin
    variable x(n)
    minimize quad_form(x,Sigma)
    subject to
        x>=0
        mu'*x>=Rmin
        sum(x) + Beta*card + Alpha'*x <= B
        x(idx) == 0
    cvx_end
    stds = [stds sqrt(cvx_optval)];

    xs = [xs x];
end
[std_l1, id] = min(stds);
x_l1 = xs(:,id);
mean_l1 = mu'*x_l1;
disp('The minimum standard deviation we obtain is: ');
disp(std_l1);
disp('The associated portfolio is: ');
disp(x_l1);
figure;
plot(gammas, stds)
xlabel('gamma');
ylabel('stddev');
figure
plot(gammas, cards)
xlabel('gamma');
ylabel('card(x)');

