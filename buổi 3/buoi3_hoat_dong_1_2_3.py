# Hoạt động 1: List cơ bản - khai báo, indexing, slicing, phương thức

# Bài tập 1.1 - Khai báo & truy cập:
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]

print(diem_so[0])       # phan tu dau tien
print(diem_so[-1])      # phan tu cuoi cung
print(diem_so[1:4])     # cat tu vi tri 1 den truoc 4
print(diem_so[::2])     # lay cach 1 phan tu (step = 2)
print(diem_so[::-1])    # dao nguoc danh sach


# Bài tập 1.2 - Các phương thức thường dùng:
ten_sv = ["An", "Binh", "Chi"]

ten_sv.append("Dung")          # them vao cuoi
ten_sv.insert(1, "Em")         # chen vao vi tri 1
print(ten_sv)

ten_sv.remove("Chi")           # xoa theo gia tri
pop_ra = ten_sv.pop()          # xoa va lay ra phan tu cuoi
print(ten_sv, "- da xoa:", pop_ra)

ten_sv.sort()                  # sap xep tang dan (theo bang chu cai)
print(ten_sv)
ten_sv.reverse()               # dao nguoc thu tu hien tai
print(ten_sv)

ten_sv.extend(["Giang", "Hoa"]) # noi them mot list khac vao
print(ten_sv)

print(" giải thích sự khác nhau giữa remove() và pop(): ")
print("- remove(x): Xóa phần tử đầu tiên có giá trị bằng x khỏi list.Không trả về giá trị vừa xóa.")
print("- pop(i): Xóa phần tử tại vị trí chỉ số i (mặc định là vị trí cuối cùng) và trả về giá trị phần tử đó." )

# Hoạt động 2: Duyệt List bằng for & List lồng nhau (ma trận)

# Bài tập 2.1 - Duyệt list bằng for:
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
tong = 0

for diem in diem_so:
    print(diem)
    tong = tong + diem

print("Tong diem:", tong)
print("Diem trung binh:", round(tong / len(diem_so), 2))


# Bài tập 2.2 - List lồng nhau (ma trận):
ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# In ra theo tung hang
for hang in ma_tran:
    print(hang)

# In ra tung phan tu, duyet theo hang roi theo cot
for hang in ma_tran:
    for phan_tu in hang:
        print(phan_tu, end=" ")
    print()

# Yêu cầu bổ sung: tính tổng tất cả phần tử trong ma_tran bằng biến tong cộng dồn qua 2 vòng for lồng nhau
tong_ma_tran = 0
for hang in ma_tran:
    for phan_tu in hang:
        tong_ma_tran = tong_ma_tran + phan_tu
print("Tong tat ca phan tu trong ma tran:", tong_ma_tran)

# Hoạt động 3: List comprehension

# Bài tập 3.1 - Lọc số chẵn/lẻ:
day_so = list(range(1, 21))   # day so tu 1 den 20

so_chan = [x for x in day_so if x % 2 == 0]
so_le = [x for x in day_so if x % 2 != 0]

print("So chan:", so_chan)
print("So le:", so_le)


# Bài tập 3.2 - Biến đổi phần tử:
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_cong = [round(diem + 0.5, 2) for diem in diem_so]
print(diem_cong)