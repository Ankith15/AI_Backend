
````markdown
# 🧾 Project Summary

This project provides two powerful, Playwright-based web scrapers built in Python for extracting structured information from publicly available sources.

---

## 🏛️ MyScheme Government Scheme Scraper

This scraper navigates the [MyScheme.gov.in](https://www.myscheme.gov.in/search) portal to extract detailed information about Indian government welfare schemes. For each scheme, it captures:

- Scheme name
- Eligibility
- Benefits
- Application process
- Availability status
- Frequently Asked Questions (including dynamic, click-to-expand answers)

**Note:**  
🔹 By default, the scraper extracts data from only the **first 5 pages** of search results.  
To scrape more, update this line in `myscheme_scrape.py`:
```python
for page_num in range(1, 6):  # Change 6 to the desired number of pages
````

The scraped output is saved in a structured JSON file:
📄 `Schemes_scrapped.json`

---

## 🧠 Microsoft Research Blog Scraper

This scraper targets [Microsoft Research Blog](https://www.microsoft.com/en-us/research/blog), extracting detailed blog entries. It captures:

* Blog title and published date
* Authors (name, title, and profile URL)
* Section-wise blog content (each `<h2>` heading and its corresponding `<p>` content)

**Note:**
🔹 The script currently scrapes only **5 pages** of blog listings.
To extract all blogs, update this line in `microsoft_scrape.py`:

```python
max_pages = 5  # Increase to 142 or more as needed
```

The output is saved in:
📄 `microsoft_research_blogs.json`

---

## 📌 Output Format Highlights

* Both outputs are in JSON format, ideal for:

  * Chatbot fine-tuning
  * LLM-based Q\&A systems
  * Search pipelines
  * Policy recommendation engines

---

## ✅ Summary

These scrapers are designed to be:

* Asynchronous and fast via Playwright
* Resilient to missing or delayed content
* Modular and easily extensible

You can export results to CSV, feed them into LangChain or RAG pipelines, or integrate with your research and automation workflows.

```

