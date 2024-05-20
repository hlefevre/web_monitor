import os
import argparse
from .utils import load_sites, fetch_site_content, save_content, load_previous_content, compare_content, save_changes_log, check_daily_log_exists

def monitor_sites(ignore_check):
    # Vérifier si le fichier de résultats du jour existe déjà, sauf si l'option ignore_check est activée
    if not ignore_check and check_daily_log_exists():
        print("Le fichier de résultats pour la date du jour existe déjà. Arrêt du programme.")
        return

    sites = load_sites('data/sites.txt')
    for site in sites:
        content = fetch_site_content(site)
        if content:
            site_filename = site.replace("https://", "").replace("http://", "").replace("/", "_") + ".txt"
            previous_content = load_previous_content(os.path.join('data', site_filename))
            if compare_content(previous_content, content):
                print(f"Changes detected on {site}")
                save_changes_log(site, content)
                save_content(os.path.join('data', site_filename), content)
            else:
                print(f"No changes on {site}")
        else:
            print(f"Failed to fetch content from {site}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor websites for changes.")
    parser.add_argument('--ignore-check', action='store_true', help="Ignore the daily log existence check.")
    args = parser.parse_args()

    monitor_sites(args.ignore_check)