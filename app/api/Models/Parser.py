# ==============================================================================
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Copyright (C) 2025 zhadev
# ==============================================================================
#                               ______________
#                         ,===:'.,            `-._
#                               `:.`---.__         `-._
#                                 `:.     `--.         `.
#                                   \.        `.         `.
#                           (,,(,    \.         `.   ____,-`.,
#                        (,'     `/   \.   ,--.___`.'
#                    ,  ,'  ,--.  `,   \.;'         `
#                     `{D, {    \  :    \;
#                       V,,'    /  /    //
#                       j;;    /  ,' ,-//.    ,---.      ,
#                       \;'   /  ,' /  _  \  /  _  \   ,'/
#                             \   `'  / \  `'  / \  `.' /
#                              `.___,'   `.__,'   `.__,'
#
#                                 Feed me Stars ⭐️
# ==============================================================================
#
# Links:
# - https://github.com/zhadevv
# - https://github.com/zhadevv/donghua-unofficial-api
#
# ==============================================================================

import httpx
import asyncio
from bs4 import BeautifulSoup
import re
from typing import Dict, List, Any, Optional
from urllib.parse import urljoin, quote
import base64

class DonghubParser:
    def __init__(self):
        self.base_url = "https://donghub.vip"
        self.client = None
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Referer": "https://donghub.vip",
            "Origin": "https://donghub.vip"
        }
        
    async def __aenter__(self):
        self.client = httpx.AsyncClient(
            headers=self.headers, 
            timeout=30.0,
            follow_redirects=True
        )
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            await self.client.aclose()
            
    async def get_soup(self, url: str) -> BeautifulSoup:
        if not self.client:
            self.client = httpx.AsyncClient(
                headers=self.headers, 
                timeout=30.0,
                follow_redirects=True
            )
            
        if not url.endswith('/') and not url.endswith('?') and '?' not in url:
            url += '/'
            
        response = await self.client.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    
    def extract_text(self, element, selector: str) -> str:
        if element:
            selected = element.select_one(selector)
            return selected.get_text(strip=True) if selected else ""
        return ""
    
    def extract_attribute(self, element, selector: str, attribute: str) -> str:
        if element:
            selected = element.select_one(selector)
            return selected.get(attribute) if selected else ""
        return ""
    
    def extract_list(self, element, selector: str) -> List[str]:
        if element:
            selected = element.select(selector)
            return [elem.get_text(strip=True) for elem in selected]
        return []
    
    async def scrape_homepage(self, page: int = 1) -> Dict[str, Any]:
        url = f"{self.base_url}/page/{page}/" if page > 1 else self.base_url
        soup = await self.get_soup(url)
        
        result = {
            "popular_today": [],
            "latest_releases": [],
            "recommendation": [],
            "popular_series": [],
            "new_movie": [],
            "genres": []
        }
        
        popular_container = soup.select_one(".listupd.popularslider")
        if popular_container:
            for item in popular_container.select(".bs .bsx"):
                result["popular_today"].append({
                    "title": self.extract_text(item, ".tt"),
                    "slug": self.extract_attribute(item, "a", "href").replace(self.base_url, "").strip("/"),
                    "thumbnail": self.extract_attribute(item, ".limit img", "src"),
                    "current_episode": self.extract_text(item, ".epx"),
                    "type": self.extract_text(item, ".typez"),
                    "sub_badge": self.extract_text(item, ".sb.Sub"),
                    "donghub_url": self.extract_attribute(item, "a", "href")
                })
        
        latest_container = soup.select_one(".listupd.normal")
        if latest_container:
            for item in latest_container.select(".bs.styleegg .bsx"):
                result["latest_releases"].append({
                    "title": self.extract_text(item, ".tt"),
                    "slug": self.extract_attribute(item, "a", "href").replace(self.base_url, "").strip("/"),
                    "thumbnail": self.extract_attribute(item, ".limit img", "src"),
                    "current_episode": self.extract_text(item, ".eggepisode"),
                    "type": self.extract_text(item, ".eggtype"),
                    "sub_badge": self.extract_text(item, ".sb.Sub"),
                    "donghub_url": self.extract_attribute(item, "a", "href")
                })
        
        rec_container = soup.select_one(".series-gen")
        if rec_container:
            tabs = rec_container.select(".nav-tabs li")
            tab_panes = rec_container.select(".tab-pane")
            
            for i, pane in enumerate(tab_panes):
                if i < len(tabs):
                    genre = self.extract_text(tabs[i], "a")
                    for item in pane.select(".bs .bsx"):
                        result["recommendation"].append({
                            "genre": genre,
                            "title": self.extract_text(item, ".tt"),
                            "slug": self.extract_attribute(item, "a", "href").replace(self.base_url, "").strip("/"),
                            "thumbnail": self.extract_attribute(item, ".limit img", "src"),
                            "current_episode": self.extract_text(item, ".epx"),
                            "type": self.extract_text(item, ".typez"),
                            "status": self.extract_text(item, ".status"),
                            "sub_badge": self.extract_text(item, ".sb.Sub"),
                            "donghub_url": self.extract_attribute(item, "a", "href")
                        })
        
        pop_series_container = soup.select_one("#wpop-items")
        if pop_series_container:
            for item in pop_series_container.select(".serieslist.pop ul li"):
                result["popular_series"].append({
                    "time": "weekly",
                    "title": self.extract_text(item, "h4 a"),
                    "slug": self.extract_attribute(item, "h4 a", "href").replace(self.base_url, "").strip("/"),
                    "thumbnail": self.extract_attribute(item, ".imgseries img", "src"),
                    "donghub_url": self.extract_attribute(item, "h4 a", "href")
                })
        
        movie_container = soup.select(".serieslist")
        for container in movie_container:
            if container.select("ul li"):
                for item in container.select("ul li"):
                    if "Movie" in self.extract_text(item, ".leftseries span:first-child") or "movie" in self.extract_text(item, "h4 a").lower():
                        result["new_movie"].append({
                            "title": self.extract_text(item, "h4 a"),
                            "slug": self.extract_attribute(item, "h4 a", "href").replace(self.base_url, "").strip("/"),
                            "thumbnail": self.extract_attribute(item, ".imgseries img", "src"),
                            "type": "Movie",
                            "genres": self.extract_text(item, ".leftseries span:first-child"),
                            "date": self.extract_text(item, ".leftseries span:last-child"),
                            "donghub_url": self.extract_attribute(item, "h4 a", "href")
                        })
        
        genre_container = soup.select_one("ul.genre")
        if genre_container:
            for item in genre_container.select("li"):
                result["genres"].append({
                    "name": self.extract_text(item, "a"),
                    "slug": self.extract_attribute(item, "a", "href").replace(f"{self.base_url}/genres/", "").strip("/"),
                    "donghub_url": self.extract_attribute(item, "a", "href")
                })
        
        return result
    
    async def scrape_search(self, query: str, page: int = 1) -> Dict[str, Any]:
        url = f"{self.base_url}/page/{page}/?s={quote(query)}" if page > 1 else f"{self.base_url}/?s={quote(query)}"
        soup = await self.get_soup(url)
        
        result = {"results": [], "pagination": {}}
        
        container = soup.select_one(".listupd")
        if container:
            for item in container.select(".bs .bsx"):
                result["results"].append({
                    "title": self.extract_text(item, ".tt h2"),
                    "slug": self.extract_attribute(item, "a", "href").replace(self.base_url, "").strip("/"),
                    "thumbnail": self.extract_attribute(item, ".limit img", "src"),
                    "type": self.extract_text(item, ".typez"),
                    "current_episode": self.extract_text(item, ".epx"),
                    "sub_badge": self.extract_text(item, ".sb.Sub"),
                    "donghub_url": self.extract_attribute(item, "a", "href")
                })
        
        pagination = soup.select_one(".pagination")
        if pagination:
            current_page = pagination.select_one(".page-numbers.current")
            if current_page:
                result["pagination"]["current_page"] = current_page.get_text(strip=True)
            
            next_page = pagination.select_one(".next.page-numbers")
            if next_page:
                result["pagination"]["next_page"] = next_page.get("href")
            
            pages = pagination.select(".page-numbers")
            result["pagination"]["pages"] = [page.get_text(strip=True) for page in pages]
        
        return result
    
    async def scrape_schedule(self) -> Dict[str, Any]:
        url = f"{self.base_url}/schedule/"
        soup = await self.get_soup(url)
        
        result = {}
        days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        
        for day in days:
            day_class = f".sch_{day.lower()}"
            container = soup.select_one(f".bixbox.schedulepage{day_class}")
            result[day] = []
            
            if container:
                for item in container.select(".listupd .bs .bsx"):
                    result[day].append({
                        "title": self.extract_text(item, ".tt"),
                        "slug": self.extract_attribute(item, "a", "href").replace(self.base_url, "").strip("/"),
                        "thumbnail": self.extract_attribute(item, ".limit img", "src"),
                        "countdown": self.extract_attribute(item, ".epx.cndwn", "data-cndwn"),
                        "release_time": self.extract_attribute(item, ".epx.cndwn", "data-rlsdt"),
                        "current_episode": self.extract_text(item, ".sb.Sub"),
                        "type": self.extract_text(item, ".typez"),
                        "donghub_url": self.extract_attribute(item, "a", "href")
                    })
        
        return result
    
    async def scrape_popular(self, page: int = 1) -> Dict[str, Any]:
        url = f"{self.base_url}/anime/page/{page}/?status=&sub=&order=popular" if page > 1 else f"{self.base_url}/anime/?status=&sub=&order=popular"
        soup = await self.get_soup(url)
        
        result = {"results": [], "pagination": {}}
        
        container = soup.select_one(".listupd")
        if container:
            for item in container.select(".bs .bsx"):
                result["results"].append({
                    "title": self.extract_text(item, ".tt h2"),
                    "slug": self.extract_attribute(item, "a", "href").replace(self.base_url, "").strip("/"),
                    "thumbnail": self.extract_attribute(item, ".limit img", "src"),
                    "type": self.extract_text(item, ".typez"),
                    "current_episode": self.extract_text(item, ".epx"),
                    "sub_badge": self.extract_text(item, ".sb.Sub"),
                    "donghub_url": self.extract_attribute(item, "a", "href")
                })
        
        pagination = soup.select_one(".hpage")
        if pagination:
            next_page = pagination.select_one(".r")
            if next_page:
                result["pagination"]["next_page"] = next_page.get("href")
        
        return result
    
    async def scrape_latest(self, page: int = 1) -> Dict[str, Any]:
        url = f"{self.base_url}/anime/page/{page}/?type=&order=latest" if page > 1 else f"{self.base_url}/anime/?type=&order=latest"
        soup = await self.get_soup(url)
        
        result = {"results": [], "pagination": {}}
        
        container = soup.select_one(".listupd")
        if container:
            for item in container.select(".bs .bsx"):
                result["results"].append({
                    "title": self.extract_text(item, ".tt h2"),
                    "slug": self.extract_attribute(item, "a", "href").replace(self.base_url, "").strip("/"),
                    "thumbnail": self.extract_attribute(item, ".limit img", "src"),
                    "type": self.extract_text(item, ".typez"),
                    "current_episode": self.extract_text(item, ".epx"),
                    "sub_badge": self.extract_text(item, ".sb.Sub"),
                    "donghub_url": self.extract_attribute(item, "a", "href")
                })
        
        pagination = soup.select_one(".hpage")
        if pagination:
            next_page = pagination.select_one(".r")
            if next_page:
                result["pagination"]["next_page"] = next_page.get("href")
        
        return result
    
    async def scrape_ongoing(self, page: int = 1) -> Dict[str, Any]:
        url = f"{self.base_url}/anime/page/{page}/?status=ongoing&sub=&order=/" if page > 1 else f"{self.base_url}/anime/?status=ongoing&sub=&order=/"
        soup = await self.get_soup(url)
        
        result = {"results": [], "pagination": {}}
        
        container = soup.select_one(".listupd")
        if container:
            for item in container.select(".bs .bsx"):
                result["results"].append({
                    "title": self.extract_text(item, ".tt h2"),
                    "slug": self.extract_attribute(item, "a", "href").replace(self.base_url, "").strip("/"),
                    "thumbnail": self.extract_attribute(item, ".limit img", "src"),
                    "type": self.extract_text(item, ".typez"),
                    "current_episode": self.extract_text(item, ".epx"),
                    "sub_badge": self.extract_text(item, ".sb.Sub"),
                    "donghub_url": self.extract_attribute(item, "a", "href")
                })
        
        pagination = soup.select_one(".hpage")
        if pagination:
            next_page = pagination.select_one(".r")
            if next_page:
                result["pagination"]["next_page"] = next_page.get("href")
        
        return result
    
    async def scrape_completed(self, page: int = 1) -> Dict[str, Any]:
        url = f"{self.base_url}/anime/page/{page}/?status=completed&sub=&order=/" if page > 1 else f"{self.base_url}/anime/?status=completed&sub=&order=/"
        soup = await self.get_soup(url)
        
        result = {"results": [], "pagination": {}}
        
        container = soup.select_one(".listupd")
        if container:
            for item in container.select(".bs .bsx"):
                result["results"].append({
                    "title": self.extract_text(item, ".tt h2"),
                    "slug": self.extract_attribute(item, "a", "href").replace(self.base_url, "").strip("/"),
                    "thumbnail": self.extract_attribute(item, ".limit img", "src"),
                    "type": self.extract_text(item, ".typez"),
                    "current_episode": self.extract_text(item, ".epx"),
                    "sub_badge": self.extract_text(item, ".sb.Sub"),
                    "donghub_url": self.extract_attribute(item, "a", "href")
                })
        
        pagination = soup.select_one(".hpage")
        if pagination:
            next_page = pagination.select_one(".r")
            if next_page:
                result["pagination"]["next_page"] = next_page.get("href")
        
        return result
    
    async def scrape_genres(self, slug: str, page: int = 1) -> Dict[str, Any]:
        url = f"{self.base_url}/genres/{slug}/page/{page}/" if page > 1 else f"{self.base_url}/genres/{slug}/"
        soup = await self.get_soup(url)
        
        result = {"results": [], "pagination": {}, "genre_title": ""}
        
        genre_title = soup.select_one(".releases h1 span")
        if genre_title:
            result["genre_title"] = genre_title.get_text(strip=True)
        
        container = soup.select_one(".listupd")
        if container:
            for item in container.select(".bs .bsx"):
                result["results"].append({
                    "title": self.extract_text(item, ".tt h2"),
                    "slug": self.extract_attribute(item, "a", "href").replace(self.base_url, "").strip("/"),
                    "thumbnail": self.extract_attribute(item, ".limit img", "src"),
                    "type": self.extract_text(item, ".typez"),
                    "current_episode": self.extract_text(item, ".epx"),
                    "sub_badge": self.extract_text(item, ".sb.Sub"),
                    "donghub_url": self.extract_attribute(item, "a", "href")
                })
        
        pagination = soup.select_one(".pagination")
        if pagination:
            current_page = pagination.select_one(".page-numbers.current")
            if current_page:
                result["pagination"]["current_page"] = current_page.get_text(strip=True)
            
            next_page = pagination.select_one(".next.page-numbers")
            if next_page:
                result["pagination"]["next_page"] = next_page.get("href")
            
            pages = pagination.select(".page-numbers")
            result["pagination"]["pages"] = [page.get_text(strip=True) for page in pages]
        
        return result
    
    async def scrape_detail(self, slug: str) -> Dict[str, Any]:
        if not slug.endswith('/'):
            slug += '/'
            
        url = f"{self.base_url}/{slug}"
        soup = await self.get_soup(url)
        
        result = {}
        
        container = soup.select_one(".animefull")
        if not container:
            return {"error": "Detail page not found or invalid structure"}
        
        result["banner"] = self.extract_attribute(container, ".bigcover img", "src")
        result["thumbnail"] = self.extract_attribute(container, ".thumb img", "src")
        result["title"] = self.extract_text(container, ".entry-title")
        result["alter_title"] = self.extract_text(container, ".alter")
        result["bookmark_count"] = self.extract_text(container, ".bmc")
        
        synopsis_container = soup.select_one(".bixbox.synp .entry-content")
        if synopsis_container:
            result["synopsis"] = synopsis_container.get_text(strip=True)
        else:
            result["synopsis"] = ""
        
        info_data = {}
        
        info_elements = container.select(".spe span")
        for element in info_elements:
            text = element.get_text(strip=True)
            if 'Status' in text:
                info_data["status"] = text.replace('Status:', '').strip()
            elif 'Network' in text:
                info_data["network"] = text.replace('Network:', '').strip()
            elif 'Studio' in text:
                info_data["studio"] = text.replace('Studio:', '').strip()
            elif 'Released' in text:
                info_data["released"] = text.replace('Released:', '').strip()
            elif 'Duration' in text:
                info_data["duration"] = text.replace('Duration:', '').strip()
            elif 'Season' in text:
                info_data["season"] = text.replace('Season:', '').strip()
            elif 'Country' in text:
                info_data["country"] = text.replace('Country:', '').strip()
            elif 'Type' in text:
                info_data["type"] = text.replace('Type:', '').strip()
            elif 'Episodes' in text:
                info_data["episodes"] = text.replace('Episodes:', '').strip()
        
        result["info"] = info_data
        
        genres_container = container.select_one(".genxed")
        if genres_container:
            result["genres"] = [a.get_text(strip=True) for a in genres_container.select("a")]
        else:
            result["genres"] = []
        
        episode_nav = {}
        first_ep = container.select_one(".inepcx:first-child")
        if first_ep:
            episode_nav["first_episode"] = {
                "number": self.extract_text(first_ep, ".epcur.epcurfirst"),
                "url": self.extract_attribute(first_ep, "a", "href")
            }
        
        new_ep = container.select_one(".inepcx:last-child")
        if new_ep:
            episode_nav["new_episode"] = {
                "number": self.extract_text(new_ep, ".epcur.epcurlast"),
                "url": self.extract_attribute(new_ep, "a", "href")
            }
        
        result["episode_nav"] = episode_nav
        
        episodes_container = container.select_one(".eplister ul")
        if episodes_container:
            result["episodes"] = []
            for item in episodes_container.select("li"):
                result["episodes"].append({
                    "number": self.extract_text(item, ".epl-num"),
                    "title": self.extract_text(item, ".epl-title"),
                    "subtitle": self.extract_text(item, ".epl-sub .status"),
                    "date": self.extract_text(item, ".epl-date"),
                    "url": self.extract_attribute(item, "a", "href")
                })
        else:
            result["episodes"] = []
        
        tags_container = container.select_one(".bottom.tags")
        if tags_container:
            result["tags"] = [a.get_text(strip=True) for a in tags_container.select("a")]
        else:
            result["tags"] = []
        
        return result
    
    async def scrape_stream(self, slug: str, episode: Optional[int] = None, server_id: Optional[int] = None) -> Dict[str, Any]:
        if episode:
            if not slug.endswith('-subtitle-indonesia'):
                slug = f"{slug}-episode-{episode}-subtitle-indonesia"
                
        if not slug.endswith('/'):
            slug += '/'
            
        url = f"{self.base_url}/{slug}"
        
        if server_id:
            soup = await self.get_soup(url)
            
            servers_container = soup.select_one("select.mirror")
            if servers_container:
                server_options = servers_container.select("option[value!='']")
                for option in server_options:
                    data_index = option.get("data-index")
                    if data_index and int(data_index) == server_id:
                        embed_data = option.get("value")
                        if embed_data:
                            try:
                                decoded_data = base64.b64decode(embed_data).decode('utf-8')
                                return {"embed_url": decoded_data}
                            except:
                                return {"embed_url": embed_data}
            
            return {"embed_url": ""}
        else:
            soup = await self.get_soup(url)
            
            result = {}
            
            result["title"] = self.extract_text(soup, ".entry-title")
            
            episode_meta = soup.select_one("meta[itemprop='episodeNumber']")
            if episode_meta:
                result["episode_number"] = episode_meta.get("content")
            else:
                title = result["title"] or ""
                episode_match = re.search(r'Episode\s*(\d+)', title, re.IGNORECASE)
                result["episode_number"] = episode_match.group(1) if episode_match else ""
            
            result["thumbnail"] = self.extract_attribute(soup, ".thumb img", "src")
            
            current_embed = soup.select_one("#pembed iframe")
            if current_embed:
                result["current_embed"] = current_embed.get("src")
            else:
                result["current_embed"] = ""
            
            servers_container = soup.select_one("select.mirror")
            if servers_container:
                result["servers"] = []
                for option in servers_container.select("option[value!='']"):
                    result["servers"].append({
                        "name": option.get_text(strip=True),
                        "embed_data": option.get("value"),
                        "data_index": option.get("data-index")
                    })
            else:
                result["servers"] = []
            
            navigation = {}
            prev_ep = soup.select_one(".naveps .nvs a[rel='prev']")
            if prev_ep:
                navigation["prev_episode"] = prev_ep.get("href")
            else:
                navigation["prev_episode"] = ""
            
            next_ep = soup.select_one(".naveps .nvs a[rel='next']")
            if next_ep:
                navigation["next_episode"] = next_ep.get("href")
            else:
                navigation["next_episode"] = ""
            
            all_eps = soup.select_one(".naveps .nvsc a")
            if all_eps:
                navigation["all_episodes"] = all_eps.get("href")
            else:
                navigation["all_episodes"] = ""
            
            result["navigation"] = navigation
            
            episode_list_container = soup.select_one("#singlepisode .episodelist ul")
            if episode_list_container:
                result["episode_list"] = []
                for item in episode_list_container.select("li"):
                    result["episode_list"].append({
                        "title": self.extract_text(item, ".playinfo h3"),
                        "episode_number": self.extract_text(item, ".playinfo span"),
                        "url": self.extract_attribute(item, "a", "href"),
                        "thumbnail": self.extract_attribute(item, ".thumbnel img", "src")
                    })
            else:
                result["episode_list"] = []
                
            series_info = {}
            series_info["title"] = self.extract_text(soup, ".infolimit h2") or result.get("title", "")
            
            info_elements = soup.select(".spe span")
            for element in info_elements:
                text = element.get_text(strip=True)
                if 'Status:' in text:
                    series_info["status"] = text.replace('Status:', '').strip()
                elif 'Type:' in text:
                    series_info["type"] = text.replace('Type:', '').strip()
                elif 'Episodes:' in text:
                    series_info["episodes"] = text.replace('Episodes:', '').strip()
            
            genres_elements = soup.select(".genxed a")
            if genres_elements:
                series_info["genres"] = [genre.get_text(strip=True) for genre in genres_elements]
            else:
                series_info["genres"] = []
            
            stream_synopsis = soup.select_one(".bixbox.synp .entry-content")
            if stream_synopsis:
                series_info["synopsis"] = stream_synopsis.get_text(strip=True)
            else:
                series_info["synopsis"] = ""
            
            rating_element = soup.select_one(".rating strong")
            series_info["rating"] = rating_element.get_text(strip=True) if rating_element else ""
            
            result["series_info"] = series_info
            
            return result
    
    async def scrape_episodes(self, slug: str) -> Dict[str, Any]:
        url = f"{self.base_url}/{slug}/"
        soup = await self.get_soup(url)
        
        result = {"episodes": []}
        
        first_ep_element = soup.select_one(".inepcx:first-child")
        new_ep_element = soup.select_one(".inepcx:last-child")
        
        if first_ep_element and new_ep_element:
            first_ep_number_text = self.extract_text(first_ep_element, ".epcurfirst")
            new_ep_number_text = self.extract_text(new_ep_element, ".epcurlast")
            
            try:
                first_num = int(''.join(filter(str.isdigit, first_ep_number_text)) or 1)
                new_num = int(''.join(filter(str.isdigit, new_ep_number_text)) or 1)
                
                base_slug = slug.rstrip('/')
                
                for ep_num in range(first_num, new_num + 1):
                    episode_slug = f"{base_slug}-episode-{ep_num}-subtitle-indonesia"
                    episode_url = f"{self.base_url}/{episode_slug}/"
                    
                    result["episodes"].append({
                        "episode_number": ep_num,
                        "slug": episode_slug,
                        "url": episode_url,
                        "donghub_url": episode_url
                    })
                        
            except ValueError:
                pass
        
        return result
    
    async def scrape_filters(self) -> Dict[str, Any]:
        url = f"{self.base_url}/anime/"
        soup = await self.get_soup(url)
        
        result = {}
        
        advanced_search = soup.select_one(".advancedsearch")
        if not advanced_search:
            return result
        
        genre_container = advanced_search.select_one(".filter.dropdown:has(button:contains('Genre'))")
        if genre_container:
            result["genres"] = []
            for input_elem in genre_container.select("input[name='genre[]']"):
                label = input_elem.find_next("label")
                if label:
                    result["genres"].append({
                        "value": input_elem.get("value"),
                        "label": label.get_text(strip=True)
                    })
        
        status_container = advanced_search.select_one(".filter.dropdown:has(button:contains('Status'))")
        if status_container:
            result["status"] = []
            for input_elem in status_container.select("input[name='status']"):
                label = input_elem.find_next("label")
                if label:
                    result["status"].append({
                        "value": input_elem.get("value"),
                        "label": label.get_text(strip=True)
                    })
        
        type_container = advanced_search.select_one(".filter.dropdown:has(button:contains('Type'))")
        if type_container:
            result["types"] = []
            for input_elem in type_container.select("input[name='type']"):
                label = input_elem.find_next("label")
                if label:
                    result["types"].append({
                        "value": input_elem.get("value"),
                        "label": label.get_text(strip=True)
                    })
        
        sub_container = advanced_search.select_one(".filter.dropdown:has(button:contains('Sub'))")
        if sub_container:
            result["subs"] = []
            for input_elem in sub_container.select("input[name='sub']"):
                label = input_elem.find_next("label")
                if label:
                    result["subs"].append({
                        "value": input_elem.get("value"),
                        "label": label.get_text(strip=True)
                    })
        
        order_container = advanced_search.select_one(".filter.dropdown:has(button:contains('Order by'))")
        if order_container:
            result["orders"] = []
            for input_elem in order_container.select("input[name='order']"):
                label = input_elem.find_next("label")
                if label:
                    result["orders"].append({
                        "value": input_elem.get("value"),
                        "label": label.get_text(strip=True)
                    })
        
        return result
