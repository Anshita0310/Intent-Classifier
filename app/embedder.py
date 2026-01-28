# import os
# from openai import OpenAI
# from dotenv import load_dotenv
#
# load_dotenv()
#
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#
# def get_embedding(text: str):
#     response = client.embeddings.create(
#         model="text-embedding-3-small",
#         input=text
#     )
#     return response.data[0].embedding

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_embedding(text: str):
    result = genai.embed_content(
        model="models/embedding-001",
        content=text
    )
    return result["embedding"]
