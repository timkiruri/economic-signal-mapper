# src/database/repositories/price_repository.py
from datetime import datetime
from sqlalchemy.orm import Session
from src.models.price import Price
from src.models.item import Item
from src.models.store import Store


def get_current_prices(item_name=None, region=None, store=None, db: Session = None):
    query =(
        db.query(Price)
        .join(Item, Price.item_id ==Item.id)
        .join(Store, Price.store_id ==Store.id)
    )

    if item_name:
        query = query.filter(Item.name.ilike(f"%{item_name}%"))
    if region:
        query = query.filter(Store.location.ilike(f"%{region}%"))
    if store:
        query = query.filter(Store.name.ilike(f"%{store}%"))

        query = query.order_by(Item.id, Price.timestamp.desc())

    # Picks latest price per (item, store)
    results = {}
    for row in query:
        key = (row.item_id, row.store_id)
        if key not in results:
            results[key] = row

    return [
        {
            "item_name": p.item.name,
            "category": p.item.category.name,
            "price": p.price,
            "currency": p.currency,
            "store": p.store.name,
            "region": p.store.location,
            "timestamp": p.timestamp,
            "source_url": p.source_url,
            "data_quality": p.data_quality
        }
        for p in results.values()
    ]

