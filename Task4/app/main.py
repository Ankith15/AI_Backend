from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def root():
    start = time.time()
    while time.time() - start < 1.5:
        _ = [x**2 for x in range(10000)]
    return {"message": "CPU-intensive task completed"}
