import nest_asyncio; nest_asyncio.apply()  # This is needed to use sync API in repl

from playwright.sync_api import sync_playwright

pw = sync_playwright().start()

chrome = pw.chromium.launch(headless=False)

page = chrome.new_page()

page.goto("https://twitch.tv")