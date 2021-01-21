#prendi in input una lista e tramite importazione dell modulo ove sono definite le funzioni per i parametri descrittivi, restiuiscine i risultati. VEDI SCREEN

import TerzaLezione 
print("Inserire sequenza di numeri interi")
prompt = "Enter a number, press -1 to quit.\n"

L = []
x = int(input(prompt))
while x != -1:
    L.append(x)
    x = int(input(prompt))

print(L, ": lista")
print(len(L), ": lunghezza lista")
print(TerzaLezione.range(L), ": range lista")
print(TerzaLezione.media(L), ": valore medio")
print(TerzaLezione.mediana(L), ": valore della mediana")
print(TerzaLezione.primoQuartile(L), ": primo quartile")
print(TerzaLezione.terzoQuartile(L), ": terzo quartile")




