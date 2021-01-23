""" modulo che analizza il gioco dei dai """
from die import Die

class Player(object):
    
    def __init__(self):
        """ coppia dei dadi da lanciare ed una lista vuota """
        self.die1 = Die()
        self.die2 = Die()
        self.rolls = []

    def __str__(self):
        """ stringa con i valori dei lanci """
        result = " "
        for (v1,v2) in self.rolls:
            result += str((v1,v2)) + " " + str(v1, v2)
        return result

    def getNumberRolls(self):
        """ numero dei lanci """
        return len(self.rolls)

    def play(self):
        """ gioca una partita, true vittora-false sconfitta"""
        self.rolls = []
        self.die1.roll()
        self.die2.roll()
        (v1,v2) = (self.die1.getValue(), self.die2.getValue())
        self.rolls.append((v1,v2))

        initialSum = v1 + v2
        if initialSum in (2,3,12):
            return False
        elif initialSum in (7,11):
            return True
        while True:
            self.die1.roll()
            self.die2.roll()  
            (v1,v2) = (self.die1.getValue(), self.die2.getValue())
            self.rolls.append((v1,v2))
            if (v1 + v2) == 7:
                return False
            elif (v1 + v2) == initialSum:
                return True


def playOneGame():
    """ gioca una partia """
    player = Player()
    youWin = player.play()
    print(player)

    if youWin:
        return "WIN!"
    else:
        return "LOSE!"

    
def playManyGame(number):
    """ gioca number partite e ne visualizza le statistiche """
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    player = Player()

    for count in range(number):
        hasWon = player.play()
        rolls = player.getNumberRolls()
        if hasWon:
            wins += 1
            winRolls += rolls
        else:
            losses += 1
            lossRolls += rolls

    print("total win are: " , wins)
    print("total losses are: " , losses)
    print("avarange number of rolls wins is %0.2f" % (winRolls//losses))
    print("winning percentage is %0.3f" %  (winRolls/losses))
    
def main():
    numbers = int(input("Enter the number of games: "))
    playManyGame(numbers)


if __name__ == "__main__":
    main()