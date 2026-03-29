# โปรแกรมคำนวณผิวทางแยกแต่ละชั้น

# รับค่า
width = float(input("ความกว้างถนน (เมตร): "))
length = float(input("ความยาวถนน (เมตร): "))

# ความหนาแต่ละชั้น (cm)
subbase_thk = float(input("ความหนา Subbase (cm): "))
base_thk = float(input("ความหนา Base (cm): "))
asphalt_thk = float(input("ความหนา Asphalt (cm): "))
concrete_thk = float(input("ความหนา Concrete (cm): "))

# แปลงเป็นเมตร
def cm_to_m(cm):
    return cm / 100

# พื้นที่
area = width * length

# คำนวณแต่ละชั้น
subbase_vol = area * cm_to_m(subbase_thk)
base_vol = area * cm_to_m(base_thk)
asphalt_vol = area * cm_to_m(asphalt_thk)
concrete_vol = area * cm_to_m(concrete_thk)

# แปลง Asphalt เป็นตัน
asphalt_ton = asphalt_vol * 2.3

# แสดงผล
print("\n--- ผลลัพธ์ ---")
print(f"พื้นที่รวม = {area:.2f} ตร.ม.\n")

print("Subbase:")
print(f"  ปริมาตร = {subbase_vol:.2f} ลบ.ม.")

print("Base:")
print(f"  ปริมาตร = {base_vol:.2f} ลบ.ม.")

print("Asphalt:")
print(f"  ปริมาตร = {asphalt_vol:.2f} ลบ.ม.")
print(f"  น้ำหนัก = {asphalt_ton:.2f} ตัน")

print("Concrete:")
print(f"  ปริมาตร = {concrete_vol:.2f} ลบ.ม.")
