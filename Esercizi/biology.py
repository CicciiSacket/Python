NumberOrganismsPresent = int(input("Enter the number of present organisms: "))
GrowthRate = 0
HoursPerRate = float(input("Enter the hours needed to reach the growth rate: ")) #ore per raggiungere il tasso di crescita degli organismi
HoursTotal = int(input("Enter the number of total hours: "))

while HoursTotal >= 0:
    HoursTotal -= HoursPerRate 
    GrowthRate+=1
   
NumberOrganismsFinal = (GrowthRate * NumberOrganismsPresent)
print(NumberOrganismsFinal)

