import os
from pathlib import Path
from dotenv import load_dotenv

# Force load .env from project root (uni_advisor_backend/.env)
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_FILE)

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60