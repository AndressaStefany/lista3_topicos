from matplotlib import pyplot as plt
import numpy as np

def mmq(x, y, coef):
    A= []
    B= []
    for j in range(0,len(y)):
        row= []
        for c in coef:
            row.append(x[j]**c)
        A.append(row)
        B.append(y[j])
    A= np.asarray(A)
    B= np.asarray(B).T
    c= np.dot(np.linalg.inv(np.dot(A.T,A)), np.dot(A.T,B))
    return c

fig = plt.figure()
x= [4,6,8,10,14,16,20,22,24,28,34,36,38]
y= [30,18,22,28,14,22,16,8,20,14,14,0,8]
c= mmq(x, y, [0, 1])
x1= np.array(x)#np.linspace(min(x), max(x), 100)
y1= c[0]+c[1]*x1
plt.plot(x, y,'x', x1,y1)
print("Coeficientes ", c)
print("Media y real ", np.mean(y), np.std(y))
print("Media y apro ", np.mean(y1), np.std(y1))
st=np.sum((y-np.mean(y))**2)
sr=np.sum((y-y1)**2)
r=np.sqrt((st-sr)/st)
print("r= ", r)

fig = plt.figure()
x= [2.5,3.5,5,6,7.5,10,12.5,15,17.5,20]
y= [5,3.4,2,1.6,1.2,0.8,0.6,0.4,0.3,0.3]
c= mmq(np.log(x), np.log(y), [0, 1])
x1= np.array(x)#np.linspace(min(x), max(x), 100)
y1= np.exp(c[0])*x1**c[1]
plt.plot(x, y,'x', x1,y1)
print("Coeficientes ", c)
print("Media y real ", np.mean(y), np.std(y))
print("Media y apro ", np.mean(y1), np.std(y1))
st=np.sum((y-np.mean(y))**2)
sr=np.sum((y-y1)**2)
r=np.sqrt((st-sr)/st)
print("r= ", r)


x1= [1,1,2,2,3,3,4,4]
x2= [1,2,1,2,1,2,1,2]
y= [18,12.8,25.7,20.6,25,29.8,45.5,40.3]
A=[]
B=[]
for i in range(len(y)):
    a= [1, x1[i], x2[i]]
    A.append(a)
    B.append(y[i])
A= np.asarray(A)
B= np.asarray(B).T
c= np.dot(np.linalg.inv(np.dot(A.T,A)), np.dot(A.T,B))
y1= []
for a,b in zip(x1,x2):
    y1.append(c[0]+c[1]*a+c[2]*b)
y1= np.asarray(y1)
print("Coeficientes ", c)
print("Media y real ", np.mean(y), np.std(y))
print("Media y apro ", np.mean(y1), np.std(y1))
st=np.sum((y-np.mean(y))**2)
sr=np.sum((y-y1)**2)
r=np.sqrt((st-sr)/st)
print("r= ", r)

plt.show()