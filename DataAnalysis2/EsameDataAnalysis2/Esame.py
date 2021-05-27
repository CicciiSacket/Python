""" Consideriamo il data_set del file weight-height.csv. Questi dati riguardano informazioni su: genere, altezza e peso di 10.000 soggetti."""
# Import e gestione del data_set
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
from scipy import stats 
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier

data_set = pd.read_csv('weight-height.csv')
data_set.columns = ['Gender', 'Height', 'Weight']
data_set.head()



""" Effettuare un'analisi statistica calcolando i principali indici statistici """ 
data_set.describe()
#Si generano due dataframe che filtrano tutti i maschi e le femmine
Males = data_set.loc[data_set['Gender']== 'Male'] 
Females = data_set.loc[data_set['Gender']== 'Female']
Males.describe() #restituisce media, deviazione standard, min
Females.describe() #restituisce media, deviazione standard, min

#Interpretazione visiva degli indici statistici
plt.figure(figsize=(8,5))
plt.title('Height histogram', size = 20)
plt.hist(data_set['Height'][data_set['Gender'] == 'Male'], alpha = 0.5, label = 'Males')
plt.hist(data_set['Height'][data_set['Gender'] == 'Female'], alpha = 0.5, label = 'Females')
plt.xlabel('Height', size = 15)
plt.ylabel('Frequency', size = 15)
plt.legend(fontsize = 14)

#Interpretazione visiva degli indici statistici
plt.figure(figsize=(8,5))
plt.title('Weight histogram', size = 20)
plt.hist(data_set['Weight'][data_set['Gender'] == 'Male'], alpha = 0.5, label = 'Males')
plt.hist(data_set['Weight'][data_set['Gender'] == 'Female'], alpha = 0.5, label = 'Females')
plt.xlabel('Weight', size = 15)
plt.ylabel('Frequency', size = 15)
plt.legend(fontsize = 14)



""" Effettuare un'analisi di verifica di ipotesi statistica per determinare se esiste una distinzione tra le feature degli uomini e quelle delle donne """
M = list(zip(Males['Weight'], Males['Height']))
F = list(zip(Females['Weight'], Females['Height']))

#Gli istogrammi fatti ci portano a pensare che la classe degli uomini può essere distinta da quella delle donne e per testare questa ipotesi utilizziamo il t-test su Height e Weight 
t_test = stats.ttest_ind(M,F) #I risultati del t-test sono in accordo con la nostra previsione che i due generi sono statisticamente separabili 
alpha = .05
prob = 1- alpha
print(t_test.statistic)
print(t_test.pvalue)

plt.figure(figsize=(16,9))
plt.title('Height vs Weight scatter plot', size= 25)
plt.scatter(Males['Weight'], Males['Height'], c = 'DarkBlue', alpha= 0.4, marker= '^', label = 'Male')
plt.scatter(Females['Weight'], Females['Height'], c = 'DarkRed', alpha= 0.4 , marker='*', label = 'Female')
plt.xlabel('Weights', size= 25)
plt.ylabel('Heights', size= 25)
plt.legend(fontsize = 25)



""" Effettuare una analisi di regressione lineare creando un grafico che mostra i punti e la retta di regressione trovata """
#Usando la funzione stats.linregress() su altezza e peso è possibile ottenere tutte le informazioni richieste per il fit lineare
print('Males')
ym, xm = data_set['Height'][data_set['Gender'] == 'Male'], data_set['Weight'][data_set['Gender'] == 'Male']
slope_m, intercept_m,r_value_m,p_value_m, std_err_m = stats.linregress(xm,ym)
print('Slope: ', slope_m)
print('Intercept: ', intercept_m)
print('r value: ', r_value_m, 'R2: ', r_value_m**2)
print('p value: ', p_value_m)
print('Std err: ', std_err_m)
print('')
print('Females')
yf, xf = data_set['Height'][data_set['Gender'] == 'Female'], data_set['Weight'][data_set['Gender'] == 'Female']
slope_f, intercept_f,r_value_f, p_value_f, std_err_f = stats.linregress(xf,yf)
print('Slope: ', slope_f)
print('Intercept: ', intercept_f)
print('r value: ', r_value_f, 'R2: ', r_value_f**2)
print('p value: ', p_value_f)
print('Std err: ', std_err_f)

def predict(x,a,b):
    return a * x +b

fitLine = predict(xm,slope_m, intercept_m)
plt.title('Regressione lineare tra altezza e peso')
plt.scatter(xm,ym, c = 'DarkBlue', alpha = 0.4, label = 'Maschi')
plt.plot(xm,fitLine, c='DarkRed',  label = 'Reg. maschi')

fitLine = predict(xf,slope_f, intercept_f)
plt.scatter(xf,yf, c = 'yellow', alpha = 0.4, label = 'Femmine')
plt.plot(xf,fitLine, c='green', label = 'Reg. femmine')
plt.legend()
#Nel plot viene mostrato lo scatter plot di altezza e peso senza considerare il sesso con la linea che rappresenta la retta che fitta i dati, inoltre dato che la dipendenza tra altezza e peso per i due generi è compatibile, si può fare un unico fit



""" Allenare uno o più algoritmi di classificazione dividendo il dataset in train e target """
X, y = data_set[['Weight', 'Height']], data_set['Gender']
len(X)
y.head()

scaler = StandardScaler()
pipeline = Pipeline([('transformer', scaler), ('estimator', GaussianNB())]) #pipeline per scalare e poi allenare l'estimatore
scores = cross_val_score(pipeline, X, y, cv=20) #restituisce i valori della cross validation
print(scores)
print(np.mean(scores))

score = []
for P in range(1,10):
    pipeline = Pipeline([('transformer', scaler), ('estimator', DecisionTreeClassifier(max_depth = P))])
    scores = cross_val_score(pipeline, X, y, cv=20)
    print('')
    print(scores)
    print('Max depth = ', P, ' Average score = ',np.mean(scores))
    score.append(np.mean(scores))

plt.title('Best depth decision tree')
plt.xlabel('Max depth')
plt.ylabel('Score')
plt.plot(range(1,10), score)

plt.show() #io che uso visual studio devo insere questo per far si che si visualizzino i grafici (li visualizzo con python launcher e python IDLE)
#I due metodi di classificazione hanno risultati compatibili
