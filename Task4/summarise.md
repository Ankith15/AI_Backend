```markdown
# 📌 Summary – Kubernetes Pod Autoscaling with FastAPI

This project demonstrates **Kubernetes Horizontal Pod Autoscaling (HPA)** by deploying a lightweight **FastAPI** application to a local **Minikube** cluster. It includes a load simulation script to trigger autoscaling and showcases real-time pod scaling based on CPU usage.

---

## ✅ Objectives Achieved

- ✅ Containerized a FastAPI app using Docker.
- ✅ Deployed the app to a Minikube-based Kubernetes cluster.
- ✅ Exposed the app using a ClusterIP Kubernetes Service.
- ✅ Configured resource `requests` and `limits` in the deployment.
- ✅ Enabled Horizontal Pod Autoscaler (HPA) based on CPU usage.
- ✅ Simulated CPU load to auto-scale pods in real-time.

---

## 📁 Project Structure

```

Task4/
├── app/
│   ├── main.py              # FastAPI app
│   └── Dockerfile           # Docker container definition
│
├── ks8/
│   ├── deployment.yaml      # Kubernetes Deployment config
│   ├── service.yaml         # ClusterIP Service definition
│   └── hpa.yaml             # Horizontal Pod Autoscaler definition
│
└── scripts/
└── load\_test.sh         # Bash script to simulate HTTP load

````

---

## ⚙️ Stack Used

| Component        | Tool / Tech        |
|------------------|--------------------|
| Web Framework     | FastAPI (Python)   |
| Containerization  | Docker             |
| Orchestration     | Kubernetes (Minikube) |
| Autoscaling       | Kubernetes HPA     |
| Load Simulation   | PowerShell loop / Bash script |
| Monitoring        | `kubectl` + `metrics-server` |

---

## 🚀 How to Run the Project (Locally)

### 1. Start Minikube Cluster

```bash
minikube start --cpus=4 --memory=4g
````

---

### 2. Build Docker Image & Load to Minikube

```bash
cd app/
docker build -t fastapi-cpu:latest .
minikube image load fastapi-cpu:latest --daemon
```

---

### 3. Apply Kubernetes Resources

```bash
cd ../ks8/
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml
```

---

### 4. Access the FastAPI App

```bash
minikube service fastapi-service --url
```

Paste the URL (e.g., `http://127.0.0.1:58761`) in a browser to confirm it's running.

---

### 5. Simulate Load (PowerShell or Bash)

#### PowerShell:

```powershell
for ($i=0; $i -lt 100; $i++) {
    Invoke-WebRequest -Uri http://127.0.0.1:PORT -UseBasicParsing
}
```

Replace `PORT` with your Minikube service port.

---

### 6. Observe Autoscaling

```bash
kubectl get pods -w
kubectl get hpa -w
kubectl top pods
```

The number of pods will increase (scale-out) as CPU usage exceeds the target (50%).

---

## 📊 How Autoscaling Works

* The **FastAPI** route simulates a CPU-intensive task to increase load.
* The **deployment** includes CPU resource `requests` and `limits`.
* The **HPA** is set to maintain 50% CPU usage.
* On load, HPA increases replicas to handle traffic.
* After cooldown, the number of pods reduces automatically.

---

## 🧪 FastAPI App Logic (main.py)

```python
@app.get("/")
def read_root():
    x = 0
    for i in range(10**7):
        x += i*i
    return {"message": "CPU-intensive task completed"}
```

This loop simulates CPU usage for each request to help trigger autoscaling.

---

## 🧩 Result Snapshot

### FastAPI Response

```json
{
  "message": "CPU-intensive task completed"
}
```

### Sample HPA Output:

```bash
kubectl get hpa

NAME          TARGETS       REPLICAS
fastapi-hpa   63% / 50%     3
```

---

## 🎥 Suggested Demo Flow

1. Show the folder structure & FastAPI app.
2. Start Minikube and build the Docker image.
3. Load the image into Minikube.
4. Deploy all Kubernetes resources.
5. Open the app URL and show output.
6. Simulate traffic using PowerShell.
7. Display real-time scaling via `kubectl get pods -w` and `kubectl get hpa`.

---
