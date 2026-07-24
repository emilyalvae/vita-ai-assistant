from app.loaders.pdf_loader import load_documents
from app.rag.splitter import split_documents
from app.rag.vectorstore import create_vectorstore
from app.rag.retriever import create_retriever
from app.rag.search import search_rag


# Preparar RAG
docs = load_documents()

chunks = split_documents(docs)

vectorstore = create_vectorstore(chunks)

retriever = create_retriever(vectorstore)


mensajes_de_prueba = [
    "¿Qué seguros acepta la clínica?",
    "¿Cómo puedo cancelar una cita médica?",
    "¿Qué especialidades médicas tiene la clínica?",
    "¿Cuál es el horario de atención?",
    "¿Quién fue Napoleón Bonaparte?"
]


for pregunta in mensajes_de_prueba:

    resultado = search_rag(
        pregunta,
        retriever
    )

    print("\nPREGUNTA:")
    print(pregunta)

    print("\nRESPUESTA:")
    print(resultado["answer"])

    print("\nDOCUMENTOS ENCONTRADOS:")
    print(resultado["documents_found"])


    if resultado["documents_found"]:

        print("\nCITACIONES:")

        for i, documento in enumerate(resultado["citations"]):

            print(f"\n--- Citación {i+1} ---")
            print(
                "Archivo:",
                documento.metadata["source"]
            )

            print(
                "Contenido:",
                documento.page_content[:300]
            )


    print("\n==========================")