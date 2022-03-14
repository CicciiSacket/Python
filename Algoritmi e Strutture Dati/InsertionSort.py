#L'ordinamento viene fatto all'interno dell'array
def InsertionSort(A): #Progettazione incrementale
    for index in range(len(A)):
        current = A[index] #Primo elemento della lisata
        i = index - 1 #Variabile i, ovvero elemento precedente a quello corrente
        while i >= 0 and A[i] > current: #Cicla finchè vi sono elementi che in posizione i sono maggiori dell'elemento corrente
            A[i + 1] = A[i] #L'elemento più grande del corrente viene spostato di uno verso destra
            i -= 1 #Decremento di i per studiare l'elemento precedente
        A[i + 1] = current  #Si assegna alla posizione corretta l'elemento corrente

def main():
    A = [5,0,12,43,1,6,99]
    print(A) #Stampa lista non ordinata
    InsertionSort(A)
    print(A) #Stampa lista ordinata

    B = [43,1,6,99]
    B.sort() #Metodo di ordinamento con funzione di libreria, si può usare una callback all'interno delle parentesi
    print(B)

if __name__ == "__main__":
    main()
