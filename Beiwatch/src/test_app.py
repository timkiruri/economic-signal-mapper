from src.database.database import SessionLocal
from src.database.models.alert import Alert
from src.database.models.item import Item
from src.database.models.store import Store
from datetime import datetime

db = SessionLocal()

# Get existing item and store IDs (or create them if missing)
item = db.query(Item).filter(Item.name == "Milk").first()
store = db.query(Store).filter(Store.name == "Naivas").first()

if item and store:
    alert = Alert(
        item_id=item.id,
        store_id=store.id,
        price_change=25.0,
        direction="increase",
        threshold=15.0,
        timestamp=datetime.utcnow(),
        description="Milk price increased by 25 KES at Naivas."
    )
    db.add(alert)
    db.commit()

db.close()
