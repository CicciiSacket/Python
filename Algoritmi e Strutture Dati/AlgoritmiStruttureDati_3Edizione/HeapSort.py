def parent(i):
    return int(i/2)

def left(i):
    return 2*i

def right(i):
    return (2*i) + 1

def heapify(A, n, i): # n is the heap_size
	massimo = i # Initialize massimo as root
	l = left(i)
	r = right(i)
	if l < n and A[i] < A[l]: # See if left child of root exists and is greater than root
		massimo = l
	if r < n and A[massimo] < A[r]: # See if right child of root exists and is greater than root
		massimo = r
	if massimo != i:	# Change root, if needed
		A[i],A[massimo] = A[massimo],A[i] # swap
		heapify(A, n, massimo) # Heapify the root.

def heapSort(A):
	n = len(A) 
	for i in range(n // 2 - 1, -1, -1): # Since last parent will be at ((n//2)-1) we can start at that location (Build_max_heap).
		heapify(A, n, i)
	for i in range(n-1, 0, -1): # One by one extract elements
		A[i], A[0] = A[0], A[i] # swap
		heapify(A, i, 0)

def main():
    A = [12,22,32,1,3,4,6]
    print(A)
    heapSort(A)
    print(A)

if __name__ == "__main__":
    main() 


