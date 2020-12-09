#fattoriale
i = 4
number = 1
while i > 1:
  number *= i
  i-=1
print(number)

#logaritmo
import math 
N = 8
print(float(math.log(N,2))) #definito con metodi di math

#approssimazione della radice quadrata
import math 

x = float(input("Enter a positive number: "))
tolerance = 0.000001
estimate = 1

while True:
  estimate = (estimate + x / estimate) / 2
  difference = abs(x - estimate ** x)
  if difference <= tolerance:
    break
print("the program estimate: " , estimate)
print("the python's estimate: " , math.sqrt(x))      
      