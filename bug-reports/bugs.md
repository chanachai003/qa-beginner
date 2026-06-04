# 🐛 Bug Reports

**Repository:** qa-beginner  
**ผู้เขียน:** Chanachai Khamta  

---

## สรุป Bug ทั้งหมด

| Bug ID | ชื่อ Bug | Feature | Severity | Status |
|--------|----------|---------|----------|--------|
| BUG-01 | ไม่มี Validation เมื่อ Phone Number ว่างเปล่า | Login | 🟡 Medium | 🔴 Open |

---

## BUG-01 — ไม่มี Validation เมื่อ Phone Number ว่างเปล่า

| Field | Detail |
|-------|--------|
| **Bug ID** | BUG-01 |
| **Feature** | Login |
| **Severity** | 🟡 Medium |
| **Priority** | 🟡 Medium |
| **Status** | ⚫ Closed |
| **พบวันที่** | 28/05/2026 |
| **ผู้พบ** | Chanachai Khamta |
| **เชื่อมกับ Test Case** | TC-04 |

### 📋 Description
เมื่อผู้ใช้กด Login โดยไม่กรอก Phone Number ระบบไม่แสดง Validation Message
และยังสามารถ Submit Form ต่อไปได้ ทำให้ User Experience ไม่ดีและอาจเกิด Error ที่ฝั่ง Backend

### 🔁 Steps to Reproduce
1. เปิดหน้า Login
2. ปล่อยช่อง Phone Number ว่างเปล่า
3. กดปุ่ม Login

### ✅ Expected Result
ระบบแสดง Validation Message เช่น "กรุณากรอกหมายเลขโทรศัพท์"
และไม่อนุญาตให้ Submit Form จนกว่าจะกรอกข้อมูล
หรือ
ไม่สามารถกด Login และ ไม่อนุญาตให้ Submit Form จนกว่าจะกรอกข้อมูล

### ❌ Actual Result
ระบบไม่แสดง Validation ใดๆ และยังสามารถกด Submit ต่อไปได้

### 🌍 Environment
| Item | Detail |
|------|--------|
| Browser | Chrome 124 |
| OS | Android 16 |
| Device | Samsung Galaxy A53 |

### 📎 Evidence
> _(แนบ Screenshot หรือ Video ที่นี่ — ลาก & วางไฟล์ภาพลงใน GitHub Editor ได้เลย)_

---

## Template สำหรับ Bug ถัดไป

> Copy Section นี้ทุกครั้งที่พบ Bug ใหม่

### BUG-XX — (ชื่อ Bug)

| Field | Detail |
|-------|--------|
| **Bug ID** | BUG-XX |
| **Feature** | |
| **Severity** | 🔴 Critical / 🟠 High / 🟡 Medium / 🟢 Low |
| **Priority** | 🔴 High / 🟡 Medium / 🟢 Low |
| **Status** | 🔴 Open / 🟡 In Progress / ✅ Fixed |
| **พบวันที่** | |
| **ผู้พบ** | |
| **เชื่อมกับ Test Case** | |

### 📋 Description


### 🔁 Steps to Reproduce
1. 
2. 
3. 

### ✅ Expected Result


### ❌ Actual Result


### 🌍 Environment
| Item | Detail |
|------|--------|
| Browser | |
| OS | |
| Device | |

### 📎 Evidence
> _(Screenshot / Video)_
