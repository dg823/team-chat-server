# 설정 정보 (팀 공통)
import os
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("GROQ_API_KEY")
MODEL = "openai/gpt-oss-20b"
