from fastapi import APIRouter
from app.api.Models.Parser import DonghubParser
from app.api.Models.ApiResponseModels import BaseResponse

router = APIRouter()

@router.get("/filters", response_model=BaseResponse)
async def get_filters():
    async with DonghubParser() as parser:
        data = await parser.scrape_filters()
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": data
        }