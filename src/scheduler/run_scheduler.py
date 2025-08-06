from datetime import datetime
import subprocess

def run_naivas_loader():
    print(f"[{datetime.now()}]  Loading Naivas data...")
    subprocess.run(["python", "src/database/load_naivas_data.py"])
    print(f"[{datetime.now()}]  Finished loading Naivas data.\n")

def run_carrefour_loader():
    print(f"[{datetime.now()}]  Loading Carrefour data...")
    subprocess.run(["python", "src/database/load_carrefour_data.py"])
    print(f"[{datetime.now()}]  Finished loading Carrefour data.\n")

def run_quickmart_loader():
    print(f"[{datetime.now()}]  Loading Quickmart data...")
    subprocess.run(["python", "src/database/load_quickmart_data.py"])
    print(f"[{datetime.now()}]  Finished loading Quickmart data.\n")

# --- TEMPORARY IMMEDIATE RUN ---
print(" Running all scrapers immediately for testing...\n")
run_naivas_loader()
run_carrefour_loader()
run_quickmart_loader()
print(" All scrapers completed.\n")

