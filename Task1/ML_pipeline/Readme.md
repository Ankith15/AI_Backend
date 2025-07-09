# ML Pipeline: End-to-End Machine Learning Workflow

This repository contains a complete end-to-end Machine Learning pipeline built using PySpark, MLflow, Airflow, and Docker. The pipeline processes data, trains a model, evaluates its performance, and logs all relevant metrics and artifacts.

## 📁 Folder Structure

```
ML_LLM_Pipeline/
├── dags/                  # Airflow DAGs for orchestration
│   └── ml_pipeline.py     # Main DAG definition
├── data/                  # Input dataset files (CSV/Parquet)
├── spark_scripts/         # Spark scripts for preprocessing and training
│   ├── preprocessing.py   # Data cleaning and feature engineering
│   └── train_model.py     # Model training and evaluation
├── mlruns/                # MLflow tracking artifacts (auto-generated)
├── Dockerfile             # Docker setup for Spark + Airflow + MLflow
├── docker-compose.yaml    # Container orchestration
├── requirements.txt       # Python dependencies
└── README.md              # Project overview and instructions
```

---

## 🚀 Features

* 📊 **Data Preprocessing**: Using PySpark for large-scale data cleaning and transformation.
* 🤖 **Model Training**: Logistic Regression or other models trained via Spark MLlib.
* 📈 **MLflow Integration**: Tracks parameters, metrics, models, and artifacts.
* 📅 **Airflow DAGs**: Orchestrates ETL, training, and evaluation workflows.
* 🐳 **Dockerized Setup**: Ensures reproducibility and ease of deployment.

---

## ⚙️ Prerequisites

* Python 3.8+
* Docker & Docker Compose
* (Optional) Airflow CLI if running outside Docker

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd ML_LLM_Pipeline
```

### 2. Build and Start Docker Containers

```bash
docker-compose up -d --build
```

This will spin up:

* Airflow Webserver (at [http://localhost:8080](http://localhost:8080))
* Airflow Scheduler
* PostgreSQL (for Airflow metadata)
* MLflow Tracking Server (optional, if configured)

---

### 3. Initialize Airflow

```bash
docker-compose run airflow-webserver airflow db init
```

### 4. Create Admin User

```bash
docker-compose run airflow-webserver airflow users create \
  --username admin \
  --firstname Ankith \
  --lastname AI \
  --role Admin \
  --email ankith@example.com \
  --password admin
```

---

### 5. Trigger the ML Pipeline DAG

Visit Airflow at [http://localhost:8080](http://localhost:8080)

* Login with:

  * **Username**: `admin`
  * **Password**: `admin`
* Enable and trigger `ml_pipeline` DAG

---

## 🧠 DAG Details

The `ml_pipeline.py` DAG consists of the following tasks:

1. **extract\_data**: Reads and validates input data.
2. **preprocess\_data**: Cleans and transforms the dataset.
3. **train\_model**: Trains a classification model using Spark.
4. **evaluate\_model**: Logs performance metrics to MLflow.

---

## 📊 MLflow UI

If MLflow is enabled:

```bash
mlflow ui
```

Visit: [http://localhost:5000](http://localhost:5000)

* View experiments
* Compare runs
* Download model artifacts

---

## 📝 Notes

* Data should be placed in the `data/` folder
* Models and metrics are logged automatically via MLflow
* Ensure your DAG schedule and default\_args are correctly configured

---

## ✅ TODO (Optional Enhancements)

* Add hyperparameter tuning
* Add model registry & deployment via MLflow
* Integrate unit testing for Spark scripts

