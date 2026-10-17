# START

# INPUT: กำหนดขนาด pot และจำนวนชิปที่ต้อง call
pot_input = "150"
hero2call_input = "50"

# PROCESS: คำนวณ pot odds
# Function คือชุดคำสั่งที่เรียกใช้ซ้ำได้; ฟังก์ชันนี้หา equity ขั้นต่ำที่ต้องมี
def calculte_pot_odds(pot, hero2call):
    try:
        # แปลงข้อความที่รับมาให้เป็นเลขทศนิยม
        pot = float(pot)
        hero2call = float(hero2call)
        # คำนวณขนาด pot หลัง call และ equity ขั้นต่ำที่ต้องมี
        final_pot = pot + hero2call
        equity = hero2call / final_pot
        return equity, final_pot

    except (ValueError, NameError):
        # ถ้าข้อมูลแปลงเป็นตัวเลขไม่ได้ ให้คืนค่า None
        return None, None

# เรียกใช้ฟังก์ชัน แล้วเก็บผลลัพธ์ไว้ในตัวแปร
req_equity, final_pot = calculte_pot_odds(pot_input, hero2call_input)

# OUTPUT: แสดงผลลัพธ์
if req_equity is not None:
    print("\n--- ผลลัพธ์ Pot Odds ---")
    print(f"ขนาดพ็อตหลัง Call: {final_pot:.2f} ชิป")
    print(f"คุณต้องมีโอกาสชนะอย่างน้อย: {req_equity:.2%}")
else:
    print("กรุณาใส่ตัวเลข")
