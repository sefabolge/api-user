import os
from dotenv import load_dotenv
from typing import List

load_dotenv()

class Settings:
    REQRES_API_KEY: str = os.getenv("REQRES_API_KEY")
    REQRES_API_URL: str = os.getenv("REQRES_API_URL")

    ALLOWED_ORIGINS: List[str] = os.getenv("ALLOWED_ORIGINS", "*").split(",")

settings = Settings()