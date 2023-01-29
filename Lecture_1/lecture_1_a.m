% solve unconstrained optimization problem to see the usage of
% data in optimization
% f(x) = exp(x) - 5*x -1;
close all
clear all
format long
clc

% define functions
fx = @(x) x(1).^2 + 3*x(2).^2 + 6*x(1) + 18*x(2) + 22 * sin(0.1*x(1).*x(2) + 1.5) - 20;


x0 = [1,2];
options = optimoptions(@fminunc,'Display','iter','Algorithm','quasi-newton');
[x,fval,exitflag,output] = fminunc(fx,x0,options)





