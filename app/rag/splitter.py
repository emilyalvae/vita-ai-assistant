from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Divide los documentos en chunks para el RAG.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=30,
    )

    return splitter.split_documents(documents)