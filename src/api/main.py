from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # controls which domains are allowed to talk to your backend API
from src.api.routes.v1 import prices
from src.api.routes.v1 import alert

app = FastAPI(
    title="Economic Signal Mapper API",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ["http://localhost:3000"] for frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(prices.router)
app.include_router(alert.router)

@app.get("/")
def read_root():
    return {"message": "Economic Signal Mapper API is running!"}

