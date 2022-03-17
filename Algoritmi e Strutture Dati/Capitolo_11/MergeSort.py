def merge(lyst,copyBuffer,low,high,middle):
    #lyst -> lista da ordinare
    #copyBuffer -> spazio/lista temporaneo da usare nella fusione 
    #low -> inizio prima sottolista ordinata
    #middle -> fine prima sottolista ordinata
    #middle + 1 -> inizio seconda sottolista ordinata
    #high -> fine seconda sottolista ordinata
    
    #Queste puntano al primo elemento della rispettiva sottolista
    i1 = low 
    i2 = middle + 1 

    #Copia alternativamente gli elementi delle due sottoliste in modo da inserirli dentro copyBuffer in maniera ordinata
    for i in range(low, high + 1):
        if i1 > middle: #La prima sottolista è finita
            copyBuffer[i] = lyst[i2]
            i2 += 1
        elif i2 > high: #La seconda sottolista è finita
            copyBuffer[i] = lyst[i1]
            i1 += 1
        elif lyst[i1] < lyst[i2]: #L'elemento della prima sottolista è minore dell'elemento della seconda sottolista
            copyBuffer[i] = lyst[i1]
            i1 += 1
        else: #L'elemento della seconda sottolista è minore minore
            copyBuffer[i] = lyst[i2]
            i2 += 1
    for i in range(low, high + 1): #Copia gli elementi da copybuffer alla lista nella zona opportuna
        lyst[i] = copyBuffer[i]

def mergeSortHelper(lyst, copyBuffer,low,high):
    #lyst -> lista da ordinare
    #copyBuffer -> spazio/lista temporaneo da usare nella fusione 
    #low, high -> estremi della sottolista
    #middle -> pt centrale della sottolista
    if low < high:
        middle = (low + high) // 2
        mergeSortHelper(lyst,copyBuffer,low,middle)
        mergeSortHelper(lyst,copyBuffer, middle + 1, high) 
        merge(lyst,copyBuffer,low,high,middle)

def MergeSort(lyst):
    copyBuffer = list(lyst)
    mergeSortHelper(lyst,copyBuffer,0, len(lyst) - 1)

def main():
    A = [5,0,12,43,1,6,99]
    print(A) #Stampa lista non ordinata
    MergeSort(A)
    print(A) #Stampa lista ordinata

if __name__ == "__main__":
    main()