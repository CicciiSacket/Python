import mgmt_pipeline as pipeline_mgmt
from dotenv import load_dotenv
import os

load_dotenv()

"""
/**
 * Script principale per la cancellazione di pipeline Azure DevOps.
 *
 * @module azure_pipelines_cleaner/main
 */

/**
 * Funzione principale che gestisce la cancellazione delle pipeline.
 * 
 * @returns {list} Lista delle pipeline trovate o None se vengono eliminate
 */
"""
def main():
    # === CONFIGURAZIONE ===
    organization = os.getenv("AZURE_ORG_NAME")      # Nome dell'organizzazione letto dal file .env
    project = os.getenv("AZURE_PROJECT_NAME")       # Nome del progetto letto dal file .env
    pat = os.getenv("AZURE_PAT")                    # PAT letto dal file .env
    keyword = "- prod"                              # Parola chiave da cercare nel nome delle pipeline

    # Se True -> mostra cosa verrebbe eliminato, ma non cancella
    # Se False -> esegue realmente la cancellazione
    dry_run_YES = True
    dry_run_FALSE = False

    # === ESECUZIONE ===
    print("Recupero tutte le pipeline...")
    pipelines = pipeline_mgmt.get_pipelines(organization, project, pat)
    print(f"\nFiltraggio pipeline con parola chiave '{keyword}'...")
    filtered_pipelines = pipeline_mgmt.filter_pipelines(pipelines, keyword)
    print(f"Pipeline filtrate ({len(filtered_pipelines)} trovate):")
    for p in filtered_pipelines:
        print(f"- {p['name']} (ID: {p['id']})")

    #pipeline_mgmt.delete_pipelines_by_name(organization, project, pat, keyword, dry_run=dry_run_YES)
    #pipeline_mgmt.delete_pipelines_by_name(organization, project, pat, keyword, dry_run=dry_run_FALSE)

if __name__ == "__main__":
    main()
