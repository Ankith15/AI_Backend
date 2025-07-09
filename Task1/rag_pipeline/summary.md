
## 🔍 Project Summary

This Retrieval-Augmented Generation (RAG) pipeline enables intelligent question answering over PDF documents. It combines document chunking, semantic search using FAISS, and generative answering using DistilGPT2. The entire workflow is served through a FastAPI web interface, with support for experiment tracking via MLflow.

---

## 🧱 Components Breakdown

| Component       | Description                                                                 |
| --------------- | --------------------------------------------------------------------------- |
| `rag_engine.py` | Handles PDF loading, text chunking, embedding, FAISS indexing, and querying |
| `main.py`       | FastAPI app that serves a simple question-answer interface                  |
| `form.html`     | Jinja2 template used as the web front-end                                   |
| `vector_score/` | Stores generated FAISS index and chunk metadata                             |
| `sample.pdf`    | The input document used for question answering                              |

---

## ⚙️ Pipeline Flow

1. **PDF Chunking**
   → Loads and breaks PDF text into meaningful chunks
   → Filters out short lines (< 40 characters)

2. **Embedding & FAISS Indexing**
   → Uses SentenceTransformer (`distilbert-base-nli-stsb-mean-tokens`)
   → Creates vector embeddings and stores them in FAISS
   → Chunk text is stored in `metadata.pkl`

3. **User Query → Answer Generation**
   → Input question is embedded
   → Top-k relevant chunks retrieved from FAISS
   → `distilgpt2` generates an answer based on context

4. **Web Interface (FastAPI)**
   → `/` route shows form
   → On submit, displays generated answer in same page

5. **MLflow Logging**
   → Logs parameters (PDF path, question)
   → Logs metrics (chunk count, retrieved chunks)
   → Stores FAISS index & metadata as artifacts

---

## 🧪 Sample Query Flow

1. **User Input**: *"What is the eligibility criteria for this scheme?"*
2. **Chunks Retrieved**: 3 most relevant paragraphs
3. **Generated Output**: LLM-generated answer using retrieved context
4. **MLflow**: Logs the query, retrieved chunk count, and generated answer

---

## 🚀 Quick Commands

```bash
# Run FastAPI app
uvicorn app.main:app --reload

# Launch MLflow UI
mlflow ui  # Then open http://127.0.0.1:5000/
```

---

## ✅ Status

| Task                      | Done |
| ------------------------- | ---- |
| PDF Chunking              | ✅    |
| FAISS Indexing            | ✅    |
| LLM Answer Generation     | ✅    |
| FastAPI UI                | ✅    |
| MLflow Integration        | ✅    |
| Docker (Optional Support) | ⚪    |

---