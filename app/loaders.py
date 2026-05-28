from langchain_community.document_loaders import PyPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from typing import List
import os


def load_and_split(pdf_path: str) -> List[Document]:
    print(f"Loading PDF: {pdf_path}")

    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    print(f"Total pages loaded: {len(pages)}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
    )

    docs = splitter.split_documents(pages)

    print(f"Total chunks created: {len(docs)}")

    for doc in docs:
        doc.metadata["source_doc"] = os.path.basename(pdf_path)

    return docs
