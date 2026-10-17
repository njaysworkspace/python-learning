name = input("กรอกชื่อ")
age = int(input("กรอกอายุ"))  # input() ได้ข้อความ จึงแปลงเป็นจำนวนเต็มด้วย int()
height = float(input("กรอกส่วนสูง"))  # แปลงข้อความเป็นเลขทศนิยมด้วย float()
numbers = int("80")  # แปลงข้อความ "80" ให้เป็นจำนวนเต็ม

add20 = numbers + 20

print(f"ชื่อ: {name}")
print(f"อายุ: {age}")
print(f"ส่วนสูง: {height}")
print(f"total numbers: {add20}")
