
# 🧠 ML + RAG Pipeline Project

This project showcases a complete AI system that combines a **Machine Learning (ML) pipeline** with a **Retrieval-Augmented Generation (RAG) pipeline**. It is built using modern tools like **Airflow**, **MLflow**, **FastAPI**, **Docker**, and **FAISS**, orchestrating both structured ML experimentation and real-time document-based question answering.

---

## 📁 Project Structure

```
├── Task1/
│   ├── ml_pipeline/                # End-to-end ML workflow
│   │   ├── airflow/               # Airflow DAGs & Docker configs
│   │   ├── mlflow_tracking/       # MLflow experiments tracking
│   │   ├── scripts/               # Training, preprocessing, evaluation
│   ├── rag_pipeline/              # Retrieval-Augmented Generation app
│   │   ├── app/                   # FastAPI + RAG logic
│   │   │   ├── main.py            # FastAPI application
│   │   │   ├── rag_engine.py      # RAG implementation (chunking, FAISS, QA)
│   │   │   ├── templates/         # HTML template for UI
│   │   │   ├── docs/              # Input PDF document(s)
│   │   │   └── vector_score/      # FAISS index and metadata
│   │   ├── requirements.txt       # Python dependencies
│   └── README.md                  # Project documentation
```

---

## 🚀 1. Machine Learning Pipeline

### 📌 Features

* Built using **Apache Airflow** for orchestration
* Uses **MLflow** for experiment tracking
* Data processing, training, and evaluation as modular DAG steps
* Dockerized for reproducibility

### 📂 Key Files

* `airflow/dags/ml_pipeline_dag.py` — defines the ML pipeline steps
* `scripts/train.py`, `preprocess.py`, `evaluate.py` — core ML logic
* `mlflow_tracking/` — stores experiment logs

### 🧪 Tracked Metrics via MLflow

* Training Accuracy
* Validation Accuracy
* Model parameters
* Logged artifacts (model.pkl, metrics.json)

### 🛠️ Run the ML Pipeline

```bash
# Step 1: Go to airflow folder
cd Task1/ml_pipeline/airflow

# Step 2: Start Airflow with Docker Compose
docker-compose up -d

# Step 3: Access Airflow UI
# Navigate to: http://localhost:8080
# Username: admin | Password: admin

# Step 4: Trigger ML DAG from UI manually
```

---

## 🧠 2. Retrieval-Augmented Generation (RAG) Pipeline

### 📌 Features

* FastAPI-based UI for interactive querying
* Uses **FAISS** for vector similarity search
* Embeddings via **SentenceTransformers**
* Answer generation via **DistilGPT2**
* Tracks chunks and query logs via **MLflow**

### 📂 Key Files

* `app/main.py` — FastAPI UI backend
* `app/rag_engine.py` — PDF chunking, vector search, generation
* `app/templates/form.html` — Query interface
* `app/docs/sample.pdf` — Input document

### 🧪 MLflow Tracks:

* Number of PDF chunks
* Indexed vectors
* Questions asked
* Generated answers

### 🛠️ Run the RAG Pipeline

```bash
# Step 1: Navigate to RAG folder
cd Task1/rag_pipeline

# Step 2: Install dependencies (inside venv)
pip install -r requirements.txt

# Step 3: Start MLflow UI
mlflow ui
# Open http://127.0.0.1:5000 to view experiments

# Step 4: Run FastAPI app
uvicorn app.main:app --reload
# Visit http://127.0.0.1:8000
```

---

## 🧱 Technologies Used

| Tool/Library         | Purpose                              |
| -------------------- | ------------------------------------ |
| Airflow              | Task scheduling and orchestration    |
| MLflow               | Experiment tracking                  |
| FastAPI              | Web application for user interaction |
| FAISS                | Efficient vector search              |
| SentenceTransformers | Embedding generation                 |
| DistilGPT-2          | Text generation                      |
| Docker               | Containerization                     |
| Uvicorn              | FastAPI ASGI server                  |

---

## ✅ Prerequisites

* Python 3.8+
* Docker & Docker Compose
* Virtual environment (`venv`) setup
* MLflow installed globally or in venv

---

## 📌 How to Clone and Run

```bash
# Clone the repo
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo

# Set up venv
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r Task1/rag_pipeline/requirements.txt
```

---

## 📬 Output Examples

* RAG app: Real-time answers to PDF-based queries
* ML pipeline: Trained model, metrics, logs on MLflow
* FAISS index: Stored in `app/vector_score/`
* Artifacts: model.pkl, answer.txt, index.bin

---
