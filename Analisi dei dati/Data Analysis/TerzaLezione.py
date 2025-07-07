#import <nome>
#import <nome> as <alias>
#from <nome> import <nome>
#from <nome> import * [importo tutto e la notazione puntata non mi serve più]
# import <../directory/nome del modulo personalizzato>


"""
INIZIAMO ANALYSIS!!!!!!
statistica descrittiva
"""
# i nostri dati sono mumeri dentro liste
esempio = [12,34,15,17,21]

#parametri descrittivi dei dati: minimo, massimo e RANGE. Altro descrittore può essere l'ampiezza dell'intervallo entro il quale sono dispersi i dati. Altro descrittore ancora è la media dei miei dati. Altro descrittore è la mediana. Altro descrittore è il Quartile(la mediana divide in due parti quindi noi abbiamo il primo quartile e il terzo quartile).

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

def range(dati):
    #restituisce intervallo entro il quale si trovano i dati, ovvero la coppia massimo minimo, ovvero una tupla di valori
    return (minimo(dati),massimo(dati))

def ampiezza(dati):
    #restiuisce la lunghezza dell'intervallo entro il quale sono dispersi i dati
    return massimo(dati) - minimo(dati)

def media(dati):
    return sum(dati) / len(dati)

def mediana(dati):
    d = dati.copy()
    d.sort() #bubblesort abbreviato, per quanto è necessaria questa scombina l'ordine dei dati, si fa quindi unca copia della lista originale per evitare problemi futuri
    #divisione intera e non reale, ovvero il numero approssimato alla cifra intera, n//n
    if len(d) % 2 == 1:
        return d[len(d)//2]
    else:
        return (d[len(d)//2] + d[len(d)//2 - 1]) / 2

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

print(primoQuartile(esempio))
print(terzoQuartile(esempio))
