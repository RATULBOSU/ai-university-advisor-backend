from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from datetime import datetime
from app.core.database import Base


class University(Base):
    __tablename__ = "universities"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False, index=True)
    location = Column(String(255), nullable=True)

    # ✅ scraped sources / facts
    website_url = Column(String(500), nullable=False, unique=True, index=True)
    tuition_text = Column(Text, nullable=True)         # raw snippet
    tuition_fee = Column(Float, nullable=True)         # parsed best number
    facilities_text = Column(Text, nullable=True)      # raw snippet

    last_scraped_at = Column(DateTime, nullable=True)

    # ✅ derived scores (computed, not manual)
    research_score = Column(Float, nullable=True)      # 0–10
    facilities_score = Column(Float, nullable=True)    # 0–10
    transport_score = Column(Float, nullable=True)     # 0–10