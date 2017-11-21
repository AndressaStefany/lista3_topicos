import numpy as np
import numpy.linalg as la

arq = open('solo.txt', 'r')
texto = arq.readlines()
arq.close()

x=[]
for linha in texto:
    lst = linha.split(' ')
    x.append(lst)

x= np.array(x, dtype=float)

# Matriz de covariancia
matriz = np.cov(np.transpose(x))

print('\n (a) Matriz de covariancia: ')
print(matriz)

# autovetores e autovalores
# os maiores autovalores correspondem aos componentes principais mais importantes
w,v=la.eig(matriz)

# Obtém índices para ordenação decrescente dos autovalores
ind=np.argsort(w)[::-1]
w_dec=w[ind]
v_dec=v[ind]

print('\n (b) \n Autovalores: ')
print(w)
print('\nAutovetores: ')
print(v)

print('\n Organizados: \n Autovalores: ')
print(w_dec)
print('\n Autovetores: ')
print(v_dec)

# checa o modulo unitario
# print(la.norm(v[0]))
# print(la.norm(v[1]))
# print(np.dot(v[0],v[1]))

# letra (c)
vT = v_dec.T

print('\n Matriz de autovetores Transposta:')
print(vT)

# Multiplicar vT * [x1,x2,x3,x4]
# sao 4 valores de Y na verdade
a = vT[0][0]*vT[1][0]*vT[2][0]*vT[3][0]
b = vT[0][1]*vT[1][1]*vT[2][1]*vT[3][1]
c = vT[0][2]*vT[1][2]*vT[2][2]*vT[3][2]
d = vT[0][3]*vT[1][3]*vT[2][3]*vT[3][3]

string = 'Y = '+str(a)+'x1 + '+str(b)+' x2 + '+str(c)+' x3 + '+str(d)+' x4'
print('\n (c)')
print(string)

# letra (d)
variancia = w/np.sum(w)

print('\n (d) \n Variancia: ')
print(variancia)

variancia.sort()
print('\n % Varianças ordenadas: ')
print(variancia)
