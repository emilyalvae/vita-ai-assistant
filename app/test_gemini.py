from app.config import llm


response = llm.invoke(
    """
    Eres Vita, asistente virtual de la Clínica Vitalis.
    Preséntate brevemente.
    """
)

print(response.content)