````markdown
# Prodigal AI - Advanced Backend Engineering Hiring Tasks

Welcome to the GitHub repository for the Prodigal AI Advanced Backend Engineering Hiring challenge! This repository serves as a comprehensive demonstration of my capabilities in designing, implementing, and orchestrating complex backend systems across various domains, including AI, data, infrastructure, and automation.

Each task within this suite has been meticulously completed, focusing on system design, backend infrastructure, ML Ops orchestration, real-time data processing, access control, and scalable software development. The solutions provided aim for robustness, efficiency, and maintainability.

## General Guidelines (As per Prodigal AI Requirements)

To ensure clarity, reproducibility, and ease of evaluation, the following guidelines have been adhered to across all tasks:

* **Submission Format:** The repository is clearly structured with dedicated folders for each task.

* **Documentation:** Each sub-task includes:

  * `README.md`: Providing an architecture overview, environment setup, and step-by-step instructions on how to run the task.

  * `DEMO.mp4`: A video demonstrating the end-to-end execution of the task.

  * `SUMMARY.md`: A detailed document describing challenges faced, architectural decisions made, and scope for future improvement.

* **Dockerization:** All services and applications are containerized using Docker to ensure consistent environments and reproducibility across different systems.

* **Video Walkthroughs:** A video (Loom or MP4) is provided for each task, showcasing execution and a code walkthrough (5-10 minutes per task).

* **Frontend (Minimal):** Where a frontend was necessary, it was kept minimal (e.g., React, Next.js, Streamlit) with the primary focus remaining on the backend API behavior and functionality.

## How to Run This Repository

To set up and run the projects within this repository, follow these general steps. Specific instructions for each task are detailed in their respective directories.

### Prerequisites

* **Docker & Docker Compose:** Ensure Docker Desktop (or Docker Engine and Docker Compose) is installed and running on your system. This is crucial for running the containerized services.

* **Git:** For cloning the repository.

### General Setup

1. **Clone the Repository:**

   ```bash
   git clone [https://github.com/Ankith15/AI_backend.git](https://github.com/Ankith15/AI_backend.git)
   cd AI_backend
````

2.  **Navigate to Specific Task Directory:**
    Each task has its own directory (e.g., `Task1`, `Task2_RBAC_System`). Navigate into the desired task's directory to find its specific `README.md` for detailed setup and execution instructions.

    ```bash
    cd TaskX_NameOfTask
    ```

3.  **Build and Run Docker Containers (Task-Specific):**
    Most tasks will involve building and running Docker containers using `docker compose`. Refer to the `README.md` within each task's directory for the exact commands. A common pattern will be:

    ```bash
    docker compose build
    docker compose up -d
    ```

    (Use `docker compose down` to stop and remove containers.)

4.  **Install Dependencies (if any, Task-Specific):**
    Some tasks might have Python or Node.js dependencies for scripts outside of Docker containers (e.g., simulation scripts, client applications). Check the individual `README.md` files for these requirements.

## Table of Contents

  * [Task 1: ML + LLM Pipeline Orchestration](https://www.google.com/search?q=%23task-1-ml--llm-pipeline-orchestration-airflow--mlflow--spark--docker)

      * [Part A: ML Pipeline](https://www.google.com/search?q=%23part-a-ml-pipeline)

      * [Part B: RAG-style LLM Pipeline (Mini POC)](https://www.google.com/search?q=%23part-b-rag-style-llm-pipeline-mini-poc)

  * [Task 2: Role-Based Access Control System (RBAC + Organizations + Guests)](https://www.google.com/search?q=%23task-2-role-based-access-control-system-rbac--organizations--guests)

  * [Task 3: Kafka + Zookeeper for High-Throughput API Ingestion](https://www.google.com/search?q=%23task-3-kafka--zookeeper-for-high-throughput-api-ingestion)

  * [Task 4: Kubernetes Pod Scaling (K8s + HPA)](https://www.google.com/search?q=%23task-4-kubernetes-pod-scaling-k8s--hpa)

  * [Task 5: Binance WebSocket Price Precision Capture (BTC/ETH)](https://www.google.com/search?q=%23task-5-binance-websocket-price-precision-capture-btceth)

  * [Task 6: Article + Scheme Scraper & Summary Report](https://www.google.com/search?q=%23task-6-article--scheme-scraper--summary-report)

  * [Task 7: Multi-Agent Newsletter Generator using LangChain](https://www.google.com/search?q=%23task-7-multi-agent-newsletter-generator-using-langchain)

## Task 1: ML + LLM Pipeline Orchestration (Airflow + MLflow + Spark + Docker)

**Objective:** Demonstrate full-cycle orchestration of an ML model and a basic LLM system.

### Part A: ML Pipeline

**Description:** This part focuses on building and orchestrating a machine learning pipeline using Airflow, MLflow, and Spark. It covers data ingestion, feature engineering, model training, evaluation, versioning, and deployment.

**Key Features:**

  * Data preprocessing with Spark.

  * Model training using scikit-learn/XGBoost/LightGBM.

  * Model versioning and tracking with MLflow.

  * Model deployment as a Flask/FastAPI microservice.

  * Airflow DAGs for pipeline orchestration.

**Deliverables:**

  * Code for ML pipeline components.

  * MLflow logs.

  * Airflow DAGs.

  * REST APIs for model inference.

[**Link to Task 1A Directory**](https://www.google.com/search?q=./Task1/PartA_ML_Pipeline)

### Part B: RAG-style LLM Pipeline (Mini POC)

**Description:** This section implements a retrieval-augmented generation (RAG) workflow using a small open-source LLM. It includes PDF/CSV ingestion for embeddings, a vector database, and a query handler.

**Key Features:**

  * Simple PDF/CSV ingestion for embedding generation.

  * Vector database (e.g., FAISS) for storing embeddings.

  * Query handler for retrieving relevant chunks and interacting with the LLM.

  * Deployment via FastAPI and Docker.

**Deliverables:**

  * Code for RAG pipeline components.

  * RAG endpoint demo via a simple query page.

[**Link to Task 1B Directory**](https://www.google.com/search?q=./Task1/PartB_RAG_LLM_Pipeline)

## Task 2: Role-Based Access Control System (RBAC + Organizations + Guests)

**Objective:** Architect and implement a production-level RBAC system with nested access layers.

**Description:** This task involves building a robust authentication and authorization system supporting organizations, departments, users with roles (Admin, Manager, Contributor, Viewer), and resource-level permissions (CRUD + sharing). It also includes guest link permissions.

**Key Features:**

  * Auth system with sign-up/sign-in (JWT/OAuth).

  * Entities: Organizations, Departments (nested), Users with Roles.

  * Resource permissions (files or endpoints) with CRUD + sharing.

  * Guest link permissions for view/edit access via shareable tokens.

  * Minimal frontend for user flows.

**Deliverables:**

  * REST API documentation.

  * User flows tested via frontend or Postman.

  * Guest shareable links functionality.

[**Link to Task 2 Directory**](https://www.google.com/search?q=./Task2_RBAC_System)

## Task 3: Kafka + Zookeeper for High-Throughput API Ingestion

**Objective:** Simulate massive request handling using Kafka and scalable consumers.

**Description:** This task demonstrates handling high-throughput API requests using Kafka and Zookeeper. It involves setting up Kafka, simulating a high volume of requests, and building producer and scalable consumer applications.

**Key Features:**

  * Deployment of Kafka + Zookeeper (locally or via Docker Compose).

  * Simulation of 10,000+ requests/min.

  * Dummy APIs: `/register_event` and `/get_status`.

  * Kafka producer for sending events.

  * Scalable Kafka consumers for processing and logging requests, showcasing queue reliability.

**Deliverables:**

  * Kafka topology diagram.

  * Docker Compose setup.

  * Consumer logs, error handling, and retry mechanisms.

[**Link to Task 3 Directory**](https://www.google.com/search?q=./Task3_Kafka_Ingestion)

## Task 4: Kubernetes Pod Scaling (K8s + HPA)

**Objective:** Implement a scalable K8s deployment with Horizontal Pod Autoscaling.

**Description:** This task focuses on deploying a Dockerized FastAPI application on Kubernetes and configuring Horizontal Pod Autoscaling (HPA) based on CPU load.

**Key Features:**

  * Dockerized FastAPI app that loads CPU on request.

  * Deployment on Minikube or any managed Kubernetes cluster.

  * HPA configuration based on CPU utilization.

  * Automatic scaling of replicas from 1 to 10 based on traffic.

  * Monitoring using `kubectl top` or Kubernetes dashboard.

**Deliverables:**

  * YAML files for deployment, service, and HPA.

  * Video demonstrating traffic-based scale-up/down.

  * Commands used and CPU load scripts.

[**Link to Task 4 Directory**](https://www.google.com/search?q=./Task4_K8s_HPA)

## Task 5: Binance WebSocket Price Precision Capture (BTC/ETH)

**Objective:** Consume live price updates from Binance WebSocket and persist accurately.

**Description:** This task involves connecting to Binance WebSocket to capture real-time price updates for BTC/USDT and ETH/USDT, and persisting this data accurately in a database.

**Key Features:**

  * Connection to Binance WebSocket for BTC/USDT and ETH/USDT.

  * Handling multi-millisecond updates.

  * Data storage with timestamp, symbol, and price.

  * Database design (PostgreSQL or InfluxDB preferred) to handle 1 day of data per pair.

  * Demonstrating queries for latest price, price at specific second, and highest/lowest in 1-minute intervals.

**Deliverables:**

  * WebSocket client (Node.js or Python).

  * DB schema and storage logic.

  * Query examples with output.

[**Link to Task 5 Directory**](https://www.google.com/search?q=./Task5_Binance_WebSocket)

## Task 6: Article + Scheme Scraper & Summary Report

**Objective:** Demonstrate scraping from dynamic and static sources and summarizing issues.

**Description:** This task focuses on building a web scraper for different targets (e.g., Microsoft Research Blog, MyScheme Portal) to extract article/scheme titles, links, and descriptions. It also includes handling pagination and providing a summary report on scraping challenges.

**Key Features:**

  * Scraping article/scheme titles, links, and descriptions.

  * Handling pagination/load more behavior.

  * Storing data in a structured format (JSON/CSV/DB).

  * Summary report on page structure challenges, anti-bot mechanisms, and data completeness.

**Deliverables:**

  * Scraper code (Python + Playwright/Scrapy).

  * Exported dataset.

  * Summary report and demo video.

[**Link to Task 6 Directory**](https://www.google.com/search?q=./Task6_Scraper_Report)

## Task 7: Multi-Agent Newsletter Generator using LangChain

**Objective:** Build an automated multi-agent system to create daily Telegram newsletters from top Web3 news sources.

**Description:** This task involves creating an automated system to scrape Web3 news, deduplicate articles, identify top articles, generate summaries using LangChain agents, compose newsletters, and automate daily pushes to a Telegram group.

**Key Features:**

  * Scraping from top 5 Web3 publications (CoinDesk, Coin Telegraph, Decrypt, Bankless, The Block).

  * Deduplication of similar news (cosine similarity/title match).

  * Identification of top 10 articles daily.

  * Summary generation via LangChain agents.

  * Newsletter composition (Header, Body, Footer).

  * Automation via scheduler (2+ days simulation).

  * Daily push to Telegram group via bot.

**Tech Used:**

  * LangChain agents + Pydantic validation.

  * Telegram Bot API.

  * Vector DB (optional).

**Deliverables:**

  * Scraper pipelines.

  * Newsletter samples (for 2 days).

  * Code, Readme, and Demo.

  * Telegram group invite for testing.

[**Link to Task 7 Directory**](https://www.google.com/search?q=./Task7_Newsletter_Generator)

## Conclusion

This repository represents a significant effort in demonstrating a wide range of backend engineering skills, from ML Ops and real-time data processing to robust access control and scalable infrastructure. Each task has been approached with a focus on best practices, clear documentation, and reproducible environments.
