# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 22:38:13 2021

@author: Giovanni
"""

from math import sin, cos, tan
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# Serie, creazione

# da una lista
valori=[12,34,12,17]
S1=pd.Series(valori)

# da due liste
valori=[12,34,12,17]
etichette=["mele","pere","banane","kiwi"]
S2=pd.Series(valori,index=etichette)

# da un dizionario
dizionario={"mele":12,"pere":34,"banane":12,"kiwi":17}
S3=pd.Series(dizionario)

# Serie, accesso agli elementi e slicing
print(S1[0]) # restituisce valore
print(S1[1:3]) # restituisce una serie
print(S2["kiwi"])
print(S2[3])
print(S2[["kiwi","mele"]])
print(S2[[3,0]])

# slicing logico
print(S2>13)
print(S2[S2>13])

# accesso a Serie senza etichette esplicite, sono equivalenti
S1[2]
S1.loc[2]
S1.iloc[2]

# accesso a serie con etichette esplicite
S2[2]
S2.loc[2] # errore
S2["banane"]
S2.loc["banane"]

S2.iloc[2]
S2.iloc["banane"] # errore

# REGOLA
#loc per le etichette
#iloc per gli indici di posizione

# operazioni sulle Serie - elemento per elemento che abbiano eguali indici
S4=S1*S1
S5=S1*S2

# metodi delle Serie - apply
def doppio(x):
    return 2*x
S6=S2.apply(doppio)

# metodi delle Serie - copy
S7=S2.copy()

# metodi delle Serie - head e tail
S6.head()
S6.tail()

# medoti delle Serie, descrittori statistici
S1.min()
S1.max()
S1.mean()
S1.median()
S1.quantile(.25)
S1.quantile(.75)
S1.var()
S1.std()
S1.describe()
S1.sum()
S1.cumsum()

# metodi delle Serie, restituzione parti e eleimianzione doppi
S2.index
S2.values
S2.nunique()
S2.unique()

# altri metodi
S1.rank() # restituisce la posizione in ordine
S8=S2.drop("banane")
S9=S2+S8
S9.hasnans
S9.isna()
S10=S9.dropna()

S2.pop("banane") # toglie l'elemento con etichetta/posto dato
S11=S2.replace(12,1000)
S12=S2.append(S1)
 
