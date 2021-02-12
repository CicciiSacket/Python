"""
recupera dalla rete i dati più recenti circa il numero di abitanti maschi e di abitanti femmine delle 9 provincie siciliane.
costruisci un dizionario che includa le provincie con chiave e valore il numero di abitanti totali in ciascuna provincia
calcola la percentuale di abitanti totali per ciascuna provincia rispetto al totale
produci un diagramma a torta che illustri la distribuzione degli abitanti per provincie
calcola il rapporto num_maschi/num_femmine per provincia. Quale provincia rende minimo questo rapporto?
"""
import numpy as np
import matplotlib.pyplot as plt 


totalPopulation = 5026989
Populations = [
    {
        "AG" : 438276,
        "M" : 213270,
        "F" : 225006
    },
    {
        "CL" : 266427,
        "M" : 129388,
        "F" : 137039
    },
    {
        "CT" : 1109888,
        "M" : 539157,
        "F" : 570731
    },
    {
        "EN" : 166259,
        "M" : 80517,
        "F" : 85742
    },
    {
        "ME" : 631297,
        "M" : 304443,
        "F" : 326854
    },
    {
        "PA" : 1260193,
        "M" : 609705,
        "F" : 650488
    },
    {
        "RG" : 321370,
        "M" : 159282,
        "F" : 162088
    },
    {
        "SR" : 400881,
        "M" : 197558,
        "F" : 203323
    },
    {
        "TP" : 432398,
        "M" : 212023,
        "F" : 220375
    },
]

def AgPercentage():
    return Populations[0]["AG"] / totalPopulation * 100

def ClPercentage():
    return Populations[1]["CL"] / totalPopulation * 100

def CtPercentage():
    return Populations[2]["CT"] / totalPopulation * 100

def EnPercentage():
    return Populations[3]["EN"] / totalPopulation * 100

def MePercentage():
    return Populations[4]["ME"] / totalPopulation * 100

def PaPercentage():
    return Populations[5]["PA"] / totalPopulation * 100

def RgPercentage():
    return Populations[6]["RG"] / totalPopulation * 100

def SrPercentage():
    return Populations[7]["SR"] / totalPopulation * 100

def TpPercentage():
    return Populations[8]["TP"] / totalPopulation * 100

def rapportMF():
    Rapport = []
    for n in range(len(Populations)):
        rpfm = str(Populations[n]["M"] / Populations[n]["F"] ) +"\t"+str(Populations[n])
        Rapport.append(rpfm)
    minimo = str(min(Rapport))
    return minimo


x = np.array([AgPercentage(),ClPercentage(),CtPercentage(),EnPercentage(),MePercentage(),PaPercentage(),RgPercentage(),SrPercentage(),TpPercentage()])
label = ["AG", "CL", "CT", "EN","ME","PA","RG","SR","TP"]
plt.pie(x, labels=label)
plt.show()




