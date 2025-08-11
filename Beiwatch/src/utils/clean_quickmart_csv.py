import csv
import os

# File paths
RAW_FILE = os.path.join("src", "scraper", "data", "quickmart_products.csv")
CLEAN_FILE = os.path.join("src", "scraper", "data", "quickmart_cleaned.csv")

def clean_price(price_str):
    try:
        return price_str.replace("KES", "").replace(",", "").replace(" ", "").strip()
    except:
        return None

def clean_csv():
    with open(RAW_FILE, newline='', encoding='utf-8') as infile, \
         open(CLEAN_FILE, mode='w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        writer.writerow(["id", "name", "url", "price"])  # Header row

        seen = set()  # To remove exact duplicates

        for row in reader:
            if len(row) < 4 or row[0] == "No.":
                continue

            item_id = row[0].strip()
            name = row[1].strip()
            url = row[2].strip()
            raw_price = row[3].strip()
            clean = clean_price(raw_price)

            if not clean:
                continue

            key = (name.lower(), url)
            if key in seen:
                continue
            seen.add(key)

            writer.writerow([item_id, name, url, clean])

    print("✅ Cleaned Quickmart CSV saved as:", CLEAN_FILE)

if __name__ == "__main__":
    clean_csv()
