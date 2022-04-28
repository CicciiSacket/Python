from Swap import swap

def partition(lyst,left,right):
    """ Trova il pivot, e sposta alla sua sinistra gli elementi minori e alla sua destra gli elementi maggiori dello stesso pivot; Restituisce la posizione del pivot. """
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    #Pone il confine prima della prima posizione
    boundary = left 
    #Sposta a sinistra gli elementi minori del pivot
    for index in range(left,right):
        if lyst[index] < pivot:
            swap(lyst,index,boundary)
            boundary += 1
    #Scambia il pivot con l'elemento a destra del confine
    swap(lyst,right,boundary)
    return boundary

def quickSortHelper(lyst,left,right):
    """" Partiziona la porzione di lyst compresa tra left e right e poi ordina le sottoliste """
    if left < right:
        pivotLocation = partition(lyst,left,right)
        quickSortHelper(lyst,left, pivotLocation - 1)
        quickSortHelper(lyst, pivotLocation + 1, right)

def QuickSort(lyst):
    """" Ordina list in modo crescente; Divide et impera quindi prestazioni nell'ordine di nLogn """
    quickSortHelper(lyst,0, len(lyst) - 1)

def main():
    A = [5,0,12,43,1,6,99]
    print(A) #Stampa lista non ordinata
    QuickSort(A)
    print(A) #Stampa lista ordinata

if __name__ == "__main__":
    main()



