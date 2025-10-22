
from fastapi import APIRouter
from app.api.v1.Home import router as home_router
from app.api.v1.Search import router as search_router
from app.api.v1.Schedule import router as schedule_router
from app.api.v1.Popular import router as popular_router
from app.api.v1.Latest import router as latest_router
from app.api.v1.Ongoing import router as ongoing_router
from app.api.v1.Completed import router as completed_router
from app.api.v1.Genres import router as genres_router
from app.api.v1.Detail import router as detail_router
from app.api.v1.EpisodeLists import router as episodes_router
from app.api.v1.Stream import router as stream_router
from app.api.v1.Filters import router as filters_router
from app.api.v1.Test import router as test_router
from app.api.Health import router as health_router

api_router = APIRouter()

api_router.include_router(home_router, prefix="/v1", tags=["Home"])
api_router.include_router(search_router, prefix="/v1", tags=["Search"])
api_router.include_router(schedule_router, prefix="/v1", tags=["Schedule"])
api_router.include_router(popular_router, prefix="/v1", tags=["Popular"])
api_router.include_router(latest_router, prefix="/v1", tags=["Latest"])
api_router.include_router(ongoing_router, prefix="/v1", tags=["Ongoing"])
api_router.include_router(completed_router, prefix="/v1", tags=["Completed"])
api_router.include_router(genres_router, prefix="/v1", tags=["Genres"])
api_router.include_router(detail_router, prefix="/v1", tags=["Detail"])
api_router.include_router(episodes_router, prefix="/v1", tags=["Episodes"])
api_router.include_router(stream_router, prefix="/v1", tags=["Stream"])
api_router.include_router(filters_router, prefix="/v1", tags=["Filters"])
api_router.include_router(test_router, prefix="/v1", tags=["Testing"])
api_router.include_router(health_router, prefix="", tags=["Health"])