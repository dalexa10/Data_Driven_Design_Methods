clear all; format long; clc

% STEP 1: Generate N number of uniform random sample 
    N = 100000;
    samp1 = unifrnd(0, 1, [N,1]);
    samp2 = unifrnd(0, 1, [N,1]);

% STEP 2: Converting the sample to Normal Distribution
    X1 = norminv(samp1,4.5,0.6);
    X2 = norminv(samp2,4.5,0.6);

    % note: X1 can also be generated directly with X1 = normrnd(4.5, 0.6, N, 1); 
    
% STEP 3: Calculating the performance function G (X)
    G = 1 - 80./(X1.^2+8*X2+5);

% STEP 4: Estimate Reliability
    PoF = sum(G>0)/N
