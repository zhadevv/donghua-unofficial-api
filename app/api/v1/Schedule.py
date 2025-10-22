from fastapi import APIRouter
from app.api.Models.Parser import DonghubParser
from app.api.Models.ApiResponseModels import BaseResponse, ScheduleResponse

router = APIRouter()

@router.get("/schedule", response_model=BaseResponse)
async def get_schedule():
    async with DonghubParser() as parser:
        data = await parser.scrape_schedule()
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": data
        }