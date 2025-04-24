import logging

def dismiss_cookie_banner(page):
    cookie_selector = "#onetrust-banner-sdk"
    close_btn_selector = "button.banner-close-button"

    try:
        # wait cookie appear
        logging.info("🍪 wait Cookie showing")
        page.wait_for_selector(cookie_selector, state="visible", timeout=8000)

        # wait cookie complete viewable
        for _ in range(10):
            box = page.locator(cookie_selector).bounding_box()
            if box and box["height"] > 50:
                break
            page.wait_for_timeout(300)

        # ensure clost button clickable
        logging.info("🚫 prepare Cookie colse button")
        page.locator(close_btn_selector).click()

        # wait cookie disappear
        page.wait_for_selector(cookie_selector, state="hidden", timeout=5000)

        logging.info("✅ Cookie closed")

    except Exception as e:
        logging.info(f"⚠️ Cookie unshown or close failed: {e}")