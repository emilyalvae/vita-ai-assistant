from app.loaders.pdf_loader import load_documents
from app.rag.splitter import split_documents
from app.rag.vectorstore import create_vectorstore
from app.rag.retriever import create_retriever

from app.rag.rag_chain import document_chain

docs = load_documents()
chunks = split_documents(docs)
vectorstore = create_vectorstore(chunks)
retriever = create_retriever(vectorstore)

question = "¿Qué seguros acepta la clínica?"

documents = retriever.invoke(question)

response = document_chain.invoke(
    {
        "context": documents,
        "input": question,
    }
)

print(response)