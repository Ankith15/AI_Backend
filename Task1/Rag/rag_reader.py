from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os
import google.generativeai as genai
import faiss
import numpy as np

load_dotenv()
apikey= os.getenv("GEMINI")
genai.configure(api_key=apikey)

def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text+= page.extract_text() +"\n"
    return text

def chunk_text(text,chunk_size = 200,overlap=100):
    chunk = []
    for i in range(0,len(text),chunk_size-overlap):
        chunk.append(text[i:i+chunk_size])
    return chunk

# Embedding with mistral 7b model
def Model_store(file_path):
    text = load_pdf(file_path)
    chunks = chunk_text()
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    chunk_map = {i: chunk for i, chunk in enumerate(chunks)}

def search_faiss(query,k=4):
    query_embedding = model.encode([query])
    D,I = index.search(np.array(query_embedding),k)
    return [chunk_map[i] for i in I[0]]



def ask_gemini_rag(query):
    context = "\n\n".join(search_faiss(query))
    prompt =f"context:\n{context}\n\nQuestion: {query}\nAnswer:"

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text