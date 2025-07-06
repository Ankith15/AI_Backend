````markdown
# 🚀 Kafka High-Throughput Event Ingestion System

A scalable, event-driven backend system built with **Flask**, **Apache Kafka**, and **Python** to simulate and handle high-throughput event ingestion and processing.

---

## 📌 Overview

This project demonstrates a robust architecture for handling real-time event ingestion at scale. It features:
- A **Flask API** that accepts incoming user events
- **Apache Kafka** for event streaming and message brokering
- A **Kafka consumer** that listens, logs, and processes events
- A **simulator** that stress-tests the system with 10,000+ concurrent requests

---

## ⚙️ Architecture

```plaintext
           [ simulate_requests.py ]
                     │
                 (POST 10K events)
                     ▼
              ┌────────────────┐
              │   Flask API    │
              │ (Producer App) │
              └────────────────┘
                     │
              Kafka Topic: "events"
                     │
              ┌────────────────┐
              │  KafkaConsumer │
              │ (Consumer App) │
              └────────────────┘
                     │
              logs/events.log
````

---

## 🛠️ Tech Stack

| Component        | Technology                              |
| ---------------- | --------------------------------------- |
| API              | Flask                                   |
| Messaging        | Apache Kafka                            |
| Concurrency      | Threading (Python)                      |
| Containerization | Docker + Docker Compose                 |
| Testing Tool     | `simulate_requests.py` with 200 threads |

---

## 🚀 Getting Started

### 1️⃣ Clone the repository & activate virtual environment

```bash
cd Task3
.\venv\Scripts\activate     # For Windows
# or
source venv/bin/activate    # For Mac/Linux
```

---

### 2️⃣ Start Kafka + Zookeeper (Docker)

```bash
docker-compose up -d
```

> Wait 10–15 seconds for services to stabilize

---

### 3️⃣ Start the Kafka Consumer

```bash
cd consumer_app
python consumer.py
```

---

### 4️⃣ Start the Flask API Producer

Open a **new terminal**:

```bash
cd producer_app
python app.py
```

---

### 5️⃣ (Optional) Manually Test the API

```bash
curl -X POST http://127.0.0.1:5000/register_event \
     -H "Content-Type: application/json" \
     -d "{\"event\": \"signup\", \"user_id\": 123}"
```

---

### 6️⃣ Run the Load Simulator

Open another terminal (or use the Flask one):

```bash
python simulate_requests.py
```

Expected Output:

```
✅ Finished in ~60 seconds
```

---

## 📁 Folder Structure

```plaintext
Task3/
├── docker-compose.yml
├── producer_app/
│   ├── app.py
│   └── simulate_requests.py
├── consumer_app/
│   └── consumer.py
├── logs/
│   └── events.log
```

---

## 📒 Logs

All received events are logged in:

```bash
logs/events.log
```

Each log entry looks like:

```json
2025-07-06 23:18:56,847 - {"event": "purchase", "user_id": 1432, "timestamp": ...}
```

---

## ✅ Features

* Handles 10,000+ concurrent event requests
* Real-time ingestion and logging
* Configurable Kafka and topic setup
* Modular and production-ready codebase

---

## 📌 Requirements

* Python 3.8+
* Docker & Docker Compose
* Virtualenv (optional but recommended)

