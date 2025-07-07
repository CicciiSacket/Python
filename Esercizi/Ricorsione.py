def displayRange(lower,upper): #defininizione di funzione senza usare la ricorsività
    """ visualizza i numeri interi compresi tra lower e upper """
    while lower <= upper:
        print(lower)
        lower += 1 


def displayRangeR(lower,upper): #defininzione della funzione con un richiamo a se stessa e l'utilizzo della selezione, diventa così una funzione ricorsiva
    """ visualizza i numeri interi compresi tra lower e upper """
    if (lower <= upper):
        print(lower)
        displayRangeR(lower + 1, upper)

# print(displayRange(1,6))
# print(displayRangeR(1,6))
#otteremo lo stesso risultato in quanto l'algoritmo è praticamente uguale anche se la definizione delle funzioni risulta essere diversa

def summation(lower,upper,margin):
    blanks = " " * margin
    print(blanks,lower,upper)
    if lower > upper:
        print(blanks,0) 
        return 0
    else:
        result = lower + summation(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result

# print(summation(1,4,0))

def fibonacci(n): #caso più "elementare" per comprendere il concetto di ricorsività
    """ ritorna la sequenza di fibonacci di ordine n """
    if n > 3:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
