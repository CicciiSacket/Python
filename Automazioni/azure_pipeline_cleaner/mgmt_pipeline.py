import requests
from requests.auth import HTTPBasicAuth

API_VERSION = "7.1-preview.7"

"""
/**
 * Recupera tutte le pipeline di build per un progetto Azure DevOps.
 *
 * @param {str} organization - Nome dell'organizzazione Azure DevOps.
 * @param {str} project - Nome del progetto Azure DevOps.
 * @param {str} pat - Personal Access Token per autenticazione.
 * @returns {list} Lista di pipeline.
 */
"""
def get_pipelines(organization, project, pat):
    url = f"https://dev.azure.com/{organization}/{project}/_apis/build/definitions?api-version={API_VERSION}"
    auth = HTTPBasicAuth("", pat)
    response = requests.get(url, auth=auth)
    if response.status_code != 200:
        raise Exception(f"Error pipeline recovery: {response.status_code} - {response.text}")
    return response.json().get("value", [])
"""
/**
 * Filtra le pipeline in base a una parola chiave nel nome.
 *
 * @param {list} pipelines - Lista di pipeline.
 * @param {str} keyword - Parola chiave da cercare.
 * @returns {list} Pipeline filtrate.
 */
"""
def filter_pipelines(pipelines, keyword):
    keyword = keyword.lower()
    return [p for p in pipelines if keyword in p["name"].lower()]

"""
/**
 * Elimina una pipeline specifica tramite ID.
 *
 * @param {str} organization - Nome dell'organizzazione Azure DevOps.
 * @param {str} project - Nome del progetto Azure DevOps.
 * @param {int} pipeline_id - ID della pipeline da eliminare.
 * @param {str} pat - Personal Access Token per autenticazione.
 * @returns {bool} True se la cancellazione ha successo.
 */
"""
def delete_pipeline(organization, project, pipeline_id, pat):
    url = f"https://dev.azure.com/{organization}/{project}/_apis/build/definitions/{pipeline_id}?api-version={API_VERSION}"
    auth = HTTPBasicAuth("", pat)
    response = requests.delete(url, auth=auth)
    if response.status_code not in [200, 204]:
        raise Exception(f"Delete error pipeline {pipeline_id}: {response.status_code} - {response.text}")
    return True

"""
/**
 * Trova e cancella (opzionalmente) tutte le pipeline che corrispondono a una parola chiave.
 *
 * @param {str} organization - Nome dell'organizzazione Azure DevOps.
 * @param {str} project - Nome del progetto Azure DevOps.
 * @param {str} pat - Personal Access Token per autenticazione.
 * @param {str} keyword - Parola chiave da cercare nel nome della pipeline.
 * @param {bool} dry_run - Se True, mostra solo cosa verrebbe eliminato.
 */
"""
def delete_pipelines_by_name(organization, project, pat, keyword, dry_run=True):
    pipelines = get_pipelines(organization, project, pat)
    print(f" Trovate {len(pipelines)} pipeline totali nel progetto '{project}'.")
    to_delete = filter_pipelines(pipelines, keyword)
    print(f" Trovate {len(to_delete)} pipeline da eliminare con parola chiave '{keyword}'.")
    if not to_delete:
        print(f"Not found pipeline - '{keyword}' ")
        return
    print(" Pipeline to delete:")
    for p in to_delete:
        print(f"  - {p['name']} (ID: {p['id']})")
    if dry_run:
        print("\n Only'dry run': no pipeline deleted.")
        return
    for p in to_delete:
        delete_pipeline(organization, project, p["id"], pat)
        print(f" PIPELINE '{p['name']}' (ID: {p['id']}) DELETED.")