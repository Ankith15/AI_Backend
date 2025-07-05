import os
import time
from datetime import datetime

# ✅ Full path to your venv's Python interpreter
PYTHON_PATH = r"F:\\machine learning\\Prodigal_Assignment\\venv\\Scripts\\python.exe"

def run_pipeline():
    print("\n🚀 Running daily Web3 newsletter pipeline...\n")

    # Step 1: Summarize articles using LLM
    os.system(f'"{PYTHON_PATH}" summarize.py')

    # Step 2: Generate PDF newsletter
    os.system(f'"{PYTHON_PATH}" generate_newsletter.py')

    # Step 3: Send newsletter via Telegram
    os.system(f'"{PYTHON_PATH}" telegrambot.py')

    print("\n✅ Newsletter pipeline completed.\n")

if __name__ == "__main__":
    print("📅 Scheduler started. Waiting for the next scheduled time...")

    while True:
        now = datetime.now()
        if now.hour == 9 and now.minute == 0:
            run_pipeline()
            time.sleep(60)  
        time.sleep(10)

    run_pipeline()
