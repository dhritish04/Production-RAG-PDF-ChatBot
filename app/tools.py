# app/tools.py

# from langchain.tools import Tool
from langchain_core.tools import Tool
from app.rag import answer_query
from app.vector_space import get_vectorstore
from app.summarizer import summarize_text


def answer_from_knowledge_base(query: str) -> str:
    vector_store = get_vectorstore()
    docs = vector_store.search(query, k=5)
    result = answer_query(query, docs)
    return result["answer"]

def get_tools():
    return [
        Tool(
            name="RAG_Answer",
            func=answer_from_knowledge_base,
            description="Use this tool to answer questions using the PDF knowledge base"
        ),
        Tool(
            name="Summarize_Text",
            func=summarize_text,
            description="Use this tool to summarize a passage or document"
        )
    ]
