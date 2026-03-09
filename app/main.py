from apscheduler.schedulers.background import BackgroundScheduler
from app.services.refresh_service import refresh_all_universities

from fastapi import FastAPI
from app.core.database import Base, engine
from app import models

# Import routers
from app.api.university_routes import router as university_router
from app.api.user_routes import router as user_router
from app.api.scrape_routes import router as scrape_router

app = FastAPI(title="AI University Advisor Backend")

# START SCHEDULER
scheduler = BackgroundScheduler()
scheduler.add_job(refresh_all_universities, "interval", hours=24)
scheduler.start()

# Include routers
app.include_router(university_router)
app.include_router(user_router)
app.include_router(scrape_router)

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Backend is running successfully"}