import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base, Product, Price, Retailer, Category
from datetime import datetime

# Set up DB connection
engine = create_engine("sqlite:///./economic_data.db")
SessionLocal = sessionmaker(bind=engine)

def scrape_carrefour():
    print("Starting Carrefour scraper...")
    
    session = SessionLocal()

    # Retailer setup (ensure it exists)
    retailer_name = "Carrefour"
    retailer = session.query(Retailer).filter_by(name=retailer_name).first()
    if not retailer:
        retailer = Retailer(name=retailer_name, website_url="https://www.carrefour.ke")
        session.add(retailer)
        session.commit()

    url = "https://www.carrefour.ke/mafken/en/c/FK-Kenya-Carrefour"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    product_tiles = soup.find_all("div", class_="product-tile")  # adjust this class based on actual HTML

    for tile in product_tiles:
        name_tag = tile.find("span", class_="product-title")
        price_tag = tile.find("span", class_="selling-price")

        if not name_tag or not price_tag:
            continue

        name = name_tag.text.strip()
        price = float(price_tag.text.strip().replace("KES", "").replace(",", "").strip())

        # Optional: assign to a default category
        category = session.query(Category).filter_by(name="Uncategorized").first()
        if not category:
            category = Category(name="Uncategorized")
            session.add(category)
            session.commit()

        # Get or create product
        product = session.query(Product).filter_by(name=name).first()
        if not product:
            product = Product(name=name, category_id=category.id)
            session.add(product)
            session.commit()

        # Add price record
        new_price = Price(
            product_id=product.id,
            retailer_id=retailer.id,
            price=price,
            timestamp=datetime.utcnow()
        )
        session.add(new_price)

    session.commit()
    session.close()
    print("Carrefour scraping complete and saved to DB.")
