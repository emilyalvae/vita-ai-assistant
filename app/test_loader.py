from loaders.pdf_loader import load_documents
from rag.splitter import split_documents


docs = load_documents()

docs_splits = split_documents(docs)

print(f"\nTotal de chunks: {len(docs_splits)}\n")

print(docs_splits[0])

for i, chunk in enumerate(docs_splits[:5], start=1):
    print(f"\n===== Chunk {i} =====")
    print(chunk.page_content)
    print("--------------------")