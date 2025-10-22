from fastapi import APIRouter, Request
from app.api.Models.ApiResponseModels import BaseResponse

router = APIRouter()

request_count = 0

@router.get("/health", response_model=BaseResponse)
async def health_check(request: Request):
    global request_count
    request_count += 1
    
    return {
        "status": 200,
        "success": True,
        "author": "zhadev",
        "data": {
            "message": "API is healthy",
            "total_requests": request_count,
            "status": "operational"
        }
    }

@router.get("/stats", response_model=BaseResponse)
async def get_stats():
    return {
        "status": 200,
        "success": True,
        "author": "zhadev",
        "data": {
            "total_requests": request_count,
            "endpoints": [
                "/api/home",
                "/api/search",
                "/api/schedule", 
                "/api/popular",
                "/api/latest",
                "/api/ongoing",
                "/api/completed",
                "/api/genres/{slug}",
                "/api/detail/{slug}",
                "/api/episodes/{slug}",
                "/api/stream/{slug}",
                "/api/filters"
            ]
        }
    }