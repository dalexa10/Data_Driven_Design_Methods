__author__ = 'Dario Rodriguez'

# Code yourself here if you want to generalize any function in this module

if __name__ == '__main__':
    import numpy as np
    from statistics import NormalDist
    from scipy.linalg import norm
    from scipy.stats import norm as normcdf
    import matplotlib.pyplot as plt

    # -----------------------------------------
    #           Monte Carlo Simulation
    # ----------------------------------------
    N = 1e6  # Number of samples
    G = lambda x1, x2: 1 - ((x1 + x2 - 5)**2)/30 - ((x1 - x2 - 12)**2)/120

    # STEP 1: Generate N number of uniform random sample
    samp1 = np.random.uniform(low=0, high=1., size=int(N))
    samp2 = np.random.uniform(low=0, high=1., size=int(N))

    # % STEP 2: Converting the sample to Normal Distribution
    x1 = np.array([NormalDist(mu=3.5, sigma=0.5).inv_cdf(i) for i in samp1])
    x2 = np.array([NormalDist(mu=3.8, sigma=0.5).inv_cdf(i) for i in samp2])

    # STEP 3: Calculating the performance function G (X)
    G_eval = G(x1, x2)

    # STEP 4: Estimate Reliability
    PoF = G_eval[G_eval > 0.].size / N
    print('The probability of failure with Monte Carlo Simulation is {:.5f}'.format(PoF))

    # Plotting just to test normal distribution of points
    # fig, ax = plt.subplots()
    # ax.hist(X1, bins=100, color='g')
    # ax.hist(X2, bins=100, color='b')
    # plt.show()


    # -----------------------------------------
    #          FORM HLRF Simulation
    # ----------------------------------------
    # Inputs
    mu = np.array([[3.5, 3.8]])
    stdx = np.array([[0.5, 0.5]])
    nd = 2
    u = np.zeros([1, nd])
    iter = 0
    Dif = 1

    # dG functions (G is the same as above)
    dG1 = lambda x1, x2: - (stdx[0, 0] * (x1 + x2 - 5) / 15) - (stdx[0, 0] * (x1 - x2 - 12))/60
    dG2 = lambda x1, x2: - (stdx[0, 1] * (x1 + x2 - 5) / 15) + (stdx[0, 1] * (x1 - x2 - 12))/60

    U = []
    # Start HR_RF loop
    while Dif >= 1e-5 and iter < 50:
        iter += 1
        x = mu + u * stdx
        Gx = G(x[0, 0], x[0, 1])
        DG = np.array([[dG1(x[0, 0], x[0, 1]), dG2(x[0, 0], x[0, 1])]])
        u = ((DG@u.T - Gx) / norm(DG)**2) * DG
        U.append(u/norm(u))
        if iter > 1:
            Dif = abs(U[iter - 2]@U[iter - 1].T - 1)

    beta = norm(u)  # Reliability index
    PoF_hlrf = 1 - normcdf.cdf(beta, loc=0, scale=1)  # Probability of failure
    print('The probability of failure with HL- RF method is {:.5f}'.format(PoF_hlrf))
