from fastapi import APIRouter
from app.api.Models.Parser import DonghubParser
from app.api.Models.ApiResponseModels import BaseResponse, EpisodeListResponse
from app.api.Health import request_counters

router = APIRouter()

@router.get("/episodes/{slug}", response_model=BaseResponse)
async def get_episodes(slug: str):
    request_counters["episodes"] += 1
    
    async with DonghubParser() as parser:
        data = await parser.scrape_episodes(slug)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": data
        }
