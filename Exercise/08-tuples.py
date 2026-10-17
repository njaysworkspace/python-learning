# สร้าง tuple ด้วยวงเล็บ ()
colour = ("Red", "Blue", "Green")
student = ("NJ", 25)
# หลังสร้าง tuple แล้ว จะเพิ่ม ลบ หรือเปลี่ยนสมาชิกไม่ได้
""" ตัวอย่าง: การเปลี่ยนสมาชิกจะทำให้เกิด TypeError
colors = ("red", "blue", "green")

colors[0] = "yellow"
"""

print(f"Colour: {colour}")
print(f"Student name: {student[0]}")
print(f"Age: {student[1]}")
