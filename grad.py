import numpy as np
from scipy.stats import chi2

f = lambda p: 476**2 / (2020*p**2) + 1017**2 / (2020 * 2*p*(1-p)) + 527**2/(2020 * (1-p)**2) - 2020
gradf = lambda p: - 2 * 476**2 / (2020*p**3) + (1017**2 / (2 * 2020)) * (1/((1-p)**2) - 1/(p**2)) + 2 * 527**2 / (2020 * (1-p)**3)
iters = 10000
alpha = 0.00001
cur_x = 0.5
for i in range(iters):
    cur_x = cur_x - alpha * gradf(cur_x)
                
print(cur_x, f(cur_x))
