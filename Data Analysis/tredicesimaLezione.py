""" 
Correlazione -> misura la dipendenza tra coppie di variabili
Indici di correlazione: Pearson(figlio della pera)and Spearman(uomo della lancia)
"""

import math
import pandas as pd
import matplotlib.pyplot as plt
import scipy


D = pd.read_csv('Data Analysis/popolazioneSicilia.csv')
D = D.set_index("prov")
D.describe()
plt.figure()
D.boxplot()
D.hist() #come si distribuiscono lungo le provincie1, istogramma
D.plot.density() #istogramma curvo
plt.figure()
plt.plot(D.maschi,D.femmine,'*',markersize=22)
D.corr() #indice di person, ovvero la correlazione tra le variabili, più vicino ad uno più direttamente proporzionali, mentre se -1 inversamente proporzionali [ >0.5 || <-0.5 signifigicativa, compresa tra i due valori è indicativa ma non significativa]

#####
df01 = pd.read_csv("Data Analysis/RieslingYield_vs_avgTemp_no_comment.csv")
df01 = df01.set_index("year")
plt.figure()
plt.plot(df01.temp,df01.racc,"o",markersize=10) 
plt.show()
print(df01.corr())