import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_chi_tieu as db

DANH_SACH_DANH_MUC = ["Ăn uống", "Đi lại", "Giải trí", "Học tập", "Mua sắm", "Khác"]

class UngDungChiTieu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý Chi tiêu Cá nhân")
        self.geometry("580x500")
        self.resizable(False, False)
        
        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach_chi_tieu()

    def khoi_tao_giao_dien(self):
        # Khung nhập thông tin
        khung_nhap = tk.Frame(self)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Tên khoản chi:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_ten_khoan = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ten_khoan.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Số tiền (VNĐ):").grid(row=1, column=0, sticky="w", pady=5)
        self.o_nhap_so_tien = tk.Entry(khung_nhap, width=30)
        self.o_nhap_so_tien.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Danh mục:").grid(row=2, column=0, sticky="w", pady=5)
        self.chon_danh_muc = ttk.Combobox(khung_nhap, values=DANH_SACH_DANH_MUC, width=27, state="readonly")
        self.chon_danh_muc.current(0)
        self.chon_danh_muc.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(khung_nhap, text="Thêm khoản chi", command=self.xu_ly_them_chi_tieu).grid(
            row=3, column=0, columnspan=2, pady=10
        )

        # Khung danh sách
        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox_chi_tieu = tk.Listbox(khung_danh_sach, width=75, height=14)
        self.listbox_chi_tieu.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox_chi_tieu.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_chi_tieu.config(yscrollcommand=thanh_cuon.set)

        # Khung nút thao tác
        khung_nut_thao_tac = tk.Frame(self)
        khung_nut_thao_tac.pack(pady=10)

        tk.Button(khung_nut_thao_tac, text="Đánh dấu đã thanh toán", command=self.xu_ly_danh_dau_da_thanh_toan).grid(
            row=0, column=0, padx=5
        )
        tk.Button(khung_nut_thao_tac, text="Xóa khoản chi", command=self.xu_ly_xoa_chi_tieu).grid(
            row=0, column=1, padx=5
        )
        tk.Button(khung_nut_thao_tac, text="Thống kê theo danh mục", command=self.xu_ly_thong_ke).grid(
            row=0, column=2, padx=5
        )

    def tai_lai_danh_sach_chi_tieu(self):
        self.listbox_chi_tieu.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_chi_tieu()
        for item in self.danh_sach_hien_tai:
            id_item, ten_khoan, so_tien, danh_muc, da_thanh_toan = item
            trang_thai = "[Đã thanh toán]" if da_thanh_toan == 1 else "[Chưa thanh toán]"
            self.listbox_chi_tieu.insert(
                tk.END, f"{trang_thai} {ten_khoan} - {so_tien:,.0f} VNĐ - ({danh_muc})"
            )

    def xu_ly_them_chi_tieu(self):
        ten_khoan = self.o_nhap_ten_khoan.get().strip()
        so_tien_str = self.o_nhap_so_tien.get().strip()
        danh_muc = self.chon_danh_muc.get()

        if ten_khoan == "" or so_tien_str == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ tên khoản chi và số tiền.")
            return

        try:
            so_tien = float(so_tien_str)
            if so_tien <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Lỗi", "Số tiền phải là số hợp lệ lớn hơn 0.")
            return

        db.them_chi_tieu(ten_khoan, so_tien, danh_muc)
        self.o_nhap_ten_khoan.delete(0, tk.END)
        self.o_nhap_so_tien.delete(0, tk.END)
        self.tai_lai_danh_sach_chi_tieu()
        messagebox.showinfo("Thành công", f"Đã thêm khoản chi: {ten_khoan}")

    def xu_ly_xoa_chi_tieu(self):
        lua_chon = self.listbox_chi_tieu.curselection()
        if not lua_chon:
            messagebox.showerror("Lỗi", "Vui lòng chọn một khoản chi trong danh sách để xóa.")
            return
        id_chi_tieu = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_chi_tieu(id_chi_tieu)
        self.tai_lai_danh_sach_chi_tieu()

    def xu_ly_danh_dau_da_thanh_toan(self):
        lua_chon = self.listbox_chi_tieu.curselection()
        if not lua_chon:
            messagebox.showerror("Lỗi", "Vui lòng chọn một khoản chi để đánh dấu đã thanh toán.")
            return
        id_chi_tieu = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.danh_dau_da_thanh_toan(id_chi_tieu)
        self.tai_lai_danh_sach_chi_tieu()

    def xu_ly_thong_ke(self):
        du_lieu_thong_ke = db.thong_ke_theo_danh_muc()
        if not du_lieu_thong_ke:
            messagebox.showinfo("Thông báo", "Chưa có dữ liệu chi tiêu để thống kê.")
            return

        cac_danh_muc = [dong[0] for dong in du_lieu_thong_ke]
        tong_tien = [dong[1] for dong in du_lieu_thong_ke]

        plt.figure(figsize=(7, 4.5))
        plt.bar(cac_danh_muc, tong_tien, color="cornflowerblue")
        plt.title("TỔNG CHI TIÊU THEO DANH MỤC")
        plt.xlabel("Danh mục")
        plt.ylabel("Tổng tiền (VNĐ)")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    ung_dung = UngDungChiTieu()
    ung_dung.mainloop()