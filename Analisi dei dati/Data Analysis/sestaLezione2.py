import numpy as np

A = np.zeros(5) #torna un array di zero tanti quanti l'argomento, tipo per iniziallizare gli array a zero e modificarli in seguito
print(A)
B = np.zeros([5,5]) #torna una matrice di 5x5
print(B)
print('\n')

C = np.eye(3) #torna una matrice "identica" di ordine 3, si chiama eye perchè la matrice identica o identità nei libri viene indicata con la i maiuscola che appunto si leggere con la stessa pronuncia di eye
print(C)
print('\n')

D = np.ones(3) #ritorna un array di float 1.
L = np.ones([3,3]) #matrice di uno 3x3
print(D)
print(L)
print('\n')

F = np.linspace(start=0, stop=20,num=10) #comincia da 0 arriva fino a 20 e lo fa in 10 elementi, ovvero numeri equidistanti da loro, crea sempre un array; ovviamente si può bypassare il nome dei parametri
print(F)
K = np.linspace(0,20,5)
print(K)
print('\n')

N = np.arange(start=0,stop=20,step=1) #da zero a 19 a step a step, l'ultimo numero ovvero lo stop viene escluso
print(N)
J = np.arange(0,100,25) 
print(J)
W = np.arange(0,1,0.2)#posso mettere numeri decimali, tipo nello step
print(W)


