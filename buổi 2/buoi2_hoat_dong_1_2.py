# ==========================================
# HOẠT ĐỘNG 1: NHẬP/XUẤT DỮ LIỆU & FORMATTING
# ==========================================

# 1.1 Sử dụng input(), print() với sep và end
ho_ten = input("Nhap ho va ten cua bạn: ")
tuoi = int(input("Nhap tuoi cua ban: "))
chuyen_nganh = input("Nhap chuyen nganh hoc: ")

print("\n--- THÔNG TIN SINH VIÊN ---")
print("Họ tên", ho_ten, sep=": ")
print("Tuổi", tuoi, sep=": ")
print("Chuyên ngành", chuyen_nganh, sep=": ")

print("Chào mừng", ho_ten, end=" - ")
print("Chúc bạn một ngày học tập tốt lành!")

# 1.2 So sánh 3 cách định dạng chuỗi
giam_gia = 0.155  # 15.5%
gia_goc = 1500000

print("\n--- KẾT QUẢ ĐỊNH DẠNG CHUỖI ---")
# Cách 1: f-string (Khuyên dùng)
print(f"[f-string] Sản phẩm giá {gia_goc:,} VNĐ, giảm {giam_gia:.1%}")

# Cách 2: str.format()
print("[str.format()] Sản phẩm giá {:,} VNĐ, giảm {:.1%}".format(gia_goc, giam_gia))

# Cách 3: Toán tử %
print("[Toán tử %%] Sản phẩm giá %d VNĐ, giảm %.1f%%" % (gia_goc, giam_gia * 100))


# ==========================================
# HOẠT ĐỘNG 2: CHÚ THÍCH & TRÍCH DẪN (QUOTES)
# ==========================================

# 2.1 Escape Characters & Raw String
print("\n--- ESCAPE CHARACTERS & RAW STRING ---")
path_normal = "C:\\new_folder\\test\\readme.txt"
path_raw = r"C:\new_folder\test\readme.txt"

print("Đường dẫn thường (dùng \\\\):", path_normal)
print("Đường dẫn Raw string (r\"...\"): ", path_raw)

# 2.2 Docstring & Triple Quotes
def gioi_thieu_khoa_hoc():
    """
    Hàm này dùng để hiển thị thông tin khóa học Python.
    Mục đích: Minhh họa Docstring nhiều dòng trong Python.
    """
    mo_ta = '''Khóa học: Python Cơ Bản
Thời lượng: 10 buổi
Mục tiêu: Nắm vững nền tảng lập trình Python.'''
    print("\n" + mo_ta)

gioi_thieu_khoa_hoc()
# In docstring của hàm
print("\nDocstring của hàm gioi_thieu_khoa_hoc():")
print(gioi_thieu_khoa_hoc.__doc__)