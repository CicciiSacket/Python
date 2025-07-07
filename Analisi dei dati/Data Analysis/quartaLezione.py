#OOP, in python tutto è pubblico per fare tipo un confronto con java; le variabili __name__ sono invece variabili "PRIVATE"

class Animal(object):
    pass #in questa classe non c'è nulla, abbiamo solo creato solamente uno schema, esiste il modello astratto

Leo1 = Animal() #istanziato un nuovo oggetto di tipo animal

class Animale(object):
    #qui possiamo mettere due tipi di variabili, quelle di classe costruite usando la classe; e le variabili di istanza, ciascuna copia di oggetti costruiti ha le sue, definite grazie al costruttore
    vivente = True #variabile di classe 

    def __init__(self, phylum, specie,alimentazione, nome): #self = ci riferiamo all'istanza di oggetto che andremo a costruire; COSTRUTTORE!
        self.phylum = phylum
        self.specie = specie
        self.alimentazione = alimentazione
        self.nome = nome

    def __str__(self): #ridefiniamo il metodo "toStrin"
        return self.phylum + "\t" + self.specie + "\t" + self.alimentazione + "\t" + self.nome

    def cosaMangia(self):
        if (self.alimentazione == "carnivoro" and Animale.vivente): #con self si riferisce alle variabili di istanza con classe. alle variabili di classe
            return "mangia carne"
        else:
            return "non mangia carne"

    def __eq__(self,secondoOggetto):
        return (self.phylum == secondoOggetto.phylum and self.specie == secondoOggetto.specie and self.alimentazione == secondoOggetto.alimentazione and self.nome == secondoOggetto.nome) #questa è buona programmazione restituisce true o false
           

Leo = Animale("mammifero","felino","carnivoro","Kimba")
print(Leo) #out: <__main__.Animale object at 0x7febaba2afa0>, una volta definito il metodo __str__ però questo restituisce ciò che anniamo ridefinito nel "toStgring", stesso output di Leo.__str__()
print(Leo.specie) #out: felino
Leo.nome = "Pippo"
print(Leo.nome) #out: Pippo
print(Leo.__str__())
print(Leo.cosaMangia())

Micio = Animale("mammifero","felino","carnivoro","lillo")

print(Leo == Micio) #out: False, perchè controlla i riferimenti agli indirizzi di memoria

Micio2 = Animale("mammifero","felino","carnivoro","lillo")
print(Micio2 == Micio) #out: False, perchè controlla i riferimenti agli indirizzi di memoria
#comparazione tra oggetti, quando confronto oggetti per default viene chiamato il metodo __eq__, confronta gli indirri di memoria e nom gli attributi dell'oggetto;
#se però ridefinisco il metodo eq posso ottenere un confronto di valori

print(Micio2 == Micio) #dopo la ridefinizione del metodo __eq__ si avranno i return che abbiamo definito nel metodo, e il confronto è per valore


class Person(object):
    def __init__(self,name,annoNascita,genere):
        self.name = name
        self.annoNascita = annoNascita
        self.genere = genere
    
    def __str__(self):
        if (self.genere == "M"):
            return self.name +" "+ self.annoNascita + "è un uomo"
        elif (self.genere == "F"):
            return self.name +" "+ self.annoNascita + "è una donna"
        else:
            return "genere non specificato"
        
    def __eq__(self, secondoOggetto):
        return (self.genere == secondoOggetto.genere and self.name == secondoOggetto.name and self.annoNascita == secondoOggetto.annoNascita)

    def __ge__(self,secondoOggetto): #abbbreviazione di greater of equal, tipo ordinare i miei oggetti, ad esempio ordine alfabetico o anno nascita
        pass

    def menoGiovane(self,secondoOggetto):
        return(self.annoNascita < secondoOggetto.annoNascita)

    def isGirl(self):
        return (self.genere == "F")

    def isBoy(self):
        return (self.genere == "M")