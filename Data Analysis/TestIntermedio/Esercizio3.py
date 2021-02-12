"""
scrivi una classe Python per descrivere l'oggetto “Punto” definito dalle coordinate cartesiane (x,y), x e y sono dei float. 
    Il “Punto” abbia:
        – metodo __init__
        – metodo piuDistante(Q,d) che restituisce True se Q ha distanza da P maggiore di d, False altrimenti
usando la classe “punto” scrivi un programma che generi 10 punti a caso con coordinate tra 0 e 1 
    e calcola quanti di essi distano più di 0.5 dall'origine (0,0).
"""
from numpy import random
class Point(object):
    def __init__(self,x,y):
        self.x:float = x
        self.y:float = y

    def moreDistance(self,Qx,Qy,dx,dy):
        return False if (Qy < dy and Qx < dx) else True 

    def __to_string__(self):
        return str(self.x)+"\t"+str(self.y)     

def miniProgram():
    for n in range(0,10):
        x = random.rand()
        y = random.rand()
        n = Point(x,y)
        # print(n.__to_string__())
        if n.y > 0.5 and n.x > 0.5 and n.y > 0 and n.x > 0:
            return (str(n.y)+"\t"+str(n.x))

