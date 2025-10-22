from fastapi import FastAPI
from app.api.Router import api_router
from app.web.index import web_router

app = FastAPI(
    title="Donghua Unofficial API",
    description="Unofficial API for Donghub.vip - Chinese Animation Streaming",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(api_router, prefix="/api")
app.include_router(web_router, prefix="")

@app.get("/")
async def root():
    return {
        "status": 200,
        "success": True,
        "author": "zhadev",
        "message": "Donghua Unofficial API is running!",
        "docs": "/docs"
    }