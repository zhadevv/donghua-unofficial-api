<div align="center">

<a href="https://ibb.co.com/Kxy1vMZF"><img src="https://i.ibb.co.com/hF8qzP5D/Proyek-Baru-58-958-F661.png" alt="Donghua Unofficial Api" border="0" width="600"></a>

### **Donghua Unofficial Api**

<img src="https://img.shields.io/badge/python-%3E%3D3.9-blue" />&nbsp;
<img src="https://img.shields.io/badge/framework-FastAPI-green" />
<img src="https://img.shields.io/badge/async-httpx%2Bbeautifulsoup4-orange" />&nbsp;

*Scrape donghua data, streaming links, schedules, and more with this powerful unofficial API*

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

## ⚠️ DISCLAIMER

This project was built for learning and education, of course this will violate the policies and regulations of the relevant parties, therefore, Therefore, I as the creator will not be responsible "IF" you create your own donghua streaming website/app, you bear the risk yourself

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

```bash
# Clone repository
git clone https://github.com/zhadevv/donghua-unofficial-api.git
cd donghua-unofficial-api

# Install Dependencies
pip install -r requirements.txt

# Start development server
python start.py
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
