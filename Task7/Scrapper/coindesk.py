import requests
from bs4 import BeautifulSoup
from newspaper import Article
import json

def scrape_coindesk_articles():
    rss_url = "https://www.coindesk.com/arc/outboundfeeds/rss/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(rss_url, headers=headers)
    soup = BeautifulSoup(response.content, "xml")
    items = soup.find_all("item")[:5]

    articles = []

    for item in items:
        title = item.title.text.strip()
        link = item.link.text.strip()
        pub_date = item.pubDate.text.strip()

        print(f"🔗 Extracting: {link}")
        try:
            article = Article(link)
            article.download()
            article.parse()

            content = article.text.strip()

            articles.append({
                "title": title,
                "url": link,
                "published": pub_date,
                "content": content,
                "source": "CoinDesk"
            })
        except Exception as e:
            print(f"⚠️ Failed to extract: {e}")
            continue

    with open("coindesk_latest_news.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=4, ensure_ascii=False)

    print("✅ Saved to 'coindesk_latest_news.json'")

