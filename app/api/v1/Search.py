from fastapi import APIRouter, Query
from app.api.Models.Parser import DonghubParser
from app.api.Models.ApiResponseModels import BaseResponse, SearchResponse

router = APIRouter()

@router.get("/search", response_model=BaseResponse)
async def search_donghua(s: str = Query(..., min_length=1), page: int = Query(1, ge=1)):
    async with DonghubParser() as parser:
        data = await parser.scrape_search(s, page)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": data
        }