"""
genera un dizionario D con 20 elementi dove le chiavi sono numeri interi a caso tra 0 e 100 
    e i valori sono float a caso estratti uniformemente tra 0 e 1. Attento a non duplicare le chiavi!
calcola la somma di tutti i valori in D
trova la chiave del valore minimo in D
"""
from numpy import random

def generate():
    D = {}
    keys = []
    values = []
    summ:float = 0.0
    for y in range(0,21):
        y = random.rand()
        values.append(y)
        x = random.randint(100)
        keys.append(x)    
        D[x] = y
        summ += y
    minValue = min(list(D.keys()))
    return "The sum value of D's values is "+ str(summ)+" min value of D's keys is " +str(minValue)