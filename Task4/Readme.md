
```markdown
# 🚀 Kubernetes Pod Autoscaling with FastAPI 

This project demonstrates **Horizontal Pod Autoscaling (HPA)** in Kubernetes using a simple **FastAPI** app. The app is containerized with Docker, deployed to a Minikube cluster, and auto-scales based on CPU usage.

---

## 📁 Project Structure

```

Task4/
├── app/
│   ├── main.py              # FastAPI app
│   └── Dockerfile           # Container definition
│
├── ks8/
│   ├── deployment.yaml      # Kubernetes Deployment
│   ├── service.yaml         # ClusterIP Service
│   └── hpa.yaml             # Horizontal Pod Autoscaler
│
└── scripts/
└── load\_test.sh         # Bash script to simulate load

````

---

## ⚙️ Prerequisites

- Docker Desktop
- Minikube
- kubectl
- Git Bash (for Windows) or use PowerShell alternative

---

## 🚀 Setup & Deployment

### 1. Start Minikube

```bash
minikube start --cpus=4 --memory=4g
````

---

### 2. Build Docker Image on Host

```bash
docker build -t fastapi-cpu:latest ./app
```

---

### 3. Load Image into Minikube

```bash
minikube image load fastapi-cpu:latest --daemon
```

---

### 4. Deploy Kubernetes Resources

```bash
kubectl apply -f ks8/deployment.yaml
kubectl apply -f ks8/service.yaml
kubectl apply -f ks8/hpa.yaml
```

---

### 5. Access the FastAPI App

```bash
minikube service fastapi-service --url
```

This exposes the FastAPI app on a local port, e.g., `http://127.0.0.1:52326`

---

## 💻 Simulate Load to Trigger Autoscaling

### Option 1: PowerShell

```powershell
for ($i=0; $i -lt 100; $i++) {
    Invoke-WebRequest -Uri http://127.0.0.1:52326 -UseBasicParsing
}
```

### Option 2: Git Bash

```bash
bash scripts/load_test.sh http://127.0.0.1:52326
```

---

## 📊 Monitor Autoscaling Behavior

```bash
kubectl get pods -w
kubectl get hpa -w
kubectl top pods
```

The number of pods should increase when load increases and scale back down when idle.

---

## 🧠 How It Works

* The app exposes a root `/` endpoint via FastAPI.
* The Kubernetes Deployment sets CPU requests and limits.
* HPA is configured to maintain CPU below 50%.
* Sending traffic increases CPU usage, causing new pods to spawn automatically.

---

## 🛠 Tip: Simulate More CPU Load

Modify `main.py` for heavier processing:

```python
@app.get("/")
def read_root():
    x = 0
    for i in range(10**7):
        x += i*i
    return {"message": "Loaded"}
```

Rebuild and reload the image:

```bash
docker build -t fastapi-cpu:latest ./app
minikube image load fastapi-cpu:latest --daemon
kubectl delete deployment fastapi-cpu
kubectl apply -f ks8/deployment.yaml
```

---

## 📸 Recommended Demo Flow

1. Show code: `main.py`, `Dockerfile`, YAMLs
2. Build Docker image and load into Minikube
3. Deploy app and expose service
4. Simulate load using script/loop
5. Watch pods auto-scale using `kubectl get pods` and `kubectl get hpa`
6. Wrap up with explanation

---

## ✍️ Author

**Ankith**
