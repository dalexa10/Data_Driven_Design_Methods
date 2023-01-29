% solve unconstrained optimization problem to see the usage of
% data in optimization
% f(x) = exp(x) - 5*x -1;
close all
clear all
format long
clc

% define functions
fx = @(x) exp(x) - 5*x - 1;  % Function to analyze
dfx = @(x) exp(x) - 5;  % First derivartive
d2fx = @(x) exp(x);  % Second derivative
x = 0.5;  % Initial point
tol = 1e-5;
Nmax = 20; 
n=1;

Outputs = [];

% Try changing the noise of the derivative

while n < Nmax
    fx_val = fx(x);
    dfx_val = dfx(x) + normrnd(0, 0.00001, 1, 1);
    d2fx_val = d2fx(x);
    Outputs(n, :) = [n, x, fx_val, dfx_val, d2fx_val];
    
    x = x - dfx_val/d2fx_val;
    
    if abs(dfx_val) < tol
       break;
    end
    n = n + 1;
end 

Outputs 





