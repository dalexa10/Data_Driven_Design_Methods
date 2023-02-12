__author__ = 'Dario Rodriguez'

import numpy as np

def G_fun(Px, Py):
    """ Compute performance function.
    Note, fixed parameters are locally implemented within the function """
    L = 100
    E = 2.9e7
    w = 2
    t = 4
    Do = 2.5
    G = ((4 * L**3) / (E * w * t)) * np.sqrt((Px / w**2)**2 + (Py / t**2)**2) - Do
    return G

def dGdPx_fun(Px, Py, sigma_Px):
    L = 100
    E = 2.9e7
    w = 2
    t = 4
    dGdPx = (((4 * L**3) / (E * w * t)) * ((Px / w**2)**2 + (Py / t**2))**(-1/2)) * (2 * Px) * sigma_Px
    return dGdPx

def dGdPy_fun(Px, Py, sigma_Py):
    L = 100
    E = 2.9e7
    w = 2
    t = 4
    dGdPy = (((4 * L**3) / (E * w * t)) * ((Px / w**2)**2 + (Py / t**2))**(-1/2)) * (2 * Py) * sigma_Py
    return dGdPy


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

    # STEP 1: Generate N number of uniform random sample
    samp1 = np.random.uniform(low=0, high=1., size=int(N))
    samp2 = np.random.uniform(low=0, high=1., size=int(N))

    # % STEP 2: Converting the sample to Normal Distribution
    Px = np.array([NormalDist(mu=500, sigma=100).inv_cdf(i) for i in samp1])
    Py = np.array([NormalDist(mu=1000, sigma=100).inv_cdf(i) for i in samp2])

    # STEP 3: Calculating the performance function G (X)
    G_eval = G_fun(Px, Py)

    # STEP 4: Estimate Reliability
    PoF = G_eval[G_eval > 0.].size / N
    print('The probability of failure with Monte Carlo Simulation is {:.5f}'.format(PoF))

    # Plotting just to test normal distribution of points
    # fig, ax = plt.subplots()
    # ax.hist(Px, bins=300, color='g')
    # ax.hist(Py, bins=300, color='b')
    # plt.show()

    # -----------------------------------------
    #          FORM HLRF Simulation
    # ----------------------------------------
    # Inputs
    mu = np.array([[500, 1000]])
    stdx = np.array([[100, 100]])
    nd = 2
    u = np.zeros([1, nd])
    iter = 0
    Dif = 1

    U = []
    # Start HR_RF loop
    while Dif >= 1e-5 and iter < 50:
        iter += 1
        P = mu + u * stdx
        Gx = G_fun(P[0, 0], P[0, 1])
        DG = np.array([[dGdPx_fun(P[0, 0], P[0, 1], stdx[0, 0]), dGdPy_fun(P[0, 0], P[0, 1], stdx[0, 1])]])
        u = ((DG@u.T - Gx) / norm(DG)**2) * DG
        U.append(u/norm(u))
        if iter > 1:
            Dif = abs(U[iter - 2]@U[iter - 1].T - 1)

    beta = norm(u)  # Reliability index
    PoF_hlrf = 1 - normcdf.cdf(beta, loc=0, scale=1)  # Probability of failure
    print('The probability of failure with HL- RF method is {:.5f}'.format(PoF_hlrf))
