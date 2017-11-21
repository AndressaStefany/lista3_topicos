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

string1 = 'Y_1 = '+str(vT[0][0])+' x1 + '+str(vT[0][1])+' x2 + '+str(vT[0][2])+' x3 + '+str(vT[0][3])+' x4'
string2 = 'Y_2 = '+str(vT[1][0])+' x1 + '+str(vT[1][1])+' x2 + '+str(vT[1][2])+' x3 + '+str(vT[1][3])+' x4'
string3 = 'Y_3 = '+str(vT[2][0])+' x1 + '+str(vT[2][1])+' x2 + '+str(vT[2][2])+' x3 + '+str(vT[2][3])+' x4'
string4 = 'Y_4 = '+str(vT[3][0])+' x1 + '+str(vT[3][1])+' x2 + '+str(vT[3][2])+' x3 + '+str(vT[3][3])+' x4'

print('\n (c)\n'+string1+'\n'+string2+'\n'+string3+'\n'+string4)

# letra (d)
variancia = w/np.sum(w)

print('\n (d) \n Variancia: ')
print(variancia)

variancia.sort()
print('\n % Varianças ordenadas: ')
print(variancia)
