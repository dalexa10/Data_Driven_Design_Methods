% solve unconstrained optimization problem to see the usage of
% data in optimization
% f(x) = exp(x) - 5*x -1;
function lecture1_exp()
close all
clear all
format long
clc

global Outputs n
Outputs = [];
n = 1;
x0 = [1,2];
options = optimoptions(@fminunc,'Display','iter','Algorithm','quasi-newton');
[x,fval,exitflag,output] = fminunc(@obj,x0,options)
Outputs 

function [obj] = obj(x)
global Outputs n
obj = x(1).^2 + 3*x(2).^2 + 6*x(1) + 18*x(2) + 22 * sin(0.1*x(1).*x(2) + 1.5) - 20;
Outputs(n, :) = [x, obj];
n = n+1;



