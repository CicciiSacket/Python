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
    for x in range(20):
        x = random.randint(100)
        keys.append(x)
    values = []
    for y in range(20):
        y = random.rand()
        values.append(y)
    for i in keys:
        for n in range(len(values)):
            D[i] = values[n]
    return  D
print(generate())