import numpy as np

class Cluster:
	 #inicializa o clusters com um vetor
    def __init__(self, vector, label):
        self.elements= np.array([vector], dtype=float)
        self.label= [label]
	# mostra informacoes sobre o cluster
    def __str__(self):
        str= "Cluster( "
        for l in self.label:
            str+=l
            if l != self.label[-1]:
                str+=","
        str+=" )"
        return str
	# adiciona outro cluster a ele
    def add(self, other):
        self.elements= np.vstack((self.elements, other.elements))
        self.label= self.label+other.label
	# retorna o centro do cluster
    def centroid(self):
        return np.mean(self.elements.T,axis=1)
	# calcula a distancia para outro cluster
    def distance(self, other):
        k= (self.elements.shape[0]*other.elements.shape[0])/\
           (self.elements.shape[0]+other.elements.shape[0])
        return np.sum((self.centroid()-other.centroid())**2)*k

# ler os dados de um arquivo e retorna os clusters
def load_file(name): 
    arq = open(name, 'r')
    texto = arq.readlines()
    arq.close()
    clusters= []
    mean= np.array(texto[-2].split(' ')[1:], dtype=float)
    std= np.array(texto[-1].split(' ')[1:], dtype=float)
    for linha in texto[:-2]:
        c_= (np.array(linha.split(' ')[1:],dtype=float)-mean)/std
        c= Cluster(c_, linha.split(' ')[0])
        clusters.append(c)
    return clusters, mean, std

# algoritimo de Ward
def computeClusters(clusters, media): 
    R = []
    PST2= []
    while len(clusters) > 1:
		# calcula distancia entre clusters
        min_dis = 999999
        a = Cluster([], "")
        b = Cluster([], "")
        for ci in clusters:
            for cl in clusters:
                if ci != cl and ci.distance(cl) < min_dis:
                    min_dis = ci.distance(cl)
                    a = ci
                    b = cl
		# junta clusters com menor distancia
        a.add(b)
		# remove o cluster adiciona da lista de clusters
        clusters.remove(b)
		# Mostra todos os clusters atuais
        str= ''
        for ci in clusters: str+=ci.__str__()+", "
		# calcula R
        SSB = 0
        SST = 0
        for ci in clusters:
            SSB += ci.elements.shape[0] * np.sum((ci.centroid() - media) ** 2)
        for ci in clusters:
            for x in ci.elements:
                SST += np.sum((x - ci.centroid()) ** 2)
		# calcula PST2
        pstMax= 0
        for ci in clusters:
            for cl in clusters:
                Bil= ci.distance(cl)
                s1= 0
                s2= 0
                for x in ci.elements: s1= np.sum((x - ci.centroid()) ** 2)
                for x in cl.elements: s2= np.sum((x - cl.centroid()) ** 2)
                if (s1+s2) == 0: continue
                pst= Bil/(s1+s2)*(ci.elements.shape[0]+cl.elements.shape[0]-2)
                if pst > pstMax: pstMax= pst
		R.append(SSB / SST)
        PST2.append(pstMax)
    return R, PST2
