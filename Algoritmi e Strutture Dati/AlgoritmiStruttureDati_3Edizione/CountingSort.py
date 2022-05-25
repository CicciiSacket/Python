def counting_sort(A):
    """ 
    A = array di input | C = array ausiliario | B = array ordinato  
    Counting sort determina per ogni elemento di input il numero di elementi minori di esso.
    L'array C contiene il numero di occorrenze degli elementi distinti di A. Ogni elemento dell’array C è incrementato del numero di elementi che lo precedono.
    I numeri con lo stesso valore si presentano nell’array di output nello stesso ordine in cui si trovano nell’array di input. 
    { Il numero che si presenta per primo nell’array di input sarà inserito per primo nell’array di output. }
    """
    k = max(A)
    C = [0 for i in range(0, k+1)]
    B = [0 for j in range(0, len(A))]
    for j in range(0, len(A)): 
        C[A[j]] = C[A[j]] + 1
    for i in range(1, k+1): 
        C[i] = C[i] + C[i-1]
    for j in range(len(A)-1, -1, -1): 
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]] - 1
    return B

def main():
    A = [5,0,12,43,1,6,99]
    print(A) #Stampa lista non ordinata
    A = counting_sort(A)
    print(A) #Stampa lista ordinata

if __name__ == "__main__":
    main()