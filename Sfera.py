#dato in input il raggio di una sfera (virgola mobile), visualizzarne il diametro, il volume, la circonferenza e l'area superficiale
import math

Radius = float(input("Insert radius of ball: "))

Diameter = Radius * 2
Circumference = 2 * math.pi * Radius
Volume = (4/3) * math.pi * pow(Radius,3)
AreaSuperf = 4 * math.pi * pow(Radius,2)

print("diameter: "+ str(Diameter) + "\n"
      "Circumference: "+ str(Circumference) + "\n"
      "Volume: " + str(Volume) + "\n"
      "Area: " + str(AreaSuperf))