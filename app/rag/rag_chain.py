from langchain_classic.chains.combine_documents import create_stuff_documents_chain

from app.config import llm
from app.rag.prompt import PROMPT_RAG


document_chain = create_stuff_documents_chain(
    llm,
    PROMPT_RAG,
)