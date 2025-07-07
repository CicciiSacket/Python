high = float(input("Enter the height of the throw: "))
bounces = int(input("Enter the number of bounces: "))
rebound_index = 6 / high #6-> altezza di rimbalzo media di una palla lanciata da circa 10m
totalFt = high + (bounces * 6) + rebound_index * 6

print("Total distance traveled by the ball in ft: ",totalFt) 