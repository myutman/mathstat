import numpy as np
from scipy.stats import chi2
from scipy.stats import norm
from numpy.random import normal
import matplotlib.pyplot as plt

sigma = 1
gamma = 0.5

def len_chi2(sumsq, n):
    return sumsq * (1 / chi2.ppf((1 - gamma) / 2, n) - 1 / chi2.ppf((1 + gamma) / 2, n))

def avelen_chi2(n, m):
    return np.average([len_chi2(np.sum([normal(0, sigma)**2 for i in range(n)]), n) for i in range(m)])

def len_stand(ave, n):
    return n * (ave**2) * (1 / (norm.ppf((3 - gamma) / 4, 0, 1)**2) - 1 / (norm.ppf((3 + gamma) / 4, 0, 1)**2))

def avelen_stand(n, m):
    return np.average([len_stand(np.average([normal(0, sigma) for i in range(n)]), n) for i in range(m)])

if __name__ == '__main__' :
    m = 250
    x_from = 4
    x_to = 200
    x_step = 4
    t = np.arange(x_from, x_to, x_step)

    plt.subplot(211)
    s = np.array(list(map(lambda n : avelen_chi2(n, m), t)))
    plt.plot(t, s)

    plt.xlabel('Size of sample')
    plt.ylabel('Average length of interval')
    plt.title('Chi square interval, sigma={}, gamma={}, m={}'.format(sigma, gamma, m))
    plt.grid(True)

    plt.subplot(212)
    s = np.array(list(map(lambda n : avelen_stand(n, m), t)))
    plt.plot(t, s)

    plt.xlabel('Size of sample')
    plt.ylabel('Average length of interval')
    plt.title('Standart interval, sigma={}, gamma={}, m={}'.format(sigma, gamma, m))
    plt.grid(True)

    plt.subplots_adjust(hspace=0.75)

    plt.show()

