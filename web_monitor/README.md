# Web Monitor

## Description
A Python script to monitor changes on specified websites and log the results.

## Setup

1. **Clone the repository:**
bash
git clone <repository_url>
cd web_monitor

2. **Create a virtual environment:**
bash
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate

3. **Install dependencies:**
bash
pip install -r requirements.txt


4. **Configure the sites to monitor:**
    - Add the URLs of the sites you want to monitor in `data/sites.txt`, one per line.

5. **Add your OpenAI API key:**
    - Create a file named `key.txt` in the root directory of the project.
    - Add your OpenAI API key to this file.

## Usage

Run the main script to start monitoring:
bash
python main.py --ignore-check


## Configuration

- Adjust the check interval in `web_monitor/config.py` by modifying the `CHECK_INTERVAL` variable.
- Configure the ChatGPT settings in `web_monitor/config.py`:
    - `CHATGPT_ENGINE`: The model to use (e.g., `"gpt-3.5-turbo"`).
    - `CHATGPT_PROMPT_TEMPLATE`: The template for the prompt.
    - `CHATGPT_MAX_TOKENS`: The maximum number of tokens for the response.
    - `CHATGPT_TEMPERATURE`: The temperature setting for the response.

## .gitignore

Ensure your `.gitignore` file includes the following to avoid committing sensitive and unnecessary files:

plaintext
## Ignorer les fichiers de configuration sensibles
key.txt
## Ignorer les répertoires de synthèse et de résultats
synthesis/
results/
## Ignorer les fichiers de log
.log
## Ignorer les fichiers de cache et temporairespycache/
.pyc
.pyo
.pyd
.tmp
.bak
.swp
## Ignorer les environnements virtuels
venv/
.env/
## Ignorer les fichiers spécifiques à l'IDE
.vscode/
.idea/