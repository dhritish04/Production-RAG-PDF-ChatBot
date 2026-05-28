# app/model.py

# from langchain_community.llms import HuggingFaceEndpoint
# from dotenv import load_dotenv
# import os

# load_dotenv()

# def get_llm():
#     return HuggingFaceHub(
#         repo_id="mistralai/Mistral-7B-Instruct-v0.1",
#         model_kwargs={"temperature": 0.7, "max_new_tokens": 256},
#         huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
#     )





# from langchain_community.llms import HuggingFaceEndpoint
# from dotenv import load_dotenv
# import os

# load_dotenv()

# def get_llm():
#     return HuggingFaceEndpoint(
#         repo_id="mistralai/Mistral-7B-Instruct-v0.1",
#         temperature=0.7,
#         max_new_tokens=512,
#         huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
#         timeout=120  # This is the magic key that tells the server to wait for the model to wake up
#     )






from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set. Add it to your .env file.")

    return ChatGroq(
        temperature=0.7,
        # model_name="llama3-8b-8192",
        model_name="llama-3.1-8b-instant",
        api_key=api_key
    )
