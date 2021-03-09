import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy

P = pd.read_csv('Data Analysis/popolazioneSicilia.csv')
S = pd.read_csv('Data Analysis/superfici.csv')

#aggiungere colonne 
P = P.set_index("prov")
S = S.set_index("prov")
P["sup"] = S["sup"]
P["comuni"] = S["comuni"]
#salviamo in un file.csv
P.to_csv("Data Analysis/Province.csv")

plt.figure("M vs F")
plt.plot(P["maschi"],P["femmine"],"or",markerSize=10)
mediaM = P["maschi"].mean() 
mediaF = P["femmine"].mean()
plt.plot(mediaM , mediaF, "*b",markerSize=10)
plt.text(mediaM,mediaF,"media")
plt.axvline(mediaM)
plt.axhline(mediaF)
# plt.show()

#Covarianza
P["maschi"].cov(P["femmine"])
P["popTot"].cov(P["comuni"])

#Z scoring è una forma di normalizzazione, un modo assoluto ed apprezzato dagli analisti
P["popTot"].std() #deviazione standard
P["comuni"].std #deviazione standard
P["zTot"] = (P["popTot"] - P["popTot"].mean()) /  P["popTot"].std() #aggiunta di una nuova colonna
P["zCom"] = (P["comuni"] - P["comuni"].mean()) /  P["comuni"].std() 
P.to_csv("Data Analysis/Province.csv")


plt.figure("TOT vs COM")
plt.plot(P["zTot"],P["zCom"],"or",markerSize=10)
plt.show()


""" 
Covarianza(x,y)= 1/N ∑(xi - mx) (yi - my)   
Z_scoring = (voto - media) / (deviazione standard dei voti) #tutto viene riportato nella stessa scala a differenza dei dati in forma normale
"""