from fastapi import FastAPI
from app.api.routes_items import router as items_router

app = FastAPI(title="AI Agents API")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(items_router)
