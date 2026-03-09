from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.core.database import get_db
from app.models.university import University
from app.schemas.university_schema import UniversityScrapeRequest, UniversityOut

from app.services.firecrawl_service import firecrawl_scrape_markdown
from app.services.parsing_service import extract_tuition, extract_facilities
from app.services.scoring_service import (
    facilities_score_from_text,
    transport_score_from_text,
    research_score_placeholder,
)

router = APIRouter(prefix="/scrape", tags=["Scraping"])


@router.post("/university", response_model=UniversityOut)
def scrape_and_upsert_university(
    payload: UniversityScrapeRequest,
    db: Session = Depends(get_db)
):
    markdown = firecrawl_scrape_markdown(str(payload.website_url))
    if not markdown:
        raise HTTPException(status_code=400, detail="No content extracted from URL")

    tuition_fee, tuition_text = extract_tuition(markdown)
    facilities_text = extract_facilities(markdown)

    fac_score = facilities_score_from_text(facilities_text)
    trans_score = transport_score_from_text(facilities_text)
    res_score = research_score_placeholder(markdown)

    uni = db.query(University).filter(
        University.website_url == str(payload.website_url)
    ).first()

    if not uni:
        uni = University(
            website_url=str(payload.website_url),
            name=payload.name
        )

    uni.name = payload.name
    uni.location = payload.location
    uni.tuition_fee = tuition_fee
    uni.tuition_text = tuition_text or None
    uni.facilities_text = facilities_text or None
    uni.facilities_score = fac_score
    uni.transport_score = trans_score
    uni.research_score = res_score
    uni.last_scraped_at = datetime.utcnow()

    db.add(uni)
    db.commit()
    db.refresh(uni)
    return uni