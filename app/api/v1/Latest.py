from fastapi import APIRouter, Query
from app.api.Models.Parser import DonghubParser
from app.api.Models.ApiResponseModels import BaseResponse, ListResponse

router = APIRouter()

@router.get("/latest", response_model=BaseResponse)
async def get_latest(page: int = Query(1, ge=1)):
    async with DonghubParser() as parser:
        data = await parser.scrape_latest(page)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": data
        }