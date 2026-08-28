import math

# ==========================================
# HOẠT ĐỘNG 3: KIỂU SỐ & HÀM TOÁN HỌC
# ==========================================

# 3.1 Minh họa các hàm toán học cơ bản
print("--- HÀM TOÁN HỌC CƠ BẢN ---")
so_am = -15.7
goc_luy_thua = 2
so_mũ = 5

print(f"Giá trị tuyệt đối của {so_am}: {abs(so_am)}")
print(f"Làm tròn {so_am} (1 chữ số thập phân): {round(so_am, 1)}")
print(f"{goc_luy_thua} lũy thừa {so_mũ} (pow): {pow(goc_luy_thua, so_mũ)}")

thuong, du = divmod(17, 5)
print(f"17 chia 5 -> Thương: {thuong}, Dư: {du}")

# 3.2 Giải phương trình bậc 2: ax^2 + bx + c = 0
print("\n--- GIẢI PHƯƠNG TRÌNH BẬC 2 ---")
a = float(input("Nhập a (a khác 0): "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    print("Đây không phải là phương trình bậc 2")
else:
    delta = b**2 - 4*a*c
    print(f"Delta = {delta}")
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có 2 nghiệm phân biệt: x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {x:.2f}")
    else:
        print("Phương trình vô nghiệm thực")


# ==========================================
# HOẠT ĐỘNG 4: XỬ LÝ CHUỖI STRING
# ==========================================

print("\n--- XỬ LÝ CHUỖI STRING ---")
chuoi_goc = "  Lập Trình Python Cơ Bản 2026  "

# Strip, Upper, Lower
chuoi_sach = chuoi_goc.strip()
print(f"Chuỗi gốc: {chuoi_goc}")
print(f"Sau khi strip(): {chuoi_sach}")
print(f"In hoa toàn bộ: {chuoi_sach.upper()}")

# Indexing và Slicing (Đảo ngược chuỗi)
chuoi_dao_nguoc = chuoi_sach[::-1]
print(f"Chuỗi đảo ngược: {chuoi_dao_nguoc}")

# Split và Join
danh_sach_tu = chuoi_sach.split()
print(f"Tách thành danh sách từ: {danh_sach_tu}")
chuoi_noicau = "-".join(danh_sach_tu)
print(f"Nối lại bằng dấu '-': {chuoi_noicau}")