from sklearn.cluster import KMeans
import numpy as np

# processa o arquivo de entrada
def load_file(name):
	arq = open(name, 'r')
	texto = arq.readlines()
	arq.close()
	x=[]
	y=[]
	for linha in texto[:-2]:
	    lst = linha.split(' ')[1:]
	    x.append(lst)
	    y.append(linha.split(' ')[0])
	# normaliza
	x= np.array(x, dtype=float)
	x = x - x.mean(axis=0)
	x = x / x.std(axis=0)
	return x, y

def computeClusters(x):
	nclus= 4
	# utiliza o k-means	
	kmeans = KMeans(n_clusters=nclus, random_state=0).fit(x)
	predict = kmeans.predict(x)
	# agrupa paises do mesmo cluster
	clus= [[] for i in range(nclus)]
	for i in range(len(x)):
	    for j in range(nclus):
    	    if predict[i] == j:
    	        clus[j].append(y[i])
	#mostra os agrupamentos
	for c in clus:
    	print(c)
