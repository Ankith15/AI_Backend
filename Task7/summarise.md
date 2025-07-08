
```markdown
# 🧠 Summary: Multi-Agent Web3 Newsletter Generator 

## 📌 Objective
This project automates the generation of a **daily Web3 newsletter** using AI and news scraped from five top crypto websites. It performs:

- Web scraping from 5 sources
- Deduplication using semantic similarity
- Summarization using LLMs (Groq)
- PDF newsletter creation
- Telegram bot dispatch
- All automated via a daily scheduler

---

## 🗂️ Project Structure

```

Task7/
├── Scrapper/
│   ├── coindesk.py
│   ├── coin\_telegraph.py
│   ├── decrypt.py
│   ├── bankless.py
│   └── theblock.py
│
├── duplicator.py               # Deduplicates articles using cosine similarity
├── summarize.py                # Summarizes top 10 articles using LLM
├── generate\_newsletter.py      # Converts summaries to a formatted PDF
├── telegrambot.py              # Sends PDF via Telegram bot
├── scheduler.py                # Runs the entire pipeline daily
├── .env                        # Stores GROQ API key and Telegram credentials
├── requirements.txt            # All Python dependencies
├── summarized\_articles.json    # Output: summarized content
├── top10\_articles.json         # Output: deduplicated articles
├── newsletter.pdf              # Output: final newsletter PDF
└── summary.md                  # This file

```

---

## 🌍 Scraping (Scrapper/*.py)

Each scraper file targets one news site:
- `coindesk.py`
- `coin_telegraph.py`
- `decrypt.py`
- `bankless.py`
- `theblock.py`

Each script extracts:
- Title
- URL
- Published date
- Full content

These scripts **return Python lists of article dictionaries**, which are later consumed in the pipeline.

---

## 🧠 Deduplication (`duplicator.py`)

Combines all scraped articles and removes duplicates using:
- Exact title matching
- Cosine similarity on TF-IDF vectors of content

### Output:
- `top10_articles.json` — Top 10 most unique and relevant articles across all sources.

---

## ✍️ Summarization (`summarize.py`)

Summarizes the top 10 deduplicated articles using:
- `LangChain`
- `ChatGroq` (e.g., `llama3-70b-8192`)
- API key loaded from `.env` as `GROQ_API`

### Output:
- `summarized_articles.json` — Adds a `"summary"` field to each article.

---

## 📰 PDF Generation (`generate_newsletter.py`)

Uses `reportlab` to create a clean, formatted A4 newsletter:
- Includes title, source, and summary
- Title: bold and large
- Summary: paragraph form
- Footer with date

### Output:
- `newsletter.pdf` — Your final AI-curated Web3 newsletter.

---

## 📲 Telegram Bot (`telegrambot.py`)

Sends `newsletter.pdf` to a Telegram channel using:
- Telegram Bot API
- Bot token and chat ID from `.env`

### Required `.env` Variables:
```

GROQ\_API=your\_groq\_api\_key
BOT\_TOKEN=your\_telegram\_bot\_token
CHAT\_ID=your\_telegram\_chat\_id

````

---

## ⏱️ Automation (`scheduler.py`)

Runs the entire end-to-end pipeline **once per day** using the `schedule` library.

### It sequentially runs:
1. `summarize.py`
2. `generate_newsletter.py`
3. `telegrambot.py`

### How it works:
```python
schedule.every().day.at("08:00").do(job)
````

> You can change the time in `scheduler.py` to suit your timezone.

---

## 🛠️ How to Run

### Step-by-step (Manual):

```bash
# 1. Activate virtual environment
source venv/bin/activate  # Or .\venv\Scripts\activate on Windows

# 2. Install requirements
pip install -r requirements.txt

# 3. Run pipeline manually
python summarize.py
python generate_newsletter.py
python telegrambot.py
```

### Step-by-step (Automated):

```bash
# Run scheduler (keep it running in background or server)
python scheduler.py
```

---

## 🧪 Output Files

| File                       | Description                 |
| -------------------------- | --------------------------- |
| `top10_articles.json`      | Deduplicated articles       |
| `summarized_articles.json` | Articles with LLM summaries |
| `newsletter.pdf`           | Final daily newsletter      |

---

## 🔐 Environment Setup

`.env` file should include:

```dotenv
GROQ_API=your_groq_api_key
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_chat_id_or_channel_id
```

---

## 📦 Dependencies

Install all with:

```bash
pip install -r requirements.txt
```

### Key libraries:

* `langchain`
* `langchain-groq`
* `python-telegram-bot`
* `schedule`
* `reportlab`
* `scikit-learn`
* `beautifulsoup4`, `requests`

---

## ✅ Status

* [x] Scrapers working for all 5 sources
* [x] Deduplication via TF-IDF + cosine similarity
* [x] Summarization via Groq (LLM)
* [x] PDF generation with formatting
* [x] Telegram bot integration
* [x] Daily automation via `scheduler.py`

---

## 📽️ Video Demonstration Guide

You can refer to `README.md` for how to present this in a video format.

