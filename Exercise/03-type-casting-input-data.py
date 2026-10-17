name = input("กรอกชื่อ")
age = int(input("กรอกอายุ")) # input รับข้อมูลเป็น str แปลงเป็น int
height = float(input("กรอกส่วนสูง")) # input รับข้อมูลเป็น str แปลงเป็น float
numbers = int("80") # input รับข้อมูลเป็น str แปลงเป็น int

add20 = numbers + 20

print(f"ชื่อ: {name}")
print(f"อายุ: {age}")
print(f"ส่วนสูง: {height}")
print(f"total numbers: {add20}")
