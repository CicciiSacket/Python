import numpy as np 
import matplotlib.pyplot as plt 
from scipy import stats 

#genero mille campioni con distribuzione gaussiana e con media dieci e sigma cinque
np.random.seed(24)
values = np.random.normal(10.0,5.0,1000)

#visualizzo l'istogramma e il boxplot
plt.subplot(121)
plt.hist(values,50)
plt.subplot(122)
plt.boxplot(values)
#plt.show()

#calcolo dei quartili
q1 = np.percentile(values,25)
q2 = np.percentile(values,50)
q3 = np.percentile(values,75)
media = np.mean(values)
mediana = np.median(values)
print(str(q1))
print(str(q2))
print(str(q3))
print(media)
print(mediana)

#generiamo numeri da una distribuzine diversa con media 1500 e uguale sigma dei precedenti, qui solo 50 campioni
noise = np.random.normal(1500.0,5.0,50)
noisy_values = np.append(values, noise)
plt.subplot(121)
plt.hist(noisy_values,50)
plt.subplot(122)
plt.boxplot(noisy_values)
#plt.show()
media2 = np.mean(noisy_values)
mediana2 = np.median(noisy_values)
# print(media2)
# print(mediana2)

#confronto media trim-mean(media interquartile)
print(media2)
print(mediana2)
print(stats.trim_mean(noisy_values,0.05)) #tolgo il 5% a destra e lo stesso a sinistra #media interquartile
print(stats.trim_mean(noisy_values,0.1))                                               #media interquartile
print(stats.trim_mean(noisy_values,0.2))                                               #media interquartile
print(stats.trim_mean(noisy_values,0.25))                                              #media interquartile

#variazione di trim_mean al variare del valore di taglio
trim_parameters = np.linspace(0.01, 0.1, 100)
y_values = []
for t in trim_parameters:
    val = stats.trim_mean(tuple(noisy_values),t)
    y_values.append(val)

plt.figure()
plt.plot(trim_parameters,y_values)
# plt.show()
plt.hlines(mediana2, xmin = np.min(trim_parameters), xmax = np.max(trim_parameters), color = 'g', linestyles = '--')
plt.axvline(0.048, color = 'r', linestyle = '--')
plt.show() 
