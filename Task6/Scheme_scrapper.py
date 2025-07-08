import asyncio
import json
from playwright.async_api import async_playwright

async def extract_qa_playwright(page):
    faq_data = {}
    try:
        blocks = await page.query_selector_all('div.py-4.first\\:pt-0.last\\:pb-0.undefined')
        for block in blocks:
            try:
                q_el = await block.query_selector('p.font-bold.dark\\:text-white.w-11\\/12')
                if not q_el:
                    continue
                question = (await q_el.text_content()).strip()
                await q_el.click()
                try:
                    await block.wait_for_selector("div.rounded-b.dark\\:text-gray-300.mt-3.block span[data-slate-string='true']", timeout=3000)
                except:
                    pass
                a_el = await block.query_selector("div.rounded-b.dark\\:text-gray-300.mt-3.block span[data-slate-string='true']")
                answer = (await a_el.text_content()).strip() if a_el else "Answer not found"
                faq_data[question] = answer
            except Exception as e:
                print(f"⚠️ Error processing FAQ block: {e}")
    except Exception as e:
        print(f"⚠️ FAQ section not found: {e}")
    return faq_data

async def scrape_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.myscheme.gov.in/search")
        await page.wait_for_selector("li.h-8.w-8")

        Data = {}
        scheme_id = 1
        for page_num in range(1, 6):  # Change range for more pages
            print(f"\n🔍 Scraping page {page_num}")
            if page_num > 1:
                try:
                    page_number = page.locator("li.h-8.w-8", has_text=str(page_num)).first
                    await page_number.click()
                    await page.wait_for_load_state("networkidle")
                    await page.wait_for_timeout(1000)
                except Exception as e:
                    print(f"❌ Failed to click page {page_num}: {e}")
                    continue

            await page.wait_for_selector("div.p-4.lg\\:p-8.w-full")
            card_locator = page.locator("div.p-4.lg\\:p-8.w-full")
            count = await card_locator.count()

            for i in range(count):
                card = card_locator.nth(i).locator("a")
                tit = await card.text_content()
                detail_page = await context.new_page()

                try:
                    url = await card.get_attribute("href")
                    if not url:
                        print(f"⚠️ No URL for card: {tit}")
                        await detail_page.close()
                        continue

                    full_url = "https://www.myscheme.gov.in" + url
                    await detail_page.goto(full_url)
                    await detail_page.wait_for_load_state("networkidle")

                    # Wait for content to be ready
                    try:
                        await detail_page.wait_for_selector("div.markdown-options", timeout=10000)
                    except:
                        print(f"⚠️ Content blocks not ready for: {tit}")

                    # Extract scheme details
                    title_elements = await detail_page.query_selector_all(
                        "div.grid.grid-cols-4.gap-2 > div.col-span-4.shadow-md.rounded-md.bg-white.dark\\:bg-dark.py-4 > div > div.overflow-x-auto.overflow-y-hidden.flex.flex-row.items-center.mb-2.border-0.border-b.border-solid.border-gray-200.pr-2.md\\:pr-4.no-scrollbar span"
                    )
                    info_elements = await detail_page.query_selector_all("div.markdown-options")

                    titles = [(await el.text_content()).strip() for el in title_elements]
                    infos = [(await el.text_content()).strip() for el in info_elements]

                    details_dict = {'scheme_id': scheme_id}
                    for j in range(min(len(titles), len(infos))):
                        details_dict[titles[j]] = infos[j]

                    # Extract FAQs
                    faq_data = await extract_qa_playwright(detail_page)
                    details_dict["Frequently Asked Questions"] = faq_data

                    Data[tit.strip()] = details_dict
                    scheme_id += 1

                except Exception as e:
                    print(f"❌ Error scraping scheme {tit}: {e}")
                finally:
                    await detail_page.close()

        await browser.close()
        with open("Schemes_scrapped.json", "w", encoding="utf-8") as f:
            json.dump(Data, f, indent=4, ensure_ascii=False)

        print(f"\n✅ Done. Total schemes scraped: {len(Data)}")

if __name__ == "__main__":
    asyncio.run(scrape_page())
