import numpy as np 
import matplotlib.pyplot as plt 
from scipy import stats 

values = np.random.normal(15.0,5.0,5000)
q1 = np.percentile(values,25)
q2 = np.percentile(values,50)
q3 = np.percentile(values,75)
mean = np.mean(values)
median = np.median(values)
plt.figure("Dati senza rumore")
plt.subplot(121)
plt.hist(values,50)
plt.subplot(122)
plt.boxplot(values)

noise = np.random.normal(100.0,5.0,1000)
noisy_values = np.append(values, noise)
mean2 = np.mean(noisy_values)
median2 = np.median(noisy_values)
plt.figure("Dati con rumore")
plt.subplot(121)
plt.hist(noisy_values,50)
plt.subplot(122)
plt.boxplot(noisy_values)
q1R = np.percentile(noisy_values,25)
q2R = np.percentile(noisy_values,50)
q3R = np.percentile(noisy_values,75)

filteredWithoutRumors = []
for t in noisy_values:
    if t >= q1R and t <= q3R:
        filteredWithoutRumors.append(t)
print(filteredWithoutRumors)

ID = q3R - q1R
filteredWithoutRumors2 = []
for t in noisy_values:
    if  q1R - (1,5 * ID) < t < q3R + (1,5 * ID): 
        filteredWithoutRumors2.append(t)
print(filteredWithoutRumors2)

plt.show()