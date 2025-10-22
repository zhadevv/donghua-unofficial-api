from typing import Any, Dict, List, Optional
from pydantic import BaseModel

class BaseResponse(BaseModel):
    status: int = 200
    success: bool = True
    author: str = "zhadev"
    data: Optional[Any] = None

class HomeResponse(BaseModel):
    popular_today: List[Dict[str, str]]
    latest_releases: List[Dict[str, str]]
    recommendation: List[Dict[str, str]]
    popular_series: List[Dict[str, str]]
    new_movie: List[Dict[str, str]]
    genres: List[Dict[str, str]]

class SearchResponse(BaseModel):
    results: List[Dict[str, str]]
    pagination: Optional[Dict[str, Any]]

class ScheduleResponse(BaseModel):
    Friday: List[Dict[str, str]]
    Saturday: List[Dict[str, str]]
    Sunday: List[Dict[str, str]]
    Monday: List[Dict[str, str]]
    Tuesday: List[Dict[str, str]]
    Wednesday: List[Dict[str, str]]
    Thursday: List[Dict[str, str]]

class ListResponse(BaseModel):
    results: List[Dict[str, str]]
    pagination: Optional[Dict[str, Any]]

class GenreResponse(BaseModel):
    results: List[Dict[str, str]]
    pagination: Optional[Dict[str, Any]]
    genre_title: str

class DetailResponse(BaseModel):
    banner: Optional[str]
    thumbnail: Optional[str]
    title: Optional[str]
    alter_title: Optional[str]
    rating: Optional[str]
    rating_value: Optional[str]
    bookmark_count: Optional[str]
    synopsis: Optional[str]
    short_description: Optional[str]
    info: Optional[Dict[str, str]]
    genres: Optional[List[str]]
    episode_nav: Optional[Dict[str, Any]]
    episodes: Optional[List[Dict[str, str]]]
    tags: Optional[List[str]]

class StreamResponse(BaseModel):
    title: Optional[str]
    series_name: Optional[str]
    episode_number: Optional[str]
    thumbnail: Optional[str]
    current_embed: Optional[str]
    servers: Optional[List[Dict[str, str]]]
    navigation: Optional[Dict[str, str]]
    episode_list: Optional[List[Dict[str, str]]]

class EpisodeListResponse(BaseModel):
    episodes: List[Dict[str, Any]]

class FilterResponse(BaseModel):
    genres: Optional[List[Dict[str, str]]]
    status: Optional[List[Dict[str, str]]]
    types: Optional[List[Dict[str, str]]]
    subs: Optional[List[Dict[str, str]]]
    orders: Optional[List[Dict[str, str]]]