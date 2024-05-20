import os
import requests
import re
from datetime import datetime


def check_file_exists(filepath):
    """
    Vérifie si un fichier existe à l'emplacement spécifié.
    
    :param filepath: Chemin du fichier à vérifier.
    :return: True si le fichier existe, False sinon.
    """
    return os.path.exists(filepath)

def load_sites(filepath):
    """
    Charge les URLs des sites à surveiller à partir d'un fichier.
    
    :param filepath: Chemin du fichier contenant les URLs des sites.
    :return: Une liste de chaînes de caractères, chaque chaîne étant une URL.
    :raises FileNotFoundError: Si le fichier n'existe pas.
    """
    if not check_file_exists(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")
    
    with open(filepath, 'r') as file:
        return [line.strip() for line in file.readlines()]

def fetch_site_content(url):
    """
    Récupère le contenu HTML d'un site web.
    
    :param url: URL du site web à récupérer.
    :return: Le contenu HTML du site web sous forme de chaîne de caractères.
    :raises requests.RequestException: Si une erreur se produit lors de la requête HTTP.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lève une exception pour les réponses HTTP erronées
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def save_content(filepath, content):
    """
    Sauvegarde le contenu dans un fichier.
    
    :param filepath: Chemin du fichier où sauvegarder le contenu.
    :param content: Contenu à sauvegarder.
    """
    with open(filepath, 'w') as file:
        file.write(content)

def load_previous_content(filepath):
    """
    Charge le contenu précédent d'un fichier.
    
    :param filepath: Chemin du fichier à charger.
    :return: Le contenu du fichier sous forme de chaîne de caractères, ou None si le fichier n'existe pas.
    """
    if not check_file_exists(filepath):
        return None
    
    with open(filepath, 'r') as file:
        return file.read()

def compare_content(old_content, new_content):
    """
    Compare le contenu précédent et le contenu actuel.
    
    :param old_content: Contenu précédent.
    :param new_content: Contenu actuel.
    :return: True si le contenu est différent, False sinon.
    """
    return old_content != new_content

def save_changes_log(site, content):
    """
    Sauvegarde les modifications détectées dans un fichier journalier.
    
    :param site: URL du site web.
    :param content: Contenu modifié.
    """
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_dir = 'results'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_filepath = os.path.join(log_dir, f"{date_str}.txt")
    
    with open(log_filepath, 'a') as log_file:
        log_file.write(f"Changes detected on {site}:\n")
        log_file.write(content) 
        log_file.write("\n\n")

def check_daily_log_exists():
    """
    Vérifie si un fichier de résultats pour la date du jour existe déjà.
    
    :return: True si le fichier existe, False sinon.
    """
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_dir = 'results'
    log_filepath = os.path.join(log_dir, f"{date_str}.txt")
    return os.path.exists(log_filepath)

def clean_content(content):
    """
    Nettoie le contenu en supprimant les balises HTML et autres informations inutiles.
    
    :param content: Contenu à nettoyer.
    :return: Contenu nettoyé.
    """
    # Supprimer les balises HTML
    clean_text = re.sub(r'<[^>]+>', '', content)
    # Supprimer les espaces multiples et les nouvelles lignes
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    return clean_text

def split_content(content, max_length=2000):
    """
    Divise le contenu en sous-éléments si nécessaire.
    
    :param content: Contenu à diviser.
    :param max_length: Longueur maximale de chaque sous-élément.
    :return: Liste de sous-éléments.
    """
    words = content.split()
    parts = []
    current_part = []

    for word in words:
        if len(' '.join(current_part + [word])) > max_length:
            parts.append(' '.join(current_part))
            current_part = [word]
        else:
            current_part.append(word)
    
    if current_part:
        parts.append(' '.join(current_part))
    
    return parts

def save_summary(date_str, summary):
    """
    Sauvegarde la synthèse dans un fichier.
    
    :param date_str: Date sous forme de chaîne de caractères (YYYY-MM-DD).
    :param summary: Synthèse à sauvegarder.
    """
    summary_dir = 'synthesis'
    if not os.path.exists(summary_dir):
        os.makedirs(summary_dir)
    summary_filepath = os.path.join(summary_dir, f"{date_str}.txt")
    
    with open(summary_filepath, 'w') as summary_file:
        summary_file.write(summary)

def read_daily_log(date_str):
    """
    Lit le fichier de résultats du jour et retourne son contenu.
    
    :param date_str: Date sous forme de chaîne de caractères (YYYY-MM-DD).
    :return: Contenu du fichier de résultats du jour.
    """
    log_dir = 'results'
    log_filepath = os.path.join(log_dir, f"{date_str}.txt")
    
    if not os.path.exists(log_filepath):
        raise FileNotFoundError(f"No log file found for date {date_str}.")
    
    with open(log_filepath, 'r') as log_file:
        return log_file.read()

def get_api_key(filepath='key.txt'):
    """
    Lit la clé API à partir d'un fichier.
    
    :param filepath: Chemin du fichier contenant la clé API.
    :return: Clé API sous forme de chaîne de caractères.
    """
    with open(filepath, 'r') as file:
        return file.read().strip()