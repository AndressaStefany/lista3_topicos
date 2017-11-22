import matplotlib.pyplot as plt
import numpy as np

class SOM:
    def __init__(self, l, c, n):
        self.l= l
        self.c= c
        self.n= n
        self.eta= 0.01
        self.sigma= 4
        self.nInterations= 2000
        self.initW()

    def initW(self):
        self.W= np.random.random((self.l, self.c, self.n))
        self.ij = np.array(np.meshgrid(np.arange(self.l),\
		          np.arange(self.c))).T.reshape(-1, 2)

    def winner(self, x):
        s = np.sum((self.W - x) ** 2, axis=2)
        mini, minj = np.unravel_index(s.argmin(), s.shape)
        return 0, mini, minj

    def updateW(self, x, wi, wj):
        wij= np.array([wi, wj])
        A= np.exp(-np.sum((self.ij-wij)**2,axis=1)\
          /(2*self.sigma))
        A= np.repeat(A, self.n, axis=0)
		A= A.reshape((self.l, self.c, self.n))
        self.W+=self.eta*(x-self.W)*A

    def train(self, X):
        X_=X.copy()
        for i in range(self.nInterations):
            np.random.shuffle(X_)
            for x in X_:
                min, mini, minj= self.winner(x)
                self.updateW(x, mini, minj)
            if i%100 == 0:
                print("It", i)

    def output(self, y):
        out = np.empty((self.l, self.c))
        for i in range(self.l):
            for j in range(self.c):
                out[i,j]= np.sum((y-self.W[i,j])**2)
        return out

    def clusters(self, Y, labels):
        clus= [[] for i in range(self.c*self.l)]
        for y, l in zip(Y, labels):
            min, i, j= self.winner(y)
            clus[i*self.c+j].append(l)
        return clus


def load_file(name):
    arq = open(name, 'r')
    texto = arq.readlines()
    arq.close()
    x= []
    y= []
    for linha in texto[:-2]:
        x.append(linha.split(' ')[1:])
        y.append(linha.split(' ')[0])
	x=np.array(x,dtype=float)
    x=x-x.mean(axis=0)
    x=x/x.std(axis=0)
    return x, y

def paises():
    x, y= load_file('paises.txt')

    som= SOM(1,4,4)
    som.train(x)
    clus= som.clusters(x, y)
    for c in clus:
        print(c)

    f, axis = plt.subplots(len(x), sharex=True)
    for i in range(len(x)):
        out = som.output(x[i])=
        axis[i].imshow(out, cmap='gray', interpolation='nearest')
        axis[i].set_title(y[i], color='C0', y=-0.2)
        axis[i].set_yticks([])

    plt.legend(y)
    plt.show()
