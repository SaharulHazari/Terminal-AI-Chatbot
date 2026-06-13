import os
from dotenv import load_dotenv

load_dotenv()

os.environ['GOOGLE_API_KEY'] = "AIzaSyBs5vZagdBU7tcOC-pWKwY90XcT1sOAPAU"

class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    EMBEDDING_MODEL = "models/gemini-embedding-001"
    LLM_MODEL = "gemini-2.5-flash"

    VECTOR_TOP_K = 4

settings = Settings()