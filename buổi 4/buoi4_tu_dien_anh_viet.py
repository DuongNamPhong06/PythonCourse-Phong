# Hoạt động 5: Vận dụng - Từ điển Anh - Việt

tu_dien_anh_viet = {
    "hello": "xin chao",
    "book": "quyen sach",
    "table": "cai ban"
}

# Tra từ
print("Tra từ 'hello':", tu_dien_anh_viet.get("hello", "Khong tim thay tu nay"))
print("Tra từ 'computer':", tu_dien_anh_viet.get("computer", "Khong tim thay tu nay"))

# Thêm từ mới
tu_dien_anh_viet["computer"] = "may tinh"

# Xóa một từ
tu_dien_anh_viet.pop("table")

# In từ điển hiện tại
print("\nTừ điển hiện tại:")
for tu_anh, tu_viet in tu_dien_anh_viet.items():
    print(f"{tu_anh} - {tu_viet}")