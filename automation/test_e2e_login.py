# test_e2e_login.py
# E2E Test สำหรับ Login Feature
# ทดสอบที่: https://the-internet.herokuapp.com/login

from playwright.sync_api import Page, expect

# ✅ TC-01: Login สำเร็จด้วยข้อมูลถูกต้อง
def test_login_success(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("You logged into a secure area!")).to_be_visible()

# ✅ TC-02: Login ด้วย Password ผิด
def test_login_wrong_password(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("wrongpassword")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Your password is invalid!")).to_be_visible()

# ✅ TC-03: Login ด้วย Username ผิด
def test_login_wrong_username(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("wronguser")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Your username is invalid!")).to_be_visible()

# ✅ TC-06: Logout หลัง Login สำเร็จ
def test_logout(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Logout").click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")