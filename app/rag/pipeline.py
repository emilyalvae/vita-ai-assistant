from app.rag.vectorstore import load_vectorstore
from app.rag.retriever import create_retriever


def initialize_rag():

    print("Inicializando RAG...")

    vectorstore = load_vectorstore()

    retriever = create_retriever(vectorstore)

    print("RAG listo.")

    return retriever