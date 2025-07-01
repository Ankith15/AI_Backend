import asyncio
import json
from playwright.async_api import async_playwright

BASE_URL = "https://www.microsoft.com/en-us/research/blog/page/{}/"

async def scrape_blog_details():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # use headless=True if needed
        context = await browser.new_context()
        page = await context.new_page()

        all_data = []
        seen_urls = set()
        max_pages = 142  # You can increase or decrease this based on actual total

        for page_number in range(1, max_pages + 1):
            url = BASE_URL.format(page_number)
            print(f"\n🌍 Scraping Page {page_number}: {url}")
            try:
                await page.goto(url)
                await page.wait_for_selector('article.card.material-card h3.h4 a', timeout=10000)
            except:
                print(f"❌ Skipping page {page_number}, failed to load.")
                continue

            blog_links = await page.query_selector_all('article.card.material-card h3.h4 a')
            print(f"📄 Found {len(blog_links)} blog links on this page")

            for link in blog_links:
                href = await link.get_attribute("href")
                if not href:
                    continue

                full_url = href if href.startswith("http") else f"https://www.microsoft.com{href}"
                if full_url in seen_urls:
                    continue
                seen_urls.add(full_url)

                blog_page = await context.new_page()
                try:
                    await blog_page.goto(full_url)
                    await blog_page.wait_for_load_state("domcontentloaded")

                    title_elem = await blog_page.query_selector('h1[itemprop="headline"]')
                    date_elem = await blog_page.query_selector('p.single-post__header-date time')
                    content_elem = await blog_page.query_selector('#main > div > div.row > div.col.col-12.col-lg-8.offset-lg-2')

                    title = (await title_elem.inner_text()).strip() if title_elem else "N/A"
                    date = (await date_elem.inner_text()).strip() if date_elem else "N/A"
                    content = (await content_elem.inner_text()).strip() if content_elem else "N/A"

                    all_data.append({
                        "url": full_url,
                        "title": title,
                        "published_date": date,
                        "content": content
                    })

                    print(f"✅ Scraped: {title}")
                except Exception as e:
                    print(f"❌ Error extracting {full_url}: {e}")
                finally:
                    await blog_page.close()

        await browser.close()

        # Save all data to JSON
        with open("microsoft_research_blogs.json", "w", encoding="utf-8") as f:
            json.dump(all_data, f, indent=4, ensure_ascii=False)

        print(f"\n✅ Done. Total blogs scraped: {len(all_data)}")

if __name__ == "__main__":
    asyncio.run(scrape_blog_details())
