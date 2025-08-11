from fastapi import FastAPI
from src.api.routes.v1.prices import router as prices_router 
from src.api.routes.v1.products import router as products_router
from src.api.routes.v1.categories import router as categories_router
from src.api.routes.v1.retailers import router as retailers_router
from src.api.routes.v1.forecast import router as forecast_router

app = FastAPI()

app.include_router(prices_router, prefix="/api/v1/prices", tags=["Prices"])
app.include_router(products_router, prefix="/api/v1/products", tags=["Products"])
app.include_router(categories_router, prefix="/api/v1/categories", tags=["Categories"])
app.include_router(retailers_router, prefix="/api/v1/retailers", tags=["Retailers"])
app.include_router(forecast_router)





