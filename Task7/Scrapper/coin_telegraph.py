import json
from playwright.sync_api import sync_playwright
from datetime import datetime

def scrape_cointelegraph_news():
    base_url = "https://cointelegraph.com/category/latest-news"
    base = "https://cointelegraph.com"
    articles = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context(user_agent="Mozilla/5.0")
        page = context.new_page()

        page.goto(base_url, timeout=60000, wait_until="domcontentloaded")
        page.wait_for_timeout(3000)

        # Select news cards with links
        cards = page.query_selector_all("a.post-card-inline__title-link[href^='/news/']")
        print(f"✅ Found {len(cards)} articles")

        seen = set()
        urls = []

        for card in cards:
            title = card.inner_text().strip()
            href = card.get_attribute("href")
            full_url = base + href if href else None

            # Get image inside the same article card
            img_tag = card.evaluate_handle("node => node.closest('article')?.querySelector('img.lazy-image__img')")
            img_element = img_tag.as_element() if img_tag else None
            img_src = img_element.get_attribute("src") if img_element else None

            if not title or not href or title in seen:
                continue

            seen.add(title)
            urls.append((title, full_url, img_src))

            if len(urls) == 5:
                break

        for title, url, img in urls:
            print(f"\n🔗 Visiting: {url}")
            try:
                page.goto(url, timeout=60000, wait_until="domcontentloaded")
                page.wait_for_timeout(2000)

                # Full article content
                paragraphs = page.query_selector_all("div.post-content p")
                content = "\n".join([p.inner_text().strip() for p in paragraphs if p.inner_text().strip()])

                # Date
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
                    "image": img,
                    "source": "CoinTelegraph"
                })

            except Exception as e:
                print(f"⚠️ Failed on {url}: {e}")
                continue

        browser.close()

    return articles

