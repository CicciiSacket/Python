import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class AnalisiExcel:
    def __init__(self, file_path):
        """Inizializza l'analisi caricando il file Excel"""
        self.file_path = file_path
        self.df = None
        self.carica_dati()
    
    def carica_dati(self):
        """Carica i dati dal file Excel"""
        try:
            self.df = pd.read_excel(self.file_path)
            print(f"Dataset caricato: {len(self.df)} righe, {len(self.df.columns)} colonne")
            # print("\nColonne disponibili:")
            # print(self.df.columns.tolist())
        except Exception as e:
            print(f"Errore nel caricamento del file: {e}")
    
    def distribuzione_sesso(self, tipo_grafico='bar'):
        """1. Distribuzione per sesso (colonna 'f')"""
        plt.figure(figsize=(8, 6))
        counts = self.df['Rsex'].value_counts()
        
        if tipo_grafico == 'pie':
            # Grafico a torta
            labels = ['Femminile', 'Maschile']
            colors = ['pink', 'lightblue']
            counts.plot(kind='pie', labels=labels, colors=colors, autopct='%1.1f%%',
                       title='Distribuzione per sesso')
            plt.ylabel('')  # Rimuove l'etichetta y per i grafici a torta
        else:
            # Grafico a barre (default)
            counts.plot(kind='bar', title='Distribuzione per sesso (0=F, 1=M)', 
                       color=['pink', 'blue'])
            plt.xticks([0, 1], ['Femminile', 'Maschile'], rotation=0)
            plt.xlabel('Sesso')
            plt.ylabel('Frequenza')
        
        plt.tight_layout()
        
        # Stampa statistiche
        print(f"\nDistribuzione per sesso:")
        print(f"Femminile: {counts.get(0, 0)} ({counts.get(0, 0)/len(self.df)*100:.1f}%)")
        print(f"Maschile: {counts.get(1, 0)} ({counts.get(1, 0)/len(self.df)*100:.1f}%)")
    
    def distribuzione_eta(self):
        """2. Distribuzione in base all'età (colonna 'e')"""
        plt.figure(figsize=(10, 6))
        eta_data = self.df['Rvarsta'].dropna()
        eta_data.plot(kind='hist', bins=15, title='Distribuzione Età', alpha=0.7)
        plt.xlabel('Età')
        plt.ylabel('Frequenza')
        plt.tight_layout()
        
        # Statistiche descrittive
        print(f"\nStatistiche età:")
        print(f"Min: {eta_data.min()}, Max: {eta_data.max()}")
        print(f"Media: {eta_data.mean():.1f}, Mediana: {eta_data.median():.1f}")
        print(f"Deviazione standard: {eta_data.std():.1f}")
    
    def distribuzione_fasce_eta(self, tipo_grafico='bar'):
        """3. Distribuzione per categorie d'età"""
        plt.figure(figsize=(10, 6))
        bins = [0, 18, 30, 45, 60, 75, 100]
        labels = ['0-18', '19-30', '31-45', '46-60', '61-75', '76+']
        
        self.df['fascia_eta'] = pd.cut(self.df['Rvarsta'], bins=bins, labels=labels, right=False)
        counts = self.df['fascia_eta'].value_counts().sort_index()
        
        if tipo_grafico == 'pie':
            # Grafico a torta
            counts.plot(kind='pie', autopct='%1.1f%%', title='Distribuzione per fascia d\'età')
            plt.ylabel('')  # Rimuove l'etichetta y per i grafici a torta
        else:
            # Grafico a barre (default)
            counts.plot(kind='bar', title='Distribuzione per fascia d\'età')
            plt.xlabel('Fascia d\'età')
            plt.ylabel('Frequenza')
            plt.xticks(rotation=45)
        
        plt.tight_layout()
        
        print(f"\nDistribuzione per fascia d'età:")
        for fascia, count in counts.items():
            print(f"{fascia}: {count} ({count/len(self.df)*100:.1f}%)")
    
    def distribuzione_diagnosi(self, tipo_grafico='bar'):
        """4. Distribuzione per diagnosi (colonna 't')"""
        plt.figure(figsize=(12, 6))
        counts = self.df['Diagnostic'].value_counts()
        
        if tipo_grafico == 'pie':
            counts_to_plot = counts.head(8)
            altri = counts.iloc[8:].sum()
            if altri > 0:
                counts_to_plot['Altri'] = altri
            counts_to_plot.plot(
                kind='pie',
                autopct='%1.1f%%',
                title='Distribuzione Diagnosi (Top categorie)',
                labeldistance=1.1,
                startangle=90,
                pctdistance=0.8,
                textprops={'fontsize': 8}
            )
            plt.ylabel('')
        else:
            # Grafico a barre (default)
            counts.plot(kind='bar', title='Distribuzione Diagnosi', align='center')
            plt.xlabel('Diagnosi')
            plt.ylabel('Frequenza')
            plt.xticks(ticks=range(len(counts)), labels=counts.index, rotation=90, ha='center', fontsize=8)

        plt.tight_layout()
        
        print(f"\nDistribuzione diagnosi:")
        for diagnosi, count in counts.items():
            print(f"Diagnosi {diagnosi}: {count} ({count/len(self.df)*100:.1f}%)")
    
    def distribuzione_virus(self, tipo_grafico='bar'):
        """5-7. Distribuzioni per virus vhb, vhd, vhc (colonne af, ag, ah)"""
        virus_info = [('VHB', 'VHB'), ('VHD', 'VHD'), ('VHC', 'VHC')]
        
        label_map = {0.0: 'Negativo', 1.0: 'Positivo'}
        
        if tipo_grafico == 'pie':
            fig, axes = plt.subplots(1, 3, figsize=(15, 5))
            
            for i, (virus, col) in enumerate(virus_info):
                if col in self.df.columns:
                    data = self.df[col].fillna(0).astype(float).map(label_map)
                    counts = data.value_counts()
                    counts.plot(kind='pie', ax=axes[i], autopct='%1.1f%%', title=f'Distribuzione {virus}')
                    axes[i].set_ylabel('')
                    
                    print(f"\nDistribuzione {virus}:")
                    for status, count in counts.items():
                        print(f"  {status}: {count} ({count/len(self.df)*100:.1f}%)")
        else:
            fig, axes = plt.subplots(1, 3, figsize=(15, 5))
            for i, (virus, col) in enumerate(virus_info):
                if col in self.df.columns:
                    data = self.df[col].fillna(0).astype(float).map(label_map)
                    counts = data.value_counts()
                    counts.plot(kind='bar', ax=axes[i], title=f'Distribuzione {virus}', color='royalblue')
                    axes[i].set_xlabel(f'{virus} Status')
                    axes[i].set_ylabel('Frequenza')
                    
                    print(f"\nDistribuzione {virus}:")
                    for status, count in counts.items():
                        print(f"  {status}: {count} ({count/len(self.df)*100:.1f}%)")
        
        plt.tight_layout()

    def combinazioni_virus(self):
        """8. Incrocio virus - solo pazienti con almeno 2 virus positivi"""
        plt.figure(figsize=(12, 6))

        virus_cols = ['VHB', 'VHD', 'VHC']
        virus_combo = self.df[virus_cols].fillna(0).astype(float)

        # Filtra: solo pazienti con almeno 2 virus positivi
        virus_combo = virus_combo[virus_combo.sum(axis=1) >= 2]

        # Crea etichetta leggibile
        def combo_label(row):
            return ' + '.join([virus for virus, val in zip(virus_cols, row) if val == 1.0])

        virus_combo['combo'] = virus_combo.apply(combo_label, axis=1)

        # Conta combinazioni
        counts = virus_combo['combo'].value_counts()

        # Grafico
        counts.plot(kind='bar', title='Combinazioni Multiple Virus (>= 2 positivi)', color='crimson')
        plt.xlabel('Combinazione Virus')
        plt.ylabel('Frequenza')
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Stampa dettagli
        print(f"\nCombinazioni multiple virus (almeno due positivi):")
        for combo, count in counts.items():
            print(f"  {combo}: {count} ({count/len(self.df)*100:.1f}%)")
    
    def distribuzione_alcol(self):
        """9. Distribuzione per alcol"""
        alcol_col = ['alcool']
        
        if alcol_col:
            plt.figure(figsize=(8, 6))
            col_name = alcol_col[0]
            counts = self.df[col_name].value_counts()
            counts.plot(kind='bar', title=f'Distribuzione per consumo di alcol ({col_name})')
            plt.xlabel('Consumo alcol')
            plt.ylabel('Frequenza')
            plt.tight_layout()
            
            print(f"\nDistribuzione alcol ({col_name}):")
            for status, count in counts.items():
                print(f"  {status}: {count} ({count/len(self.df)*100:.1f}%)")
        else:
            # Crea un grafico vuoto con messaggio informativo
            plt.figure(figsize=(8, 6))
            plt.text(0.5, 0.5, 'Colonna alcol non trovata nel dataset', 
                    ha='center', va='center', fontsize=14, 
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
            plt.title('Distribuzione per consumo di alcol')
            plt.axis('off')
            plt.tight_layout()
            print("Colonna alcol non trovata")
    
    def distribuzione_operazioni(self):
        """10. Distribuzione operazioni (colonna be)"""
        if 'be' in self.df.columns:
            plt.figure(figsize=(10, 6))
            counts = self.df['be'].value_counts().sort_index()
            counts.plot(kind='bar', title='Distribuzione Operazioni (colonna be)')
            plt.xlabel('Tipo operazione')
            plt.ylabel('Frequenza')
            plt.tight_layout()
            
            print(f"\nDistribuzione operazioni:")
            for op, count in counts.items():
                print(f"  Operazione {op}: {count} ({count/len(self.df)*100:.1f}%)")
        else:
            # Crea un grafico vuoto con messaggio informativo
            plt.figure(figsize=(8, 6))
            plt.text(0.5, 0.5, 'Colonna "be" non trovata nel dataset', 
                    ha='center', va='center', fontsize=14, 
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
            plt.title('Distribuzione Operazioni (colonna be)')
            plt.axis('off')
            plt.tight_layout()
            print("Colonna 'be' non trovata")
    
    def analisi_colonne_bg_bh(self):
        """11-12. Colonne bg e bh"""
        for col in ['bg', 'bh']:
            if col in self.df.columns:
                plt.figure(figsize=(8, 6))
                counts = self.df[col].value_counts()
                presenti = self.df[col].notna().sum()
                
                counts.plot(kind='bar', title=f'Distribuzione {col} (presenti: {presenti} su {len(self.df)})')
                plt.xlabel(f'Valori {col}')
                plt.ylabel('Frequenza')
                plt.tight_layout()
                
                print(f"\nDistribuzione {col}:")
                print(f"  Valori presenti: {presenti} su {len(self.df)} ({presenti/len(self.df)*100:.1f}%)")
                for val, count in counts.items():
                    print(f"  {val}: {count}")
    
    def media_perdite_sanguigne(self):
        """13. Media perdite sanguigne (colonna dd)"""
        if 'dd' in self.df.columns:
            dd_data = self.df['dd'].dropna()
            if len(dd_data) > 0:
                plt.figure(figsize=(10, 6))
                dd_data.plot(kind='hist', bins=15, title='Distribuzione Perdite Sanguigne (DD)', alpha=0.7)
                plt.xlabel('Perdite sanguigne')
                plt.ylabel('Frequenza')
                plt.tight_layout()
                
                print(f"\nStatistiche perdite sanguigne (DD):")
                print(f"  Media: {dd_data.mean():.2f}")
                print(f"  Mediana: {dd_data.median():.2f}")
                print(f"  Min: {dd_data.min():.2f}, Max: {dd_data.max():.2f}")
                print(f"  Valori disponibili: {len(dd_data)} su {len(self.df)}")
            else:
                # Crea un grafico vuoto con messaggio informativo
                plt.figure(figsize=(8, 6))
                plt.text(0.5, 0.5, 'Nessun dato disponibile per le perdite sanguigne', 
                        ha='center', va='center', fontsize=14, 
                        bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
                plt.title('Distribuzione Perdite Sanguigne (DD)')
                plt.axis('off')
                plt.tight_layout()
                print("Nessun dato disponibile per le perdite sanguigne")
        else:
            # Crea un grafico vuoto con messaggio informativo
            plt.figure(figsize=(8, 6))
            plt.text(0.5, 0.5, 'Colonna "dd" non trovata nel dataset', 
                    ha='center', va='center', fontsize=14, 
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
            plt.title('Distribuzione Perdite Sanguigne (DD)')
            plt.axis('off')
            plt.tight_layout()
            print("Colonna 'dd' non trovata")
    
    def eta_per_sesso(self):
        """14. Età per sesso"""
        plt.figure(figsize=(10, 6))
        self.df.boxplot(column='e', by='f', ax=plt.gca())
        plt.title("Distribuzione età per sesso")
        plt.suptitle('')
        plt.xlabel('Sesso (0=F, 1=M)')
        plt.ylabel('Età')
        plt.xticks([1, 2], ['Femminile', 'Maschile'])
        plt.tight_layout()
        
        # Statistiche per sesso
        print(f"\nStatistiche età per sesso:")
        for sesso in self.df['f'].unique():
            eta_sesso = self.df[self.df['f'] == sesso]['e'].dropna()
            nome_sesso = 'Femminile' if sesso == 0 else 'Maschile'
            print(f"  {nome_sesso}: Media {eta_sesso.mean():.1f}, Mediana {eta_sesso.median():.1f}")
    
    def diagnosi_per_sesso(self):
        """15. Diagnosi per sesso"""
        plt.figure(figsize=(12, 6))
        crosstab = pd.crosstab(self.df['t'], self.df['f'])
        crosstab.plot(kind='bar', stacked=True, title='Diagnosi per sesso')
        plt.xlabel('Diagnosi')
        plt.ylabel('Frequenza')
        plt.legend(['Femminile', 'Maschile'])
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        print(f"\nDiagnosi per sesso:")
        print(crosstab)
    
    def virus_per_sesso(self):
        """16. Virus per sesso"""
        virus_info = [('VHB', 'af'), ('VHD', 'ag'), ('VHC', 'ah')]
        
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        for i, (virus, col) in enumerate(virus_info):
            if col in self.df.columns:
                crosstab = pd.crosstab(self.df[col], self.df['f'])
                crosstab.plot(kind='bar', stacked=True, ax=axes[i], title=f'{virus} per sesso')
                axes[i].set_xlabel(f'{virus} Status')
                axes[i].set_ylabel('Frequenza')
                axes[i].legend(['Femminile', 'Maschile'])
                
                print(f"\n{virus} per sesso:")
                print(crosstab)
        
        plt.tight_layout()
    
    def distribuzione_mortalita(self, tipo_grafico='bar'):
        """17. Distribuzione per colonna bn (0 vivo, 1 morto)"""
        if 'bn' in self.df.columns:
            plt.figure(figsize=(8, 6))
            counts = self.df['bn'].value_counts()
            
            if tipo_grafico == 'pie':
                # Grafico a torta
                labels = ['Vivo', 'Morto']
                colors = ['green', 'red']
                counts.plot(kind='pie', labels=labels, colors=colors, autopct='%1.1f%%',
                           title='Distribuzione Vivo/Morto (BN)')
                plt.ylabel('')  # Rimuove l'etichetta y per i grafici a torta
            else:
                # Grafico a barre (default)
                counts.plot(kind='bar', title='Distribuzione Vivo/Morto (BN)', color=['green', 'red'])
                plt.xticks([0, 1], ['Vivo', 'Morto'], rotation=0)
                plt.xlabel('Status')
                plt.ylabel('Frequenza')
            
            plt.tight_layout()
            
            print(f"\nDistribuzione mortalità:")
            print(f"  Vivi: {counts.get(0, 0)} ({counts.get(0, 0)/len(self.df)*100:.1f}%)")
            print(f"  Morti: {counts.get(1, 0)} ({counts.get(1, 0)/len(self.df)*100:.1f}%)")
        else:
            # Crea un grafico vuoto con messaggio informativo
            plt.figure(figsize=(8, 6))
            plt.text(0.5, 0.5, 'Colonna "bn" non trovata nel dataset', 
                    ha='center', va='center', fontsize=14, 
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
            plt.title('Distribuzione Vivo/Morto (BN)')
            plt.axis('off')
            plt.tight_layout()
            print("Colonna 'bn' non trovata")
    
    def sopravvivenza_trapianto(self):
        """18. Sopravvivenza dopo trapianto (bp, bq, br)"""
        colonne_sopravvivenza = ['bp', 'bq', 'br']
        colonne_presenti = [col for col in colonne_sopravvivenza if col in self.df.columns]
        
        if colonne_presenti:
            fig, axes = plt.subplots(1, len(colonne_presenti), figsize=(5*len(colonne_presenti), 5))
            if len(colonne_presenti) == 1:
                axes = [axes]
            
            for i, col in enumerate(colonne_presenti):
                data = self.df[col].dropna()
                if len(data) > 0:
                    data.plot(kind='hist', bins=15, ax=axes[i], 
                             title=f'Sopravvivenza (mesi) - {col}', alpha=0.7)
                    axes[i].set_xlabel('Mesi')
                    axes[i].set_ylabel('Frequenza')
                    
                    print(f"\nStatistiche sopravvivenza {col}:")
                    print(f"  Media: {data.mean():.1f} mesi")
                    print(f"  Mediana: {data.median():.1f} mesi")
                    print(f"  Min: {data.min():.1f}, Max: {data.max():.1f}")
                    print(f"  Valori disponibili: {len(data)} su {len(self.df)}")
                else:
                    axes[i].text(0.5, 0.5, f'Nessun dato per {col}', 
                               ha='center', va='center', transform=axes[i].transAxes,
                               bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
                    axes[i].set_title(f'Sopravvivenza (mesi) - {col}')
                    axes[i].axis('off')
            
            plt.tight_layout()
        else:
            # Crea un grafico vuoto con messaggio informativo
            plt.figure(figsize=(8, 6))
            plt.text(0.5, 0.5, 'Nessuna colonna di sopravvivenza trovata\n(bp, bq, br)', 
                    ha='center', va='center', fontsize=14, 
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
            plt.title('Sopravvivenza dopo trapianto')
            plt.axis('off')
            plt.tight_layout()
            print("Nessuna colonna di sopravvivenza trovata")
    
    def esegui_analisi_completa(self, mostra_grafici=True, configurazione_grafici=None):
        """Esegue tutte le analisi con configurazione personalizzata dei grafici"""
        print("=== ANALISI COMPLETA DEL DATASET ===")
        
        # Configurazione di default (tutte le funzioni con grafici a barre)
        default_config = {
            'distribuzione_sesso': 'bar',
            'distribuzione_fasce_eta': 'bar',
            'distribuzione_diagnosi': 'bar',
            'distribuzione_virus': 'bar',
            'distribuzione_mortalita': 'bar'
        }
        
        # Usa la configurazione personalizzata se fornita, altrimenti usa quella di default
        config = configurazione_grafici if configurazione_grafici else default_config
        
        analisi_funzioni = [
            ("Distribuzione per sesso", lambda: self.distribuzione_sesso(config.get('distribuzione_sesso', 'bar'))),
            ("Distribuzione età", self.distribuzione_eta),
            ("Distribuzione fasce età", lambda: self.distribuzione_fasce_eta(config.get('distribuzione_fasce_eta', 'bar'))),
            ("Distribuzione diagnosi", lambda: self.distribuzione_diagnosi(config.get('distribuzione_diagnosi', 'bar'))),
            ("Distribuzione virus", lambda: self.distribuzione_virus(config.get('distribuzione_virus', 'bar'))),
            ("Combinazioni virus", self.combinazioni_virus),
            ("Distribuzione alcol", self.distribuzione_alcol),
            ("Distribuzione operazioni", self.distribuzione_operazioni),
            ("Analisi colonne BG/BH", self.analisi_colonne_bg_bh),
            ("Perdite sanguigne", self.media_perdite_sanguigne),
            ("Età per sesso", self.eta_per_sesso),
            ("Diagnosi per sesso", self.diagnosi_per_sesso),
            ("Virus per sesso", self.virus_per_sesso),
            ("Distribuzione mortalità", lambda: self.distribuzione_mortalita(config.get('distribuzione_mortalita', 'bar'))),
            ("Sopravvivenza trapianto", self.sopravvivenza_trapianto)
        ]
        
        for nome, funzione in analisi_funzioni:
            print(f"\n{'='*50}")
            print(f"ANALISI: {nome}")
            print(f"{'='*50}")
            try:
                funzione()
                if mostra_grafici:
                    plt.show()  # Mostra il grafico immediatamente dopo ogni analisi
            except Exception as e:
                print(f"Errore nell'analisi {nome}: {e}")
    
    def salva_tutti_grafici(self, cartella_output="grafici_analisi"):
        """Salva tutti i grafici in una cartella"""
        import os
        
        # Crea la cartella se non esiste
        if not os.path.exists(cartella_output):
            os.makedirs(cartella_output)
        
        plt.ioff()  # Disabilita la visualizzazione interattiva
        
        analisi_funzioni = [
            ("01_distribuzione_sesso", self.distribuzione_sesso),
            ("02_distribuzione_eta", self.distribuzione_eta),
            ("03_fasce_eta", self.distribuzione_fasce_eta),
            ("04_distribuzione_diagnosi", self.distribuzione_diagnosi),
            ("05_distribuzione_virus", self.distribuzione_virus),
            ("06_combinazioni_virus", self.combinazioni_virus),
            ("07_distribuzione_alcol", self.distribuzione_alcol),
            ("08_distribuzione_operazioni", self.distribuzione_operazioni),
            ("09_analisi_bg_bh", self.analisi_colonne_bg_bh),
            ("10_perdite_sanguigne", self.media_perdite_sanguigne),
            ("11_eta_per_sesso", self.eta_per_sesso),
            ("12_diagnosi_per_sesso", self.diagnosi_per_sesso),
            ("13_virus_per_sesso", self.virus_per_sesso),
            ("14_distribuzione_mortalita", self.distribuzione_mortalita),
            ("15_sopravvivenza_trapianto", self.sopravvivenza_trapianto)
        ]
        
        for nome_file, funzione in analisi_funzioni:
            print(f"Generando grafico: {nome_file}")
            try:
                funzione()
                # Salva tutti i grafici aperti
                for i in plt.get_fignums():
                    plt.figure(i)
                    plt.savefig(f"{cartella_output}/{nome_file}_fig{i}.png", 
                              dpi=300, bbox_inches='tight')
                plt.close('all')  # Chiudi tutti i grafici
            except Exception as e:
                print(f"Errore nel salvataggio {nome_file}: {e}")
        
        plt.ion()  # Riabilita la visualizzazione interattiva
        print(f"Grafici salvati nella cartella: {cartella_output}")