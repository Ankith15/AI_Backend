import os
import time
from datetime import datetime

PYTHON_PATH = r"F:\\machine learning\\Prodigal_Assignment\\venv\\Scripts\\python.exe"

def run_pipeline():
    print("\n🚀 Running daily Web3 newsletter pipeline...\n")

    os.system(f'"{PYTHON_PATH}" summarize.py')

    os.system(f'"{PYTHON_PATH}" generate_newsletter.py')

    os.system(f'"{PYTHON_PATH}" telegrambot.py')

    print("\n✅ Newsletter pipeline completed.\n")

if __name__ == "__main__":
    print("📅 Scheduler started. Waiting for the next scheduled time...")

    while True:
        now = datetime.now()
        if now.hour == 00 and now.minute == 10:
            run_pipeline()
            time.sleep(60)  
        time.sleep(10)

    run_pipeline()
