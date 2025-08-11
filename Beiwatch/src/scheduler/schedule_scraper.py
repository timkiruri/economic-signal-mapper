import schedule
import time
import subprocess
import os
from datetime import datetime
import sys

# Path to your Python executable inside the venv
venv_python = sys.executable
project_root = os.path.abspath("src")

def run_naivas_pipeline():
    print(f"[{datetime.now()}] Cleaning Naivas data...")
    subprocess.run([venv_python, "src/utils/clean_naivas_csv.py"])
    
    print(f"[{datetime.now()}] Loading Naivas data...")
    subprocess.run(
        [venv_python, "src/database/load_naivas_data.py"],
        env={**os.environ, "PYTHONPATH": project_root}
    )
    
    print(f"[{datetime.now()}] Finished Naivas pipeline.\n")

def run_carrefour_pipeline():
    print(f"[{datetime.now()}] Cleaning Carrefour data...")
    subprocess.run([venv_python, "src/utils/clean_carrefour_csv.py"])
    
    print(f"[{datetime.now()}] Loading Carrefour data...")
    subprocess.run(
        [venv_python, "src/database/load_carrefour_data.py"],
        env={**os.environ, "PYTHONPATH": project_root}
    )
    
    print(f"[{datetime.now()}] Finished Carrefour pipeline.\n")

def run_quickmart_pipeline():
    print(f"[{datetime.now()}] Cleaning Quickmart data...")
    subprocess.run([venv_python, "src/utils/clean_quickmart_csv.py"])
    
    print(f"[{datetime.now()}] Loading Quickmart data...")
    subprocess.run(
        [venv_python, "src/database/load_quickmart_data.py"],
        env={**os.environ, "PYTHONPATH": project_root}
    )
    
    print(f"[{datetime.now()}] Finished Quickmart pipeline.\n")

# Schedule tasks
#schedule.every().day.at("00:00").do(run_naivas_pipeline)          # For testing
#schedule.every().day.at("00:05").do(run_carrefour_pipeline)
#schedule.every().day.at("00:10").do(run_quickmart_pipeline)
schedule.every(1).minutes.do(run_naivas_pipeline)
schedule.every(2).minutes.do(run_carrefour_pipeline)
schedule.every(3).minutes.do(run_quickmart_pipeline)

print("Scheduler started. Waiting for tasks...\n")

while True:
    schedule.run_pending()
    time.sleep(30)


