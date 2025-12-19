# import os

# from dotenv import load_dotenv

# # from langchain.chat_models import BaseChatModel, init_chat_model
# from langchain_openai import ChatOpenAI
# from pydantic import SecretStr

# load_dotenv()


# model = ChatOpenAI(
#     base_url=os.getenv("AI_BASE_URL"),
#     api_key=SecretStr(os.getenv("AI_API_KEY") or ""),
#     model=os.getenv("AI_MODEL") or "Zhipu/GLM4.6",
# )

# # model = init_chat_model(
# #     base_url=os.getenv("AI_BASE_URL"),
# #     api_key=os.getenv("AI_API_KEY"),
# #     model=os.getenv("AI_MODEL"),
# #     model_provider="openai",
# # )
