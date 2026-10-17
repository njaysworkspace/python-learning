# โปรแกรมแจกไพ่ให้ผู้เล่น 6 คน

# นำเข้า random เพื่อใช้สับไพ่
import random

# INPUT: เตรียมข้อมูลที่ใช้สร้างไพ่

# สัญลักษณ์แทนดอกไพ่ 4 ดอก
suits = ["s", "h", "d", "c"]

# หน้าไพ่ 13 แบบ และค่าตัวเลขของแต่ละหน้า
ranks = {
    "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9,
    "T": 10, "J": 11, "Q": 12,
    "K": 13, "A": 14
}

# PROCESS 1: สร้างสำรับไพ่ โดยจับคู่หน้าไพ่กับดอกไพ่
deck = []

for suit in suits:
    for rank in ranks.keys():
        deck.append(rank + suit)

# PROCESS 2: สับไพ่ในสำรับ
random.shuffle(deck)

# PROCESS 3: กำหนดตำแหน่งผู้เล่นทั้ง 6 คน
positions = ["SB", "BB", "UTG", "HJ", "CO", "BTN", ]

# สร้าง dictionary เพื่อเก็บไพ่ของผู้เล่นแต่ละตำแหน่ง
players = {}

# แจกไพ่ให้ผู้เล่นแต่ละคน 2 ใบ
for position in positions:
    players[position] = [deck.pop(), deck.pop()]

# PROCESS 4: หยิบไพ่กองกลาง 5 ใบ
community_cards = []

for i in range(5):
    community_cards.append(deck.pop())

# OUTPUT: แสดงไพ่ของผู้เล่นแต่ละคน
for position in positions:
    print(f"{position}: {players[position]}")

# แสดงไพ่กองกลาง
print(f"Community Cards: {community_cards}")

# แสดงจำนวนไพ่ที่เหลือในสำรับ
print("Cards remaining:", len(deck))
