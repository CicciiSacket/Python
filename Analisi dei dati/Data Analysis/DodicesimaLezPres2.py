import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df01 = pd.read_csv("Data Analysis/RieslingYield_vs_avgTemp_no_comment.csv")
df01.set_index("year",inplace = True )

df01.size #torna il numero totale degli elementi, in questo caso 18+18 perchè year lo considera indice
df01.describe()
df01.head() #torna i primi elementi
df01.tail() #torna gli ultimi elementi

df01.plot()
df01.boxplot() #disegna una box con i limiti min e max e primo quartile e terzo quartile, in mezzo c'è la media e ogni tanto la mediana

plt.figure("Doppio plot")
plt.subplot(1,2,1)
plt.title("Temperature")
plt.plot(df01.temp)
plt.subplot(1,2,2)
plt.title("Raccolto")
plt.plot(df01.racc)
#plt.show()


#NORMALIZZAZIONE: portare i dati sullo stesso ordine di grandezza
#primo metodo
M = max(abs(df01.temp))
t_norm_max = df01.temp / M

#aggiungere colonna al df
df01["t_norm_max"] = t_norm_max

#secondo metodo
Maxs = max(df01.temp)
Mins = min(df01.temp)
t_norm_MinMax = (df01.temp - Mins )/ (Maxs - Mins) 
df01["t_norm_MinMax "] = t_norm_MinMax 
print(df01)