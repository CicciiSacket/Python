from Swap import swap #import della funzione definita in swap 

def SelectionSort(lyst):
    """ Ordina gli elementi in senso crescente; Complessità nell'ordine di NQuadro"""
    i = 0
    while i < len(lyst) - 1: #Esegue n-1 ricerche
        minIndex = i #Indice del minimo
        j = i + 1
        while j < len(lyst): #Inizio della ricerca del valore minimo
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lyst,minIndex,i) 
        i += 1
            
def main():
    A = [5,0,12,43,1,6,99]
    print(A) #Stampa lista non ordinata
    SelectionSort(A)
    print(A) #Stampa lista ordinata

if __name__ == "__main__":
    main()
