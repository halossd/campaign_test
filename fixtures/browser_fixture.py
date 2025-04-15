# tests/fixtures/browser_fixture.py

import pytest
from playwright.sync_api import sync_playwright
from utils.browser_helpers import dismiss_cookie_banner

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
        )
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(viewport=None)
    page = context.new_page()

    original_goto = page.goto

    def wrapped_goto(url, **kwargs):
        response = original_goto(url, **kwargs)

        dismiss_cookie_banner(page)

        try:
            page.wait_for_selector("#onetrust-banner-sdk", state="hidden", timeout=5000)
            print("✅ Cookie banner container hidden.")
        except Exception as e:
            print(f"⚠️ Cookie banner did not disappear: {e}")

        return response

    page.goto = wrapped_goto
    
    yield page
    context.close()