try:
    tuoi = int(input("Nhap tuoi: "))
    print("Tuoi cua ban la: ", tuoi)
except ValueError:
    print("Ban da nhap sai dinh dang, vui long nhap mot so nguyen !")

# Bài tập: Kết hợp While với try_except
while True: 
    try:
        so_luong = int(input("Nhập số lượng (số nguyên dương): "))
        if so_luong > 0:
            break
        print("Số lượng phải lớn hơn 0, vui lòng nhập lại !")
    except ValueError:
        print("Dữ liệu không hợp lệ, vui lòng nhập lại một số nguyên !")

print("Số lượng hợp lệ đã nhập:", so_luong)