from playwright.sync_api import sync_playwright


with sync_playwright() as pw:
    # create browser instance
    browser = pw.chromium.launch(
        # we can choose either a Headful (With GUI) or Headless mode:
        headless=False,
    )
    # create context
    # using context we can define page properties like viewport dimensions
    context = browser.new_context(
        # most common desktop viewport is 1920x1080
        viewport={"width": 1920, "height": 1080}
    )
    # create page aka browser tab which we'll be using to do everything
    page = context.new_page()
    
    # go to url
    page.goto("https://twitch.tv/directory/game/Art")
    # get HTML
    print(page.content())