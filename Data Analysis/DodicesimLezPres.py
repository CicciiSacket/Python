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


df03 = pd.read_csv("Data Analysis/RieslingYield_vs_avgTemp_no_comment.csv",index_col = "year") #tratta yera come indice e non come dato
alcune_righe = df03.loc["2001":"2009",:] #prende tutte le colonne e le righe dal 2001 al 2009

print(alcune_righe)