import asyncio
import json
from playwright.async_api import async_playwright

BASE_URL = "https://www.microsoft.com/en-us/research/blog/page/{}"

async def scrape_microsoft_blogs():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Set to True for headless scraping
        context = await browser.new_context()
        page = await context.new_page()

        all_blogs = []
        seen_urls = set()
        max_pages = 5  # Change to 142 or more to scrape full site

        for page_num in range(1, max_pages + 1):
            page_url = BASE_URL.format(page_num)
            print(f"\n🌍 Scraping listing page {page_num}: {page_url}")
            try:
                await page.goto(page_url, timeout=60000)
                await page.wait_for_selector("article h3 > a[href*='/en-us/research/blog/']", timeout=15000)
            except Exception as e:
                print(f"❌ Failed to load listing page {page_num}: {e}")
                continue

            links = await page.query_selector_all("article h3 > a[href*='/en-us/research/blog/']")
            print(f"🔗 Found {len(links)} blog post links")

            for link in links:
                href = await link.get_attribute("href")
                if not href:
                    continue

                full_url = href if href.startswith("http") else f"https://www.microsoft.com{href}"
                if full_url in seen_urls:
                    continue
                seen_urls.add(full_url)

                blog_page = await context.new_page()
                try:
                    await blog_page.goto(full_url, timeout=30000)
                    await blog_page.wait_for_load_state("domcontentloaded")

                    title_el = await blog_page.query_selector("h1")
                    date_el = await blog_page.query_selector("time")

                    title = (await title_el.inner_text()).strip() if title_el else "N/A"
                    date = (await date_el.inner_text()).strip() if date_el else "N/A"

                    author_section = await blog_page.query_selector("p.single-post__header-authors")
                    authors = []
                    if author_section:
                        author_nodes = await author_section.query_selector_all("span.msr-authors-list--author")
                        for node in author_nodes:
                            name_el = await node.query_selector("span[itemprop='author']")
                            name = (await name_el.inner_text()).strip() if name_el else "N/A"

                            url_el = await node.query_selector("a.msr-authors-list--url")
                            url = await url_el.get_attribute("href") if url_el else "N/A"

                            title_el = await node.query_selector("span.msr-authors-list--title")
                            title_text = (await title_el.inner_text()).strip() if title_el else "N/A"

                            authors.append({
                                "name": name,
                                "url": url,
                                "title": title_text
                            })

                    headings = await blog_page.query_selector_all("h2.wp-block-heading")
                    content_map = {}

                    for heading in headings:
                        heading_text = (await heading.inner_text()).strip()

                        next_para = await heading.evaluate_handle(
                            """(el) => {
                                let next = el.nextElementSibling;
                                while (next && next.tagName !== 'P') {
                                    next = next.nextElementSibling;
                                }
                                return next;
                            }"""
                        )
                        element = next_para.as_element()
                        if element:
                            content = await element.inner_text()
                            content_map[heading_text] = content.strip()
                        else:
                            content_map[heading_text] = ""

                    blog_data = {
                        "url": full_url,
                        "title": title,
                        "published_date": date,
                        "authors": authors,
                        "section_content": content_map
                    }

                    all_blogs.append(blog_data)
                    print(f"✅ Scraped: {title}")

                except Exception as e:
                    print(f"❌ Failed to scrape blog {full_url}: {e}")
                finally:
                    await blog_page.close()

        await browser.close()

        with open("microsoft_research_blogs.json", "w", encoding="utf-8") as f:
            json.dump(all_blogs, f, indent=4, ensure_ascii=False)

        print(f"\n✅ Done. Total blogs scraped: {len(all_blogs)}")

if __name__ == "__main__":
    asyncio.run(scrape_microsoft_blogs())
