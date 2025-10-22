from fastapi import APIRouter
from fastapi.responses import HTMLResponse

web_router = APIRouter()

@web_router.get("/", response_class=HTMLResponse)
async def documentation():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Donghua API • Unofficial REST API</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            :root {
                --primary: #6366f1;
                --primary-dark: #4f46e5;
                --success: #10b981;
                --warning: #f59e0b;
                --gray-50: #f9fafb;
                --gray-100: #f3f4f6;
                --gray-200: #e5e7eb;
                --gray-600: #4b5563;
                --gray-800: #1f2937;
                --gray-900: #111827;
            }
            
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Inter', sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                color: var(--gray-800);
                line-height: 1.6;
            }
            
            .container {
                max-width: 1000px;
                margin: 0 auto;
                padding: 2rem 1rem;
            }
            
            /* Header Styles */
            .header {
                text-align: center;
                margin-bottom: 3rem;
            }
            
            .logo {
                font-size: 3rem;
                margin-bottom: 1rem;
            }
            
            .title {
                font-size: 2.5rem;
                font-weight: 700;
                color: white;
                margin-bottom: 0.5rem;
                letter-spacing: -0.025em;
            }
            
            .subtitle {
                font-size: 1.25rem;
                color: rgba(255, 255, 255, 0.9);
                font-weight: 400;
                margin-bottom: 2rem;
            }
            
            /* Quick Links */
            .quick-links {
                display: flex;
                gap: 1rem;
                justify-content: center;
                flex-wrap: wrap;
                margin-bottom: 2rem;
            }
            
            .quick-link {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                color: white;
                padding: 0.75rem 1.5rem;
                border-radius: 50px;
                text-decoration: none;
                font-weight: 500;
                transition: all 0.3s ease;
                border: 1px solid rgba(255, 255, 255, 0.2);
            }
            
            .quick-link:hover {
                background: rgba(255, 255, 255, 0.2);
                transform: translateY(-2px);
            }
            
            /* Endpoints Container */
            .endpoints-container {
                background: white;
                border-radius: 12px;
                padding: 2rem;
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            }
            
            /* Details & Summary Styles */
            details {
                background: var(--gray-50);
                border-radius: 8px;
                margin-bottom: 1rem;
                border: 1px solid var(--gray-200);
                transition: all 0.3s ease;
            }
            
            details:hover {
                border-color: var(--primary);
            }
            
            details[open] {
                background: white;
                border-color: var(--primary);
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            }
            
            summary {
                padding: 1.25rem;
                cursor: pointer;
                font-weight: 600;
                color: var(--gray-900);
                list-style: none;
                display: flex;
                align-items: center;
                justify-content: between;
                transition: all 0.3s ease;
            }
            
            summary::-webkit-details-marker {
                display: none;
            }
            
            summary::after {
                content: '▶';
                font-size: 0.8rem;
                color: var(--gray-400);
                transition: transform 0.3s ease;
                margin-left: auto;
            }
            
            details[open] summary::after {
                transform: rotate(90deg);
                color: var(--primary);
            }
            
            summary:hover {
                color: var(--primary);
            }
            
            .endpoint-header {
                display: flex;
                align-items: center;
                gap: 1rem;
                flex-wrap: wrap;
            }
            
            .method {
                background: var(--primary);
                color: white;
                padding: 0.25rem 0.75rem;
                border-radius: 6px;
                font-size: 0.75rem;
                font-weight: 600;
                letter-spacing: 0.05em;
            }
            
            .url {
                font-family: 'Monaco', 'Consolas', monospace;
                font-size: 0.9rem;
                color: var(--gray-600);
                font-weight: 500;
            }
            
            .badge {
                font-size: 0.7rem;
                padding: 0.2rem 0.6rem;
                border-radius: 20px;
                font-weight: 600;
            }
            
            .badge.working {
                background: var(--success);
                color: white;
            }
            
            .badge.testing {
                background: var(--warning);
                color: white;
            }
            
            /* Content Styles */
            .endpoint-content {
                padding: 0 1.25rem 1.25rem 1.25rem;
                border-top: 1px solid var(--gray-200);
                margin-top: 1rem;
            }
            
            .description {
                color: var(--gray-600);
                margin-bottom: 1.5rem;
                font-size: 0.95rem;
                line-height: 1.6;
            }
            
            .params {
                background: var(--gray-50);
                padding: 1.25rem;
                border-radius: 8px;
                margin-bottom: 1.5rem;
            }
            
            .param-title {
                font-size: 0.8rem;
                font-weight: 600;
                color: var(--gray-600);
                margin-bottom: 0.75rem;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }
            
            .param-item {
                font-family: 'Monaco', 'Consolas', monospace;
                font-size: 0.85rem;
                color: var(--gray-600);
                margin: 0.5rem 0;
                padding-left: 1rem;
            }
            
            .example-code {
                background: var(--gray-800);
                color: var(--gray-200);
                padding: 1.25rem;
                border-radius: 8px;
                font-family: 'Monaco', 'Consolas', monospace;
                font-size: 0.85rem;
                line-height: 1.5;
                overflow-x: auto;
                margin-top: 1rem;
            }
            
            .example-title {
                font-size: 0.9rem;
                font-weight: 600;
                color: var(--gray-700);
                margin-bottom: 0.5rem;
            }
            
            /* Footer */
            .footer {
                text-align: center;
                margin-top: 3rem;
                padding: 2rem;
                color: white;
            }
            
            .footer-links {
                display: flex;
                justify-content: center;
                gap: 2rem;
                margin-top: 1rem;
                flex-wrap: wrap;
            }
            
            .footer-link {
                color: rgba(255, 255, 255, 0.8);
                text-decoration: none;
                transition: color 0.3s ease;
                font-size: 0.9rem;
            }
            
            .footer-link:hover {
                color: white;
            }
            
            /* Animation */
            @keyframes slideDown {
                from { opacity: 0; transform: translateY(-10px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            details[open] .endpoint-content {
                animation: slideDown 0.3s ease-out;
            }
            
            /* Responsive */
            @media (max-width: 768px) {
                .container {
                    padding: 1rem;
                }
                
                .endpoints-container {
                    padding: 1.5rem;
                }
                
                .endpoint-header {
                    gap: 0.5rem;
                }
                
                .url {
                    font-size: 0.8rem;
                }
                
                .quick-links {
                    gap: 0.5rem;
                }
                
                .quick-link {
                    padding: 0.6rem 1rem;
                    font-size: 0.9rem;
                }
            }
            
            /* Section Header */
            .section-header {
                display: flex;
                align-items: center;
                gap: 1rem;
                margin-bottom: 2rem;
                padding-bottom: 1rem;
                border-bottom: 2px solid var(--gray-200);
            }
            
            .section-icon {
                font-size: 1.5rem;
            }
            
            .section-title {
                font-size: 1.5rem;
                font-weight: 700;
                color: var(--gray-900);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Header -->
            <div class="header">
                <div class="logo">🎌</div>
                <h1 class="title">Donghua API</h1>
                <p class="subtitle">Unofficial REST API for Chinese Animation Streaming</p>
                
                <div class="quick-links">
                    <a href="/docs" class="quick-link">📚 Interactive Docs</a>
                    <a href="/redoc" class="quick-link">📖 ReDoc</a>
                    <a href="/health" class="quick-link">❤️ Health Check</a>
                    <a href="/api/v1/test/all" class="quick-link">🧪 Test All</a>
                </div>
            </div>

            <!-- Endpoints Container -->
            <div class="endpoints-container">
                <!-- Content Endpoints -->
                <div class="section-header">
                    <span class="section-icon">🎬</span>
                    <h2 class="section-title">Content Endpoints</h2>
                </div>

                <!-- Home -->
                <details>
                    <summary>
                        <div class="endpoint-header">
                            <span class="method">GET</span>
                            <span class="url">/api/v1/home?page=1</span>
                            <span class="badge working">WORKING</span>
                        </div>
                    </summary>
                    <div class="endpoint-content">
                        <p class="description">Get homepage sections including popular today, latest releases, recommendations, popular series, new movies, and genres.</p>
                        
                        <div class="params">
                            <div class="param-title">Query Parameters</div>
                            <div class="param-item">page (optional) - Page number, default: 1</div>
                        </div>
                        
                        <div class="example-title">Example Response:</div>
                        <div class="example-code">
{
  "status": 200,
  "success": true,
  "author": "zhadev",
  "data": {
    "popular_today": [...],
    "latest_releases": [...],
    "recommendations": [...]
  }
}
                        </div>
                    </div>
                </details>

                <!-- Search -->
                <details>
                    <summary>
                        <div class="endpoint-header">
                            <span class="method">GET</span>
                            <span class="url">/api/v1/search?s=query&page=1</span>
                            <span class="badge working">WORKING</span>
                        </div>
                    </summary>
                    <div class="endpoint-content">
                        <p class="description">Search for donghua by query string with pagination support.</p>
                        
                        <div class="params">
                            <div class="param-title">Query Parameters</div>
                            <div class="param-item">s (required) - Search query</div>
                            <div class="param-item">page (optional) - Page number, default: 1</div>
                        </div>
                        
                        <div class="example-title">Example Usage:</div>
                        <div class="example-code">
GET /api/v1/search?s=battle+through+the+heavens&page=1
                        </div>
                    </div>
                </details>

                <!-- Schedule -->
                <details>
                    <summary>
                        <div class="endpoint-header">
                            <span class="method">GET</span>
                            <span class="url">/api/v1/schedule</span>
                            <span class="badge working">WORKING</span>
                        </div>
                    </summary>
                    <div class="endpoint-content">
                        <p class="description">Get weekly release schedule organized by days (Monday to Sunday) with countdown timers.</p>
                        
                        <div class="example-title">Response Includes:</div>
                        <div class="example-code">
{
  "monday": [...],
  "tuesday": [...],
  "wednesday": [...],
  // ... all days
}
                        </div>
                    </div>
                </details>

                <!-- Popular -->
                <details>
                    <summary>
                        <div class="endpoint-header">
                            <span class="method">GET</span>
                            <span class="url">/api/v1/popular?page=1</span>
                            <span class="badge working">WORKING</span>
                        </div>
                    </summary>
                    <div class="endpoint-content">
                        <p class="description">Get popular donghua list ordered by popularity with pagination.</p>
                        
                        <div class="params">
                            <div class="param-title">Query Parameters</div>
                            <div class="param-item">page (optional) - Page number, default: 1</div>
                        </div>
                    </div>
                </details>

                <!-- Latest -->
                <details>
                    <summary>
                        <div class="endpoint-header">
                            <span class="method">GET</span>
                            <span class="url">/api/v1/latest?page=1</span>
                            <span class="badge working">WORKING</span>
                        </div>
                    </summary>
                    <div class="endpoint-content">
                        <p class="description">Get latest released donghua ordered by release date.</p>
                        
                        <div class="params">
                            <div class="param-title">Query Parameters</div>
                            <div class="param-item">page (optional) - Page number, default: 1</div>
                        </div>
                    </div>
                </details>

                <!-- Detail -->
                <details>
                    <summary>
                        <div class="endpoint-header">
                            <span class="method">GET</span>
                            <span class="url">/api/v1/detail/slug-name</span>
                            <span class="badge working">WORKING</span>
                        </div>
                    </summary>
                    <div class="endpoint-content">
                        <p class="description">Get detailed information about a specific donghua including episodes, synopsis, ratings, and metadata.</p>
                        
                        <div class="params">
                            <div class="param-title">Path Parameters</div>
                            <div class="param-item">slug - Donghua slug from search/home results</div>
                        </div>
                        
                        <div class="example-title">Example Response:</div>
                        <div class="example-code">
{
  "status": 200,
  "success": true,
  "author": "zhadev", 
  "data": {
    "title": "Battle Through The Heavens",
    "episodes": [...],
    "synopsis": "In a land where no magic is present...",
    "rating": "9.2",
    "genres": ["Action", "Adventure", "Fantasy"]
  }
}
                        </div>
                    </div>
                </details>

                <!-- Stream Endpoints -->
                <div class="section-header" style="margin-top: 3rem;">
                    <span class="section-icon">🎥</span>
                    <h2 class="section-title">Streaming Endpoints</h2>
                </div>

                <!-- Episodes -->
                <details>
                    <summary>
                        <div class="endpoint-header">
                            <span class="method">GET</span>
                            <span class="url">/api/v1/episodes/slug-name</span>
                            <span class="badge working">WORKING</span>
                        </div>
                    </summary>
                    <div class="endpoint-content">
                        <p class="description">Get all episodes from first to latest for a donghua series. Automatically generates episode list based on first and latest episode numbers.</p>
                        
                        <div class="params">
                            <div class="param-title">Path Parameters</div>
                            <div class="param-item">slug - Donghua slug</div>
                        </div>
                    </div>
                </details>

                <!-- Stream -->
                <details>
                    <summary>
                        <div class="endpoint-header">
                            <span class="method">GET</span>
                            <span class="url">/api/v1/stream/slug-name?episode=1&serverId=1</span>
                            <span class="badge working">WORKING</span>
                        </div>
                    </summary>
                    <div class="endpoint-content">
                        <p class="description">Get streaming data, embed URLs, servers list, and episode navigation for specific episodes.</p>
                        
                        <div class="params">
                            <div class="param-title">Parameters</div>
                            <div class="param-item">slug (path) - Donghua slug</div>
                            <div class="param-item">episode (query) - Episode number, defaults to latest</div>
                            <div class="param-item">serverId (query) - Server ID (1=DailyMotion, 2=OKRU)</div>
                        </div>
                        
                        <div class="example-title">With serverId (returns only embed URL):</div>
                        <div class="example-code">
{
  "embed_url": "https://dailymotion.com/embed/video/xxx"
}
                        </div>
                        
                        <div class="example-title">Without serverId (full response):</div>
                        <div class="example-code">
{
  "servers": [...],
  "embed_url": "...", 
  "current_episode": 1,
  "next_episode": 2,
  "prev_episode": null
}
                        </div>
                    </div>
                </details>

                <!-- Filter Endpoints -->
                <div class="section-header" style="margin-top: 3rem;">
                    <span class="section-icon">🔍</span>
                    <h2 class="section-title">Filter Endpoints</h2>
                </div>

                <!-- Filters -->
                <details>
                    <summary>
                        <div class="endpoint-header">
                            <span class="method">GET</span>
                            <span class="url">/api/v1/filters</span>
                            <span class="badge working">WORKING</span>
                        </div>
                    </summary>
                    <div class="endpoint-content">
                        <p class="description">Get available filters for advanced search including genres, status, types, subtitle options, and order options.</p>
                        
                        <div class="example-title">Response Structure:</div>
                        <div class="example-code">
{
  "genres": [...],
  "status": [...], 
  "types": [...],
  "subtitles": [...],
  "order": [...]
}
                        </div>
                    </div>
                </details>

                <!-- Genres -->
                <details>
                    <summary>
                        <div class="endpoint-header">
                            <span class="method">GET</span>
                            <span class="url">/api/v1/genres/action?page=1</span>
                            <span class="badge working">WORKING</span>
                        </div>
                    </summary>
                    <div class="endpoint-content">
                        <p class="description">Get donghua filtered by genre slug with pagination support.</p>
                        
                        <div class="params">
                            <div class="param-title">Parameters</div>
                            <div class="param-item">slug (path) - Genre slug (action, romance, comedy, etc.)</div>
                            <div class="param-item">page (query) - Page number, default: 1</div>
                        </div>
                    </div>
                </details>

                <!-- Test Endpoints -->
                <div class="section-header" style="margin-top: 3rem;">
                    <span class="section-icon">🧪</span>
                    <h2 class="section-title">Test Endpoints</h2>
                </div>

                <!-- Test All -->
                <details>
                    <summary>
                        <div class="endpoint-header">
                            <span class="method">GET</span>
                            <span class="url">/api/v1/test/all</span>
                            <span class="badge testing">TESTING</span>
                        </div>
                    </summary>
                    <div class="endpoint-content">
                        <p class="description">Comprehensive test suite to verify all API endpoints are working correctly.</p>
                    </div>
                </details>

                <!-- Test Detail -->
                <details>
                    <summary>
                        <div class="endpoint-header">
                            <span class="method">GET</span>
                            <span class="url">/api/v1/test/detail?slug=one-piece</span>
                            <span class="badge testing">TESTING</span>
                        </div>
                    </summary>
                    <div class="endpoint-content">
                        <p class="description">Test detail endpoint with specific slug.</p>
                    </div>
                </details>

                <!-- Test Stream -->
                <details>
                    <summary>
                        <div class="endpoint-header">
                            <span class="method">GET</span>
                            <span class="url">/api/v1/test/stream?slug=one-piece-episode-1</span>
                            <span class="badge testing">TESTING</span>
                        </div>
                    </summary>
                    <div class="endpoint-content">
                        <p class="description">Test stream endpoint with specific episode.</p>
                    </div>
                </details>

            </div>
        </div>

        <!-- Footer -->
        <div class="footer">
            <p><strong>Donghua Unofficial API</strong> • Built with FastAPI • Deployed on Vercel</p>
            <div class="footer-links">
                <a href="https://github.com/zhadevv/donghua-unofficial-api" class="footer-link">⭐ GitHub</a>
                <a href="https://pypi.org/project/donghua" class="footer-link">📦 PyPI Package</a>
                <a href="/docs" class="footer-link">📚 Interactive Docs</a>
                <a href="https://donghub.vip" class="footer-link">🌐 Original Site</a>
            </div>
        </div>

        <script>
            document.addEventListener('DOMContentLoaded', function() {
            
                const sections = document.querySelectorAll('details');
                if (sections.length > 0) {
                    sections[0].open = true; // Open first endpoint
                }
                
                const allDetails = document.querySelectorAll('details');
                allDetails.forEach(detail => {
                    detail.addEventListener('toggle', function() {
                        if (this.open) {
                            // Optional: close other details in the same section
                            const parentSection = this.closest('.section-header')?.nextElementSibling;
                            if (parentSection) {
                                const siblings = parentSection.querySelectorAll('details');
                                siblings.forEach(sib => {
                                    if (sib !== this && sib.open) {
                                        sib.open = false;
                                    }
                                });
                            }
                        }
                    });
                });
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
