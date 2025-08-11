def get_current_prices(item_name=None, region=None, store=None):
    return [
        {
            "item_name": "Maize Flour",
            "price": 123.45,
            "currency": "KES",
            "store": "Naivas",
            "region": "Nairobi",
            "timestamp": "2025-07-29T12:00:00Z",
            "source_url": "https://mock-store.com/item",
            "data_quality": 0.99
        }
    ]

def get_historical_prices(item_name=None, start_date=None, end_date=None):
    return [
        {
            "item_name": "Maize Flour",
            "price": 170.0,
            "currency": "KES",
            "store": "Naivas",
            "region": "Nairobi",
            "timestamp": "2025-07-10T08:00:00Z",
            "source_url": "https://naivas.online/item/maize-flour",
            "data_quality": 0.92
        },
        {
            "item_name": "Maize Flour",
            "price": 180.0,
            "currency": "KES",
            "store": "Naivas",
            "region": "Nairobi",
            "timestamp": "2025-07-28T08:00:00Z",
            "source_url": "https://naivas.online/item/maize-flour",
            "data_quality": 0.95
        }
    ]