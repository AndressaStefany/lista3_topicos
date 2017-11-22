import numpy as np
from scipy.stats import binom

r= lambda t, l: np.exp(-l*t)

n= 5
l= 0.002
t= 1000
print("Probabilidade de durar mais de 1000 horas", r(t,l))
c= r(t,l)
print("Confiabilidade de sobrevivencia pelo menos 2 unidade ", 1-binom.cdf(1,n,r(t,l)))
print("Confiabilidade de sobrevivencia pelo menos 1 unidade ", 1-binom.cdf(0,n,r(t,l)))

R=1
for i in range(n):
    R*=1-r(t,l)
R=1-R
print("Confiabilidade paralelo", R)