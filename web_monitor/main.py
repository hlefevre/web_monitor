import argparse
from datetime import datetime
from web_monitor.monitor import monitor_sites
from web_monitor.utils import read_daily_log, save_summary, clean_content, split_content, get_api_key
from web_monitor.chatgpt import generate_summary

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor websites for changes.")
    parser.add_argument('--ignore-check', action='store_true', help="Ignore the daily log existence check.")
    args = parser.parse_args()

    api_key = get_api_key()
    if not api_key:
        raise ValueError("API key for ChatGPT is not set. Please set the key in key.txt.")

    monitor_sites(args.ignore_check)
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    content = read_daily_log(date_str)
    cleaned_content = clean_content(content)
    content_parts = split_content(cleaned_content)

    summaries = [generate_summary(part, api_key) for part in content_parts]
    final_summary = generate_summary("\n\n".join(summaries), api_key)
    
    save_summary(date_str, final_summary)
    print(f"Synthèse sauvegardée dans synthesis/{date_str}.txt")