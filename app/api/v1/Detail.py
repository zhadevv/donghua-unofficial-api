from fastapi import APIRouter
from app.api.Models.Parser import DonghubParser
from app.api.Models.ApiResponseModels import BaseResponse, DetailResponse
from app.api.Health import request_counters

router = APIRouter()

@router.get("/detail/{slug}", response_model=BaseResponse)
async def get_detail(slug: str):
    request_counters["detail"] += 1
    
    async with DonghubParser() as parser:
        data = await parser.scrape_detail(slug)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": data
        }
