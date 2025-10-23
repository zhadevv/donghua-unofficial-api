from fastapi import APIRouter, Request
from app.api.Models.ApiResponseModels import BaseResponse

router = APIRouter()
request_counters = {
    "home": 0,
    "search": 0,
    "schedule": 0,
    "popular": 0,
    "latest": 0,
    "ongoing": 0,
    "completed": 0,
    "genres": 0,
    "detail": 0,
    "episodes": 0,
    "stream": 0,
    "download": 0,
    "filters": 0,
    "test": 0,
    "status": 0
}

@router.get("/status", response_model=BaseResponse)
async def get_status(request: Request):
    global request_counters
    request_counters["status"] += 1
    
    total_requests = sum(request_counters.values())
    
    return {
        "status": 200,
        "success": True,
        "author": "zhadev",
        "data": {
            "message": "Donghua Unofficial API Status",
            "api_status": "operational",
            "total_requests": total_requests,
            "endpoint_stats": {
                "home": request_counters["home"],
                "search": request_counters["search"],
                "schedule": request_counters["schedule"],
                "popular": request_counters["popular"],
                "latest": request_counters["latest"],
                "ongoing": request_counters["ongoing"],
                "completed": request_counters["completed"],
                "genres": request_counters["genres"],
                "detail": request_counters["detail"],
                "episodes": request_counters["episodes"],
                "stream": request_counters["stream"],
                "download": request_counters["download"],
                "filters": request_counters["filters"],
                "test": request_counters["test"],
                "status": request_counters["status"]
            },
            "uptime": "Running",
            "version": "1.0.0"
        }
    }
