"""
genera lista A con multipli di 8 da 0 100
genera lista B con multipli di 6 da 0 a 100
usa una funzione marge per concatenare le due liste senza avere doppioni
"""

def generateA ():
    A = []
    for x in range(100):
        if (x%8) == 0:
            A.append(x)
    return A

def generateB ():
    B = []
    for x in range(100):
        if (x%6) == 0:
            B.append(x)
    return B

def marge():
    A = generateA()
    B = generateB()
    C = list(set(A+B))
    return C

