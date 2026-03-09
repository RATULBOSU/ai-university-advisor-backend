from pydantic import BaseModel, Field, HttpUrl


class UniversityScrapeRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
    website_url: HttpUrl
    location: str | None = None


class UniversityOut(BaseModel):
    id: int
    name: str
    location: str | None
    website_url: str
    tuition_fee: float | None
    tuition_text: str | None
    facilities_text: str | None
    research_score: float | None
    facilities_score: float | None
    transport_score: float | None

    class Config:
        from_attributes = True