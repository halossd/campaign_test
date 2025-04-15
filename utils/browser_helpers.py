def dismiss_cookie_banner(page):
    try:
        btn = page.locator('.banner-close-button')
        if btn.is_visible():
            btn.click()
            print("✅ Cookie banner dismissed.")
        else:
            print("ℹ️ Cookie banner not visible.")
    except Exception as e:
        print(f"⚠️ Failed to dismiss cookie banner: {e}")