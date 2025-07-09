
# 📰 Web3 Newsletter Automation with LLMs & Telegram Bot

This project automates the end-to-end pipeline for generating a **daily Web3 newsletter**, summarizing articles using **Groq’s Mixtral/LLama3 model**, generating a **PDF**, and posting it to **Telegram**.
Telegram Link: https://t.me/+AdPjFyXvxqIxMGJl
---

### 📌 Features

* 🔎 Scrapes the latest news from 5 major crypto sources:

  * CoinDesk
  * CoinTelegraph
  * Decrypt
  * Bankless
  * The Block
* 🧠 Deduplicates articles using **title + cosine similarity (TF-IDF)**.
* ✍️ Summarizes top 10 articles using **LangChain + Groq** LLMs.
* 📄 Generates a clean **PDF newsletter** with titles, summaries, and source info.
* 📤 Sends the newsletter directly to a **Telegram channel** or group.
* ⏰ Fully **automated with a scheduler**.

---

### 🗂 Folder Structure

```
Task7/
│
├── Scrapper/                   # All scraper scripts (1 per news source)
│   ├── coindesk.py
│   ├── coin_telegraph.py
│   ├── decrypt.py
│   ├── bankless.py
│   └── theblock.py
│
├── duplicator.py              # Deduplication & Top 10 selector
├── summarize.py               # Uses LangChain + Groq to summarize articles
├── generate_newsletter.py     # Converts summaries to a formatted PDF
├── telegrambot.py             # Sends PDF to Telegram
├── scheduler.py               # Automates all steps together
├── .env                       # API keys & secrets (not committed)
├── requirements.txt           # All necessary packages
└── README.md                  # This file
```

---

### ⚙️ Setup Instructions

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/web3-newsletter-automation.git
cd web3-newsletter-automation/Task7
```

#### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Set Up `.env` File

Create a `.env` file in the root of the `Task7/` directory with the following content:

```env
GROQ_API=your_groq_api_key
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

> 📝 You can get your Groq API key from [https://console.groq.com](https://console.groq.com)
> You can get your Telegram bot token from [BotFather](https://t.me/BotFather)
> Use `@getidsbot` on Telegram to get your chat ID.

---

### 🚀 How to Run

#### Step-by-Step (Manual):

```bash
python summarize.py                # Scrape, deduplicate, summarize articles
python generate_newsletter.py     # Create PDF
python telegrambot.py             # Send newsletter to Telegram
```

#### One-Click Scheduler (Automated Pipeline):

```bash
python scheduler.py
```

You can uncomment the `while True` loop in `scheduler.py` to run it daily at a scheduled time.

---

### ✅ Output

* `summarized_articles.json`: Summarized top 10 articles with metadata
* `daily_newsletter.pdf`: Final newsletter sent to Telegram

---

### 📦 requirements.txt

```txt
langchain>=0.1.20
langchain-core>=0.1.44
langchain-community>=0.0.30
langchain-groq>=0.0.3
openai
groq
python-dotenv
scikit-learn
requests
beautifulsoup4
feedparser
reportlab
python-telegram-bot==20.7
```

---

### 📌 Future Improvements

* Add a UI dashboard (e.g., Streamlit) for on-demand newsletter generation
* Add newsletter email delivery
* Add sentiment analysis per article
* Expand to include real-time token stats or charts

