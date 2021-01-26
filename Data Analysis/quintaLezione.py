"""
formattazione della stampa 
"""

nome = 'Giovanni'
print("ciao {}" .format(nome)) #piuttosto che le parentesi graffe stampa "ciao giovanni"

#stampa un saluto a tutte le persone nella lista
L = ['Bina','Gina','Tina','Lina','Pina']
for nome in L:
    print("ciao {}" .format(nome))  


class City(object):
    def __init__(self, name, population, nation = "Italia" ): #valore di default, se non passo la nation si prende come valore italia
        self.name = name
        self.nation = nation
        self.population = population

    def __str__(self):
        return "La citta di {}".format(self.name) + " si trova in {}".format(self.nation) + " ed ha una popolazione di {} abitanti".format(self.population)  
        
    
Catania = City('Catania',1000000)
print(Catania)
Catania2 = City('Catania',1435675,'USA')
print(Catania2)

class CAP(City): #erediatirietà
    """ IMPORTANTE UTILIZZO DI SUPER """
 
    def __init__(self,name,population,regione,nation = "Italia"): #per aggiungere nuove proprietà
        super().__init__(name,population,nation) #SUPER ->prende dalla classe padre, nel caso in cui le classi ereditate sono più di una al super viene sostituito il nome della classe direttamente 
        self.regione = regione #attributo in più per la citta che è capoluogo di una regione
    
    def __str__(self): #overload del metedo str 
        return super().__str__() + " ed è capoluogo della {}".format(self.regione)
        

ME = CAP('MESSINA',1234567,'Sicilia') 
print(ME)
