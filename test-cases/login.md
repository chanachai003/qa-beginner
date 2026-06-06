# 🔐 Test Cases — Login Feature

**App ที่ทดสอบ:** https://the-internet.herokuapp.com/login  
**ผู้เขียน: Chanachai Khamta**  
**วันที่: 28/05/2026**

---

## สรุป
| ทั้งหมด | Pass | Fail | Blocked |
|---------|------|------|---------|
| 6 | 5 | 1 | 0 |

---

## Test Cases

| TC ID | Test Case | Precondition | Steps | Expected Result | Actual Result | Status |
|-------|-----------|--------------|-------|-----------------|---------------|--------|
| TC-01 | Login สำเร็จด้วยข้อมูลถูกต้อง | มีบัญชีอยู่แล้ว | 1. ไปที่หน้า Login 2. กรอก Phone Number: `092xxxxxxx` 3. กรอก OTP: `820386` 4. กด Login | Redirect ไปหน้า Account พร้อมข้อความต้อนรับ | เป็นไปตามที่คาด | ✅ Pass |
| TC-02 | Login ด้วย Password ผิด | มีบัญชีอยู่แล้ว | 1. กรอก Phone Number ถูกต้อง 2. กรอก OTP ผิด 3. กด Login | แสดง OTP ไม่ถูกต้อง สีแดง | เป็นไปตามที่คาด | ✅ Pass |
| TC-03 | Login ด้วย Phone Number ผิด | - | 1. กรอก Phone Number ที่ไม่มีในระบบ 2. กด Login | ไม่สามารถกด Login ได้ แสดง error "เบอร์โทรศัพท์ไม่ถูกต้อง กรุณาลองใหม่" | เป็นไปตามที่คาด | ✅ Pass |
| TC-04 | Login ด้วย Phone Number ว่างเปล่า | - | 1. ปล่อย Phone Number ว่าง 2. กด Login | แสดง validation ไม่ให้ Submit | ไม่มี validation แสดง | ✅ Pass |
| TC-05 | Login ด้วย OTP ว่างเปล่า | - | 1. กรอก Phone Number 2. ปล่อย OTP ว่าง 3. กด Login | ไม่สามารถกด Login ได้ | เป็นไปตามที่คาด | ✅ Pass |
| TC-06 | Logout หลัง Login สำเร็จ | Login เข้ามาแล้ว | 1. กด Logout | Redirect กลับหน้าหลัก | เป็นไปตามที่คาด | ✅ Pass |
