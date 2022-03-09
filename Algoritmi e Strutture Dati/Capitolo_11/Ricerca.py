
#Ricerca del valore minimo ( Funzione min() dello standard python )
from turtle import left, right


def ourMin(List):
    pos_min = 0
    current = 1
    while current < len(List):
        if List[current] < List[pos_min]:
            pos_min = current
        current += 1
    return pos_min


#Ricerca SEQUENZIALE (Funzione contains dello standard list)
def sequentialSearch(target,List):  #-> Data la presenza del return lo studio della complessità di questo algoritmo dipende dal caso (pessimo/ottimo/medio)
    position = 0
    while position < len(list):
        if target == List[position]:
            return position
        position += 1
    return -1 #Torna meno uno quando non trova l'elemento target


#Ricerca BINARIA 
def binarySearch(target,List): #Parte a cercare da metà dimezzando la "complessita", va verso dx o verso sx in caso pessimo va fino alla fine ed eventualmente -1
    left = 0 
    right = len(list) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target == List[midpoint]:
            return midpoint #Target trovato
        elif target < List[midpoint]:
            right = midpoint - 1 #Cerca nella metà di sinistra
        else :
            left = midpoint + 1 #Cerca nella metà di destra
    return -1
