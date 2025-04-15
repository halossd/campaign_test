import pytest
from utils.data_loader import load_json
from playwright.sync_api import expect

test_data = load_json("data/contact_inputs.json")

@pytest.mark.parametrize("user", test_data)
def test_contact_form(page, user):
    page.goto("https://ec-qa.subaru.jp/subaroad/contact")

    page.screenshot(path="results/screenshots/before_input.png", full_page=True)

    try:
        page.locator("text=同意する").click(timeout=3000)
    except:
        pass

    page.fill("#firstName", user["sei"])
    page.fill("#lastName", user["mei"])
    page.fill("#sei", user["seiKana"])
    page.fill("#mei", user["meiKana"])
    page.fill("#mailAdr", user["email"])
    page.fill("#goiken", user["goiken"])

    page.screenshot(path="results/screenshots/after_input.png", full_page=True)

    # 等待它在逻辑上“可点击”
    expect(page.locator("#kakuninBtn")).to_be_visible()
    expect(page.locator("#kakuninBtn")).to_be_enabled()

    # 再点击
    page.click("#kakuninBtn")

    page.wait_for_load_state("networkidle")
    assert page.locator("text=お問い合わせ内容確認").is_visible(timeout=5000)

    page.screenshot(path="results/screenshots/confirm.png", full_page=True)

    # page.click("#compleBtn")

    # page.wait_for_load_state("networkidle")

    # page.screenshot(path="results/screenshots/complete.png", full_page=True)