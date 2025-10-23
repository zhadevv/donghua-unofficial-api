from fastapi import APIRouter, Query
from app.api.Models.Parser import DonghubParser
from app.api.Models.ApiResponseModels import BaseResponse, ListResponse
from app.api.Health import request_counters

router = APIRouter()

@router.get("/popular", response_model=BaseResponse)
async def get_popular(page: int = Query(1, ge=1)):
    request_counters["popular"] += 1
    
    async with DonghubParser() as parser:
        data = await parser.scrape_popular(page)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": data
        }
