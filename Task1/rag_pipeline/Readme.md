
# RAG Pipeline: Retrieval-Augmented Question Answering System

## Overview

The RAG Pipeline is a modular system that enables intelligent question answering over PDF documents using a combination of embedding-based retrieval (FAISS) and generative language models (DistilGPT2). It supports real-time FastAPI serving and experiment tracking with MLflow.

---

## Features

* ✅ Extracts and chunks text from PDF documents.
* ✅ Generates semantic embeddings using Sentence Transformers.
* ✅ Indexes document chunks using FAISS for fast similarity search.
* ✅ Retrieves top relevant chunks for a given user query.
* ✅ Generates answers using a DistilGPT2 model with contextual input.
* ✅ Logs experiment metadata using MLflow.
* ✅ Provides a FastAPI web interface for user interaction.

---

## Folder Structure

```
rag_pipeline/
│
├── app/
│   ├── main.py                 # FastAPI app with form UI and query handling
│   ├── rag_engine.py           # Core RAG engine for chunking, indexing, retrieval, and generation
│   ├── templates/
│   │   └── form.html           # HTML template for UI
│   ├── docs/
│   │   └── sample.pdf          # Input document for retrieval
│   └── vector_score/           # Folder for FAISS index and metadata
│       ├── faiss_index.bin
│       └── metadata.pkl
│
├── Dockerfile                  # (Optional) For Docker containerization
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## Setup Instructions

### 1️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt` (example):

```text
fastapi
uvicorn
jinja2
PyMuPDF
sentence-transformers
faiss-cpu
transformers
mlflow
```

---

## Run the FastAPI App

```bash
uvicorn app.main:app --reload
```

* Open browser and navigate to: `http://127.0.0.1:8000/`
* Enter your question in the form and receive answers from the document context.

---

## How It Works

1. **PDF Loading**:

   * Reads and chunks the document into coherent paragraphs.
   * Each chunk must be at least 40 characters to ensure semantic richness.

2. **Embedding and Indexing**:

   * Uses `distilbert-base-nli-stsb-mean-tokens` from SentenceTransformers to create embeddings.
   * Stores them in a FAISS index file (`faiss_index.bin`).
   * Stores the corresponding metadata (chunks) in `metadata.pkl`.

3. **Querying**:

   * Embeds the user question and retrieves top-k chunks from FAISS.
   * Uses `distilgpt2` to generate an answer based on the most relevant chunks.

4. **Logging**:

   * Each step (chunking, indexing, querying) logs parameters, metrics, and artifacts to MLflow.

---

## MLflow Tracking

To run the MLflow UI locally:

```bash
mlflow ui
```

* Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)
* View runs, parameters, metrics, and artifacts for PDF processing and question answering.

---

## Optional: Docker Support

If you want to containerize the app:

**Dockerfile** (example)

```Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Build and Run:**

```bash
docker build -t rag-pipeline .
docker run -p 8000:8000 rag-pipeline
```
**Video

https://github.com/user-attachments/assets/f6ce5592-e623-4e04-9f4c-aaf348f2cabb



---

## Example Questions

* "What is the eligibility criteria mentioned in the PDF?"
* "Summarize the process discussed in the document."
* "What are the benefits listed?"

---

## To-Do / Enhancements

* [ ] Switch to more powerful LLMs via API (e.g., OpenAI, Gemini)
* [ ] Improve chunking logic with sentence-level granularity
* [ ] Add PDF upload interface
* [ ] Store run metadata to database backend (e.g., SQLite, PostgreSQL)

---

