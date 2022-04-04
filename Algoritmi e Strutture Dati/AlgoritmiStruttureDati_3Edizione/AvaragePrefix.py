def prefix_average_1(S): 
    """ La dichiarazione n = len(s) è eseguita con tempo costante. La classe lista mantiene una variabile che memorizza il valore corrente di lunghezza della lista.
        La dichiarazione A = [0] * n causa la creazione ed inizializzazione di una lista di lunghezza 𝑛 con tutti i valori pari a zero. Questo usa un costante numero di operazioni primitive ed esegue in tempo 𝑂(𝑛).
        Il corpo del ciclo esterno, controllato da j è eseguito n volte. Quindi le dichiarazioni total = 0 e A[j] = total / (j+1) sono eseguite 𝑛 volte ognuna. Queste due dichiarazioni controbuiscono per un numero do operazioni primitive proporzionali a 𝑛, cioè un tempo 𝑂(𝑛). 
        Il corpo del ciclo interno, controllato da 𝑖 è eseguito 𝑗 + 1 volte, in dipendenza del valore corrente del ciclo esterno conteggiato come j. Quindi, la dichiarazione total += S[i] è eseguita 1+2+3+⋯+𝑛 = 𝑛(𝑛+1)/2 volte, che implica la dichiarazione contribuisce per 𝑂(𝑛2).
        Il tempo di esecuzione di questa implementazione è dato dalla somma dei termini: O(n), O(n) e O(n2).
        Il tempo di esecuzione è quindi O(n2). """
    n = len(S)  
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j+1):
            total += S[i]
        A[j] = total / (j + 1)
    return A


def prefix_average_2(S):
    """ L’espressione sum(S[0:j+1]) è una chiamata a funzione e richiede un tempo 𝑂(𝑗 + 1) . La computazione dello slice S[0:j+1] anche usa un costo 𝑂(𝑗 + 1).
        Il costo computazionale di questa implementazione è dominato da una serie di step che richiedono un tempo proporzionale a 1 + 2 + 3 + ...+ 𝑛 = 𝑛(𝑛 + 1)/2, e quindi 𝑂(𝑛2)."""
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j + 1) 
    return A


def prefix_average_3(S): 
    """ L’inizializzazione della variabile n e total usa un cost 𝑂(1).
        L’inizializzazione della lista A usa un costo 𝑂(𝑛).
        C’è un loop controllato da 𝑗 che ha un contributo di 𝑂(𝑛).
        Il corpo del loop è eseguito 𝑛 volte,per 𝑗=0,1,...,𝑛−1.Quindi,la
        dichiarazione total += S[j] e A[j] = total / (j+1) sono eseguite 𝑛 volte
        ciascuna. Il loro contributo è 𝑂(𝑛).
        Il tempo di esecuzione di questa implementazione è dato dalla
        somma dei quattro termini: 𝑂(1), 𝑂(𝑛), 𝑂(𝑛), 𝑂(𝑛).
        il tempo di esecuzione è quindi 𝑂(𝑛). """
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total / (j + 1)
    return A