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

