from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import csv

# List of Naivas category URLs
urls = [
    "https://naivas.online/fats-oils",
    "https://naivas.online/food-additives",
    "https://naivas.online/snacks",
    "https://naivas.online/commodities",
    "https://naivas.online/canned-frozen-meals",
    "https://naivas.online/naivas-dry-cereals-nuts",
    "https://naivas.online/naivas-bakery",
    "https://naivas.online/fruit-veggie",
    "https://naivas.online/dairy",
    "https://naivas.online/pre-packed-meat-products",
    "https://naivas.online/cold-deli",
    "https://naivas.online/naivas-butchery",
    "https://naivas.online/outsourced-bakery",
    "https://naivas.online/baby-hygiene",
    "https://naivas.online/baby-skincare",
    "https://naivas.online/kitchen-appliances",
    "https://naivas.online/fridges-freezers",
    "https://naivas.online/air-conditioning",
    "https://naivas.online/sound-system",
    "https://naivas.online/washing-machine",
    "https://naivas.online/spirits",
    "https://naivas.online/beer",
    "https://naivas.online/wine",
    "https://naivas.online/intimate"
]

# Setup headless Chrome
options = Options()
options.headless = True
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/114.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

def scroll_page():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # wait for page to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Prepare CSV file
with open("naivas_products.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["No.", "Product", "Link", "Price"])

    counter = 1
    for url in urls:
        try:
            driver.get(url)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.flex.flex-col.grow")))

            scroll_page()  # trigger lazy loading if used

            soup = BeautifulSoup(driver.page_source, "html.parser")
            containers = soup.select("div.flex.flex-col.grow")

            for item in containers:
                try:
                    name_tag = item.select_one("div.text-black-50.py-2.font-medium a")
                    name = name_tag.get_text(strip=True) if name_tag else "N/A"
                    link = "https://naivas.online" + name_tag["href"] if name_tag and "href" in name_tag.attrs else "N/A"
                    
                    price_tag = item.select_one("div.product-price span")
                    price = price_tag.get_text(strip=True) if price_tag else "N/A"

                    if name != "N/A":
                        writer.writerow([counter, name, link, price])
                        print(f"{counter}. {name} | {link} | {price}")
                        counter += 1
                except Exception as inner_e:
                    print(f"Error parsing product: {inner_e}")
        except Exception as outer_e:
            print(f"Error loading page {url}: {outer_e}")

driver.quit()
print(f"\nTotal products scraped: {counter - 1}")
