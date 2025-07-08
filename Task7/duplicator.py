import json
from Scrapper.coindesk import scrape_coindesk_articles as scrape_coindesk
from Scrapper.coin_telegraph import scrape_cointelegraph_news as scrape_cointelegraph
from Scrapper.decrypt import scrape_decrypt_rss_full_content as scrape_decrypt
from Scrapper.bankless import scrape_bankless_news as scrape_bankless
from Scrapper.theblock import scrape_theblock as scrape_theblock

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def deduplicate_and_select_top_articles(articles):
    print(f"🔍 Deduplicating {len(articles)} articles...")
    seen = set()
    unique_articles = []

    for article in articles:
        title = article.get("title", "").strip()
        content = article.get("content", "").strip()
        key = (title.lower(), content[:100].lower())  

        if title and content and key not in seen:
            seen.add(key)
            unique_articles.append(article)

    print(f"✅ {len(unique_articles)} unique articles after deduplication.")

    texts = [a["content"] for a in unique_articles]
    if not texts:
        print("❌ No valid content to compute similarity.")
        return []

    # Compute TF-IDF and cosine similarity
    tfidf = TfidfVectorizer(stop_words="english").fit_transform(texts)
    sim_matrix = cosine_similarity(tfidf)
    scores = sim_matrix.sum(axis=1)

    # Attach similarity scores and sort
    for idx, score in enumerate(scores):
        unique_articles[idx]["similarity_score"] = float(score)

    sorted_articles = sorted(unique_articles, key=lambda x: x["similarity_score"], reverse=True)
    return sorted_articles[:10]


if __name__ == "__main__":
    print("🚀 Starting full deduplication pipeline...")

    # Step 1: Scrape each source safely
    coindesk_articles = scrape_coindesk() or []
    cointelegraph_articles = scrape_cointelegraph() or []
    decrypt_articles = scrape_decrypt() or []
    bankless_articles = scrape_bankless() or []
    theblock_articles = scrape_theblock() or []

    # Step 2: Combine all articles
    all_articles = (
        coindesk_articles +
        cointelegraph_articles +
        decrypt_articles +
        bankless_articles +
        theblock_articles
    )

    print(f"📦 Total articles scraped: {len(all_articles)}")

    # Step 3: Deduplicate and select top 10
    top_articles = deduplicate_and_select_top_articles(all_articles)

    # Step 4: Save to JSON
    with open("top10_articles.json", "w", encoding="utf-8") as f:
        json.dump(top_articles, f, ensure_ascii=False, indent=4)

    print("✅ Saved top 10 deduplicated articles to 'top10_articles.json'")
