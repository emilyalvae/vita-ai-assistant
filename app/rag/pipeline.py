from app.loaders.pdf_loader import load_documents
from app.rag.splitter import split_documents
from app.rag.vectorstore import create_vectorstore
from app.rag.retriever import create_retriever

print("Inicializando RAG...")

docs = load_documents()

chunks = split_documents(docs)

vectorstore = create_vectorstore(chunks)

retriever = create_retriever(vectorstore)

print("RAG listo.")