clear all; format long; clc

% define variables
mu = [4.5, 4.5]; stdx = [0.6, 0.6];
nd = 2; u=zeros(1,nd); iter=0;  Dif=1;

% define G and delta_G
G = @(x)1-80/(x(1)^2+8*x(2)-5);
DG1 = @(x)x(1)*160*stdx(1)/((x(1)^2+8*x(2)-5))^2;
DG2 = @(x)80*8*stdx(2)/((x(1)^2+8*x(2)-5))^2;

% start the HL_RF loop
while Dif >= 1d-5 & iter < 20
    iter=iter + 1;
    x = mu+u.*stdx;
    Gx= G(x);
    DG = [DG1(x), DG2(x)].*stdx;
    u=(DG*u'-Gx)/norm(DG)^2*DG;
    U(iter,:)=u/norm(u);
    if iter>1
        Dif=abs(U(iter-1,:)*U(iter,:)' - 1);
    end
end
beta = norm(u);  % reliability index
PoF = 1- normcdf(beta,0,1)  % PoF value
