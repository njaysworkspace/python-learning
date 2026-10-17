# Tuple ใช้วงเล็บ ()
colour = ("Red", "Blue", "Green")
student = ("NJ", 25)
### Tuples ไม่สามารถเพิ่มหรือเปลี่ยนค่าหลังจากสร้างได้
""" EX
colors = ("red", "blue", "green")

colors[0] = "yellow"  # จะเกิด TypeError """

print(f"Colour: {colour}")
print(f"Student name: {student[0]}")
print(f"Age: {student[1]}")
