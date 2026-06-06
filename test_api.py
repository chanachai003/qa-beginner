# test_api.py
# ทดสอบ JSONPlaceholder API ด้วย pytest

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# ✅ Test 1: GET users สำเร็จ - Status 200
def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200

# ✅ Test 2: GET user ต้องมี field 'name'
def test_get_user_has_name():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data

# ✅ Test 3: GET user ที่ไม่พบ - ต้องได้ Status 404
def test_get_nonexistent_user():
    response = requests.get(f"{BASE_URL}/users/999")
    assert response.status_code == 404

# ✅ Test 4: POST user สร้างโพสต์ใหม่สำเร็จ - ต้องได้ Status 201
def test_create_post():
    payload = {
        "title": "ทดสอบสร้างโพสต์",
        "body": "เนื้อหาโพสต์",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201

# ✅ Test 5: DELETE post สำเร็จ - ต้องได้ Status 200
def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

#✅ Test 6: Response Time ต้องไม่เกิน 3s
