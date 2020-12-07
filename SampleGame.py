import random

smaller = int(input('Enter the smaller number: '))
larger = int(input('Enter the larger number: '))
myNumber = random.randint(smaller,larger)
count = 0

while True:
    count+=1
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print('to small!')
    elif userNumber > myNumber:
        print('to large!')
    else:
        print("Congratulation! You've got it in ", count , " tries!")
        break
    