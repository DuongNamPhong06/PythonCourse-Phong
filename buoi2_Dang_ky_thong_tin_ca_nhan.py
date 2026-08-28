# ==========================================
# HOẠT ĐỘNG 5: MINI PROJECT - ĐĂNG KÝ THÔNG TIN CÁ NHÂN
# ==========================================

print("=== HỆ THỐNG ĐĂNG KÝ THÔNG TIN SINH VIÊN ===")

# 1. Nhập thông tin từ người dùng
ho_ten_raw = input("Nhập họ và tên: ")
sdt_raw = input("Nhập số điện thoại: ")
email_raw = input("Nhập địa chỉ email: ")
nam_sinh_raw = input("Nhập năm sinh: ")

# 2. Xử lý và chuẩn hóa dữ liệu
# - Chuẩn hóa Họ tên (xóa khoảng trắng thừa, viết hoa chữ cái đầu mỗi từ)
ho_ten = ho_ten_raw.strip().title()

# - Xóa khoảng trắng thừa ở SĐT và Email
sdt = sdt_raw.strip()
email = email_raw.strip().lower()

# - Tính tuổi
nam_hien_tai = 2026
tuoi = nam_hien_tai - int(nam_sinh_raw.strip())

# 3. Kiểm tra tính hợp lệ cơ bản
hop_le_sdt = len(sdt) == 10 and sdt.isdigit()
hop_le_email = "@" in email and "." in email

# 4. Xuất kết quả đăng ký
print("\n" + "="*40)
print("     KẾT QUẢ XÁC NHẬN ĐĂNG KÝ")
print("="*40)
print(f"Họ và tên     : {ho_ten}")
print(f"Tuổi          : {tuoi} (Năm sinh: {nam_sinh_raw.strip()})")
print(f"Số điện thoại : {sdt} {'(Hợp lệ)' if hop_le_sdt else '(KHÔNG HỢP LỆ - Cần 10 chữ số)'}")
print(f"Email         : {email} {'(Hợp lệ)' if hop_le_email else '(KHÔNG HỢP LỆ - Thiếu @ hoặc dấu chấm)'}")
print("="*40)