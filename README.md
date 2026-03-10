# AI University Advisor Backend

This project is a FastAPI backend that scrapes university websites and recommends universities using AI-based scoring.

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Firecrawl Web Scraping
- APScheduler
- Python

## Project Structure

```
app/
 ├── api/          # API routes
 ├── core/         # database and config
 ├── models/       # SQLAlchemy models
 ├── schemas/      # Pydantic schemas
 ├── services/     # scraping + AI logic
 ├── utils/        # helper utilities
 └── main.py       # FastAPI entry point
```

## Setup

Clone the project:

```
git clone https://github.com/RATULBOSU/ai-university-advisor-backend.git
```

Go into the project:

```
cd ai-university-advisor-backend
```

Create a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Create `.env` file:

```
DATABASE_URL=postgresql+psycopg2://user@localhost:5432/uni_advisor
SECRET_KEY=your_secret_key
FIRECRAWL_API_KEY=your_firecrawl_key
```

Run the backend:

```
uvicorn app.main:app --reload
```

Open API docs:

```
http://127.0.0.1:8000/docs
```

## Features

- University data scraping
- Automatic data extraction
- Facilities scoring
- Transport scoring
- AI-based recommendation system
