""" modulo che definisce la classe die """
from random import randint

class Die(object):
    """ questa classe definisce un oggetto dado con 6 facce """
    def __init__(self):
        self.value = 1

    def roll(self):
        """ assegnamo al dado il valore post lancio"""
        self.value = randint(1,6)
    
    def getValue(self):
        """ ritorna il valore post lancio"""
        return self.value
    
    def __str__(self):
        return str(self.getValue())
