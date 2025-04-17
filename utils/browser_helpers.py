import logging

def dismiss_cookie_banner(page):
    cookie_selector = "#onetrust-banner-sdk"
    close_btn_selector = "button.banner-close-button"

    try:
        # 等待 cookie 框出现
        logging.info("🍪 等待 Cookie 条出现")
        page.wait_for_selector(cookie_selector, state="visible", timeout=8000)

        # 等 cookie 完全展开（动画完成）
        for _ in range(10):
            box = page.locator(cookie_selector).bounding_box()
            if box and box["height"] > 50:
                break
            page.wait_for_timeout(300)

        # 确保关闭按钮可以点击
        logging.info("🚫 准备点击 Cookie 关闭按钮")
        page.locator(close_btn_selector).click()

        # 等待 cookie 条消失
        page.wait_for_selector(cookie_selector, state="hidden", timeout=5000)

        logging.info("✅ Cookie 条已关闭")

    except Exception as e:
        logging.info(f"⚠️ Cookie 条未显示或关闭失败: {e}")