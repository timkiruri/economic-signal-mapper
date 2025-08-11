from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv

# List of Quickmart category URLs (replace with actual ones)
urls = [ 
    "https://www.quickmart.co.ke/foods",
    "https://www.quickmart.co.ke/animal-feeds-pets",
    "https://www.quickmart.co.ke/baby-food",
    "https://www.quickmart.co.ke/beverages",
    "https://www.quickmart.co.ke/breakfast",
    "https://www.quickmart.co.ke/cakes-bread",
    "https://www.quickmart.co.ke/confectioneries-(sweets)",
    "https://www.quickmart.co.ke/cooking-oils-fats",
    "https://www.quickmart.co.ke/dairy-products",
    "https://www.quickmart.co.ke/ethnic",
    "https://www.quickmart.co.ke/flour",
    "https://www.quickmart.co.ke/frozen-food-consignment",
    "https://www.quickmart.co.ke/frozen-foods",
    "https://www.quickmart.co.ke/juices-carbonates",
    "https://www.quickmart.co.ke/meat-products-eggs",
    "https://www.quickmart.co.ke/pasta-noodles",
    "https://www.quickmart.co.ke/processed-canned-foods",
    "https://www.quickmart.co.ke/quickmart-bakery",
    "https://www.quickmart.co.ke/quickmart-butchery-fishery",
    "https://www.quickmart.co.ke/quickmart-deli",
    "https://www.quickmart.co.ke/rice-cereal-consignment",
    "https://www.quickmart.co.ke/rice-cereals",
    "https://www.quickmart.co.ke/seasoning-condiments",
    "https://www.quickmart.co.ke/snack-foods",
    "https://www.quickmart.co.ke/water",
    "https://www.quickmart.co.ke/fresh",
    "https://www.quickmart.co.ke/quickmart-veges",
    "https://www.quickmart.co.ke/personal-care",
    "https://www.quickmart.co.ke/baby-care",
    "https://www.quickmart.co.ke/beauty-cosmetics",
    "https://www.quickmart.co.ke/body-care",
    "https://www.quickmart.co.ke/diapers-wipes",
    "https://www.quickmart.co.ke/hair-care-products",
    "https://www.quickmart.co.ke/health-wellness",
    "https://www.quickmart.co.ke/oral-care-products",
    "https://www.quickmart.co.ke/personal-wash",
    "https://www.quickmart.co.ke/sanitary",
    "https://www.quickmart.co.ke/liquor",
    "https://www.quickmart.co.ke/beer",
    "https://www.quickmart.co.ke/spirits",
    "https://www.quickmart.co.ke/wines",
    "https://www.quickmart.co.ke/homecare",
    "https://www.quickmart.co.ke/candles-fragrances",
    "https://www.quickmart.co.ke/cleaners-polish",
    "https://www.quickmart.co.ke/cleaning-equipments",
    "https://www.quickmart.co.ke/hardware-garden-locks",
    "https://www.quickmart.co.ke/pest-control",
    "https://www.quickmart.co.ke/quickmart(internal)",
    "https://www.quickmart.co.ke/soaps-detergents",
    "https://www.quickmart.co.ke/tissue",
    "https://www.quickmart.co.ke/households",
    "https://www.quickmart.co.ke/bicycles",
    "https://www.quickmart.co.ke/cookers-and-ovens",
    "https://www.quickmart.co.ke/cooking-equipment-fuel",
    "https://www.quickmart.co.ke/furniture",
    "https://www.quickmart.co.ke/home-improvements",
    "https://www.quickmart.co.ke/kitchen-dining",
    "https://www.quickmart.co.ke/light-plasticware",
    "https://www.quickmart.co.ke/luggage",
    "https://www.quickmart.co.ke/office-supplies-stationery",
    "https://www.quickmart.co.ke/party-occasions",
    "https://www.quickmart.co.ke/toys-games",
    "https://www.quickmart.co.ke/electronics",
    "https://www.quickmart.co.ke/electrical-accessories",
    "https://www.quickmart.co.ke/fridges-and-freezers",
    "https://www.quickmart.co.ke/home-audio",
    "https://www.quickmart.co.ke/phones-tablets-accessories",
    "https://www.quickmart.co.ke/small-kitchen-home-appliance",
    "https://www.quickmart.co.ke/tv",
    "https://www.quickmart.co.ke/vehicle-care-spares-parts",
    "https://www.quickmart.co.ke/washers-and-dryers",
    "https://www.quickmart.co.ke/textile",
    "https://www.quickmart.co.ke/beddings",
    "https://www.quickmart.co.ke/gents-wear-shoes-acc",
    "https://www.quickmart.co.ke/kids-wear-shoes-accessories",
    "https://www.quickmart.co.ke/ladies-wear-shoes-acc",
    "https://www.quickmart.co.ke/linen",
    "https://www.quickmart.co.ke/other-textile",
    "https://www.quickmart.co.ke/sporting-goods(not-wearable)"
]


# Setup headless Chrome
options = Options()
options.headless = True
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/114.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

# Prepare CSV file
with open("quickmart_products.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["No.", "Product", "Link", "Price"])

    counter = 1
    for url in urls:
        try:
            driver.get(url)
            time.sleep(5)  # Wait for JS to load
            soup = BeautifulSoup(driver.page_source, "html.parser")

            product_blocks = soup.select("div.products-foot")
            for block in product_blocks:
                try:
                    # Get product name and link
                    name_tag = block.select_one("a.products-title")
                    name = name_tag.get_text(strip=True) if name_tag else "N/A"
                    link = "https://quickmart.co.ke" + name_tag['href'] if name_tag else "N/A"

                    # Get price
                    price_tag = block.select_one("span.products-price-new")
                    price = price_tag.get_text(strip=True) if price_tag else "N/A"

                    writer.writerow([counter, name, link, price])
                    print(f"{counter}. {name} | {link} | {price}")
                    counter += 1
                except Exception as e:
                    print(f"Error parsing product: {e}")

        except Exception as e:
            print(f"Error loading page {url}: {e}")

driver.quit()
print(f"\nTotal products scraped: {counter - 1}")
