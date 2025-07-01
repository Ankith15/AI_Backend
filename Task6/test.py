import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.google.com", timeout=30000)
        print("✅ Google loaded successfully")
        await browser.close()

asyncio.run(test())
