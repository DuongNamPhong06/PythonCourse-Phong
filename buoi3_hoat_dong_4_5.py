import math

# Hoạt động 4: Tuple cơ bản

# Khai báo và truy cập Tuple
thong_tin = ("Nguyen Van A", 20, "Ha Noi")
print("Ten:", thong_tin[0])
print("Tuoi:", thong_tin[1])
print("Thanh pho:", thong_tin[2])

# Tuple Unpacking
ho_ten, tuoi, thanh_pho = thong_tin
print(f"Unpacking: {ho_ten}, {tuoi} tuoi, {thanh_pho}")

# Hoán đổi giá trị 2 biến
x = 10
y = 20
x, y = y, x
print(f"Sau khi swap: x = {x}, y = {y}")

# Hoạt động 5: Tọa độ điểm & Khoảng cách

A = (1, 2)
B = (4, 6)

x1, y1 = A
x2, y2 = B

# Tính khoảng cách Euclidean
khoang_cach = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Khoang cach giua A va B: {khoang_cach:.2f}")

# Trung điểm
M = ((x1 + x2) / 2, (y1 + y2) / 2)
print(f"Trung diem M: {M}")
# --- YÊU CẦU BỔ SUNG HOẠT ĐỘNG 5 ---
cac_diem = [(0, 0), (3, 4), (6, 8)]

print("\nKhoang cach tu cac diem den goc toa do (0, 0):")
for x, y in cac_diem:
    khoang_cach_goc = math.sqrt(x**2 + y**2)
    print(f"Diem ({x}, {y}) -> Khoang cach: {khoang_cach_goc:.2f}")