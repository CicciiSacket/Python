class SavingAcoount(object):
    """ conto bancario """
    RATE = 0.02 #tasso unico per tutti i conti

    def __init__(self, name, pin,balance = 0.0):
        self.name = name
        self.pin = pin 
        self.balance = balance
    
    def __str__(self):
        return self.name + '\n' + self.pin + '\n' + str(self.balance) + '\n' 

    def getBalance(self):
        return self.balance
    
    def getName(self):
        return self.name
    
    def getPin(self):
        return self.pin

    def deposit(self,amount):
        """ tenta di depositare amount nel conto, restiuendo none se operazione è riuscita """
        if amount < 0:
            return "Amount not found"
        self.balance += amount
        return None
    
    def withdraw(self, amount):
        """ tenta di prelevare amount dal conto, restiuendo none se operazione è riuscita """
        if amount < 0:
            return "Amount not found"
        elif self.balance < amount:
                return "Insufficent founds"
        else: 
            self.balance -= amount
            return None

    def computerInterest(self):
        """ calcola gli interessi e li inserisce nel conto restituendone il valore """
        interest = SavingAcoount.RATE * self.balance
        self.deposit(interest)
        return interest
