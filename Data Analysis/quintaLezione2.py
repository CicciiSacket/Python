import math
import random #la funzione .seed(N) viene usata per ottenere la stessa sequenza di numeri casuali più volte


# print(random.random()) #tra zero ed uno, stessa probabilità per tutti gli infiniti numeri
# print(random.randint(1,4)) #intero a "caso" tra gli argomenti

L = [1,2,3,4,5]
# print(random.choice(L)) #sceglie a caso un elemento dell'iterabile che passo come argomento
N = "mario"
# print(random.choice(N)) #sceglie a caso un elemento dell'iterabile che passo come argomento

campione = random.sample(L,2) #torna n numeri tra quelli passati come primo argomento tipo
# print(campione)

#first
S = []
for i in range(1000000): #più grande è il numero più preciso sarà il risultato di tutte queste funzioni 
    S.append(random.random())

def media(dati):
    return sum(dati) / len(dati)
print(media(S)) #viene circa 0.5

def mediana(dati):
    d = dati.copy()
    d.sort()
    if len(d) % 2 == 1:
        return d[len(d)//2]
    else:
        return (d[len(d)//2] + d[len(d)//2 - 1]) // 2
print(mediana(S)) #torna sempre 0.0

def minimo(dati):
    min(dati)
    #oppure
    temp = dati[0]
    for x in dati:
        if temp > x:
            temp = x
    return temp
print(minimo(S))

def massimo(dati):
    max(dati)
    #oppure
    temp = dati[0]
    for x in dati:
        if temp < x:
            temp = x
    return temp
print(massimo(S))

def primoQuartile(dati): 
    firstHalf = []
    m = mediana(dati)
    for x in dati:
        if x <= m:
            firstHalf.append(x)
    return mediana(firstHalf)
print(primoQuartile(S))


def terzoQuartile(dati):
    secondHalf = []
    m = mediana(dati)
    for y in dati:
        if y > m:
            secondHalf.append(y)
        return mediana(secondHalf)
print(terzoQuartile(S))

#inserire varianza e deviazione standard in terza lezione!
