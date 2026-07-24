from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader


def load_documents(documents_path: str = "documents"):
    """
    Carga todos los archivos PDF de la carpeta indicada.

    Args:
        documents_path (str): Ruta de la carpeta con los PDFs.

    Returns:
        list: Lista de documentos cargados por LangChain.
    """

    docs = []

    pdf_folder = Path(documents_path)

    for pdf_file in pdf_folder.glob("*.pdf"):
        try:
            loader = PyMuPDFLoader(str(pdf_file))
            docs.extend(loader.load())

            print(f"✅ Archivo cargado: {pdf_file.name}")

        except Exception as e:
            print(f"❌ Error cargando {pdf_file.name}: {e}")

    print(f"\n📄 Total de páginas cargadas: {len(docs)}")

    return docs