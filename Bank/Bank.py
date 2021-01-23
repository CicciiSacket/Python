from savingsAccount import SavingAcoount

class Bank(object):
    def __init__(self,fileName = None):
        self.accounts = {}

    def __str__(self):
        """ restituisce una striga con tutti i conti della banca """
        return '\n'.join(map(str, self.accounts.values()))
    
    def makeKey(self, name, pin):
        """ crea una chiave usando nome e pin del conto """ 
        return name + "/" + pin

    def add(self, account):
        """ aggiunge un conto alla banca """
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        """ rimuove un conto dalla banca, torna None se tutto apposto """
        key = self.makeKey(name,pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        """ ritorna conto della banca associato a nome e pin altrimenti torna none """
        Key = self.makeKey(name, pin)
        return self.accounts.get(Key, None)

    def computerInterest(self):
        """ calcola e accredita gli interessi in tutti i conti della banca e ne torna la somma """
        total = 0
        for account in self.accounts.values():
            total += account.computerInterest()
        return total
    

    
