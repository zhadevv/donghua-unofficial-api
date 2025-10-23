from fastapi import APIRouter, Query
from app.api.Models.Parser import DonghubParser
from app.api.Models.ApiResponseModels import BaseResponse
import json
from app.api.Health import request_counters

router = APIRouter()

@router.get("/test/home", response_model=BaseResponse)
async def test_homepage(page: int = Query(1, ge=1)):
    request_counters["test"] += 1
    
    async with DonghubParser() as parser:
        data = await parser.scrape_homepage(page)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": {
                "test_type": "homepage",
                "page": page,
                "sections": {
                    "popular_today_count": len(data.get("popular_today", [])),
                    "latest_releases_count": len(data.get("latest_releases", [])),
                    "recommendation_count": len(data.get("recommendation", [])),
                    "popular_series_count": len(data.get("popular_series", [])),
                    "new_movie_count": len(data.get("new_movie", [])),
                    "genres_count": len(data.get("genres", []))
                },
                "sample_data": {
                    "popular_today_sample": data.get("popular_today", [])[:2] if data.get("popular_today") else [],
                    "latest_releases_sample": data.get("latest_releases", [])[:2] if data.get("latest_releases") else []
                }
            }
        }

@router.get("/test/search", response_model=BaseResponse)
async def test_search(query: str = Query("a"), page: int = Query(1, ge=1)):
    request_counters["test"] += 1
    
    async with DonghubParser() as parser:
        data = await parser.scrape_search(query, page)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": {
                "test_type": "search",
                "query": query,
                "page": page,
                "results_count": len(data.get("results", [])),
                "pagination_info": data.get("pagination", {}),
                "sample_results": data.get("results", [])[:3] if data.get("results") else []
            }
        }

@router.get("/test/schedule", response_model=BaseResponse)
async def test_schedule():
    request_counters["test"] += 1
    
    async with DonghubParser() as parser:
        data = await parser.scrape_schedule()
        
        day_counts = {}
        for day in ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]:
            day_counts[day] = len(data.get(day, []))
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": {
                "test_type": "schedule",
                "day_counts": day_counts,
                "total_releases": sum(day_counts.values()),
                "sample_data": {
                    day: data.get(day, [])[:2] for day in list(day_counts.keys())[:2]
                }
            }
        }

@router.get("/test/popular", response_model=BaseResponse)
async def test_popular(page: int = Query(1, ge=1)):
    request_counters["test"] += 1
    
    async with DonghubParser() as parser:
        data = await parser.scrape_popular(page)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": {
                "test_type": "popular",
                "page": page,
                "results_count": len(data.get("results", [])),
                "pagination_info": data.get("pagination", {}),
                "sample_results": data.get("results", [])[:3] if data.get("results") else []
            }
        }

@router.get("/test/latest", response_model=BaseResponse)
async def test_latest(page: int = Query(1, ge=1)):
    request_counters["test"] += 1
    
    async with DonghubParser() as parser:
        data = await parser.scrape_latest(page)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": {
                "test_type": "latest",
                "page": page,
                "results_count": len(data.get("results", [])),
                "pagination_info": data.get("pagination", {}),
                "sample_results": data.get("results", [])[:3] if data.get("results") else []
            }
        }

@router.get("/test/ongoing", response_model=BaseResponse)
async def test_ongoing(page: int = Query(1, ge=1)):
    request_counters["test"] += 1
    
    async with DonghubParser() as parser:
        data = await parser.scrape_ongoing(page)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": {
                "test_type": "ongoing",
                "page": page,
                "results_count": len(data.get("results", [])),
                "pagination_info": data.get("pagination", {}),
                "sample_results": data.get("results", [])[:3] if data.get("results") else []
            }
        }

@router.get("/test/completed", response_model=BaseResponse)
async def test_completed(page: int = Query(1, ge=1)):
    request_counters["test"] += 1
    
    async with DonghubParser() as parser:
        data = await parser.scrape_completed(page)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": {
                "test_type": "completed",
                "page": page,
                "results_count": len(data.get("results", [])),
                "pagination_info": data.get("pagination", {}),
                "sample_results": data.get("results", [])[:3] if data.get("results") else []
            }
        }

@router.get("/test/genres", response_model=BaseResponse)
async def test_genres(slug: str = Query("action"), page: int = Query(1, ge=1)):
    request_counters["test"] += 1
    
    async with DonghubParser() as parser:
        data = await parser.scrape_genres(slug, page)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": {
                "test_type": "genres",
                "slug": slug,
                "page": page,
                "genre_title": data.get("genre_title", ""),
                "results_count": len(data.get("results", [])),
                "pagination_info": data.get("pagination", {}),
                "sample_results": data.get("results", [])[:3] if data.get("results") else []
            }
        }

@router.get("/test/detail", response_model=BaseResponse)
async def test_detail(slug: str = Query("battle-through-the-heavens-season-5")):
    request_counters["test"] += 1
    
    async with DonghubParser() as parser:
        data = await parser.scrape_detail(slug)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": {
                "test_type": "detail",
                "slug": slug,
                "has_data": bool(data),
                "title": data.get("title"),
                "episodes_count": len(data.get("episodes", [])),
                "genres_count": len(data.get("genres", [])),
                "episode_nav": data.get("episode_nav", {}),
                "sample_episodes": data.get("episodes", [])[:3] if data.get("episodes") else []
            }
        }

@router.get("/test/episodes", response_model=BaseResponse)
async def test_episodes(slug: str = Query("renegade-immortal")):
    request_counters["test"] += 1
    
    async with DonghubParser() as parser:
        data = await parser.scrape_episodes(slug)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": {
                "test_type": "episodes",
                "slug": slug,
                "episodes_count": len(data.get("episodes", [])),
                "episodes_range": f"{data['episodes'][0]['episode_number']}-{data['episodes'][-1]['episode_number']}" if data.get('episodes') else "N/A",
                "sample_episodes": data.get("episodes", [])[:5] if data.get("episodes") else []
            }
        }

@router.get("/test/stream", response_model=BaseResponse)
async def test_stream(slug: str = Query("renegade-immortal-episode-100-subtitle-indonesia")):
    request_counters["test"] += 1
    
    async with DonghubParser() as parser:
        data = await parser.scrape_stream(slug)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": {
                "test_type": "stream",
                "slug": slug,
                "has_data": bool(data),
                "servers_count": len(data.get("servers", [])),
                "episode_list_count": len(data.get("episode_list", [])),
                "has_embed": bool(data.get("current_embed")),
                "navigation": data.get("navigation", {}),
                "sample_servers": data.get("servers", [])[:2] if data.get("servers") else []
            }
        }

@router.get("/test/stream-embed", response_model=BaseResponse)
async def test_stream_embed(slug: str = Query("renegade-immortal-episode-99-subtitle-indonesia"), server_id: int = Query(1)):
    request_counters["test"] += 1
    
    async with DonghubParser() as parser:
        data = await parser.scrape_stream(slug, server_id)
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": {
                "test_type": "stream_embed",
                "slug": slug,
                "server_id": server_id,
                "embed_url": data.get("embed_url", ""),
                "has_embed": bool(data.get("embed_url"))
            }
        }

@router.get("/test/filters", response_model=BaseResponse)
async def test_filters():
    request_counters["test"] += 1
    
    async with DonghubParser() as parser:
        data = await parser.scrape_filters()
        
        filter_counts = {}
        for key in ["genres", "status", "types", "subs", "orders"]:
            filter_counts[key] = len(data.get(key, []))
        
        return {
            "status": 200,
            "success": True,
            "author": "zhadev",
            "data": {
                "test_type": "filters",
                "filter_counts": filter_counts,
                "sample_genres": data.get("genres", [])[:5] if data.get("genres") else [],
                "sample_status": data.get("status", [])[:3] if data.get("status") else []
            }
        }

@router.get("/test/all", response_model=BaseResponse)
async def test_all_endpoints():
    test_results = {}
    
    async with DonghubParser() as parser:
        try:
            homepage = await parser.scrape_homepage(1)
            test_results["homepage"] = {
                "success": True,
                "sections": len([k for k in homepage.keys() if k != "error"]),
                "total_items": sum(len(v) for k, v in homepage.items() if isinstance(v, list))
            }
        except Exception as e:
            test_results["homepage"] = {"success": False, "error": str(e)}
        
        try:
            search = await parser.scrape_search("anime", 1)
            test_results["search"] = {
                "success": True,
                "results": len(search.get("results", [])),
                "has_pagination": bool(search.get("pagination", {}))
            }
        except Exception as e:
            test_results["search"] = {"success": False, "error": str(e)}
        
        try:
            schedule = await parser.scrape_schedule()
            test_results["schedule"] = {
                "success": True,
                "days": len(schedule),
                "total_releases": sum(len(releases) for releases in schedule.values())
            }
        except Exception as e:
            test_results["schedule"] = {"success": False, "error": str(e)}
        
        try:
            popular = await parser.scrape_popular(1)
            test_results["popular"] = {
                "success": True,
                "results": len(popular.get("results", [])),
                "has_pagination": bool(popular.get("pagination", {}))
            }
        except Exception as e:
            test_results["popular"] = {"success": False, "error": str(e)}
        
        try:
            latest = await parser.scrape_latest(1)
            test_results["latest"] = {
                "success": True,
                "results": len(latest.get("results", [])),
                "has_pagination": bool(latest.get("pagination", {}))
            }
        except Exception as e:
            test_results["latest"] = {"success": False, "error": str(e)}
        
        try:
            filters = await parser.scrape_filters()
            test_results["filters"] = {
                "success": True,
                "filter_categories": len(filters),
                "total_options": sum(len(options) for options in filters.values())
            }
        except Exception as e:
            test_results["filters"] = {"success": False, "error": str(e)}
    
    total_tests = len(test_results)
    passed_tests = sum(1 for result in test_results.values() if result.get("success"))
    
    return {
        "status": 200,
        "success": True,
        "author": "zhadev",
        "data": {
            "test_type": "comprehensive_test",
            "summary": {
                "total_tests": total_tests,
                "passed_tests": passed_tests,
                "failed_tests": total_tests - passed_tests,
                "success_rate": f"{(passed_tests/total_tests)*100:.1f}%"
            },
            "detailed_results": test_results
        }
    }
