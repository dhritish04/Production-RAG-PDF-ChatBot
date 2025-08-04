# app/loaders.py

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document
import os

def load_and_split(pdf_path: str) -> List[Document]:
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    # Each `page` already contains metadata like 'source' (file) and 'page'
    docs = splitter.split_documents(pages)

    for doc in docs:
        doc.metadata["source_doc"] = os.path.basename(pdf_path)
        # Optionally you could parse section headers here too later

    return docs
