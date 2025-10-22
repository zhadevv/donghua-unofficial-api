<div align="center">

<a href="https://ibb.co.com/Kxy1vMZF"><img src="https://i.ibb.co.com/hF8qzP5D/Proyek-Baru-58-958-F661.png" alt="Donghua Unofficial Api" border="0" width="600"></a>

### **Donghua Unofficial Api**

<img src="https://img.shields.io/badge/python-%3E%3D3.8-blue" />&nbsp;
<img src="https://img.shields.io/badge/framework-FastAPI-green" />
<img src="https://img.shields.io/badge/async-httpx%2Bbeautifulsoup4-orange" />&nbsp;
<img src="https://img.shields.io/pypi/v/donghua-unofficial-api?color=blue" />&nbsp;
<img src="https://img.shields.io/pypi/l/donghua-unofficial-api?color=blue" />&nbsp;
<img src="https://img.shields.io/pypi/dm/donghua-unofficial-api?color=success" />
<img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" />

*Scrape donghua data, streaming links, schedules, and more with this powerful unofficial Python API*

[Quick Start](#-quick-install) • [Features](#-features) • [API Reference](#-endpoints) • [Examples](#-examples)

</div>

## 🚀 Introduction

**Donghua Unofficial API** is a comprehensive Python library that provides programmatic access to Chinese animation (donghua) data. Built with **FastAPI** and **Async HTTPX**, it offers lightning-fast asynchronous scraping capabilities for donghua information, streaming links, release schedules, and much more.

Perfect for developers building:
- 📱 Donghua tracking apps
- 🎬 Streaming platforms  
- 📊 Release calendar services
- 🤖 Discord/Telegram bots
- 🔍 Search engines for Chinese animation
- 🐍 Python-based data analysis tools

## ✨ Features

<div align="center">

| Category | Features |
|----------|----------|
| **🎯 Core** | Complete donghua database • Async scraping • Fast responses |
| **🔍 Search** | Advanced search • Genre filtering • Status-based filtering |
| **📺 Streaming** | Multiple server support • Episode navigation • Base64 embed extraction |
| **📅 Schedule** | Daily release schedule • Countdown timers • Weekly calendar |
| **⚡ Performance** | Async/Await • HTTP/2 support • Connection pooling |
| **🔧 Development** | Type hints • RESTful API • Swagger/ReDoc documentation |

</div>

## 🛠 Quick Install

### 1. Install from PyPI

```bash
# Using pip
pip install donghua-unofficial-api

# Using poetry
poetry add donghua-unofficial-api

# Using uv
uv add donghua-unofficial-api
```

2. Start the API Server

Option A: CLI Command (Recommended)

```bash
# After installation, run directly
donghua-api

# Or with custom port
donghua-api --port 8080 --host 0.0.0.0
```

Option B: Python Script

```python
# start.py
from donghua_unofficial_api import start_server

if __name__ == "__main__":
    start_server(host="0.0.0.0", port=8000, reload=True)
```

Option C: Import as Module

```python
import uvicorn
from app.main import app

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
```

3. Verify Installation

```bash
# Server starts on http://localhost:8000
# Test the API
curl http://localhost:8000/api/v1/home

# Expected response:
{
  "status": 200,
  "success": true,
  "author": "zhadev",
  "data": {
    "popular_today": [...],
    "latest_releases": [...]
  }
}
```

📥 Install From Source

For latest features and development version:

```bash
# Clone repository
git clone https://github.com/zhadevv/donghua-unofficial-api.git
cd donghua-unofficial-api

# Install in development mode
pip install -e .

# Or with development dependencies
pip install -e ".[dev]"

# Start development server
python start.py
```

⚙️ Configuration

Create .env file for custom configuration:

```env
# Server Configuration
HOST=0.0.0.0
PORT=8000
RELOAD=true

# Scraping Configuration
BASE_URL=https://donghub.vip
TIMEOUT=30.0
MAX_RETRIES=3

# Logging
LOG_LEVEL=info
DEBUG=false
```

Or use environment variables:

```bash
PORT=8080 LOG_LEVEL=debug python start.py
```

📡 Endpoints

<div align="center">

| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| GET | /api/v1/home | Homepage data | page (optional) |
| GET | /api/v1/search | Search donghua | s (required), page |
| GET | /api/v1/schedule | Release schedule | - |
| GET | /api/v1/popular | Popular donghua | page |
| GET | /api/v1/latest | Latest releases | page |
| GET | /api/v1/ongoing | Ongoing series | page |
| GET | /api/v1/completed | Completed series | page |
| GET | /api/v1/genres/{slug} | Donghua by genre | slug, page |
| GET | /api/v1/detail/{slug} | Detailed info | slug |
| GET | /api/v1/episodes/{slug} | All episodes list | slug |
| GET | /api/v1/stream/{slug} | Streaming data | episode, serverId |
| GET | /api/v1/filters | Available filters | - |
| GET | /api/v1/test/* | Health check | - |

</div>

🎯 Examples

Search for Donghua

```python
import httpx
import asyncio

async def search_donghua():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "http://localhost:8000/api/v1/search", 
            params={"s": "renegade"}
        )
        data = response.json()
        print(data["data"]["results"])

asyncio.run(search_donghua())
```

Get Donghua Details

```python
async def get_detail():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "http://localhost:8000/api/v1/detail/battle-through-the-heavens"
        )
        data = response.json()
        print(data["data"])

asyncio.run(get_detail())
```

Get Streaming Links

```python
async def get_stream():
    async with httpx.AsyncClient() as client:
        # Get episode 100 with Dailymotion server
        response = await client.get(
            "http://localhost:8000/api/v1/stream/battle-through-the-heavens",
            params={"episode": 100, "serverId": 1}
        )
        data = response.json()
        print(data["data"]["embed_url"])

asyncio.run(get_stream())
```

Using the Parser Directly

```python
from donghua_unofficial_api import DonghubParser
import asyncio

async def main():
    async with DonghubParser() as parser:
        # Search directly
        results = await parser.scrape_search("全职高手")
        
        # Get detailed information
        detail = await parser.scrape_detail("king-s-avatar")
        
        # Get streaming data
        stream = await parser.scrape_stream("king-s-avatar", episode=12, server_id=2)

asyncio.run(main())
```

📋 Example Responses

Search Response

```json
{
  "status": 200,
  "success": true,
  "author": "zhadev",
  "data": {
    "results": [
      {
        "title": "Battle Through The Heavens",
        "slug": "battle-through-the-heavens",
        "thumbnail": "https://...",
        "current_episode": "150",
        "type": "Donghua",
        "donghub_url": "https://..."
      }
    ],
    "pagination": {
      "current_page": 1,
      "next_page": 2
    }
  }
}
```

Detail Response

```json
{
  "status": 200,
  "success": true,
  "author": "zhadev", 
  "data": {
    "title": "Battle Through The Heavens",
    "alter_title": "斗破苍穹",
    "thumbnail": "https://...",
    "synopsis": "In a land where no magic is present...",
    "genres": ["Action", "Adventure", "Fantasy"],
    "episodes": [
      {
        "number": "150",
        "title": "Episode 150",
        "url": "/battle-through-the-heavens-episode-150"
      }
    ],
    "episode_nav": {
      "first_episode": {"number": "1", "url": "/..."},
      "new_episode": {"number": "150", "url": "/..."}
    }
  }
}
```

Stream Response

```json
{
  "status": 200,
  "success": true,
  "author": "zhadev",
  "data": {
    "title": "Battle Through The Heavens Episode 100",
    "episode_number": "100",
    "servers": [
      {
        "name": "Dailymotion",
        "data_index": "1",
        "embed_data": "base64_encoded_data"
      }
    ],
    "current_embed": "https://dailymotion.com/embed/video/xyz",
    "navigation": {
      "prev_episode": "/battle-through-the-heavens-episode-99",
      "next_episode": "/battle-through-the-heavens-episode-101"
    }
  }
}
```

🐳 Docker Support

```bash
# Build and run
docker build -t donghua-api .
docker run -p 8000:8000 donghua-api

# Or use docker-compose
docker-compose up -d

# With custom configuration
docker run -p 8000:8000 -e PORT=8000 -e HOST=0.0.0.0 donghua-api
```

🔧 Development

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black .
isort .

# Lint code
flake8

# Type checking
mypy .
```

🤝 Contributing

We love contributions! Here's how to help:

1. Fork the repository
2. Create a feature branch: git checkout -b feature/amazing-feature
3. Commit changes: git commit -m 'Add amazing feature'
4. Push to branch: git push origin feature/amazing-feature
5. Open a Pull Request

📚 API Documentation

Once the server is running, visit:

· Interactive Swagger UI: https://dh.zhadev.my.id/docs
· ReDoc Documentation: https://dh.zhadev.my.id/redoc
· Web Documentation: https://dh.zhadev.my.id

⚠️ Disclaimer

This API is designed for educational purposes and personal use. Please:

· Respect the terms of service of scraped websites
· Use responsibly and consider rate limiting
· Support official releases when possible

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

<div align="center">

    🚀 FastAPI • ⚡ Async

👇 Report Bug • ⭐ Give a Star

<img src="https://img.shields.io/github/stars/zhadevv/donghua-unofficial-api?color=gold" alt="Donghua Unofficial Api" />&nbsp;
<img src="https://img.shields.io/github/issues/zhadevv/donghua-unofficial-api?color=orange" alt="Donghua Unofficial Api" />&nbsp;

</div>
