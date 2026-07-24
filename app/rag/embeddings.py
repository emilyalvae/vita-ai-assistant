from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.config import GEMINI_API_KEY


def get_embeddings():

    return GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=GEMINI_API_KEY,
    )