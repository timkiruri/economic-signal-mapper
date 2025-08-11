from fastapi import APIRouter
from .retailers import router as retailers_router
from .products import router as products_router
from .forecast import router as forecast_router
from .prices import router as prices_router
from .categories import router as categories_router

router = APIRouter(prefix="/v1")

router.include_router(retailers_router)
router.include_router(products_router)
router.include_router(forecast_router)
router.include_router(prices_router)
router.include_router(categories_router)
