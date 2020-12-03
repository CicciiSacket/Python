#calcola le tasse sul reddito di una persona fisica CASO DI STUDIO UNO

#importi il modulo math di python, anche se la funzione round è disponibile in quanto appartiene al modulo __builtin__;
import math

#inizializzazione delle costanti [maiuscolo proprio perchè costanti] 
TAX_RATE = 0.20
STD_REDUCE = 10000.0
DEP_REDUCT = 3000.0

#acquisizione dei dati in input
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

#calcolo della tassa
taxableIncome = grossIncome - STD_REDUCE - DEP_REDUCT * numDependents
incomeTax = round(taxableIncome * TAX_RATE,2) #round->funzione che arrotanda il primo argomento al numero di cifre rappresentato dal secondo argomento

#visualizzazione della tassa calcolata 
print("The income tax is\n" + str(incomeTax) + "$") 
