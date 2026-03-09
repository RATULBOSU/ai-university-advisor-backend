import re
from typing import Optional, Tuple


def extract_tuition(markdown: str) -> Tuple[Optional[float], str]:
    text = markdown or ""

    patterns = [
        r"tuition\s*fee\s*[:\-]?\s*([\d,]+)",
        r"per\s*credit\s*[:\-]?\s*([\d,]+)",
        r"credit\s*hour\s*[:\-]?\s*([\d,]+)",
        r"total\s*cost\s*[:\-]?\s*([\d,]+)",
    ]

    for pat in patterns:
        m = re.search(pat, text, flags=re.IGNORECASE)
        if m:
            raw = m.group(1).replace(",", "")
            try:
                value = float(raw)
            except ValueError:
                value = None
            snippet = text[max(0, m.start() - 120) : min(len(text), m.end() + 120)]
            return value, snippet.strip()

    return None, ""


def extract_facilities(markdown: str) -> str:
    if not markdown:
        return ""

    keywords = [
        "library",
        "laboratory",
        "lab",
        "hostel",
        "dorm",
        "gym",
        "sports",
        "transport",
        "bus",
        "shuttle",
        "campus",
        "facility",
        "facilities",
    ]

    lines = markdown.splitlines()
    hits = []
    for line in lines:
        low = line.lower()
        if any(k in low for k in keywords):
            cleaned = line.strip()
            if cleaned:
                hits.append(cleaned)
        if len(hits) >= 40:
            break

    return "\n".join(hits).strip()