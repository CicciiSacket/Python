import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import pearsonr
from scipy import stats 
from statsmodels.formula.api import ols

"""
Esercizio 1
"""
TUTTI_0 = pd.read_csv("Data Analysis/Esame/infarto.csv")

"""
Esercizio 2
"""
TUTTI = pd.DataFrame()
TUTTI["gender"] = TUTTI_0["gender"]
TUTTI["age"] = TUTTI_0["age"]
TUTTI["bmi"] = TUTTI_0["bmi"]
TUTTI["avg_glucose_level"] = TUTTI_0["avg_glucose_level"]
TUTTI["smoking_status"] = TUTTI_0["smoking_status"]
TUTTI["stroke"] = TUTTI_0["stroke"]
TUTTI = TUTTI.dropna()

"""
Esercizio 3
"""
print(TUTTI.describe())

"""
Esercizio 4
"""
plt.figure("Esercizio 4")
plt.subplot(2,2,1)
plt.title("age")
TUTTI["age"].hist()
plt.subplot(2,2,2)
plt.title("bmi")
TUTTI["bmi"].hist()
plt.subplot(2,2,3)
plt.title("avg_glucose_level")
TUTTI["avg_glucose_level"].hist()
#plt.show()

"""
Esercizio 5
"""
P_TUTTI = TUTTI.corr()
print(P_TUTTI)

"""
Esercizio 6
"""
Z = pd.DataFrame()
Z['Z_Bmi'] = (TUTTI["bmi"] - TUTTI["bmi"].mean() / TUTTI["bmi"])
Z['Z_Glucosio'] = (TUTTI["avg_glucose_level"] - TUTTI["avg_glucose_level"].mean() / TUTTI["avg_glucose_level"])
print(Z)

"""
Esercizio 7
"""
print(Z.describe())

"""
Esercizio 8
"""
plt.figure('Esercizio 8')
plt.scatter(Z['Z_Bmi'],Z['Z_Glucosio'])
#plt.show()

"""
Esercizio 9
"""
modello = ols("Z_Bmi ~ Z_Glucosio",Z).fit()
modello.params
modello.rsquared
modello.pvalues

"""
Esercizio 10
"""
ToZ1 = TUTTI_0[TUTTI_0["stroke"] == 1]
ToZ0 = TUTTI_0[TUTTI_0["stroke"] == 0]
Z1 = pd.DataFrame(ToZ1)
Z0 = pd.DataFrame(ToZ0)

"""
Esercizio 11
"""
plt.figure('Esercizio 11,-Z0-')
plt.scatter(Z0["age"],Z0["smoking_status"])
plt.figure('Esercizio 11,-Z1-')
plt.scatter(Z1["age"],Z1["smoking_status"])
plt.show()

"""
Esercizio 12
"""
modello = ols("age ~ smoking_status",Z0).fit()
modello.params
modello.rsquared
modello.pvalues

"""
Esercizio 13
"""
modello = ols("age ~ smoking_status",Z1).fit()
modello.params
modello.rsquared
modello.pvalues