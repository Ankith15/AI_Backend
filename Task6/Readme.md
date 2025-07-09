
# 🔍 Web Scrapers for Public Data Extraction

```markdown

This repository contains two robust Python-based web scrapers built with **Playwright** for real-time structured data extraction:

1. 🏛️ **MyScheme Scraper** – Extracts Indian government scheme information, including eligibility, benefits, application process, and FAQs from [MyScheme.gov.in](https://www.myscheme.gov.in).
2. 🧠 **Microsoft Research Scraper** – Extracts detailed blog content from [Microsoft Research Blog](https://www.microsoft.com/en-us/research/blog), including titles, dates, authors, and section-wise insights.

---
```

## 📁 Project Structure


project/
│
├── myscheme\_scrape.py              # Scraper for MyScheme schemes
├── microsoft\_scrape.py             # Scraper for Microsoft blogs
├── Schemes\_scrapped.json           # Output: government schemes data
├── microsoft\_research\_blogs.json   # Output: research blog articles
├── README.md                       # Documentation
└── requirements.txt                # Python dependencies

````

---

## 🚀 Technologies Used

- [x] **Python 3.9+**
- [x] **Playwright**
- [x] **asyncio**
- [x] **JSON Output**
- [x] Structured logging and error handling

---

## 🏛️ 1. MyScheme Scraper

### 🔧 Features
- Handles paginated results on MyScheme.gov.in
- Clicks into each scheme detail page
- Extracts:
  - Eligibility, Benefits, How to Apply
  - Availability (via button presence)
  - Dynamically loaded FAQs (click-to-expand logic)

### 🧪 Run Instructions

```bash
# Activate your environment and install requirements
pip install playwright
playwright install

# Run the scraper
python myscheme_scrape.py
````

### 📦 Output Format (`Schemes_scrapped.json`)

```json
{
  "PMAY-U": {
    "scheme_id": 1,
    "Eligibility": "...",
    "Benefits": "...",
    "How to Apply": "...",
    "Frequently Asked Questions": {
      "What is PMAY-U?": "It provides subsidy on housing loans.",
      ...
    }
  }
}
```

---

## 🧠 2. Microsoft Research Blog Scraper

### 🔧 Features

* Scrapes paginated Microsoft Research blog listings
* Navigates to each blog post
* Extracts:

  * Title, Publication Date
  * Authors (name, profile URL, title)
  * Section-wise content: `<h2>` headings + next `<p>`
* Deduplicates blog URLs

### 🧪 Run Instructions

```bash
# Activate your environment and install requirements
pip install playwright
playwright install

# Run the scraper
python microsoft_scrape.py
```

### 📦 Output Format (`microsoft_research_blogs.json`)

```json
{
  "url": "https://www.microsoft.com/en-us/research/blog/...",
  "title": "New Breakthroughs in AI",
  "published_date": "July 7, 2025",
  "authors": [
    {
      "name": "Jane Doe",
      "url": "https://www.microsoft.com/en-us/research/people/janedoe/",
      "title": "Senior Scientist"
    }
  ],
  "section_content": {
    "Introduction": "Microsoft's new AI technique...",
    "Technical Contributions": "We used Transformer-based..."
  }
}
```
## Video's


Uploading Task6_Microsoft_scrapper.mp4…



Uploading Task6_scheme_scrapper.mp4…



---

## 🔄 Customization Options

* Adjust `max_pages = X` in either script to control how many paginated pages are scraped.
* Add CSV/PDF output using `pandas` or `pdfkit` if required.
* Easily integrate scraped data with LangChain or vector DBs (e.g., FAISS) for downstream NLP pipelines.

---

## ⚠️ Error Handling

* Both scripts implement:

  * `try/except` blocks for page-level and element-level failures
  * Timeout handling for dynamic content
  * Graceful fallback logging and continuation

---



