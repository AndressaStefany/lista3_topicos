import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet
from scipy.spatial.distance import pdist
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

media= np.array(texto[-2].split(' ')[1:], dtype=float)

R= []
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
    #print(a, " Com ", b)
    a.add(b)
    cluters.remove(b)

    SSB = 0
    SST = 0
    for ci in cluters:
        SSB += ci.elements.shape[0] * np.sum((ci.centroid() - media)**2)
    for ci in cluters:
        for x in ci.elements:
            SST += np.sum((x - ci.centroid()) ** 2)
    R.append(SSB/SST)
    #print(SSB, SST, R[-1])


plt.plot(np.arange(len(R))+1, R)
plt.xticks(np.arange(len(R))+1)
#plt.show()
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

    #fig = plt.figure()
    #knee = np.diff(Z[::-1, 2], 2)
    #plt.plot(range(2, len(Z)), knee)
    plt.show()

teste()
