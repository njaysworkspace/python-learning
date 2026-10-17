numbers = "50" # str
numbers = int(numbers) # แปลงข้อมูลของตัวแปร numbers จาก str -> int
total_numbers = numbers + 20

# ใช้ input เพื่อรับข้อมูลแล้วเป็นเป็น int
# การรับข้อมูลด้วย input จะรับข้อมูลเป็น str เสมอ
age = int(input("กรอกอายุ"))

print(f"Total Numbers {total_numbers}") # ใช้ f-string แทรกค่าตัวแปร
print(type(total_numbers))
print(f"Age: {age}") # ใช้ f-string แทรกค่าตัวแปร
print(type(age))
