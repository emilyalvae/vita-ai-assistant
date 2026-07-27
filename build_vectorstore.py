from app.loaders.pdf_loader import load_documents
from app.rag.splitter import split_documents
from app.rag.vectorstore import create_vectorstore


def main():
    print("Generando vectorstore...")

    docs = load_documents()

    chunks = split_documents(docs)

    create_vectorstore(chunks)

    print("Vectorstore creado correctamente.")


if __name__ == "__main__":
    main()