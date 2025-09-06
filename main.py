from fastapi import Depends
from app import app
import httpx
from bs4 import BeautifulSoup

@app.get("/")
async def root():
    return {"message": "Welcome to Scraper API 🚀"}

@app.get("/scrape")
async def scrape(url: str):
    """
    Example: /scrape?url=https://httpbin.org/html
    """
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)

        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, "lxml")

        # Get title
        title = soup.title.string if soup.title else "No title found"

        return {
            "url": url,
            "status": response.status_code,
            "title": title
        }
    except Exception as e:
        return {"error": str(e)}
