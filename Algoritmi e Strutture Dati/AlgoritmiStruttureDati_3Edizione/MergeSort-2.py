#mergesort con libro di algoritmi, errore nella conversione pseudocdice -> codide...
def merge(A,p,q,r):
    n1 = q - p
    n2 = r - q
    L = list(range(n1))
    R = list(range(n2))
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j]
    i = j = 0
    k = p
    for k in range(len(A)):
        print(len(L),len(R))
        if L[i] <= R[j]:
            print(len(L),len(R))
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def MergeSort(A,p,r):
    if p < r:
        q = int((p + r) // 2)
        MergeSort(A,p,q)
        MergeSort(A,q + 1,r)
        merge(A,p,q,r)

def main():
    A = [5,2,4,7,1,3,8,6]
    MergeSort(A,0,len(A))

if __name__ == "__main__":
    main() 