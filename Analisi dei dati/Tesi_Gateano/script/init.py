from matplotlib import pyplot as plt
from function import AnalisiExcel

def main():
    # Inizializza l'analisi
    file_path = 'originale-per-analisi.xlsx'
    analisi = AnalisiExcel(file_path)

    print("\n=== MODALITÀ 2: ANALISI SINGOLE PERSONALIZZATE ===")
    analisi.distribuzione_sesso(tipo_grafico='pie')     # Grafico a torta
    analisi.distribuzione_eta()                         # Grafico a barre
    analisi.distribuzione_fasce_eta(tipo_grafico='pie') # Grafico a torta
    analisi.distribuzione_diagnosi(tipo_grafico='bar')  # Grafico a barre
    analisi.distribuzione_virus(tipo_grafico='pie')     # Grafici a torta per VHB, VHD, VHC
    analisi.combinazioni_virus()                        # Grafico a barre

    

    plt.show() # Mostra tutti i grafici
    

if __name__ == "__main__":
    main()