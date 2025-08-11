import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time

def scrape_naivas():
    urls = [
        "https://naivas.online/food-cupboard",
        "https://naivas.online/food-cupboard/food-items",
        "https://naivas.online/snacks",
        "https://naivas.online/fats-oils",
        "https://naivas.online/fresh-food",
        "https://naivas.online/naivas-butchery",
        "https://naivas.online/baby-&-kids",
        "https://naivas.online/electronics",
        "https://naivas.online/naivas-liqour"
    ]

    all_data = []

    for url in urls:
        print(f"Scraping {url} ...")
        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(response.text, 'html.parser')

            # This may need adjusting based on actual site structure
            products = soup.find_all("div", class_="product-grid-item")

            for product in products:
                name_tag = product.find("h2")
                price_tag = product.find("span", class_="price")

                if not name_tag or not price_tag:
                    continue

                name = name_tag.text.strip()
                price = price_tag.text.strip().replace("KSh", "").replace(",", "")

                all_data.append({
                    "product_name": name,
                    "price": price,
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "url": url  # track which category it came from
                })

            time.sleep(1)  # Be polite, avoid hammering the server

        except Exception as e:
            print(f"❌ Error scraping {url}: {e}")

    # Save to CSV
    with open("src/scraper/data/naivas_raw.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["product_name", "price", "date", "url"])
        writer.writeheader()
        writer.writerows(all_data)

    print(f"✅ Scraping complete: {len(all_data)} products saved to naivas_raw.csv")

if __name__ == "__main__":
    scrape_naivas()
