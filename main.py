import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

arq = open('paises.txt', 'r')
texto = arq.readlines()
arq.close()

class Cluster:
    def __init__(self, vector, label):
        self.elements= np.array([vector], dtype=float)
        self.label= [label]

    def __str__(self):
        str= "Cluster( "
        for l in self.label:
            str+=l
            if l != self.label[-1]:
                str+=","
        str+=" )"
        return str

    def add(self, other):
        self.elements= np.vstack((self.elements, other.elements))
        self.label= self.label+other.label

    def centroid(self):
        return np.mean(self.elements.T,axis=1)

    def distance(self, other):
        k= (self.elements.shape[0]*other.elements.shape[0])/\
           (self.elements.shape[0]+other.elements.shape[0])
        return np.sum((self.centroid()-other.centroid())**2)*k

cluters= []
lables= []
for linha in texto[:-2]:
    c= Cluster(linha.split(' ')[1:], linha.split(' ')[0])
    cluters.append(c)

while len(cluters)>1:
    min_dis= 999999
    a= Cluster([], "")
    b= Cluster([], "")
    for ci in cluters:
        for cl in cluters:
            if ci != cl and ci.distance(cl) < min_dis:
                min_dis= ci.distance(cl)
                a= ci
                b= cl
    print(a, " Com ", b)
    a.add(b)
    cluters.remove(b)


def teste():
    x= []
    y= []
    for linha in texto[:-2]:
        lst= linha.split(' ')[1:]
        x.append(lst)
        y.append(linha.split(' ')[0])

    x= np.array(x, dtype=float)
    Z = linkage(x, 'ward')
    fig = plt.figure(figsize=(25, 10))
    dn = dendrogram(Z, labels=y)
    plt.show()

teste()
