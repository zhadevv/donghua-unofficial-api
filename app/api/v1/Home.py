from fastapi import APIRouter, Query
from app.api.Models.Parser import DonghubParser
from app.api.Models.ApiResponseModels import BaseResponse, HomeResponse

router = APIRouter()

@router.get("/home", response_model=BaseResponse)
async def get_home(page: int = Query(1, ge=1)):
    async with DonghubParser() as parser:
        data = await parser.scrape_homepage(page)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": data
        }