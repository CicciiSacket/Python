""" Consideriamo il data_set del file weight-height.csv. Questi dati riguardano informazioni su: genere, altezza e peso di 10.000 soggetti."""
# Import e gestione del data_set
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
from scipy import stats 
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

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
prob = 1 - alpha
df = len(M)+len(F)-2
cv = stats.t.ppf(prob, df)

print(t_test.statistic[0])
print(df)
print(cv)
print(t_test.pvalue[0])

if abs(t_test.statistic[0]) >= cv:
    print('popolazione diverse') 
else:
    print('stessa popolazione')

if t_test.pvalue[0] < alpha:
    print('diversa popolazione')
else:
    print('popolazione stessa')

plt.figure(figsize=(16,9))
plt.title('Height vs Weight scatter plot', size= 25)
plt.scatter(Males['Weight'], Males['Height'], alpha= 0.4, marker= '^', label = 'Male')
plt.scatter(Females['Weight'], Females['Height'], alpha= 0.4 , marker='*', label = 'Female')
plt.xlabel('Weights', size= 25)
plt.ylabel('Heights', size= 25)
plt.legend(fontsize = 25)



""" Effettuare una analisi di regressione lineare creando un grafico che mostra i punti e la retta di regressione trovata """
#Usando la funzione stats.linregress() su altezza e peso è possibile ottenere tutte le informazioni richieste per il fit lineare
print('Males')
ym, xm = data_set['Height'][data_set['Gender'] == 'Male'], data_set['Weight'][data_set['Gender'] == 'Male']
slope_male, intercept_male,r_value_male,p_value_male, std_err_male = stats.linregress(xm,ym)
print('Slope: ', slope_male)
print('Intercept: ', intercept_male)
print('r value: ', r_value_male, 'R2: ', r_value_male**2)
print('p value: ', p_value_male)
print('Std err: ', std_err_male)
print('')
print('Females')
yf, xf = data_set['Height'][data_set['Gender'] == 'Female'], data_set['Weight'][data_set['Gender'] == 'Female']
slope_female, intercept_female,r_value_female, p_value_female, std_err_female = stats.linregress(xf,yf)
print('Slope: ', slope_female)
print('Intercept: ', intercept_female)
print('r value: ', r_value_female, 'R2: ', r_value_female**2)
print('p value: ', p_value_female)
print('Std err: ', std_err_female)



fit_line = slope_male * xm + intercept_male
plt.title('Regressione lineare tra altezza e peso')
plt.scatter(xm,ym, c = 'Blue', alpha = 0.4, label = 'Maschi')
plt.plot(xm,fit_line, c='Red',  label = 'Reg. maschi')

fit_line = slope_female * xf + intercept_female
plt.scatter(xf,yf, c = 'yellow', alpha = 0.4, label = 'Femmine')
plt.plot(xf,fit_line, c = 'green', label = 'Reg. femmine')
plt.legend()
#Nel plot viene mostrato lo scatter plot di altezza e peso senza considerare il sesso con la linea che rappresenta la retta che fitta i dati, inoltre dato che la dipendenza tra altezza e peso per i due generi è compatibile, si può fare un unico fit



""" Allenare uno o più algoritmi di classificazione dividendo il dataset in train e target """
spec, gender = data_set[['Weight', 'Height']], data_set['Gender']


scaler = StandardScaler()
pipeline = Pipeline([('transformer', scaler), ('estimator', GaussianNB())]) #pipeline per scalare e poi allenare l'estimatore
goal = cross_val_score(pipeline, spec, gender, cv=20) #restituisce i valori della cross validation
print(goal)
print(np.mean(goal))#ritorna al 90%

plt.show() #io che uso visual studio devo insere questo per far si che si visualizzino i grafici (li visualizzo con python launcher e python IDLE)

