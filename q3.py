
import matplotlib.pyplot as plt
import numpy as np
import time

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
        self.ij = np.array(np.meshgrid(np.arange(self.l), np.arange(self.c))).T.reshape(-1, 2)

    def winner(self, x):
        s = np.sum((self.W - x) ** 2, axis=2)
        mini, minj = np.unravel_index(s.argmin(), s.shape)
        return 0, mini, minj

    def updateW(self, x, wi, wj):
        wij= np.array([wi, wj])
        A= np.exp(-np.sum((self.ij-wij)**2,axis=1)/(2*self.sigma))
        A= np.repeat(A, self.n, axis=0).reshape((self.l, self.c, self.n))
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

    def predict(self, Y, labels):
        clusters= [[] for i in range(self.c*self.l)]
        for y, l in zip(Y, labels):
            min, i, j= self.winner(y)
            clusters[i*self.c+j].append(l)
        #print(self.W)
        return clusters


def load_file(name):
    arq = open(name, 'r')
    texto = arq.readlines()
    arq.close()
    x= []
    y= []
    for linha in texto[:-2]:
        x.append(linha.split(' ')[1:])
        y.append(linha.split(' ')[0])

    #media= np.array(texto[-2].split(' ')[1:], dtype=float)

    return x, y

def paises():
    x, y= load_file('paises.txt')
    x=np.array(x,dtype=float)
    x=x-x.mean(axis=0)
    x=x/x.std(axis=0)
    som= SOM(1,4,4)
    som.train(x)

    clus= som.predict(x, y)

    f, axis = plt.subplots(len(x), sharex=True)
    for c in clus:
        print(c)
    for i in range(len(x)):
        out = som.output(x[i])
        #print(y[i], out)
        axis[i].imshow(out, cmap='gray', interpolation='nearest')
        #axis[i].set_ylabel(y[i])
        axis[i].set_title(y[i], color='C0')

    plt.legend(y)
    plt.show()

def testeSOM1():
    x= np.random.uniform(0,1,(100,2))
    som= SOM(5,5,2)
    for i in range(som.l):
        for j in range(som.c):
            plt.plot(som.W[i, j][0], som.W[i, j][1], 'rx')

    plt.figure()
    som.train(x)

    for i in range(som.l):
        for j in range(som.c):
            plt.plot(som.W[i, j][0], som.W[i, j][1], 'bx')
    plt.show()

def testeSOM2():
    colors = np.array(
             [[0., 0., 0.],
              [0., 0., 1.],
              [0., 0., 0.5],
              [0.125, 0.529, 1.0],
              [0.33, 0.4, 0.67],
              [0.6, 0.5, 1.0],
              [0., 1., 0.],
              [1., 0., 0.],
              [0., 1., 1.],
              [1., 0., 1.],
              [1., 1., 0.],
              [1., 1., 1.],
              [.33, .33, .33],
              [.5, .5, .5],
              [.66, .66, .66]])
    color_names = \
            ['black', 'blue', 'darkblue', 'skyblue',
             'greyblue', 'lilac', 'green', 'red',
             'cyan', 'violet', 'yellow', 'white',
             'darkgrey', 'mediumgrey', 'lightgrey']
    som = SOM(20,30,3)
    som.train(colors)
    print(som.W)
    plt.imshow(som.W, origin='lower')
    for i in range(len(color_names)):
        out, mi, mj = som.winner(colors[i])
        print(colors[i], color_names[i], som.W[mi,mj])
        plt.text(mj, mi, color_names[i], ha='center', va='center',
                bbox=dict(facecolor='white', alpha=0.5, lw=0))

    plt.show()

#testeSOM1()
#testeSOM2()
paises()