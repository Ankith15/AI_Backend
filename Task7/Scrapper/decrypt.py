import feedparser
import json
from bs4 import BeautifulSoup
from datetime import datetime
import requests

def scrape_decrypt_rss_full_content():
    feed_url = "https://decrypt.co/feed"
    feed = feedparser.parse(feed_url)
    articles = []

    print("🌐 Visiting Decrypt RSS feed...")
    for entry in feed.entries[:5]:  # top 5 articles
        title = entry.title
        url = entry.link
        published = entry.published if hasattr(entry, 'published') else datetime.utcnow().isoformat()

        print(f"🔗 Scraping: {title} | {url}")
        try:
            res = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(res.text, 'html.parser')

            # In brief section
            in_brief_section = soup.find("div", class_="pt-8 pb-10 border-t border-b border-decryptGridline")
            in_brief = []
            if in_brief_section:
                list_items = in_brief_section.find_all("li")
                in_brief = [li.get_text(strip=True) for li in list_items]

            # Main content
            paragraphs = soup.find_all("p", class_="font-meta-serif-pro scene:font-noto-sans scene:text-base scene:md:text-lg font-normal text-lg md:text-xl md:leading-9 tracking-px text-body gg-dark:text-neutral-100")
            content = "\n".join([p.get_text(strip=True) for p in paragraphs])

            if in_brief:
                content = "In Brief:\n" + "\n".join(f"- {pt}" for pt in in_brief) + "\n\n" + content

        except Exception as e:
            print(f"⚠️ Failed to fetch content: {e}")
            content = entry.summary

        articles.append({
            "title": title,
            "url": url,
            "published": published,
            "content": content,
            "source": "Decrypt"
        })

    return articles

if __name__ == "__main__":
    results = scrape_decrypt_rss_full_content()
    with open("decrypt_latest_news.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print("\n✅ Saved to 'decrypt_latest_news.json'")
