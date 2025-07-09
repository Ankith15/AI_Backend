

```markdown
# 🔍 Project Summary: Heart Disease Prediction ML Pipeline using MLflow+Docker+Apache Airflow

---

## 📌 Objective

To build and orchestrate a full machine learning pipeline for heart disease prediction using:

- Apache Airflow for workflow orchestration
- Apache Spark for scalable preprocessing
- Scikit-learn for model training
- MLflow for tracking and versioning
- Docker for isolated, reproducible environments
- FastAPI for serving predictions

---

## 📂 Pipeline Breakdown

### 1. **Data Preprocessing** (Spark)
- Reads `heart.csv`
- Encodes categorical variables manually
- Drops nulls and original categorical columns
- Outputs `processed_heart.csv`

### 2. **Model Training** (Scikit-learn + MLflow)
- Random Forest Classifier
- Accuracy evaluated on test split
- MLflow logs:
  - `accuracy`
  - `n_estimators`
  - model artifact
  - scaler artifact (`heart_scaler.pkl`)

---

## 🛠️ Orchestration via Airflow

**DAG Name:** `heart_disease_ml_pipeline`

- **Task 1:** `spark_preprocessing` → runs `spark_preprocess.py`
- **Task 2:** `train_model_with_mlflow` → runs `train_with_mlflow.py`
- `@daily` schedule ensures retraining every 24 hours
- Logs and task statuses available via Airflow UI

---

## 📊 Experiment Tracking with MLflow

- Each DAG run creates a new **experiment run**
- Accessible via: [http://localhost:5000](http://localhost:5000)
- Tracks parameters, metrics, and artifacts
- Visual comparison of runs is supported

---

## 🌐 Model Deployment (FastAPI)

- Predicts heart disease via form-based input
- Scaler and model are loaded from `.pkl` files
- Interface available at [http://localhost:8000](http://localhost:8000)

---

## 🐳 Docker Integration

- Docker Compose starts Airflow (scheduler, webserver, PostgreSQL)
- `../training` is mounted as `/opt/airflow/project`
- Everything runs in containers for reproducibility

---

## ✅ Key Outcomes

- ✔️ End-to-end retraining on every Airflow DAG execution
- ✔️ Full visibility of model metrics and experiments in MLflow
- ✔️ Clean pipeline structure ready for production use
```
