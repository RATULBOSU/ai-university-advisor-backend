import requests
from app.config import FIRECRAWL_API_KEY

def firecrawl_scrape_markdown(url: str) -> str:
    if not FIRECRAWL_API_KEY:
        raise ValueError("FIRECRAWL_API_KEY not loaded from .env")

    resp = requests.post(
        "https://api.firecrawl.dev/v1/scrape",
        headers={"Authorization": f"Bearer {FIRECRAWL_API_KEY}"},
        json={"url": url, "formats": ["markdown"]},
        timeout=60,
    )

    if resp.status_code != 200:
        raise ValueError(f"Firecrawl error {resp.status_code}: {resp.text}")

    data = resp.json()
    return (data.get("data", {}) or {}).get("markdown", "") or ""