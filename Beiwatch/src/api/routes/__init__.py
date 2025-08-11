from fastapi import APIRouter
from .v1 import (
    retailers_router,
    products_router,
    forecast_router,
    prices_router,
)

router = APIRouter(prefix="/v1")

router.include_router(retailers_router)
router.include_router(products_router)
router.include_router(forecast_router)
router.include_router(prices_router)
