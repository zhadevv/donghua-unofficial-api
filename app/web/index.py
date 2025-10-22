from fastapi import APIRouter
from fastapi.responses import HTMLResponse

web_router = APIRouter()

@web_router.get("/", response_class=HTMLResponse)
async def documentation():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Donghua Unofficial API - Documentation</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                margin: 0;
                padding: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            .header {
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                margin-bottom: 30px;
                text-align: center;
            }
            .header h1 {
                color: #333;
                margin: 0;
                font-size: 2.5em;
            }
            .header p {
                color: #666;
                font-size: 1.2em;
                margin: 10px 0 0 0;
            }
            .endpoints-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }
            .endpoint-card {
                background: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                border-left: 5px solid #667eea;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .endpoint-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            }
            .method {
                background: #667eea;
                color: white;
                padding: 5px 12px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 0.9em;
                display: inline-block;
                margin-right: 10px;
            }
            .url {
                font-family: 'Courier New', monospace;
                background: #f8f9fa;
                padding: 8px 12px;
                border-radius: 5px;
                border: 1px solid #e9ecef;
                color: #e83e8c;
                font-weight: bold;
            }
            .description {
                color: #555;
                margin: 15px 0;
                line-height: 1.6;
            }
            .parameters {
                background: #f8f9fa;
                padding: 15px;
                border-radius: 8px;
                margin: 15px 0;
            }
            .param-title {
                font-weight: bold;
                color: #333;
                margin-bottom: 8px;
            }
            .param-item {
                margin: 5px 0;
                font-family: 'Courier New', monospace;
                color: #666;
            }
            .response-example {
                background: #2d3748;
                color: #e2e8f0;
                padding: 15px;
                border-radius: 8px;
                margin: 15px 0;
                font-family: 'Courier New', monospace;
                font-size: 0.9em;
                overflow-x: auto;
            }
            .footer {
                text-align: center;
                color: white;
                padding: 30px;
                margin-top: 40px;
            }
            .badge {
                background: #48bb78;
                color: white;
                padding: 3px 8px;
                border-radius: 12px;
                font-size: 0.8em;
                margin-left: 10px;
            }
            .test-badge {
                background: #ed8936;
                color: white;
                padding: 3px 8px;
                border-radius: 12px;
                font-size: 0.8em;
                margin-left: 10px;
            }
            .quick-links {
                display: flex;
                justify-content: center;
                gap: 15px;
                margin: 20px 0;
            }
            .quick-link {
                background: white;
                color: #667eea;
                padding: 10px 20px;
                border-radius: 25px;
                text-decoration: none;
                font-weight: bold;
                transition: all 0.3s ease;
            }
            .quick-link:hover {
                background: #667eea;
                color: white;
                transform: translateY(-2px);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🎌 Donghua Unofficial API</h1>
                <p>Unofficial REST API for Donghub.vip - Chinese Animation Streaming Platform</p>
                <div class="quick-links">
                    <a href="/docs" class="quick-link">📚 Interactive Docs</a>
                    <a href="/redoc" class="quick-link">📖 ReDoc</a>
                    <a href="/health" class="quick-link">❤️ Health Check</a>
                    <a href="/api/v1/test/all" class="quick-link">🧪 Test All</a>
                </div>
            </div>

            <div class="endpoints-grid">
                <!-- Home -->
                <div class="endpoint-card">
                    <div>
                        <span class="method">GET</span>
                        <span class="url">/api/v1/home?page=1</span>
                        <span class="badge">WORKING</span>
                    </div>
                    <div class="description">
                        Get homepage sections including popular today, latest releases, recommendations, popular series, new movies, and genres.
                    </div>
                    <div class="parameters">
                        <div class="param-title">Query Parameters:</div>
                        <div class="param-item">page (optional) - Page number, default: 1</div>
                    </div>
                </div>

                <!-- Search -->
                <div class="endpoint-card">
                    <div>
                        <span class="method">GET</span>
                        <span class="url">/api/v1/search?s=query&page=1</span>
                        <span class="badge">WORKING</span>
                    </div>
                    <div class="description">
                        Search for donghua by query string with pagination support.
                    </div>
                    <div class="parameters">
                        <div class="param-title">Query Parameters:</div>
                        <div class="param-item">s (required) - Search query</div>
                        <div class="param-item">page (optional) - Page number, default: 1</div>
                    </div>
                </div>

                <!-- Schedule -->
                <div class="endpoint-card">
                    <div>
                        <span class="method">GET</span>
                        <span class="url">/api/v1/schedule</span>
                        <span class="badge">WORKING</span>
                    </div>
                    <div class="description">
                        Get weekly release schedule organized by days (Monday to Sunday) with countdown timers.
                    </div>
                </div>

                <!-- Popular -->
                <div class="endpoint-card">
                    <div>
                        <span class="method">GET</span>
                        <span class="url">/api/v1/popular?page=1</span>
                        <span class="badge">WORKING</span>
                    </div>
                    <div class="description">
                        Get popular donghua list ordered by popularity with pagination.
                    </div>
                    <div class="parameters">
                        <div class="param-title">Query Parameters:</div>
                        <div class="param-item">page (optional) - Page number, default: 1</div>
                    </div>
                </div>

                <!-- Latest -->
                <div class="endpoint-card">
                    <div>
                        <span class="method">GET</span>
                        <span class="url">/api/v1/latest?page=1</span>
                        <span class="badge">WORKING</span>
                    </div>
                    <div class="description">
                        Get latest released donghua ordered by release date.
                    </div>
                    <div class="parameters">
                        <div class="param-title">Query Parameters:</div>
                        <div class="param-item">page (optional) - Page number, default: 1</div>
                    </div>
                </div>

                <!-- Ongoing -->
                <div class="endpoint-card">
                    <div>
                        <span class="method">GET</span>
                        <span class="url">/api/v1/ongoing?page=1</span>
                        <span class="badge">WORKING</span>
                    </div>
                    <div class="description">
                        Get currently ongoing donghua series that are still airing.
                    </div>
                    <div class="parameters">
                        <div class="param-title">Query Parameters:</div>
                        <div class="param-item">page (optional) - Page number, default: 1</div>
                    </div>
                </div>

                <!-- Completed -->
                <div class="endpoint-card">
                    <div>
                        <span class="method">GET</span>
                        <span class="url">/api/v1/completed?page=1</span>
                        <span class="badge">WORKING</span>
                    </div>
                    <div class="description">
                        Get completed donghua series that have finished airing.
                    </div>
                    <div class="parameters">
                        <div class="param-title">Query Parameters:</div>
                        <div class="param-item">page (optional) - Page number, default: 1</div>
                    </div>
                </div>

                <!-- Genres -->
                <div class="endpoint-card">
                    <div>
                        <span class="method">GET</span>
                        <span class="url">/api/v1/genres/action?page=1</span>
                        <span class="badge">WORKING</span>
                    </div>
                    <div class="description">
                        Get donghua filtered by genre slug with pagination support.
                    </div>
                    <div class="parameters">
                        <div class="param-title">Path & Query Parameters:</div>
                        <div class="param-item">slug (path) - Genre slug (action, romance, comedy, etc.)</div>
                        <div class="param-item">page (optional) - Page number, default: 1</div>
                    </div>
                </div>

                <!-- Detail -->
                <div class="endpoint-card">
                    <div>
                        <span class="method">GET</span>
                        <span class="url">/api/v1/detail/slug-name</span>
                        <span class="badge">WORKING</span>
                    </div>
                    <div class="description">
                        Get detailed information about a specific donghua including episodes, synopsis, ratings, and metadata.
                    </div>
                    <div class="parameters">
                        <div class="param-title">Path Parameters:</div>
                        <div class="param-item">slug (path) - Donghua slug from search/home results</div>
                    </div>
                    <div class="response-example">
// Example: /api/v1/detail/battle-through-the-heavens<br>
{<br>
&nbsp;&nbsp;"status": 200,<br>
&nbsp;&nbsp;"success": true,<br>
&nbsp;&nbsp;"author": "zhadev",<br>
&nbsp;&nbsp;"data": {<br>
&nbsp;&nbsp;&nbsp;&nbsp;"title": "Battle Through The Heavens",<br>
&nbsp;&nbsp;&nbsp;&nbsp;"episodes": [...],<br>
&nbsp;&nbsp;&nbsp;&nbsp;"synopsis": "...",<br>
&nbsp;&nbsp;&nbsp;&nbsp;"rating": "9.2"<br>
&nbsp;&nbsp;}<br>
}
                    </div>
                </div>

                <!-- Episodes -->
                <div class="endpoint-card">
                    <div>
                        <span class="method">GET</span>
                        <span class="url">/api/v1/episodes/slug-name</span>
                        <span class="badge">WORKING</span>
                    </div>
                    <div class="description">
                        Get all episodes from first to latest for a donghua series. Automatically generates episode list based on first and latest episode numbers.
                    </div>
                    <div class="parameters">
                        <div class="param-title">Path Parameters:</div>
                        <div class="param-item">slug (path) - Donghua slug</div>
                    </div>
                </div>

                <!-- Stream -->
                <div class="endpoint-card">
                    <div>
                        <span class="method">GET</span>
                        <span class="url">/api/v1/stream/slug-name?episode=1&serverId=1</span>
                        <span class="badge">WORKING</span>
                    </div>
                    <div class="description">
                        Get streaming data, embed URLs, servers list, and episode navigation for specific episodes.
                    </div>
                    <div class="parameters">
                        <div class="param-title">Path & Query Parameters:</div>
                        <div class="param-item">slug (path) - Donghua slug</div>
                        <div class="param-item">episode (optional) - Episode number, defaults to latest</div>
                        <div class="param-item">serverId (optional) - Server ID (1=DailyMotion, 2=OKRU), returns only embed URL</div>
                    </div>
                    <div class="response-example">
// Without serverId: Full stream data<br>
// With serverId: Only embed_url<br>
{<br>
&nbsp;&nbsp;"embed_url": "https://dailymotion.com/embed/video/xxx"<br>
}
                    </div>
                </div>

                <!-- Filters -->
                <div class="endpoint-card">
                    <div>
                        <span class="method">GET</span>
                        <span class="url">/api/v1/filters</span>
                        <span class="badge">WORKING</span>
                    </div>
                    <div class="description">
                        Get available filters for advanced search including genres, status, types, subtitle options, and order options.
                    </div>
                </div>

                <!-- Test Endpoints -->
                <div class="endpoint-card">
                    <div>
                        <span class="method">GET</span>
                        <span class="url">/api/v1/test/all</span>
                        <span class="test-badge">TESTING</span>
                    </div>
                    <div class="description">
                        Comprehensive test suite to verify all API endpoints are working correctly.
                    </div>
                </div>

                <div class="endpoint-card">
                    <div>
                        <span class="method">GET</span>
                        <span class="url">/api/v1/test/detail?slug=one-piece</span>
                        <span class="test-badge">TESTING</span>
                    </div>
                    <div class="description">
                        Test detail endpoint with specific slug.
                    </div>
                </div>

                <div class="endpoint-card">
                    <div>
                        <span class="method">GET</span>
                        <span class="url">/api/v1/test/stream?slug=one-piece-episode-1</span>
                        <span class="test-badge">TESTING</span>
                    </div>
                    <div class="description">
                        Test stream endpoint with specific episode.
                    </div>
                </div>
            </div>

            <!-- Response Format -->
            <div class="endpoint-card">
                <h3>📋 Standard Response Format</h3>
                <div class="response-example">
{<br>
&nbsp;&nbsp;"status": 200,<br>
&nbsp;&nbsp;"success": true,<br>
&nbsp;&nbsp;"author": "zhadev",<br>
&nbsp;&nbsp;"data": {<br>
&nbsp;&nbsp;&nbsp;&nbsp;// Endpoint-specific data<br>
&nbsp;&nbsp;}<br>
}
                </div>
                <div class="description">
                    All endpoints return consistent JSON response format with status codes, success flag, author attribution, and data payload.
                </div>
            </div>

            <!-- Quick Examples -->
            <div class="endpoint-card">
                <h3>🚀 Quick Examples</h3>
                <div class="description">
                    <strong>Get popular donghua:</strong><br>
                    <code>GET /api/v1/popular</code>
                </div>
                <div class="description">
                    <strong>Search for specific donghua:</strong><br>
                    <code>GET /api/v1/search?s=battle+through+the+heavens</code>
                </div>
                <div class="description">
                    <strong>Get episode stream:</strong><br>
                    <code>GET /api/v1/stream/renegade-immortal?episode=1&serverId=1</code>
                </div>
                <div class="description">
                    <strong>Get all episodes:</strong><br>
                    <code>GET /api/v1/episodes/battle-through-the-heavens</code>
                </div>
            </div>
        </div>

        <div class="footer">
            <p><strong>🎯 API Status: <span style="color: #48bb78;">FULLY OPERATIONAL</span></strong></p>
            <p><strong>Author:</strong> zhadev | <strong>Version:</strong> 1.0.0 | <strong>Base URL:</strong> https://donghub.zhadev.my.id</p>
            <p>⭐ Feed me stars at: <a href="https://github.com/zhadevv/donghua-unofficial-api" style="color: white;">GitHub Repository</a></p>
        </div>

        <script>
            // Simple animation for badges
            document.addEventListener('DOMContentLoaded', function() {
                const badges = document.querySelectorAll('.badge, .test-badge');
                badges.forEach((badge, index) => {
                    setTimeout(() => {
                        badge.style.opacity = '0';
                        badge.style.transition = 'opacity 0.3s ease';
                        setTimeout(() => {
                            badge.style.opacity = '1';
                        }, 100);
                    }, index * 200);
                });
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)