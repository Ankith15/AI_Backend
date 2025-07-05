import os
import asyncio
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
PDF_FILE = "daily_newsletter.pdf"

async def send_pdf():
    if not BOT_TOKEN or not CHAT_ID:
        raise ValueError("❌ BOT_TOKEN or CHAT_ID not found in .env")

    bot = Bot(token=BOT_TOKEN)

    with open(PDF_FILE, "rb") as pdf:
        await bot.send_document(chat_id=CHAT_ID, document=pdf, caption="📰 Web3 Daily Digest")

    print("✅ Newsletter sent via Telegram.")

if __name__ == "__main__":
    asyncio.run(send_pdf())
