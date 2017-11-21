import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

file= open('aluminio.txt')

def load_file(name):
    arq = open(name, 'r')
    texto = arq.readlines()
    arq.close()
    x= []
    for linha in texto[1:]:
        lst= linha.split(' ')
        lst1= lst[:int(len(lst)/2)]
        x.append(lst1)
    for linha in texto[1:]:
        lst= linha.split(' ')
        lst1= lst[int(len(lst)/2):]
        x.append(lst1)

    return x

x= load_file('aluminio.txt')
x= np.asarray(x, dtype=float)

n= 5
d2= 2.326
X= np.mean(x[:,1])
R= np.mean(x[:,2])
lsc= X+3/(np.sqrt(n)*d2)*R
lic= X-3/(np.sqrt(n)*d2)*R
plt.plot(x[:,0],np.ones(len(x[:,0]))*X, label='X')
plt.plot(x[:,0],np.ones(len(x[:,0]))*lsc, label='LSC')
plt.plot(x[:,0],np.ones(len(x[:,0]))*lic, label='LIC')
plt.plot(x[:,0],x[:,1])
plt.title("Grafico de controle X")
plt.legend()
X=35
S=10
print("RCP ", (2*S)/(6*R/d2))
print("Porcentagem de itens fora do processo ", norm.cdf(lic,X,R/(np.sqrt(n)*d2))*100*2, "%")
plt.show()


n= 5
d2= 2.326
X= np.mean(x[:,1])
R= np.mean(x[:,2])
Sw= 1 # descobrir quem e
lsc= R+3/(d2)*Sw*R
lic= R-3/(d2)*Sw*R
plt.plot(x[:,0],np.ones(len(x[:,0]))*R)
plt.plot(x[:,0],np.ones(len(x[:,0]))*lsc, label='LSC')
plt.plot(x[:,0],np.ones(len(x[:,0]))*lic, label='LIC')
plt.plot(x[:,0],x[:,2])
plt.title("Grafico de controle R")
plt.show()