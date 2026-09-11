# ==========================================
# Hoạt động 1: Dictionary cơ bản - khai báo, truy xuất, thêm/sửa/xóa
# ==========================================

# Bài tập 1.1 - Khai báo & truy xuất:
sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5
}

print(sinh_vien["ho_ten"])                  # truy xuất theo khóa
print(sinh_vien.get("diem_tb"))            # truy xuất an toàn bằng get()
print(sinh_vien.get("lop", "Chua co"))     # get() với giá trị mặc định nếu không có khóa

""""
 CÂU HỎI: sinh_vien["lop"] (khi "lop" chưa tồn tại) sẽ gây lỗi KeyError, còn sinh_vien.get("lop", "chua co") thì không 
TRẢ LỜI: 
- sinh_vien["lop"] bị lỗi vì dấu ngoặc vuông [] yêu cầu khóa "lop" phải tồn tại sẵn. Nếu chưa có, 
Python sẽ báo lỗi dừng chương trình.
- sinh_vien.get("lop", "Chua co") không bị lỗi vì phương thức .get() tra cứu an toàn: 
Nếu khóa "lop" chưa tồn tại, nó không báo lỗi mà trả về giá trị mặc định là "Chua co".
"""

# Bài tập 1.2 - Thêm/sửa/xóa:
sinh_vien["lop"] = "CNTT01"                 # thêm khóa mới
sinh_vien["diem_tb"] = 9.0                  # sửa giá trị khóa đã có
print(sinh_vien)

diem_cu = sinh_vien.pop("diem_tb")          # xóa theo khóa, trả về giá trị vừa xóa
print(sinh_vien, "- diem da xoa:", diem_cu)

sinh_vien.update({"nam_sinh": 2003, "email": "a@example.com"}) # cập nhật/thêm nhiều khóa cùng lúc
print(sinh_vien)


# ==========================================
# Hoạt động 2: Duyệt Dictionary bằng for - keys/values/items
# ==========================================

diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}

for mon in diem_mon_hoc.keys():
    print(mon)

for diem in diem_mon_hoc.values():
    print(diem)

for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")

tong_diem = 0
for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem

print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))


# ==========================================
# Hoạt động 3: Dictionary comprehension & giới thiệu Set
# ==========================================

# Bài tập 3.1 - Dictionary comprehension:
diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}

diem_cong_diem = {mon: round(diem + 0.5, 2) for mon, diem in diem_mon_hoc.items()}
print("Điểm cộng:", diem_cong_diem)

ten_mon_viet_hoa = {mon.upper(): diem for mon, diem in diem_mon_hoc.items()}
print("Tên môn viết hoa:", ten_mon_viet_hoa)

# Bài tập 3.2 - So sánh nhanh với Set:
mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}

print(mon_hoc_ky1 & mon_hoc_ky2)  # giao: môn học chung 2 học kỳ
print(mon_hoc_ky1 | mon_hoc_ky2)  # hợp: tất cả môn học cả 2 học kỳ
print(mon_hoc_ky1 - mon_hoc_ky2)  # môn chỉ có ở học kỳ 1

"""
Trả lời câu hỏi:
- Set KHÔNG lưu cặp khóa-giá trị (key-value), nó chỉ lưu các phần tử đơn lẻ.
- Set KHÔNG cho phép phần tử trùng lặp vì được thiết kế theo khái niệm tập hợp toán học, 
  giúp đảm bảo tính duy nhất và hỗ trợ các phép toán tập hợp (giao, hợp, hiệu) siêu nhanh.
"""