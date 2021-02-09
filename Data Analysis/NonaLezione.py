# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
 
import math as mh
import numpy as np
import numpy.random
import matplotlib.pyplot as plt 

%matplotlib qt 

D1 = numpy.random.random(10000)
D2 = numpy.random.randn(10000)

cesto = np.array([1,1,1,1,1,1,0,0,0,0,2,2,2,2])
print(np.histogram(cesto)) #torna una tupla di due array dove nel secondo array ha diviso l'intervallo tra il min e il max in dieci intervalli più piccoli
            #ogni intervallo è uno spazio nel quale sono contenuti i numeri di quell'intervallo, questo spazio prende il nome di BIN, ci sono 10Bin ad esempio
#plt.figure()
#plt.hist(cesto)


plt.figure("Distribuzioni",(1,2))
plt.subplot(1,2,1)
plt.hist(D1,bins=25,density=True, color="blue") #distribuzione uniforme
plt.subplot(1,2,2)
plt.hist(D2,bins=25,density=True, color="magenta") #distribuzione gaussiana

#più bin è alto più si avvicina ad una curva, la curva di densità!

H = plt.hist(D1)
plt.figure()
plt.ylim((0,0.5)) #queste sono le frequenze, tra n1 e n2
plt.plot(H[1][0:10],H[0] / 10000) #x e y devono avere stessa dimensione, infatti del primo solo 10 elementi tanti quanti sono in y
                            #totale degli elementi



















