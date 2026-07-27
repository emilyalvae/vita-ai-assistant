from langchain_community.vectorstores import FAISS

from app.rag.embeddings import get_embeddings


def create_vectorstore(chunks):
    """
    Crea el vectorstore a partir de los documentos.
    Se ejecuta UNA SOLA VEZ cuando se generan los embeddings.
    """
    embeddings = get_embeddings()

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings,
    )

    vectorstore.save_local("vectorstore")

    return vectorstore

def load_vectorstore():
    """
    Carga el vectorstore ya generado.
    Se usa durante la ejecución normal de la aplicación.
    """
    embeddings = get_embeddings()

    return FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True,
    )