#START
#INPUT
pot_input = "150"
hero2call_input = "50"

# PROCESS
# Function คำนวณ Equity ขั้นต่ำ
def calculte_pot_odds(pot, hero2call):
    try:
        # แปลง Data ที่รับมาเป็นตัวเลขทศนิยม
        pot = float(pot)
        hero2call = float(hero2call)
        # คำนวณ
        final_pot = pot + hero2call
        equity = hero2call / final_pot
        return equity, final_pot

    except (ValueError, NameError):
        # ถ้าไม่ใช่ตัวเลข ให้คืนค่าเป็น None
        return None, None

# เรียกใช้ Function
req_equity, final_pot = calculte_pot_odds(pot_input, hero2call_input)

# OUTPUT
if req_equity is not None:
    print("\n--- ผลลัพธ์ Pot Odds ---")
    print(f"ขนาดพ็อตหลัง Call: {final_pot:.2f} ชิป")
    print(f"คุณต้องมีโอกาสชนะอย่างน้อย: {req_equity:.2%}")
else:
    print("กรุณาใส่ตัวเลข")
