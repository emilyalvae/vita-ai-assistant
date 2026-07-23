from langchain_google_genai import ChatGoogleGenerativeAI

from config import GEMINI_API_KEY


llm = ChatGoogleGenerativeAI(
    model="gemini-flash-lite-latest",
    google_api_key=GEMINI_API_KEY,
    temperature=0
)


response = llm.invoke(
    """
    Eres Vita, asistente virtual de la Clínica Vitalis.
    Preséntate brevemente.
    """
)


print(response.content)