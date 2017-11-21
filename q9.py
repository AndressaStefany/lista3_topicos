
from matplotlib import pyplot as plt
from scipy.stats import expon
import numpy as np

n= 100
t= 200
alpha= 0.05
x= [9,21,40,55,85]
m= np.mean(x)
print(expon.ppf(alpha/2,scale=m))
print(m)
print(expon.ppf(1-alpha/2,scale=m))
