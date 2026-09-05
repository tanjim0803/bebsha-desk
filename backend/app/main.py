from fastapi import FastAPI
from app.api.routes import routers

version = "1.0.0"

app = FastAPI(
    title="BebshaDesk API",
    summary="An Multi-tenant Saas business solution system.",
    version=version,
)


@app.get("/")
async def root():
    return {"message": "This is BebshaDesk App"}


app.include_router(routers)
