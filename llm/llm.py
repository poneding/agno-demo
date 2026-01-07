import os

from agno.models.openai import OpenAILike
from dotenv import load_dotenv

load_dotenv()


model = OpenAILike(
    base_url=os.getenv("AI_BASE_URL") or "http://localhost:1234/v1",
    api_key=os.getenv("AI_API_KEY"),
    id=os.getenv("AI_MODEL_ID") or "openai/gpt-oss-20b",
)
