import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame

np.random.seed(0)
X = DataFrame(np.random.normal(-1, 1, 10000))	#random variable X with μ of -1 and σ of 1 sampled over 100000
Y = DataFrame(np.random.normal(3, 4, 10000))	#random variable Y with μ of 3 and σ of 4 sampled over 100000
XY = pd.concat([X, Y], ignore_index=True)	#Concatenation of X and Y over 100000 samples

# weights are arranged to compute X+Y histogram
X_weights = np.ones_like(X.values) / len(XY)
Y_weights = np.ones_like(Y.values) / len(XY)
XY_weights = np.ones_like(XY.values) / len(XY)

plt_range = (XY.values.min(), XY.values.max())
fig, ax = plt.subplots()
ax.hist(X, bins=100, weights=X_weights, color='black', histtype='step', label='X', range=plt_range)	#Histogram of X
ax.hist(Y, bins=100, weights=Y_weights, color='green', histtype='step', label='Y', range=plt_range)	#Histogram of Y
ax.hist(XY, bins=100, weights=XY_weights, color='red', histtype='step', label='X+Y', range=plt_range)	#Histogram of X+Y

def th_dist(x):
	return (1/(2*np.sqrt(np.pi)))*(np.exp(-(x**2)/4))	#theoretical pdf found in the question 5.a)

x = np.arange(-10, 10, 0.1)
p = th_dist(x)
plt.plot(x, p, label='theoretical')

ax.margins(0.05)
ax.set_ylim(bottom=0)
ax.set_xlim([-10, 10])
plt.legend(loc='upper right')
plt.show()