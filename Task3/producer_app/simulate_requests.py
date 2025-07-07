import requests
import json
import time
import random
from concurrent.futures import ThreadPoolExecutor

URL = "http://localhost:5000/register_event"

def send_event(i):
    data = {
        "event": random.choice(["login", "logout", "signup", "purchase"]),
        "user_id": random.randint(1000, 9999),
        "timestamp": time.time(),
        "request_id": i
    }
    try:
        response = requests.post(URL, json=data)
        if response.status_code != 200:
            print(f"❌ Failed: {response.text}")
    except Exception as e:
        print(f"❗Error: {e}")

if __name__ == "__main__":
    num_requests = 5000
    max_workers = 200  # Number of threads

    start = time.time()
    print(f"🚀 Sending {num_requests} requests with {max_workers} threads...")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(send_event, range(num_requests))

    end = time.time()
    print(f"✅ Finished in {round(end - start, 2)} seconds.")
