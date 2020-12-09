#pag.104 n.1
x = float(input("insert a side of triangle: "))
y = float(input("insert a side of triangle: "))
z = float(input("insert a side of triangle: "))

if x == y and y == z:
    print("Equilater triangle!")
else:
    print("Triangle isn't equilater")

#pag.105 n.2
import math
x = float(input("insert a side of triangle: "))
y = float(input("insert a side of triangle: "))
z = float(input("insert a side of triangle: "))

if(x == math.sqrt(y*y + z*z) or y == math.sqrt(x*x + z*z) or z == math.sqrt(x*x + y*y)):
    print('Triangle rectangle')
else:
    print("Triangle isn't rectangle")
