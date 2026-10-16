# Hoạt động 4: Chuyển đổi kiểu dữ liệu tường minh & ngầm định
# Bài tập 4.1 - Ép kiểu tường minh:

chuoi_so = "25"
so = int(chuoi_so)
print(so, type(so))

so_thuc = float("3.14")
print(so_thuc, type(so_thuc))

danh_sach = list((1, 2, 3))                 # tuple -> list
bo_ba = tuple([4, 5, 6])                    # list -> tuple
tap_hop = set([1, 2, 2, 3, 3, 3])           # list -> set (tự loại bỏ phần tử trùng lặp)
tu_dien = dict([("a", 1), ("b", 2)])        # list các tuple -> dict

print("List:", danh_sach)
print("Tuple:", bo_ba)
print("Set:", tap_hop)
print("Dict:", tu_dien)


# Bài tập 4.2 - Trường hợp gây lỗi khi ép kiểu:
# int("abc")        -> Gây lỗi ValueError vì chuỗi chứa chữ cái không chuyển thành số được.
# int("3.14")       -> Gây lỗi ValueError vì int() không thể ép trực tiếp chuỗi số thực.

# Cách làm đúng khi chuyển chuỗi số thực về số nguyên:
so_hop_le = int(float("3.14"))             # Ép sang float trước rồi ép về int
print("Kết quả ép chuỗi '3.14' về int đúng cách:", so_hop_le)


# Bài tập 4.3 - Chuyển đổi ngầm định:
ket_qua = 5 + 2.5                          # int + float -> Python tự động chuyển kết quả thành float
print("Chuyển đổi ngầm định (int + float):", ket_qua, type(ket_qua))

ket_qua_2 = "Diem: " + str(8.5)            # Bắt buộc phải ép str() tường minh, Python KHÔNG tự động nối str với số
print(ket_qua_2)