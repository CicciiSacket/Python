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
# plt.show()
