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

P.corr()
plt.figure('mappa di calore, dal più caldo nero al più freddo bianco')
plt.imshow(P.corr(),cmap='hot', interpolation='nearest')

plt.figure('pop vs sup')
plt.plot(P["zTot"],P["sup"],"or",markerSize=10)

plt.figure('com vs sup')
plt.plot(P["comuni"],P["sup"],"or",markerSize=10)


#nuovo dataframe a partire dal precedente, rimuovendo l'outlier, in questo caso messina
P2 = pd.DataFrame(P["maschi"])
P2["femmine"] = P["femmine"]
P2["sup"] = P["sup"]
P2 ["comuni"] = P["comuni"]
P2 = P2.drop("ME")
plt.figure('com vs sup senza messina')
plt.plot(P2["comuni"],P2["sup"],"or",markerSize=10)

P2.corr()
plt.figure('mappa di calore, dal più caldo nero al più freddo bianco 2')
plt.imshow(P2.corr(),cmap='hot', interpolation='nearest')

# plt.show()
""" 
Covarianza(x,y)= 1/N ∑(xi - mx) (yi - my)   
Z_scoring = (voto - media) / (deviazione standard dei voti) #tutto viene riportato nella stessa scala a differenza dei dati in forma normale
Regressione = costruire un modello a partire dai dati [ Abuso di linguaggio storico, in quanto non vi è nessuna regressione ma semplicemente un modello matematico ]
"""

