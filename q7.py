from matplotlib import pyplot as plt
import numpy as np

n= 5

c= np.array([7, 6, 8, 10, 24, 6, 5, 4, 8, 11, 15, 8, 4, 16, 11, 12, 8, 6, 5, 9, 7, 14, 8, 21])
C= np.mean(c)

lsc= C+3*np.sqrt(C)
lic= C-3*np.sqrt(C)
plt.plot(np.arange(len(c)), np.ones(len(c))*lsc)
plt.plot(np.arange(len(c)), np.ones(len(c))*lic)
plt.plot(np.arange(len(c)), np.ones(len(c))*C)
plt.plot(np.arange(len(c)), c)
plt.show()

print("Acho que deve esta :p")