#!/usr/bin/env python3
"""
Script per convertire colonne con date in formati diversi in un file Excel
e standardizzarle in formato datetime per analisi con Python.

Autore: Script generato per sistemare date Excel
Data: 2025
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os
import warnings
warnings.filterwarnings('ignore')

def analyze_date_columns(df, potential_date_columns=None):
    """
    Analizza le colonne del DataFrame per identificare quelle che potrebbero contenere date
    """
    print("=== ANALISI COLONNE DATE ===")
    
    if potential_date_columns is None:
        # Cerca automaticamente colonne che potrebbero contenere date
        potential_date_columns = []
        for col in df.columns:
            # Controlla se il nome della colonna suggerisce una data
            col_lower = col.lower()
            date_keywords = ['data', 'date', 'nastere', 'followup', 'DateTx']
            
            if any(keyword in col_lower for keyword in date_keywords):
                potential_date_columns.append(col)
            
            # Controlla anche il contenuto per identificare possibili date
            elif df[col].dtype == 'object':
                sample_values = df[col].dropna().astype(str).head(10)
                date_like_count = 0
                for value in sample_values:
                    # Controlla se il valore sembra una data
                    if any(char in value for char in ['/', '-', '.']) and len(value) >= 6:
                        try:
                            pd.to_datetime(value, dayfirst=True)
                            date_like_count += 1
                        except:
                            pass
                
                if date_like_count >= len(sample_values) * 0.7:  # 70% dei valori sembrano date
                    potential_date_columns.append(col)
    
    print(f"Colonne identificate come possibili date: {potential_date_columns}")
    
    # Analizza ogni colonna
    for col in potential_date_columns:
        if col in df.columns:
            print(f"\n--- Analisi colonna: {col} ---")
            print(f"Tipo attuale: {df[col].dtype}")
            print(f"Valori totali: {len(df[col])}")
            print(f"Valori non nulli: {df[col].notna().sum()}")
            print(f"Valori nulli: {df[col].isna().sum()}")
            
            # Mostra esempi di valori
            sample_values = df[col].dropna().head(10)
            print("Esempi di valori:")
            for i, value in enumerate(sample_values, 1):
                print(f"  {i}. {value} (tipo: {type(value).__name__})")
            
            # Mostra valori unici (primi 10)
            unique_values = df[col].dropna().unique()[:10]
            print(f"Valori unici (primi 10): {list(unique_values)}")
    
    return potential_date_columns

def convert_mixed_dates(series, column_name=""):
    """
    Converte una serie con date in formati misti a datetime uniforme
    """
    print(f"\nConvertendo colonna: {column_name}")
    
    if series.empty:
        return series
    
    # Prima mostra alcuni esempi di valori originali
    print("  Esempi di valori originali:")
    sample_values = series.dropna().head(5)
    for i, val in enumerate(sample_values, 1):
        print(f"    {i}. '{val}' (tipo: {type(val).__name__})")
    
    # Lista di formati comuni da provare in ordine di priorità
    formats_to_try = [
        '%d/%m/%Y',     # 31/12/2023
        '%d-%m-%Y',     # 31-12-2023
        '%Y-%m-%d',     # 2023-12-31
        '%Y/%m/%d',     # 2023/12/31
        '%d.%m.%Y',     # 31.12.2023
        '%d/%m/%y',     # 31/12/23
        '%d-%m-%y',     # 31-12-23
        '%m/%d/%Y',     # 12/31/2023 (formato USA)
        '%m-%d-%Y',     # 12-31-2023 (formato USA)
        '%Y%m%d',       # 20231231
        '%d %b %Y',     # 31 Dec 2023
        '%d %B %Y',     # 31 December 2023
        '%b %d, %Y',    # Dec 31, 2023
        '%B %d, %Y',    # December 31, 2023
    ]
    
    converted_series = []
    failed_conversions = []
    successful_formats = {}
    
    for idx, value in enumerate(series):
        if pd.isna(value):
            converted_series.append(pd.NaT)
            continue
        
        # Se è già datetime, mantienilo ma controlla se è valido
        if isinstance(value, (pd.Timestamp, datetime)):
            # Controlla se la data è valida (non ha mese 0)
            if hasattr(value, 'month') and value.month == 0:
                print(f"    ATTENZIONE: Data non valida rilevata alla riga {idx}: {value}")
                converted_series.append(pd.NaT)
                failed_conversions.append((idx, str(value)))
            else:
                converted_series.append(value)
            continue
        
        # Converti in stringa e pulisci
        value_str = str(value).strip()
        
        # Rimuovi caratteri problematici
        value_str = value_str.replace('  ', ' ')  # doppi spazi
        
        # Prova formati specifici
        converted_date = None
        successful_format = None
        
        for fmt in formats_to_try:
            try:
                converted_date = pd.to_datetime(value_str, format=fmt)
                successful_format = fmt
                break
            except ValueError:
                continue
            except Exception as e:
                continue
        
        # Se non funziona, usa il parser automatico di pandas con più opzioni
        if converted_date is None:
            try:
                # Prova con dayfirst=True (formato europeo)
                converted_date = pd.to_datetime(value_str, dayfirst=True, errors='raise')
                successful_format = 'auto_dayfirst'
            except:
                try:
                    # Prova con dayfirst=False (formato USA)
                    converted_date = pd.to_datetime(value_str, dayfirst=False, errors='raise')
                    successful_format = 'auto_monthfirst'
                except:
                    try:
                        # Ultimo tentativo con inferenza automatica
                        converted_date = pd.to_datetime(value_str, infer_datetime_format=True, errors='raise')
                        successful_format = 'auto_infer'
                    except:
                        failed_conversions.append((idx, value_str))
                        converted_date = pd.NaT
        
        # Verifica che la data convertita sia valida
        if converted_date is not pd.NaT:
            if hasattr(converted_date, 'month') and converted_date.month == 0:
                print(f"    ATTENZIONE: Conversione ha prodotto mese 0 per valore '{value_str}' alla riga {idx}")
                converted_date = pd.NaT
                failed_conversions.append((idx, value_str))
            else:
                # Traccia i formati che funzionano
                if successful_format in successful_formats:
                    successful_formats[successful_format] += 1
                else:
                    successful_formats[successful_format] = 1
        
        converted_series.append(converted_date)
    
    # Statistiche conversione
    original_count = series.notna().sum()
    converted_count = pd.Series(converted_series).notna().sum()
    
    print(f"  Valori originali non nulli: {original_count}")
    print(f"  Valori convertiti con successo: {converted_count}")
    print(f"  Valori non convertiti: {len(failed_conversions)}")
    
    if successful_formats:
        print("  Formati utilizzati con successo:")
        for fmt, count in successful_formats.items():
            print(f"    {fmt}: {count} valori")
    
    if failed_conversions:
        print("  Valori che non sono stati convertiti:")
        for idx, val in failed_conversions[:5]:  # Mostra solo i primi 5
            print(f"    Riga {idx}: '{val}'")
        if len(failed_conversions) > 5:
            print(f"    ... e altri {len(failed_conversions) - 5} valori")
    
    # Mostra alcuni esempi di valori convertiti
    converted_sample = pd.Series(converted_series).dropna().head(5)
    if not converted_sample.empty:
        print("  Esempi di valori convertiti:")
        for i, val in enumerate(converted_sample, 1):
            print(f"    {i}. {val} -> {val.strftime('%d/%m/%Y')}")
    
    return pd.Series(converted_series, index=series.index)

def main():
    """
    Funzione principale dello script
    """
    print("=== SCRIPT CONVERSIONE DATE EXCEL ===")
    print("Questo script converte colonne con date in formati diversi in datetime standardizzato.\n")
    
    # 1. Richiedi il nome del file
    while True:
        file_path = input("Inserisci il percorso del file Excel (o 'q' per uscire): ").strip()
        
        if file_path.lower() == 'q':
            print("Uscita dal programma.")
            return
        
        if not file_path:
            print("Inserisci un percorso valido.")
            continue
        
        # Aggiungi estensione se mancante
        if not file_path.endswith(('.xlsx', '.xls')):
            file_path += '.xlsx'
        
        if os.path.exists(file_path):
            break
        else:
            print(f"File non trovato: {file_path}")
            print("Assicurati che il file esista e il percorso sia corretto.")
    
    # 2. Carica il file Excel
    try:
        print(f"\nCaricamento file: {file_path}")
        df = pd.read_excel(file_path)
        print(f"File caricato con successo. Righe: {len(df)}, Colonne: {len(df.columns)}")
        print(f"Nomi colonne: {list(df.columns)}")
    except Exception as e:
        print(f"Errore nel caricamento del file: {e}")
        return
    
    # 3. Identifica colonne date
    print("\n" + "="*50)
    date_columns = analyze_date_columns(df)
    
    if not date_columns:
        print("\nNessuna colonna con date identificata automaticamente.")
        print("Colonne disponibili:")
        for i, col in enumerate(df.columns, 1):
            print(f"  {i}. {col}")
        
        manual_input = input("\nVuoi specificare manualmente le colonne date? (s/n): ").strip().lower()
        if manual_input == 's':
            cols_input = input("Inserisci i nomi delle colonne separate da virgola: ").strip()
            date_columns = [col.strip() for col in cols_input.split(',') if col.strip()]
        else:
            print("Nessuna colonna da convertire. Uscita dal programma.")
            return
    
    # 4. Conferma colonne da convertire
    print(f"\nColonne da convertire: {date_columns}")
    confirm = input("Procedere con la conversione? (s/n): ").strip().lower()
    if confirm != 's':
        print("Operazione annullata.")
        return
    
    # 5. Crea backup del DataFrame originale
    df_backup = df.copy()
    
    # 6. Converti le colonne
    print("\n" + "="*50)
    print("AVVIO CONVERSIONE DATE")
    print("="*50)
    
    conversion_summary = {}
    
    for col in date_columns:
        if col in df.columns:
            original_type = df[col].dtype
            original_nulls = df[col].isna().sum()
            
            # Converti la colonna
            df[col] = convert_mixed_dates(df[col], col)
            
            # Statistiche post-conversione
            new_type = df[col].dtype
            new_nulls = df[col].isna().sum()
            
            conversion_summary[col] = {
                'original_type': original_type,
                'new_type': new_type,
                'original_nulls': original_nulls,
                'new_nulls': new_nulls,
                'date_range': f"{df[col].min()} - {df[col].max()}" if df[col].notna().any() else "Nessuna data valida"
            }
        else:
            print(f"ATTENZIONE: Colonna '{col}' non trovata nel DataFrame")
    
    # 7. Mostra riassunto conversione
    print("\n" + "="*50)
    print("RIASSUNTO CONVERSIONE")
    print("="*50)
    
    for col, stats in conversion_summary.items():
        print(f"\nColonna: {col}")
        print(f"  Tipo originale: {stats['original_type']}")
        print(f"  Tipo nuovo: {stats['new_type']}")
        print(f"  Valori nulli prima: {stats['original_nulls']}")
        print(f"  Valori nulli dopo: {stats['new_nulls']}")
        print(f"  Range date: {stats['date_range']}")
    
    # 8. Verifica finale per date non valide
    print("\n" + "="*50)
    print("VERIFICA FINALE DATE")
    print("="*50)
    
    for col in date_columns:
        if col in df.columns:
            invalid_dates = df[col].isna().sum()
            valid_dates = df[col].notna().sum()
            
            if valid_dates > 0:
                min_date = df[col].min()
                max_date = df[col].max()
                
                # Controlla se ci sono date con mese 0 (che non dovrebbero esistere)
                if hasattr(min_date, 'month') and min_date.month == 0:
                    print(f"ERRORE: Colonna {col} contiene date non valide (mese 0)")
                    continue
                
                print(f"Colonna {col}: {valid_dates} date valide, {invalid_dates} non valide")
                print(f"  Range: dal {min_date.strftime('%d/%m/%Y')} al {max_date.strftime('%d/%m/%Y')}")
                
                # Mostra alcuni esempi formattati
                sample_dates = df[col].dropna().head(3)
                print("  Esempi formattati:")
                for i, date_val in enumerate(sample_dates, 1):
                    print(f"    {i}. {date_val.strftime('%d/%m/%Y')}")
            else:
                print(f"Colonna {col}: NESSUNA data valida convertita!")
    
    # 9. Salva il file modificato
    output_path = file_path.replace('.xlsx', '_date_convertite.xlsx')
    
    try:
        # Salva con un writer personalizzato per controllare il formato
        with pd.ExcelWriter(output_path, engine='openpyxl', date_format='DD/MM/YYYY') as writer:
            df.to_excel(writer, index=False, sheet_name='Dati')
        print(f"\nFile salvato con successo: {output_path}")
    except Exception as e:
        print(f"Errore nel salvataggio: {e}")
        return
    
    # 9. Opzione per salvare anche un file di controllo
    save_control = input("\nVuoi salvare un file di controllo con esempi delle conversioni? (s/n): ").strip().lower()
    if save_control == 's':
        control_data = []
        for col in date_columns:
            if col in df.columns:
                # Prendi alcuni esempi
                sample_indices = df[col].dropna().index[:10]
                for idx in sample_indices:
                    control_data.append({
                        'colonna': col,
                        'riga': idx,
                        'valore_originale': df_backup.loc[idx, col],
                        'valore_convertito': df.loc[idx, col],
                        'formato_finale': df.loc[idx, col].strftime('%d/%m/%Y') if pd.notna(df.loc[idx, col]) else 'N/A'
                    })
        
        if control_data:
            control_df = pd.DataFrame(control_data)
            control_path = file_path.replace('.xlsx', '_controllo_conversione.xlsx')
            print(f"File di controllo salvato: {control_path}")
    
    print("\n" + "="*50)
    print("CONVERSIONE COMPLETATA!")
    print("="*50)
    print(f"File originale: {file_path}")
    print(f"File convertito: {output_path}")
    print("\nOra puoi usare il file convertito per le tue analisi Python.")
    print("Le colonne date sono ora in formato datetime e pronte per l'analisi.")

if __name__ == "__main__":
    main()