"""
Consente di gestire il nome di uno studente e il punteggio ottenuto nelle sue prove di verifica
"""

class Student(object):
    def __init__(self,name,number):#number, numero dei punteggi ottenuti
        """ Costruttore """
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)#valore default 0

    def getName(self):
        return self.name
    
    def setScore(self,i,score):
        """ Memorizza score come punteggio della prova, partendo da 1 """
        self.scores[i - 1] = score
    
    def getScore(self, i):
        return self.scores[i - 1]
    
    def getAvarage(self):
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        return max(self.scores)

    def __str__(self):
        return "Name", self.name , "\nScores: ", "".join(map(str,self.scores))

S = Student("Pippo",4)
print(S.getName())
print(S.setScore(2,30))
print(S.getScore(2))
print(S.getAvarage())
print(S.getHighScore())
print(S.__str__())



