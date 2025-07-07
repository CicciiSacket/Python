"""
Esempio di utilizzo di una funzione main()
"""
def main():
    number = float(input("Enter a number: "))
    result = square(number)
    print("The sqaure of number,",number,"is", result)

def square(x):
    return x *x

#punto di partenza dello script
if __name__ == "__main__":
    main()