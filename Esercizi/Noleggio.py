#un negozio di noleggio mette a 2dollari i vhs e a 3dollari i dvd, creane un gestionale

VHS_PRICE = 2
DVD_PRICE = 3

nRentV = int(input("how many VHS do you rent? "))
nRentD = int(input("how many DVD do you rent? "))

priceDVD = nRentD * DVD_PRICE
priceVHS = nRentV * VHS_PRICE
 
print("you spend for VHS $"+str(priceVHS) + "\t" + "you spend for DVD $"+str(priceDVD))

