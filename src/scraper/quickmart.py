from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
from datetime import datetime

CATEGORY_URLS = [
    "https://naivas.online/fresh-produce",
    "https://naivas.online/food-cupboard",
    "https://naivas.online/snacks",
    # Add more if needed
]

def scrape_naivas():
    options = Options()
    # comment headless to visually debug
    # options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    all_data = []

    for url in CATEGORY_URLS:
        print(f"\n>>> Loading page: {url}")
        driver.get(url)
        time.sleep(7)
        # Save screenshot for inspection
        screenshot = f"scrape_naivas_debug_{datetime.now().strftime('%H%M%S')}.png"
        driver.save_screenshot(screenshot)
        print(f"Screenshot saved: {screenshot}")

        products = driver.find_elements(By.CSS_SELECTOR, ".product-item-info, .product-grid-item, .product-card, .product-item")
        print(f"Found {len(products)} product elements at this page.")

        for product in products[:5]:  # print first few for debugging
            try:
                name = product.find_element(By.CSS_SELECTOR, "h2, .product-title, .product-name").text
                price = product.find_element(By.CSS_SELECTOR, ".price, .product-price").text
                print(f"Sample item: {name} — {price}")
                all_data.append({
                    "product_name": name,
                    "price": price,
                    "date": datetime.now().strftime("%Y-%m-%d")
                })
            except Exception as e:
                print(" — Failed to parse product:", e)

    driver.quit()

    print(f"\nTotal items scraped: {len(all_data)}")
    if not all_data:
        print("No data to write. Exiting.")
        return

    path = "src/scraper/data/naivas_raw.csv"
    with open(path, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["product_name","price","date"])
        writer.writeheader()
        writer.writerows(all_data)
    print(f"Data saved to {path}")

if __name__ == "__main__":
    scrape_naivas()



