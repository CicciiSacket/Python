# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
rappresentazione dei dati mediante grafici di matplotlib e numpy
"""
 
import math as mh
import numpy as np
import numpy.random
import matplotlib.pyplot as plt 

x = np.linspace(0,10,21)
x2 = np.arange(0,10,0.5) #equivalente [sono array di numpy entrambi]

y = x * x * x - 4 * x + 2 * x - 10


plt.figure('studio di una funzione polinomiale')
plt.title('Funzione di x di terzo grado')

plt.xlim((-3,13)) #i limiti sono passati da una tupla
plt.ylim((-100,800)) #i limiti sono passati da una tupla

#aggiungiamo le scale valori da visualizare
plt.xticks(np.arange(-3,13,1))
plt.yticks(np.arange(-100,800,50))
plt.grid()
#plt.grid(axis='x') #griglia solamente dall'asse delle x
#plt.grid(axis='y') #griglia solamente dall'asse delle y
#plt.grid(axis = 'x',color = 'red', linewidth=1.5) #personalizzi le linee
#plt.grid(axis = 'y',color = 'red', linewidth=1.5) #personalizzi le linee

#generiamo il grafico
plt.plot(x,y)
plt.xlabel('coord x')
plt.ylabel('f(x)')



plt.figure('Stili di grafo',(2,2))
x = np.linspace(-10,10,100)
plt.subplot(2,2,1)
plt.title('Parabola')
plt.plot(x, x * x)

plt.subplot(2,2,2)
plt.title('Parabola trattegiata')
plt.plot(x, x*x , ".") #linea tratteggiata
plt.text(0,50,"CIAO") #piazza in quelle coordinate il testo che inseriamo come parametro

plt.subplot(2,2,3)
plt.title('Parabola joy')
plt.plot(x, x*x,"ob")
plt.grid(color = (0,0,1))

plt.subplot(2,2,4)
plt.title('Directive joy')
plt.plot(x, x*x, '--g')
plt.grid(color = (0,0,1))



# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
parte due 
"""
 
import math as mh
import numpy as np
import numpy.random
import matplotlib.pyplot as plt 

#distribuzione uniforme e distribuzione gaussiana 

plt.figure('distribuzioni casuali',figsize=(1,2))

plt.subplot(1,2,1)
plt.title('distribuzione uniforme')
x = numpy.random.random(1000)
y = numpy.random.random(1000) #random per la distribuzione uniforme
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.grid()
plt.plot(x,y,'.b')

plt.subplot(1,2,2)
plt.title('distribuzione normale')
x = numpy.random.randn(1000) #randn per la distribuzione normale
y = numpy.random.randn(1000)
#plt.xlim(-5,5)
#plt.ylim(-5,5)
plt.grid()
plt.xticks(np.arange(0,100,10))#la griglia viene quadrata
plt.plot(x,y,'.b')

#%matplotlib qt in finestra nuova



# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
parte tre
"""
 
import math as mh
import numpy as np
import numpy.random
import matplotlib.pyplot as plt 

#creiamo dei dati di esempio e calcoliamo i loro descrittori
D =np.array([12,15,17,1,23,-3,60]) #posso fare riferimento ai metodi della libreria numpy o ai metodi dell'oggetto array
print(D.min())
print(D.max())
print(D.mean()) #media
print(np.median(D)) #mediano
print(np.mean(D))
print(np.max(D))
print(np.min(D))

#calcolo dei quartili, ovvero caso speciale del calcolo dei percentili
print("primo quartile", np.percentile(D,25)) #25 perchè 25% == 1/4
print("mediano", np.percentile(D,50))
print("terzo quartile", np.percentile(D,75)) #75 perchè 3/4
print("varianza", np.var(D))
print("deviazione standard", mh.sqrt(np.var(D)))
print("renge interquartile",(np.percentile(D,75) - np.percentile(D,25))) #terzo quartile - primo quartile
