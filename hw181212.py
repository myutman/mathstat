import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scp

def xi1(a):
    c = 1 / (2 * a + 2 * np.exp(-a))
    y = np.random.uniform(0, 1)
    return np.log(y / c) if (y <= c * np.exp(-a)) else \
        y/c - np.exp(-a) - a if (y <= c * (np.exp(-a) + 2 * a)) else \
        - np.log(- y / c + 2 * np.exp(-a) + 2 * a)
    
def xi2(a):
    y = np.random.uniform()
    c = 1 / (2 * a + 2 * np.exp(-a))
    return - a - np.random.exponential(1) if (y <= c * np.exp(-a)) else \
        np.random.uniform(-a, a) if (y <= c * (np.exp(-a) + 2 * a)) else \
        a + np.random.exponential(1)
        
        
if __name__ == "__main__":
    a = 1
    data = [xi1(1) for i in range(100000)]
    kde = scp.gaussian_kde(data)
    xs = np.arange(-10, 10, 0.1)
    plt.plot(xs, kde(xs))
    
    data = [xi2(1) for i in range(100000)]
    kde = scp.gaussian_kde(data)
    plt.plot(xs, kde(xs))
    
    pmax = 1 / (2 * a + 2 * np.exp(-a))
    plt.plot(xs, [pmax for x in xs])
    
    plt.legend(["xi1", "xi2", "pmax"])
    plt.show()    
