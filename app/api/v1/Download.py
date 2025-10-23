from fastapi import APIRouter, Query
from app.api.Models.Parser import DonghubParser
from app.api.Models.ApiResponseModels import BaseResponse

router = APIRouter()

@router.get("/download/{slug}", response_model=BaseResponse)
async def get_download_links(
    slug: str, 
    episode: int = Query(None, ge=1)
):
    async with DonghubParser() as parser:
        data = await parser.scrape_download_links(slug, episode)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": data
        }
