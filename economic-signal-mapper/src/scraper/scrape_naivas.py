import csv
import requests
from bs4 import BeautifulSoup
import time

# Add all Naivas category URLs here
CATEGORY_URLS = [
    "https://naivas.online/fresh-produce",
    "https://naivas.online/fruits",
    "https://naivas.online/vegetables",
    "https://naivas.online/food-cupboard",
    "https://naivas.online/dairy-eggs",
    "https://naivas.online/meat-fish",
    "https://naivas.online/beverages",
    "https://naivas.online/baby-products",
    "https://naivas.online/pet-care",
    "https://naivas.online/health-beauty",
    "https://naivas.online/household-cleaning",
    "https://naivas.online/home-kitchen",
    "https://naivas.online/electronics",
    # Add more category URLs here
]

# Headers to mimic a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def scrape_naivas():
    all_products = []

    for url in CATEGORY_URLS:
        print(f"Scraping: {url}")
        try:
            response = requests.get(url, headers=HEADERS)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_cards = soup.find_all("div", class_="product-item")
            if not product_cards:
                print(f"❌ No products found at: {url}")
                continue

            for product in product_cards:
                name_tag = product.find("a", class_="product-item-link")
                price_tag = product.find("span", class_="price")
                link = name_tag["href"] if name_tag else ""
                name = name_tag.text.strip() if name_tag else "Unknown"
                price = price_tag.text.strip() if price_tag else "Unknown"

                all_products.append({
                    "name": name,
                    "price": price,
                    "link": link,
                    "category_url": url
                })

            time.sleep(1)  # Be polite

        except Exception as e:
            print(f"Error scraping {url}: {e}")

    # Save to CSV
    if all_products:
        keys = all_products[0].keys()
        with open("naivas_products.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(all_products)
        print(f"✅ Done! Saved {len(all_products)} products to naivas_products.csv")
    else:
        print("⚠️ No products scraped.")

if __name__ == "__main__":
    scrape_naivas()
