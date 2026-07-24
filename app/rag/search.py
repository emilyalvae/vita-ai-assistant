from app.rag.rag_chain import document_chain


def search_rag(question: str, retriever) -> dict:
    """
    Realiza una búsqueda en el RAG y devuelve
    la respuesta junto con las fuentes utilizadas.
    """

    # Buscar documentos relacionados
    related_documents = retriever.invoke(question)

    # No se encontro nada
    if not related_documents:
        return {
            "answer": "No lo sé.",
            "citations": [],
            "documents_found": False,
        }

    # Generar respuesta usando el contexto encontrado
    answer = document_chain.invoke(
        {
            "input": question,
            "context": related_documents,
        }
    )

    # Si el LLM responde que no sabe
    if answer.strip().rstrip(".!?").lower() == "no lo sé":
        return {
            "answer": "No lo sé.",
            "citations": [],
            "documents_found": False,
        }

    # Caso exitoso
    return {
        "answer": answer,
        "citations": related_documents,
        "documents_found": True,
    }