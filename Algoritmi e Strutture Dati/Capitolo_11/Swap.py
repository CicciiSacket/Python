#Utilizzato come modulo perchè pluripresente
 
def swap(lyst,i,j): 
    """ Scambia gli elementi nelle posizioni i e j"""
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
