import cloudscraper
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

BASE_URL = "https://www.theblock.co"

def scrape_theblock():
    print("🌐 Visiting The Block homepage...")
    
    scraper = cloudscraper.create_scraper()
    response = scraper.get(BASE_URL)

    if response.status_code != 200:
        print(f"❌ Failed to fetch homepage: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.select("article.textCard.popularRail__item")

    print(f"✅ Found {len(articles)} article cards")
    data = []

    for card in articles[:5]:  # Limit to top 5
        try:
            link_tag = card.select_one("a.textCard__link")
            title_tag = link_tag.select_one("h2 span")
            meta_tag = card.select_one(".meta__wrapper")

            title = title_tag.get_text(strip=True) if title_tag else "No Title"
            relative_url = link_tag["href"]
            full_url = urljoin(BASE_URL, relative_url)
            published = meta_tag.get_text(strip=True) if meta_tag else ""

            # Visit article page
            article_res = scraper.get(full_url)
            article_soup = BeautifulSoup(article_res.text, "html.parser")
            content_block = article_soup.select_one("article.articleBody")
            content = content_block.get_text(separator="\n", strip=True) if content_block else "No content"

            data.append({
                "title": title,
                "url": full_url,
                "published": published,
                "content": content
            })

            print(f"🔗 Scraped: {title}")

        except Exception as e:
            print(f"⚠️ Skipping article due to error: {e}")

    # Save to JSON
    with open("theblock_latest_news.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("✅ Saved top 5 articles to 'theblock_latest_news.json'")

