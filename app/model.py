# app/model.py

from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm():
    return HuggingFaceHub(
        repo_id="mistralai/Mistral-7B-Instruct-v0.1",
        model_kwargs={"temperature": 0.7, "max_new_tokens": 256},
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
    )
