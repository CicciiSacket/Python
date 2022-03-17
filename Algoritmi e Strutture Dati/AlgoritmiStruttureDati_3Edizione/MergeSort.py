# -- IMPLEMENTAZIONE Libro python e web --
#l'array è diviso in modo ricorsivo in due metà fino a quando la dimensione diventa 1. 
# Una volta che la dimensione diventa 1, i processi di unione entrano in azione e 
# iniziano a unire gli array fino a quando l'array completo non è raggiunto
def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2 #Finding the mid of the array
        L = arr[:mid]
        R = arr[mid:]
        MergeSort(L) # Sorting the first half
        MergeSort(R) # Sorting the second half   -- VEDERE FIGURA 2.4 -- 
        i = j = k = 0 #init for fusion
        while i < len(L) and j < len(R):  # Copia in arrays L[] e R[]
            if L[i] < R[j]:
                arr[k] = L[i] 
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
                            #A questo punto a terminale il lavoro che fa passo passo è:
                                            # [5]
                                            # [2]
                                            # [4]
                                            # [7]
                                            # [2, 5]
                                            # [4, 7]
                                            # [1]
                                            # [3]
                                            # [8]
                                            # [6]
                                            # [1, 3]
                                            # [6, 8]
                                            # [2, 4, 5, 7] L
                                            # [1, 3, 6, 8] R 
        #Fonde le due liste                                   
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
                            #A questo punto a terminale il lavoro che fa passo passo è fondere i k elementi:
                                            # [2, 4, 5, 7] L
                                            # [1, 3, 6, 8] R 
                                            # [1, 2, 3, 4, 5, 6, 7, 8] -> l'array è ora ordinato
        
def main():
    A = [5,2,4,7,1,3,8,6]
    print(A)
    MergeSort(A)
    print(A)

if __name__ == "__main__":
    main() 