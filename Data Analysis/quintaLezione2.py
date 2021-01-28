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
 #viene circa 0.5

def mediana(dati):
    d = dati.copy()
    d.sort()
    if len(d) % 2 == 1:
        return d[len(d)//2]
    else:
        return (d[len(d)//2] + d[(len(d)//2) - 1]) / 2
 #torna sempre 0.0

def minimo(dati):
    min(dati)
    #oppure
    temp = dati[0]
    for x in dati:
        if temp > x:
            temp = x
    return temp

def massimo(dati):
    max(dati)
    #oppure
    temp = dati[0]
    for x in dati:
        if temp < x:
            temp = x
    return temp

def primoQuartile(dati):
    primaMeta=[]
    m=mediana(dati)
    for x in dati:
        if x<=m:
            primaMeta.append(x)
    return mediana(primaMeta)

def terzoQuartile(dati):
    secondaMeta=[]
    m=mediana(dati)
    for x in dati:
        if x>m :
            secondaMeta.append(x)
    return mediana(secondaMeta)

def varianza(dati):
    result = 0.0
    med = media(dati)
    eM = len(dati)
    for count in range(eM):
        result += (1/(eM-1)) * ((dati[count] - med) ** 2)
    return result
        
def deviazioneStandard(dati):
    return math.sqrt(varianza(dati))

print(mediana(L))
print(primoQuartile(L))
print(terzoQuartile(L))
