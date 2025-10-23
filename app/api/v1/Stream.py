from fastapi import APIRouter, Query
from app.api.Models.Parser import DonghubParser
from app.api.Models.ApiResponseModels import BaseResponse, StreamResponse
from app.api.Health import request_counters

router = APIRouter()

@router.get("/stream/{slug}", response_model=BaseResponse)
async def get_stream(
    slug: str, 
    episode: int = Query(None, ge=1),
    server_id: int = Query(None)
):
    request_counters["stream"] += 1
    
    async with DonghubParser() as parser:
        data = await parser.scrape_stream(slug, episode, server_id)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": data
        }
