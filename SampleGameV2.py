import random

smaller = 0
larger = 10
CpuNumber = random.randint(smaller,larger)

userNumber = int(input("Enter your guess from zero to ten: "))
print("choose of pc is ",CpuNumber)
if (CpuNumber == userNumber):
    print("Pc guessed it!")
else:
    print("user win!")