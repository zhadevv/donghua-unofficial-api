from fastapi import APIRouter
from fastapi.responses import RedirectResponse, JSONResponse

web_router = APIRouter()

@web_router.get("/")
async def root_redirect():
    """Redirect root to /docs"""
    return RedirectResponse(url="/docs")

@web_router.get("/health")
async def health_check():
    """Simple health check endpoint"""
    return JSONResponse(
        content={
            "status": 200,
            "success": True,
            "author": "zhadev",
            "message": "Donghua Unofficial API is running!",
            "docs": "/docs",
            "redoc": "/redoc"
        }
    )

@web_router.get("/info")
async def api_info():
    """API information endpoint"""
    return JSONResponse(
        content={
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": {
                "name": "Donghua Unofficial API - Python Edition",
                "version": "1.0.0",
                "description": "Unofficial REST API for Donghub.vip - Chinese Animation Streaming Platform",
                "endpoints": {
                    "home": "/api/v1/home",
                    "search": "/api/v1/search?s=query",
                    "schedule": "/api/v1/schedule",
                    "popular": "/api/v1/popular",
                    "latest": "/api/v1/latest", 
                    "ongoing": "/api/v1/ongoing",
                    "completed": "/api/v1/completed",
                    "genres": "/api/v1/genres/{slug}",
                    "detail": "/api/v1/detail/{slug}",
                    "episodes": "/api/v1/episodes/{slug}",
                    "stream": "/api/v1/stream/{slug}",
                    "download": "/api/v1/download/{slug}",
                    "filters": "/api/v1/filters",
                    "test": "/api/v1/test/all"
                },
                "documentation": {
                    "swagger_ui": "/docs",
                    "redoc": "/redoc"
                }
            }
        }
    )
