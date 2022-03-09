import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame

def norm_pdf_res(x, mu, sigma):
	return (1/np.sqrt(2*np.pi*sigma))*np.exp(-((x-mu)**2)/(2*sigma))

mean = 0
var = 1

sample = DataFrame(np.random.normal(mean, var, 1000))

kl_div = 0

for x in sample.values:
	kl_div = kl_div + np.log(norm_pdf_res(x, 0, 1)/norm_pdf_res(x, 0, 4))

res = kl_div/1000

print(res)