import os
import json
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

from duplicator import deduplicate_and_select_top_articles
from Scrapper.coindesk import scrape_coindesk_articles as scrape_coindesk
from Scrapper.coin_telegraph import scrape_cointelegraph_news as scrape_cointelegraph
from Scrapper.decrypt import scrape_decrypt_rss_full_content as scrape_decrypt
from Scrapper.bankless import scrape_bankless_news as scrape_bankless
from Scrapper.theblock import scrape_theblock as scrape_theblock

# Load GROQ API Key
load_dotenv()
groq_api_key = os.getenv("GROQ_API")

if not groq_api_key:
    raise ValueError("❌ GROQ_API not found in .env file.")

# Initialize LLM
llm = ChatGroq(
    api_key=groq_api_key,
    model="mixtral-8x7b-32768",  # You can also use "llama3-70b-8192"
)

prompt = ChatPromptTemplate.from_template("""
Summarize the following crypto news article in a concise paragraph:
"{article}"
""")

chain = prompt | llm | StrOutputParser()

def main():
    print("🚀 Scraping and deduplicating articles...")
    coindesk_articles = scrape_coindesk() or []
    cointelegraph_articles = scrape_cointelegraph() or []
    decrypt_articles = scrape_decrypt() or []
    bankless_articles = scrape_bankless() or []
    theblock_articles = scrape_theblock() or []

    all_articles = (
        coindesk_articles +
        cointelegraph_articles +
        decrypt_articles +
        bankless_articles +
        theblock_articles
    )

    top_articles = deduplicate_and_select_top_articles(all_articles)
    summarized_articles = []

    print("🧠 Generating summaries...")

    for article in top_articles:
        try:
            content = article["content"]
            summary = chain.invoke({"article": content})
        except Exception as e:
            summary = f"Summary failed: {e}"
        article["summary"] = summary
        summarized_articles.append(article)
        print(f"✅ Summarized: {article['title']}")

    # Save to JSON
    with open("summarized_articles.json", "w", encoding="utf-8") as f:
        json.dump(summarized_articles, f, ensure_ascii=False, indent=4)

    print("📄 Saved summarized articles to 'summarized_articles.json'")


if __name__ == "__main__":
    main()
