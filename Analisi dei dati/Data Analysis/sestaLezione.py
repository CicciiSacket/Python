#libreria numpy, ha un comando 'array' che rende array una lista py [lista = eterogenea, array = omogeneo, altrimenti fa un casting in automatico dove possibile]
import numpy as np
A = np.array([1,2,3])

from numpy import array
B = array([[1,2],[4,1]])# crea una matrice, array bidimensionale
# C = array([[1,2,3],[4,5,6,7,8,9]]) #la matrice viene generata solamente se le liste dell'array hanno stessa lunghezza
print(A)
print(B[0]) #uso gli array così posso indicizzare
print(A[-1]) #stampa l'ultimo elemento dell'array, con il negativo la conta parte dalla fine
print(A[0:2]) #da zero a due posizione
print('\n')
F = [1,3,14,12,17,23,1,-23]
L = array(F)
print(L)
print(L.min())
print(L.max())
print(L.mean())
print(L.sum())
print(L.size)
print(L.shape)
print('\n')
print(L.sort())
print('\n')
print(L.argmax())
print(L.argmin())
print('\n')
M = L.cumsum()
print(M)
print('\n')
L[7] = 33
print(L)
print(L.nonzero()) 
print('\n')
print(L*2) #tutti gli elementi moltiplicati per due e poi messi in nuovo array
C = 2*L + 40
print(C) #tutti gli elementi moltiplicati per due e sommati a 40 e poi messi in nuovo array, si somma per uno scalare
print('\n')
K = L + C #aritmetica tra array
J = L - C #aritmetica tra array 
G = L[0:3]
# H = L + G #errore, se non sono della stessa lunghezza non si può fare aritmetica tra array {Operazione permessa in linguaggio R}
print(K)
print(J)
print(G)
print(L*L) #ogni elemento di L viene moltiplicato per ogni elemento di L
print(L/L) #ogni elemento diventa float '1.', con // torna intero

#anche per gli array vale la regola degli alias e i riferimenti, uguale anche il metodo arrayNuovo = array.copy() per creare una copia dell'oggetto
print('\n')
print(B)
print(B.transpose()) #transpose, gira la matrice di 90gradi
