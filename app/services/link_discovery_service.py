import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

KEYWORDS = [
    "tuition", "fee", "fees", "cost", "admission", "apply", "undergraduate", "graduate",
    "program", "financial", "payment"
]

def discover_candidate_links(start_url: str, max_links: int = 8) -> list[str]:
    """Fetch HTML once, then find relevant internal links."""
    resp = requests.get(start_url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    base = start_url.rstrip("/")
    base_host = urlparse(base).netloc

    links = []
    seen = set()

    for a in soup.select("a[href]"):
        href = a.get("href", "").strip()
        if not href:
            continue

        full = urljoin(base + "/", href)
        parsed = urlparse(full)

        # keep only http(s) internal links
        if parsed.scheme not in ("http", "https"):
            continue
        if parsed.netloc != base_host:
            continue

        full = full.split("#")[0].rstrip("/")
        if full in seen:
            continue

        text = (a.get_text(" ", strip=True) or "").lower()
        url_l = full.lower()

        if any(k in url_l for k in KEYWORDS) or any(k in text for k in KEYWORDS):
            seen.add(full)
            links.append(full)
            if len(links) >= max_links:
                break

    return links