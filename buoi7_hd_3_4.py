# Bước 4.1 – Khai báo dữ liệu ban đầu:
danh_sach_phong = [
    {"ma_phong": "P101", "loai_phong": "Don", "gia": "trang_thai": "trong", "ten_khach": ""},
    {"ma_phong": "P102", "loai_phong": "Don", "gia": "trang_thai": "trong", "ten_khach": ""},
    {"ma_phong": "P103", "loai_phong": "Don", "gia": "trang_thai": "trong", "ten_khach": ""},
    {"ma_phong": "P104", "loai_phong": "Don", "gia": "trang_thai": "trong", "ten_khach": ""},
    {"ma_phong": "P105", "loai_phong": "Don", "gia": "trang_thai": "trong", "ten_khach": ""},
]
lich_su_doanh_thu = []

# Bước 4.2 – Hàm hiển thị & tìm kiếm:
def hien_thi_danh_sach_phong():
    print("/n" + "=" *60)
    print(f"{'Ma phong':<10}{phong['Loai phong']}")