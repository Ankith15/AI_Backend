import json
from playwright.sync_api import sync_playwright
from datetime import datetime

def scrape_latest_crypto_news():
    articles = []
    base_url = "https://www.coindesk.com"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context(user_agent="Mozilla/5.0")
        page = context.new_page()

        page.goto(base_url, timeout=60000, wait_until="domcontentloaded")
        page.wait_for_timeout(3000)

        news_links = page.query_selector_all("div.grid a[href^='/']")
        print(f"✅ Found {len(news_links)} possible news articles")

        seen = set()
        urls = []

        for a in news_links:
            title_el = a.query_selector("div.line-clamp-2")
            href = a.get_attribute("href")

            if not title_el or not href:
                continue

            title = title_el.inner_text().strip()
            full_url = base_url + href

            if title in seen:
                continue
            seen.add(title)
            urls.append((title, full_url))

            if len(urls) == 5:
                break

        for title, url in urls:
            print(f"\n🔗 Visiting: {url}")
            try:
                page.goto(url, timeout=60000, wait_until="domcontentloaded")
                page.wait_for_timeout(2000)

                paragraphs = page.query_selector_all("div article p")
                content = "\n".join([p.inner_text().strip() for p in paragraphs if p.inner_text().strip()])

                try:
                    time_tag = page.query_selector("time")
                    published = time_tag.get_attribute("datetime") if time_tag else datetime.utcnow().isoformat()
                except:
                    published = datetime.utcnow().isoformat()

                articles.append({
                    "title": title,
                    "url": url,
                    "published": published,
                    "content": content,
                    "source": "CoinDesk"
                })

            except Exception as e:
                print(f"⚠️ Failed on {url}: {e}")
                continue

        browser.close()

    return articles


if __name__ == "__main__":
    results = scrape_latest_crypto_news()

    # ✅ Save to JSON
    with open("coindesk_latest_news.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print("\n✅ Saved to 'coindesk_latest_news.json'")
