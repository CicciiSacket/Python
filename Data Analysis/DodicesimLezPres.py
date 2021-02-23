import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#dataframe = tabella modi excel
df01 = pd.read_csv("Data Analysis/RieslingYield_vs_avgTemp_no_comment.csv")
df02 = pd.read_csv("Data Analysis/RieslingYield_vs_avgTemp_no_comment.csv",header=0,names=["Anno","Temperatura","Raccolto"]) #parte da zero e gli indici sono rinominati come vogliamo noi

#colonne della tabella che per pandas sono serie
Colonna01 = df02.Anno
Colonne = df02[["Anno","Temperatura"]] #si passa una lista con nomi delle etichette
Colonne02 = df02.iloc[:,0:2] #solo i : senza indici se la prende tutta; Con iloc prendo le righe e le colonne come fosse un array [: -> tutte le righe, le colonne da 0 a 2]
Colonne03 = df02.loc[:,"Anno":"Temperatura"] #loc per usare le etichette

df03 = pd.read_csv("Data Analysis/RieslingYield_vs_avgTemp_no_comment.csv",index_col = "year") #tratta year come indice e non come dato
alcune_righe = df03.loc["2001":"2009",:] #prende tutte le colonne e le righe dal 2001 al 2009
df01.describe()

#secondo modo per creare i DB, prima si creano i records come liste [questo è passo passo ciò che fa read_csv]
A = ["Alice",12,"Maria","Pippo"]
B = ["Beatrice",10,"Laura","Diego"]
C = ["Carla",13,"Maria","Filippo"]
L = [A,B,C] #lista dei records
df06 = pd.DataFrame(L) #dataframe con le etichette messe in automatico

df07 = pd.DataFrame(L,index = ["A","B","C"]) #abbiamo dato il nome alle righe
df08 = pd.DataFrame(L,index = ["A","B","C"], columns = ["Name","Age","Mum","Dad"] ) #abbiamo dato il nome alle colonne
#df08 = df08.set_index("Name") #rendo la colonna dei nomi il mio indice; se non avessi messo df08 = .. non cambiava l'intero dataframe! Per ovviare questo problema si fa:
df08.set_index("Name", inplace = True)

#estrarre quelli con più di 11 anni:
c = df08["Age"] > 11 #così da solamente true o false, si mette infatti:
df09 = df08[c]
df10 = df08[df08["Age"] > 11] #Questo è il modo giusto!!!
df11 = df08[(df08["Age"] > 11) & (df08["Dad"] == "Pippo")]
print(df11)
