import os

from agno.models.lmstudio import LMStudio
from dotenv import load_dotenv

load_dotenv()

model = LMStudio(
    id=os.getenv("AI_MODEL") or "qwen/qwen3-30b-a3b-2507",
    base_url=os.getenv("AI_BASE_URL") or "http://127.0.0.1:1234/v1",
    # api_key=os.getenv("AI_API_KEY"),
)
