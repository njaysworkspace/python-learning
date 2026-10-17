# สร้าง set ด้วย {} คล้าย dictionary แต่ set เก็บค่าเดี่ยว ไม่ได้เก็บเป็นคู่
# set จะเก็บค่าไม่ซ้ำกัน
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)

numbers.add(5)  # เพิ่ม 5 ลงใน set
print(numbers)
print(3 in numbers)  # ตรวจว่า 3 อยู่ใน set หรือไม่
