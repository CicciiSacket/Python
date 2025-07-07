# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
 
import math as mh
import numpy as np
import numpy.random
import matplotlib.pyplot as plt 
import pandas as pd

#%matplotlib qt 


#creiamo la nostra prima serie
#modo uno, a partire da una lista
S = pd.Series([12,17,4,18,23])
print(S) #ci stampa due colonne, la prima con le chiavi e la seconda con i valori {simile ad un dizionario, le chiavi le ha generate pandas}

print(S.size) #dimensione
print(S.count()) #dimensione

print(S.sum()) #somma degli elementi

C = S.cumsum() #somma cumulativa degli elementi, il primo è il primo ma dal secondo in poi è dato dal precedente più quello in analisi
print(C)

A = S.to_string()
print(A) #stampa al solito indici da un lato e valori dall'altro

print(S.mean()) #stampa il valore della media
print(S.median()) #stampa il valore mediano

print(S.quantile(.25)) #primo quartile
print(S.var()) #varianza
print(S.std()) #deviazione standard
print(S.sort_values()) #sort

S.to_csv("SerieS.csv") #la serie s viene salvata nel file SerieS.csv!!!
S.to_csv("S_Header.csv",header=False) #viene generato il file senza l'header
S.to_csv("S_Header2.csv",header=["Numeri"]) #decidiamo noi l'header e quindi l'intestazione della seconda colonna, in questo caso numeri. La prima colonna degli indici non ha intestazione


S2 = pd.read_csv("SerieS.csv") #lettura del file, si mette il path in questo caso è nella stessa cartella. Quando lo rileggiamo da una serie questo diventa un dataframe
print(S2)

S3 = pd.read_csv("S_Header2.csv")
print(S3)

S4 = pd.read_csv("S_Header2.csv",header=None)
print(S4)


#modo 2 da un array di numpy
P = pd.Series(np.array([1,2,3,4]))
print(P)

#modo 3 con un dizionario
R = pd.Series({"a":20,"b":25,"c":18}) #in questo modo decido io le chiavi, e posso accedervi tipo con R[0]{implicito} oppure con R["a"]{esplicito} ottenendo entrambi lo stesso risultato.
print(R)

#modo 4
T = pd.Series([10,11,12], index=["x","y","z"]) #gli indici li passiamo tramite una lista
print(T)

T2 = T[["x","y"]] #slicing per indici espliciti
print(T2)

T3 = T[0:1] #slicing tipo lista con indici impliciti
print(T3)

#in generale py preferisce l'indice esplicito
