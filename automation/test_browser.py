# test_browser.py
# Test แรก — เปิดเว็บและตรวจสอบ Title

from playwright.sync_api import Page

# ✅ Test 1: เปิดเว็บและตรวจสอบ Title
def test_homepage_title(page: Page):
    page.goto("https://the-internet.herokuapp.com")
    assert "The Internet" in page.title()

# ✅ Test 2: ตรวจสอบว่าหน้าเว็บโหลดได้
def test_homepage_loads(page: Page):
    page.goto("https://the-internet.herokuapp.com")
    assert page.url == "https://the-internet.herokuapp.com/"