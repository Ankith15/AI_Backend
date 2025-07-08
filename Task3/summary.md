````markdown
# 📊 Real-Time High-Throughput Event Ingestion Pipeline

This project implements a **real-time, scalable, and high-throughput event ingestion system** using **Apache Kafka**, **Flask**, and **Python**. The system is designed to simulate, collect, and process a large volume of user-generated events in a production-ready architecture.

---

## 🚀 Project Objective

The goal is to demonstrate an end-to-end backend pipeline capable of:
- Receiving thousands of concurrent events via an HTTP API
- Forwarding events into a Kafka message broker
- Consuming and logging the events in real time with high reliability

This architecture models real-world use cases such as logging user activity, processing transaction events, or tracking system metrics at scale.

---

## 🧱 System Architecture

```plaintext
[ Event Simulator ] 
        │
     (POST)
        ▼
  ┌─────────────┐       Kafka Broker       ┌─────────────────┐
  │ Flask API   │ ───────────────────────▶ │ Kafka Consumer   │
  │ (Producer)  │                         │ (Logger)         │
  └─────────────┘                         └─────────────────┘
        │                                        │
        ▼                                        ▼
Kafka Topic: "events"                  logs/events.log
````

---

## 🔧 Tech Stack

| Component        | Technology             |
| ---------------- | ---------------------- |
| API Layer        | Flask (Python)         |
| Messaging Queue  | Apache Kafka           |
| Threaded Testing | Python `threading`     |
| Containerization | Docker, Docker Compose |
| Event Logging    | Python Logging         |

---

## ✨ Features

* Accepts **10,000+ events** via concurrent HTTP requests
* Event ingestion via **Flask API endpoint** (`/register_event`)
* **Asynchronous event streaming** using Kafka
* **Real-time consumer** that logs every event to disk
* Clean and modular codebase, suitable for real-world extensions
* Built-in **load simulator** for stress testing

---

## 🔄 Workflow

1. The API receives events via `/register_event` (JSON POST).
2. The event is published to the `events` Kafka topic.
3. The consumer app listens to the topic and logs the events.
4. All events are saved in `logs/events.log` with timestamps.

---

## 🧪 Load Simulation

To simulate high-throughput scenarios, the system includes a multithreaded testing script (`simulate_requests.py`) that:

* Spawns **200 threads**
* Sends **10,000 POST requests** concurrently
* Measures the total duration of ingestion

This allows you to validate Kafka’s performance and bottleneck handling under pressure.

---

## 🧰 Folder Structure

```plaintext
project-root/
├── docker-compose.yml         # Kafka + Zookeeper setup
├── producer_app/
│   ├── app.py                 # Flask API producer
│   └── simulate_requests.py   # High-load event simulator
├── consumer_app/
│   ├── consumer.py            # Kafka event logger
│   └── .env                   # Kafka topic and broker config
├── logs/
│   └── events.log             # Output log file
└── README.md / summary.md     # Documentation
```

---

## ▶️ How to Run the System

### 1. Start Docker Services

```bash
docker-compose up -d
```

### 2. Start the Kafka Consumer

```bash
cd consumer_app
python consumer.py
```

### 3. Start the Flask API

```bash
cd producer_app
python app.py
```

### 4. (Optional) Test with a Manual Event

```bash
curl -X POST http://127.0.0.1:5000/register_event \
     -H "Content-Type: application/json" \
     -d "{\"event\": \"login\", \"user_id\": 42}"
```

### 5. Run the Load Simulator

```bash
cd producer_app
python simulate_requests.py
```

---

## 📈 Sample Output

**Flask Output:**

```plaintext
✅ Event sent to Kafka: {'event': 'login', 'user_id': 42, 'timestamp': ...}
```

**Consumer Output:**

```plaintext
📥 Received event: {'event': 'login', 'user_id': 42, 'timestamp': ...}
```

**Simulator Output:**

```plaintext
🚀 Sending 10000 requests with 200 threads...
✅ Finished in 54.2 seconds.
```

---

## 📁 Log Format

Logs are written to `logs/events.log` in the format:

```plaintext
2025-07-08 00:12:01,782 - {"event": "purchase", "user_id": 203, "timestamp": "2025-07-08T00:12:01.781Z"}
```

---

## 📌 Key Highlights

* Fully Dockerized Kafka broker and Zookeeper
* Decoupled microservices (producer and consumer)
* Threaded simulator for performance validation
* Clean separation of concerns and environment configs
* Simple to extend with authentication, storage, or dashboards

---

## ✅ Potential Enhancements

* Add authentication to the Flask API
* Forward consumed events to a database or data lake
* Add Prometheus + Grafana for monitoring
* Build a real-time dashboard with WebSocket updates

---

```
