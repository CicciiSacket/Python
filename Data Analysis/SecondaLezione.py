#le variabili costano.. anche di appoggio
a = 2
b = 3
c = 1

if (a >= b and a >= c):
    print(a)
elif (b >= c):
    print(b)
else:
    print(c)


#creare una variabile lista che contenga du stringhe, se il numero di caratteri del nome è >= al cognome stampare name else stampare surname
test = ['Francesco','Sacco']
if (len(test[0]) >= len(test[1])):
    print(test[0])
else: 
    print(test[1])

#ciclare, ciclo FOR!!
A = [1,2,3]
for indice in range(len(A)):
    A[indice]*=2
print(A)

B = range(5) #creo appunto un range entro il quale il ciclo itererà
for x in B:
    print(x)

X = ["mario","pippo","pluto"]
for parola in X:
    print(parola.capitalize())#mette in maiuscolo la prima lettera di ogni parola


#ciclare, ciclo WHILE!!!
M = [1,2,3,4]
indice = 0 
while indice < len(M):
    print(M[indice])
    indice+=1 #aggiornamento della condizione

#funzioni produttive e non produttive --- def name(parameter): ---                                   