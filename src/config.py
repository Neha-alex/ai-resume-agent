import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=False)
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
deepseek = OpenAI(base_url=DEEPSEEK_BASE_URL, api_key=deepseek_api_key)