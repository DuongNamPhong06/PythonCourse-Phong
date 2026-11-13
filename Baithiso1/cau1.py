# a) Hàm thêm sản phẩm
def them_san_pham(danh_sach, ma, ten, gia, soluong):
    san_pham = {
        "MaSP": ma,
        "TenSP": ten,
        "Gia": float(gia),
        "SoLuong": int(soluong),
    }
    danh_sach.append(san_pham)


# b) Hàm tìm kiếm theo tên (không phân biệt hoa/thường)
def tim_kiem_theo_ten(danh_sach, tu_khoa):
    ket_qua = []
    tu_khoa_lower = tu_khoa.strip().lower()
    for sp in danh_sach:
        if tu_khoa_lower in sp["TenSP"].lower():
            ket_qua.append(sp)
    return ket_qua

# c) Hàm tính tổng giá trị tồn kho
def tong_gia_tri_ton_kho(danh_sach):
    tong = 0
    for sp in danh_sach:
        tong += sp["Gia"] * sp["SoLuong"]
    return tong

# d) Chương trình chính hiển thị menu
def main():
    danh_sach_sp = [
        {
            "MaSP": "SP001",
            "TenSP": "Bút bi Thiên Long",
            "Gia": 3000.0,
            "SoLuong": 150,
        },
        {
            "MaSP": "SP002",
            "TenSP": "Vở học sinh 96 trang",
            "Gia": 8000.0,
            "SoLuong": 8,
        },
        {"MaSP": "SP003", "TenSP": "Bút chì 2B", "Gia": 2500.0, "SoLuong": 200},
    ]

    while True:
        print("\n===== QUẢN LÝ SẢN PHẨM =====")
        print("1. Thêm sản phẩm")
        print("2. Tìm kiếm theo tên")
        print("3. Xem tổng giá trị tồn kho")
        print("4. Thoát chương trình")

        lua_chon = input("Nhập lựa chọn của bạn (1-4): ").strip()

        if lua_chon == "1":
            ma = input("Nhập Mã SP: ").strip()
            ten = input("Nhập Tên SP: ").strip()
            try:
                gia = float(input("Nhập Giá: "))
                soluong = int(input("Nhập Số lượng: "))
                them_san_pham(danh_sach_sp, ma, ten, gia, soluong)
                print("-> Thêm sản phẩm thành công!")
            except ValueError:
                print("-> Lỗi: Giá và Số lượng phải là số hợp lệ!")

        elif lua_chon == "2":
            tu_khoa = input("Nhập từ khóa tên sản phẩm cần tìm: ")
            ds_tim_thay = tim_kiem_theo_ten(danh_sach_sp, tu_khoa)
            if not ds_tim_thay:
                print("-> Không tìm thấy sản phẩm nào phù hợp.")
            else:
                print("-> Kết quả tìm kiếm:")
                for sp in ds_tim_thay:
                    print(
                        f"   {sp['MaSP']} - {sp['TenSP']} - {sp['Gia']:,.0f}vnđ -"
                        f" SL: {sp['SoLuong']} "
                    )

        elif lua_chon == "3":
            tong_tien = tong_gia_tri_ton_kho(danh_sach_sp)
            print(f"-> Tổng giá trị tồn kho hiện tại: {tong_tien:,.0f}vnđ")

        elif lua_chon == "4":
            print("Đã thoát chương trình. Tạm biệt!")
            break
        else:
            print("-> Lựa chọn không hợp lệ, vui lòng chọn lại (1-4).")


if __name__ == "__main__":
    main()