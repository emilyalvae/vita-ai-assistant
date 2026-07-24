import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


if not GEMINI_API_KEY:
    raise ValueError("No se encontró la API Key de Gemini")

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-lite-latest",
    google_api_key=GEMINI_API_KEY,
    temperature=0
)