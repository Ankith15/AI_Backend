import json
from playwright.sync_api import sync_playwright
from datetime import datetime
from urllib.parse import urlparse

def is_valid_bankless_url(url):
    return url and "bankless.com" in url and "/share" not in url

def scrape_bankless_news():
    root_url = "https://www.bankless.com/"
    articles = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print("🌐 Visiting Bankless homepage...")
        page.goto(root_url, timeout=60000)
        page.wait_for_timeout(4000)

        # ✅ Step 1: Collect all hrefs (safely)
        raw_links = page.query_selector_all(".contentGroupCard a[href]")
        hrefs = []

        for el in raw_links:
            href = el.get_attribute("href")
            if href:
                full_url = href if href.startswith("http") else "https://www.bankless.com" + href
                if is_valid_bankless_url(full_url):
                    hrefs.append(full_url)

        print(f"✅ Found {len(hrefs)} valid article URLs")

        seen = set()
        count = 0

        for url in hrefs:
            if url in seen:
                continue
            seen.add(url)

            try:
                print(f"🔗 Visiting: {url}")
                page.goto(url, timeout=60000)
                page.wait_for_timeout(3000)

                title_el = page.query_selector("h1")
                title = title_el.inner_text().strip() if title_el else "Untitled"

                meta_el = page.query_selector("span.meta")
                published = meta_el.inner_text().strip() if meta_el else datetime.now().isoformat()

                # All relevant selectors
                content_els = page.query_selector_all("div#insideEpisode p, div#insideEpisode li, div#insideEpisode span, article p")
                content = "\n".join([c.inner_text().strip() for c in content_els if c.inner_text().strip()])

                if not content:
                    print("⚠️ No content found, skipping.")
                    continue

                articles.append({
                    "title": title,
                    "url": url,
                    "published": published,
                    "content": content,
                    "source": "Bankless"
                })

                count += 1
                if count == 5:
                    break

            except Exception as e:
                print(f"⚠️ Failed on {url}: {e}")
                continue

        browser.close()

    return articles


if __name__ == "__main__":
    results = scrape_bankless_news()
    with open("bankless_latest_news.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    print("✅ Saved top 5 Bankless articles to 'bankless_latest_news.json'")
