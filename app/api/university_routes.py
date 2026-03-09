from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.university import University
from app.schemas.university_schema import UniversityOut

router = APIRouter(prefix="/universities", tags=["Universities"])


@router.get("/", response_model=list[UniversityOut])
def list_universities(db: Session = Depends(get_db)):
    return db.query(University).order_by(University.id.desc()).all()