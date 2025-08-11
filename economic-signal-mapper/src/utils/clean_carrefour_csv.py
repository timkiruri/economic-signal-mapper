import csv
import os
from datetime import datetime

# File paths
RAW_FILE = os.path.join("src", "scraper", "data", "carrefour_products.csv")
CLEAN_FILE = os.path.join("src", "scraper", "data", "carrefour_cleaned.csv")

def clean_price(price_str):
    try:
        return price_str.replace(",", "").replace(" ", "").strip()
    except:
        return None

def clean_csv():
    with open(RAW_FILE, newline='', encoding='utf-8') as infile, \
         open(CLEAN_FILE, mode='w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Write header row
        writer.writerow(["name", "url", "price", "category", "store", "date"])

        seen = set()  # To remove duplicates

        next(reader)  # Skip original header

        for row in reader:
            if len(row) < 3:
                continue

            name = row[0].strip()
            url = row[1].strip()
            raw_price = row[2].strip()
            price = clean_price(raw_price)

            if not price:
                continue

            # Extract category from URL: /en/<category>/
            category = ""
            try:
                parts = url.split("/en/")
                if len(parts) > 1:
                    category = parts[1].split("/")[0]
            except:
                pass

            store = "Carrefour"
            date = datetime.now().date()

            key = (name.lower(), url)
            if key in seen:
                continue
            seen.add(key)

            writer.writerow([name, url, price, category, store, date])

    print("✅ Cleaned Carrefour CSV saved as:", CLEAN_FILE)

if __name__ == "__main__":
    clean_csv()
