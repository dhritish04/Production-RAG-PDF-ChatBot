from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os
import pickle


class LangchainVectorStore:
    def __init__(self, embedding_model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_name)
        self.vectorstore = None

    def build_index(self, documents):
        print("Building FAISS index with LangChain...")
        self.vectorstore = FAISS.from_documents(documents, self.embedding_model)
        print(f"Indexed {len(documents)} documents.")

    def save(self, path: str):
        if self.vectorstore is None:
            raise ValueError("Vector store is empty. Build an index before saving.")

        print(f"Saving FAISS index to {path}...")
        os.makedirs(path, exist_ok=True)
        self.vectorstore.save_local(path)
        with open(os.path.join(path, "metadata.pkl"), "wb") as f:
            pickle.dump(self.vectorstore.docstore._dict, f)

    def load(self, path: str):
        print(f"Loading FAISS index from {path}...")
        self.vectorstore = FAISS.load_local(
            path,
            self.embedding_model,
            allow_dangerous_deserialization=True,
        )
        metadata_path = os.path.join(path, "metadata.pkl")
        if os.path.exists(metadata_path):
            with open(metadata_path, "rb") as f:
                self.vectorstore.docstore._dict = pickle.load(f)

    def search(self, query: str, k: int = 5):
        if self.vectorstore is None:
            raise ValueError("Vector store is not loaded. Upload a PDF or load an existing index first.")

        print(f"Retrieving top-{k} docs for query: {query}")
        return self.vectorstore.similarity_search(query, k=k)


def get_vectorstore():
    vector_store = LangchainVectorStore()
    vector_store.load("vector_store")
    return vector_store
