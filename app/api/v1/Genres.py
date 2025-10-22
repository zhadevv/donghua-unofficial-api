from fastapi import APIRouter, Query
from app.api.Models.Parser import DonghubParser
from app.api.Models.ApiResponseModels import BaseResponse, GenreResponse

router = APIRouter()

@router.get("/genres/{slug}", response_model=BaseResponse)
async def get_by_genre(slug: str, page: int = Query(1, ge=1)):
    async with DonghubParser() as parser:
        data = await parser.scrape_genres(slug, page)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": data
        }