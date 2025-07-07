from Swap import swap 

def BubbleSort(lyst):
    """ Ordina in senso crescente gli elementi; Prestazione nell'ordine di NQuadro """
    n = len(lyst)
    while n > 1:
        swapped = False #Booleano per tenere traccia degli scambi, miglioria nel caso ottimo
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                swap(lyst,i, i-1)
                swapped = True #Cambia di valore il booleano quindi significa che vi è stato uno scambio
                i += 1
            if not swapped:
                return #Esce perchè non vi sono stati o non vi sono più scambi
            n -= 1


def main():
    A = [5,0,12,43,1,6,99]
    print(A) #Stampa lista non ordinata
    BubbleSort(A)
    print(A) #Stampa lista ordinata

if __name__ == "__main__":
    main()
