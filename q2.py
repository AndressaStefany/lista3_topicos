from sklearn.cluster import KMeans
import numpy as np

arq = open('paises.txt', 'r')
texto = arq.readlines()

x=[]
y=[]
for linha in texto[:-2]:
    lst = linha.split(' ')[1:]
    x.append(lst)
    y.append(linha.split(' ')[0])

x= np.array(x, dtype=float)

kmeans = KMeans(n_clusters=3, random_state=0).fit(x)

predict = kmeans.predict(x)

clus0 = []
clus1 = []
clus2 = []

for i in range(len(x)):
    if predict[i] == 0:
        clus0.append(y[i])
    elif predict[i] == 1:
        clus1.append(y[i])
    elif predict[i] == 2:
        clus2.append(y[i])


print('\n clus0 ')
print(clus0)
print('\n')
print('clus1 ')
print(clus1)
print('\n')
print('clus2 ')
print(clus2)
print('\n')
arq.close()
