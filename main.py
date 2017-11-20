import numpy as np

def dist_euclid(n, ):
    return 'a'

arq = open('paises.txt', 'r')
texto = arq.readlines()
arq.close()

x= []
y= []
for linha in texto:
    lst= linha.split(' ')[1:]
    x.append(lst)
    y.append(linha.split(' ')[0])

x= np.array(x, dtype=float)
print 'meu nome é andressa'
print x