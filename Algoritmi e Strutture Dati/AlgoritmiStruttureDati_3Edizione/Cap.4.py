#Problema del massimo sottoarray, acquista e vendi azioni nel momento giusto
def findMaxCrossingSubarray(A,low,mid,high): #Procedura
    sum = 0
    maxLeft = 0
    leftSum = 0
    rightSum = 0
    i = mid
    for i in range(low,0,-1): #Trova il massimo sottoarray nella metà sinistra
        sum = sum + A[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i 
    j = mid + 1
    for j in range(high): #Trova il massimo sottoarray nella metà destra
        sum = sum + A[j]
        if sum > rightSum:
            rightSum = sum
            maxRight = j
    return (maxLeft,maxRight,leftSum + rightSum)

def findMaxSubarray(A,low,high):
    if high == low:
        return (low,high,A[low]) #Caso base: un solo elemento
    else:
        mid = int( (low + high) // 2 )
        (leftLow, leftHigh, leftSum) = findMaxSubarray(A,low,mid)
        (rightLow, rightHigh, rightSum) = findMaxSubarray(A,low,mid)
        (crossLow, crossHigh, crossSum) = findMaxCrossingSubarray(A,low,mid,high)
        if leftSum >= rightSum and leftSum >= crossSum:
            return (leftLow,leftHigh,leftSum)
        elif rightSum > leftSum and rightSum >= crossSum:
            return (rightLow,rightHigh,rightSum)
        else:
            return (crossLow,crossHigh,crossSum)

def main():
    A = [5,0,12,43,1,6,99]
    print(findMaxSubarray(A,0,len(A)))
if __name__ == "__main__":
    main()
