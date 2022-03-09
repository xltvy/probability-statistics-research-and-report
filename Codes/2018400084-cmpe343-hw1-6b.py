import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy.stats import binom

np.random.seed(0)

size = 10000
n = 100
p = 0.5

sample = np.random.binomial(n, p, size)

bin = np.arange(0, n, 1)

plt.hist(sample, bins=bin, edgecolor='blue')

mu, std = norm.fit(sample)

title = "n: {:d} p: {:.1f} Mean: {:.2f} Standard Deviation: {:.2f}".format(n, p, mu, std)
plt.title(title)

plt.show()