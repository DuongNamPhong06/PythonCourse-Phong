import keyword

# ==========================================
# HOẠT ĐỘNG 4: TỪ KHÓA (KEYWORD)
# ==========================================
print("--- HOẠT ĐỘNG 4: TỪ KHÓA ---")
print("Danh sach tu khoa Python:", keyword.kwlist)
print("So luong tu khoa:", len(keyword.kwlist))

# ==========================================
# HOẠT ĐỘNG 3: CHUẨN ĐẶT TÊN PEP8
# ==========================================
# Bài tập 3.2: Đặt lại tên biến đúng chuẩn PEP8 (snake_case cho biến, UPPER_CASE cho hằng số)
ten_sinh_vien = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000  # Hằng số

print("\n--- HOẠT ĐỘNG 3: PEP8 ---")
print(f"Sinh vien: {ten_sinh_vien} | Diem Toan: {diem_toan} | Diem Van: {diem_van}")
print(f"So mon hoc: {so_luong_mon_hoc} | Muc luong toi thieu: {MUC_LUONG_TOI_THIEU}")

# ==========================================
# HOẠT ĐỘNG 5: TOÁN TỬ
# ==========================================
print("\n--- HOẠT ĐỘNG 5: TOAN TU ---")
a, b = 17, 5
print(f"a+b={a+b}, a-b={a-b}, a*b={a*b}, a/b={a/b}, a//b={a//b}, a%b={a%b}, a**b={a**b}")

diem = 6.5
print("Diem dat loai Kha (6.5 <= diem < 8.0)?", 6.5 <= diem < 8.0)

x = 10
x += 5
x -= 2
x *= 3
x /= 2
print("Gia tri x sau cac phep gan:", x)

danh_sach = [1, 2, 3, "python"]
print("3 co trong danh sach?", 3 in danh_sach)

# ==========================================
# HOẠT ĐỘNG 6: DYNAMIC TYPING & MINI BÀI TOÁN
# ==========================================
print("\n--- HOẠT ĐỘNG 6: DYNAMIC TYPING & TONG HOP ---")
bien = 10
print("Bien kieu int:", bien, type(bien))
bien = "Xin chao"
print("Bien kieu str:", bien, type(bien))

# Bài tập 6.2: Tổng hợp điểm
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3
la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(f"\n{ho_ten} - DTB: {round(dtb, 2)}")
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))