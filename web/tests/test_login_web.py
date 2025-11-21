# file: test_login_web.py
# Simple login test using Playwright + Python

from playwright.sync_api import sync_playwright, expect

def test_login_success():
    with sync_playwright() as p:
        # 1. Launch browser
        browser = p.chromium.launch(headless=False)  # headless=True for background mode
        page = browser.new_page()

        # 2. Open login page (replace with real test URL if you have one)
        page.goto("https://example-login-page.com")

        # 3. Enter username and password
        page.get_by_placeholder("Email").fill("testuser@example.com")
        page.get_by_placeholder("Password").fill("CorrectPassword123")

        # 4. Click login button
        page.get_by_role("button", name="Login").click()

        # 5. Assert login success
        expect

