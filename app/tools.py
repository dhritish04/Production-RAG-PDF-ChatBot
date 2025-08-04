# app/tools.py

from langchain.tools import Tool
from app.rag import answer_query
from app.summarizer import summarize_text

def get_tools():
    return [
        Tool(
            name="RAG_Answer",
            func=answer_query,
            description="Use this tool to answer questions using the PDF knowledge base"
        ),
        Tool(
            name="Summarize_Text",
            func=summarize_text,
            description="Use this tool to summarize a passage or document"
        )
    ]
