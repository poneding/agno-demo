import os

from agno.models.openai import OpenAILike
from dotenv import load_dotenv

load_dotenv()

model = OpenAILike(
    base_url=os.getenv("AI_BASE_URL"),
    api_key=os.getenv("AI_API_KEY"),
    id=os.getenv("AI_MODEL") or "Zhipu/GLM4.6",
)
