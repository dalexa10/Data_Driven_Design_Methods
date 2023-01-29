% Author: Dario Rodriguez 

% Solve constrained optimization problem from Ex1 file
% (see the attached pdf file in the same folder)

% ---------------------------------------------------------------
% This script shows the value of x changes in each iteration
% of the optimizer and saves both the function and constraints 
% evaluations in output and output_const respectively
% ---------------------------------------------------------------

function hw1_fun()
close all
clear all
format long
clc

global Outputs Outputs_const n
Outputs = [];
Outputs_const = [];
n = 1;
x0 = [5,5];
options = optimoptions('fmincon','Display','iter','Algorithm','sqp');
[x,fval,exitflag,output] = fmincon(@obj,x0, [], [], [], [], [0, 0], [10, 10], @constrt, options)
Outputs 
Outputs_const

function [obj] = obj(x)
global Outputs n
obj = x(1) + x(2);
Outputs(n, :) = [x, obj];
n = n+1;

function [c, ceq] = constrt(x)
    global Outputs_const n
    c(1) = 1 - (x(1)^2 * x(2))/20;
    c(2) = 1 - ((x(1) + x(2) - 5)^2)/30 - ((x(1) - x(2) - 12)^2)/120;
    c(3) = 1 - 80 / (x(1)^2 + 8*x(2) + 5);
    ceq = [];
    Outputs_const(n, :) = [c(1), c(2), c(3)];


