import numpy as np
import math
import matplotlib.pyplot as plt
from math import factorial

def MQE(distr, hrev, theta, k):
    n = 200
    n1 = 200
    sm = 0
    for i in range(n1):
        m = np.average([distr(theta)**k for i in range(n)])
        theta1 = hrev(m)
        sm += (theta1 - theta)**2
    return sm / n1

def uniform(k):
    return MQE(np.random.uniform, lambda x: ((k+1)*x)**(1/k), 10, k)

def exponential(k):
    return MQE(np.random.exponential, lambda x: (x/factorial(k))**(1/k), 10, k)

x_from = 2
x_to = 50
x_step = 2
t = np.arange(x_from, x_to, x_step)

plt.subplot(211)
s = np.array(list(map(uniform, t)))
plt.plot(t, s)

plt.xlabel('Parameter k')
plt.ylabel('Mean quadratic error')
plt.title('Uniform distribution, theta=10, n=200, n1=200')
plt.grid(True)


plt.subplot(212)
s = np.array(list(map(exponential, t)))
plt.plot(t, s)

plt.xlabel('Parameter k')
plt.ylabel('Mean quadratic error')
plt.title('Exponential distribution, theta=10, n=200, n1=200')
plt.grid(True)

plt.subplots_adjust(hspace=0.75)

plt.show()

