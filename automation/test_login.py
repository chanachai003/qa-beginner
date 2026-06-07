# test_login.py
# ทดสอบ Logic ของระบบ Login อย่างง่าย

# ฟังก์ชันจำลองการ Login
def login(username, password):
    if username == "" or password == "":
        return "error: กรุณากรอกข้อมูลให้ครบ"
    if username == "admin" and password == "1234":
        return "success"
    return "error: username หรือ password ไม่ถูกต้อง"


# ✅ Test 1: Login สำเร็จด้วยข้อมูลถูกต้อง
def test_login_success():
    result = login("admin", "1234")
    assert result == "success"


# ✅ Test 2: Login ด้วย Password ผิด
def test_login_wrong_password():
    result = login("admin", "wrong")
    assert result == "error: username หรือ password ไม่ถูกต้อง"


# ✅ Test 3: Login ด้วย Username ว่างเปล่า
def test_login_empty_username():
    result = login("", "1234")
    assert result == "error: กรุณากรอกข้อมูลให้ครบ"


# ✅ Test 4: Login ด้วย Password ว่างเปล่า
def test_login_empty_password():
    result = login("admin", "")
    assert result == "error: กรุณากรอกข้อมูลให้ครบ"