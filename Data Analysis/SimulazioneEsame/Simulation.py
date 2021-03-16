import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import pearsonr
from scipy import stats 
from statsmodels.formula.api import ols

def mediana(dati):
    d = dati.copy()
    d.sort()
    if len(d) % 2 == 1:
        return d[len(d)//2]
    else:
        return (d[len(d)//2] + d[len(d)//2 - 1]) / 2

def primoQuartile(dati):
    primaMeta=[]
    m=mediana(dati)
    for x in dati:
        if x<=m:
            primaMeta.append(x)
    return mediana(primaMeta)

def terzoQuartile(dati):
    secondaMeta=[]
    m=mediana(dati)
    for x in dati:
        if x>m :
            secondaMeta.append(x)
    return mediana(secondaMeta)


"""
Esercizio 1 
"""
TUTTI = pd.read_csv('Data Analysis/SimulazioneEsame/height_weight.csv')

"""
Esercizio 2
"""
Maschi = pd.DataFrame(TUTTI[TUTTI["sex"] == "M"])
Femmine =pd.DataFrame(TUTTI[TUTTI["sex"] == "F"])

"""
Esercizio 3 (Aggiungere print)
"""
(TUTTI.describe(),'\n') 
(Maschi.describe(),'\n')
(Femmine.describe(),'\n')

"""
Esercizio 4
"""
plt.figure("Esercizio 4, figura 1")
plt.subplot(2,2,1)
plt.title("BMI Tot")
TUTTI["BMI"].hist()
plt.subplot(2,2,2)
plt.title("BMI M")
Maschi["BMI"].hist()
plt.subplot(2,2,3)
plt.title("BMI F")
Femmine["BMI"].hist()

plt.figure("Esercizio 4, figura 2")
plt.subplot(2,2,1)
plt.title("height Tot")
TUTTI["height"].hist()
plt.subplot(2,2,2)
plt.title("height M")
Maschi["height"].hist()
plt.subplot(2,2,3)
plt.title("height F")
Femmine["height"].hist()

plt.figure("Esercizio 4, figura 3")
plt.subplot(2,2,1)
plt.title("weight Tot")
TUTTI["weight"].hist()
plt.subplot(2,2,2)
plt.title("weight M")
Maschi["weight"].hist()
plt.subplot(2,2,3)
plt.title("weight F")
Femmine["weight"].hist()
#plt.show()

"""
Esercizio 5 (Aggiungere print)
"""
P_TUTTI = TUTTI.corr()
P_M = Maschi.corr()
P_F = Femmine.corr()

"""
Esercizio 6
"""
#previsioni del BMI a partire dall'height
modello = ols("BMI ~ height",TUTTI).fit()
modello.params
modello.rsquared
modello.pvalues

"""
Esercizio 7
"""
Z6 = pd.DataFrame()
Z6['Z_W'] = (TUTTI["weight"] - TUTTI["weight"].mean() / TUTTI["weight"])
Z6['Z_H']= (TUTTI["height"] - TUTTI["height"].mean() / TUTTI["height"])
Z6.describe()
#corretto quello sopra
Z7 = pd.DataFrame()
Z7["weight"] = stats.zscore(TUTTI["weight"])
Z7["height"] = stats.zscore(TUTTI["height"])

"""
Esercizio 8
"""
(Z7.corr())

"""
Esercizio 9
"""
modello = ols("weight ~ height",TUTTI).fit()
modello.params
modello.rsquared
modello.pvalues

"""
Esercizio 10
"""
Z2 = pd.DataFrame()
#print((Z7["weight"]).quantile(0.25))
first = primoQuartile(list(Z7["weight"]))
thirth = terzoQuartile(list(Z7["weight"]))
result1 = Z7["weight"][Z7["weight"] >= first]
result0 = Z7["weight"][Z7["weight"] <= thirth]
z2 = (result0) + (result1)
Z2["weight"] = z2.unique()

"""
Esercizio 11
"""
plt.figure('Esercizio 11')
plt.plot(Z2,"or")
plt.show()