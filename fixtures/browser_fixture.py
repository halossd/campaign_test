# tests/fixtures/browser_fixture.py

import pytest
from playwright.sync_api import sync_playwright
from utils.browser_helpers import dismiss_cookie_banner

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--window-position=0,0", "--window-size=1920,1080"]
        )
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        screen={"width": 1920, "height": 1080}
    )
    page = context.new_page()

    original_goto = page.goto

    def wrapped_goto(url, **kwargs):
        response = original_goto(url, **kwargs)
        page.wait_for_load_state("networkidle") 
        dismiss_cookie_banner(page)              
        return response

    page.goto = wrapped_goto
    
    yield page
    context.close()