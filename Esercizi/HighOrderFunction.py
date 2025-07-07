""" 
MAP = costruisce e restituisce una nuova lista nella quale tutti i suoi elementi sono stati mappati seguendo la funzione di ordine superiore
FILTER = una funzione predicato viene applicata a tutti i valori della lista e quelli che passano il controllo vengono filtrati
REDUCE = riceviamo una lista di valori e applichiamo la funzione di ordine superiore per produrre un solo valore "[callback per forza due argomenti]"
"""
def getValue(value):
    """ ritorna la lista value """
    return value
print(list(map(getValue, ['Ho', 'capito','PD'])))#(funzione, elemento a cui applicare la funzione che deve essere iterabile)

def getSum(value):
    """ ritorna la somma dei numeri dentro value"""
    result = 0
    for count in range(len(value)):
        result += value[count]
    return result

print(list(map(getSum,[[2,2,2,1,1]]))) #dato che il ritorno deve essere una lista, se passassi l'argomento con una sola coppia di [], diventerebbe un oggetto non iterabile

def stringa(value):
    for count in range(len(value)):
        if value[count] == 2:
            value[count] = "filtrato"
    return value

def string2(value):
    for count in range(len(value)):
        if value[count] == 'filtrato':
            value[count] = 2
    return value

print(list(filter(stringa,[[2,2,1,1]])))
print(list(filter(string2,(list(filter(stringa,[[2,2,1,1]]))))))#così come per map posso passare un invocazione filter o map ad un'altra invocazione filter o map


from functools import reduce #importazione necessaria in quanto il metodo appartiene ad un modulo 

def add(x,y): #questa funzione di ordine superiore deve NECESSARIAMENTE AVERE DUE ARGOMENTI
    return x + y

print(reduce(add,[1,1,1,1]))

def x(n,m):
    return n * m

print(reduce(x,[1,1,1,1,1,1,0,1]))

""" LAMBDA: funzione anonima che definisce i nomi dei proprio argomenti ed e seguita da un espressione, il tutto su una sola riga  """
from functools import reduce

data = [1,2,3,4]

print(reduce(lambda x,y : x + y, data)) #torna la somma
print(reduce(lambda x,y : x * y, data)) #torna il prodotto

