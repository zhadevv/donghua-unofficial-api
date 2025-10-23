from fastapi import APIRouter, Query
from app.api.Models.Parser import DonghubParser
from app.api.Models.ApiResponseModels import BaseResponse, ListResponse
from app.api.Health import request_counters

router = APIRouter()

@router.get("/completed", response_model=BaseResponse)
async def get_completed(page: int = Query(1, ge=1)):
    request_counters["completed"] += 1
    
    async with DonghubParser() as parser:
        data = await parser.scrape_completed(page)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": data
        }
