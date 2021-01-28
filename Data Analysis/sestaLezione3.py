from numpy import random

# print(random.random()) #con randint() stampa numeri interi compresi nell'intervallo 0 e argomento
# print(random.random(4)) #torna un array di 4 numeri random al solito da 0 ad 1
# print(random.random([2,3])) #torna una matrice 2x3


from  numpy.random import randn #distribuzione normale GAUSS, ritorna un campione

print(randn(2,2)) #matrice di numeri estratti con gauss dove la media è 0 e la dispersione è 1