from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.university import University
from app.services.firecrawl_service import firecrawl_scrape_markdown
from app.services.link_discovery_service import discover_candidate_links

def refresh_one_university(db: Session, uni: University) -> None:
    url = (uni.website_url or "").rstrip("/")
    if not url:
        return

    urls = [url] + discover_candidate_links(url, max_links=8)

    parts = []
    for u in urls:
        try:
            md = firecrawl_scrape_markdown(u)
            if md.strip():
                parts.append(f"\n\n# SOURCE: {u}\n\n{md}")
        except Exception:
            continue

    merged = "\n\n".join(parts)

    # TODO: replace these two with your real extraction functions
    # uni.tuition_fee = extract_tuition_fee(merged)
    # uni.tuition_text = extract_tuition_text(merged)

    # keep what already works for you
    uni.facilities_text = merged[:8000]  # or your extractor

    db.add(uni)

def refresh_all_universities() -> None:
    db = SessionLocal()
    try:
        unis = db.query(University).all()
        for uni in unis:
            refresh_one_university(db, uni)
        db.commit()
    finally:
        db.close()