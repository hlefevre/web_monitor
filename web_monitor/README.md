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

## Usage

Run the main script to start monitoring:
bash
python main.py


## Configuration

- Adjust the check interval in `web_monitor/config.py` by modifying the `CHECK_INTERVAL` variable.