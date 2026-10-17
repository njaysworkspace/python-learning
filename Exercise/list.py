# สร้าง list ด้วยวงเล็บเหลี่ยม []
rainbow = ["Red", "Orange", "Yellow", 1]  # คั่นสมาชิกแต่ละตัวด้วยเครื่องหมาย ,
# Index คือตำแหน่งของสมาชิก โดยเริ่มนับจาก 0: Red อยู่ตำแหน่ง 0
# Orange อยู่ตำแหน่ง 1 และ Yellow อยู่ตำแหน่ง 2

rb = ["Indigo", "Violet"]
numbers = [5, 7, 10, 3, 9, 18, 21, 21]
numbers.reverse()  # กลับลำดับสมาชิกใน list
print(numbers)
print(numbers.count(21))  # นับจำนวนครั้งที่ 21 ปรากฏ

rainbow.remove(1)  # ลบสมาชิกตัวแรกที่มีค่าเป็น 1
rainbow.append("Green")  # เพิ่ม Green ต่อท้าย list
rainbow.insert(-1, "Blue")  # แทรก Blue ที่ตำแหน่ง -1
colours = rainbow.extend(rb)  # เพิ่มสมาชิกทุกตัวจาก rb ต่อท้าย rainbow
rainbow.sort()  # เรียงข้อมูลจากน้อยไปมาก; ใช้ sort(reverse=True) เพื่อเรียงย้อนกลับ

print(rainbow)
print(rainbow.index("Red"))  # แสดงตำแหน่งของ Red
