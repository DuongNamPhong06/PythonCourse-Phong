# Hoạt động 5: Biến điều khiển – StringVar/IntVar/BooleanVar
import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Vi du bien dieu khien")
cua_so.geometry("350x220")

bien_ho_ten = tk.StringVar(value="Nguyen Van A")
bien_tuoi = tk.IntVar(value=18)
bien_dong_y_dieu_khoan = tk.BooleanVar(value=False)

tk.Label(cua_so, text="Ho ten:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
tk.Entry(cua_so, textvariable=bien_ho_ten).grid(row=0, column=1, padx=10, pady=10)
tk.Label(cua_so, text="Tuoi:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
tk.Entry(cua_so, textvariable=bien_tuoi).grid(row=1, column=1, padx=10, pady=10)
tk.Checkbutton(cua_so, text="Dong y dieu khoan", variable=bien_dong_y_dieu_khoan).grid(
row=2, column=0, columnspan=2, pady=10)

def xem_gia_tri_bien():

    print("Ho ten (StringVar):", bien_ho_ten.get())
print("Tuoi (IntVar):", bien_tuoi.get())
print("Dong y dieu khoan (BooleanVar):", bien_dong_y_dieu_khoan.get())

bien_tuoi.set(bien_tuoi.get() + 1) # vi du dung set() de cap nhat gia tri

tk.Button(cua_so, text="Xem gia tri bien (va +1 tuoi)", command=xem_gia_tri_bien).grid(
row=3, column=0, columnspan=2, pady=10)

cua_so.mainloop()

# Hoạt động 6: 

import tkinter as tk
from tkinter import messagebox

# 1. Hàm xử lý khi nhấn nút Submit
def xu_ly_submit():
    ho_ten = entry_ho_ten.get().strip()
    tuoi_nhap = entry_tuoi.get().strip()
    email = entry_email.get().strip()

    # Kiểm tra Họ tên không được để trống
    if ho_ten == "":
        messagebox.showerror("Loi", "Ho ten khong duoc de trong.")
        return

    # Kiểm tra Tuổi phải là số nguyên
    try:
        tuoi = int(tuoi_nhap)
    except ValueError:
        messagebox.showerror("Loi", "Tuoi phai la mot so nguyen.")
        return

    # Kiểm tra Email phải có ký tự @
    if "@" not in email:
        messagebox.showerror("Loi", "Email khong hop le (thieu ky tu @).")
        return

    # Hiển thị thông báo thành công
    messagebox.showinfo("Thanh cong", f"Da nhan thong tin:\n{ho_ten} - {tuoi} tuoi - {email}")

# 2. Khởi tạo cửa sổ chính
cua_so = tk.Tk()
cua_so.title("Form co validate")
cua_so.geometry("380x220")

# 3. Tạo các Label và Entry
tk.Label(cua_so, text="Ho ten:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_ho_ten = tk.Entry(cua_so, width=25)
entry_ho_ten.grid(row=0, column=1, padx=10, pady=10)

tk.Label(cua_so, text="Tuoi:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_tuoi = tk.Entry(cua_so, width=25)
entry_tuoi.grid(row=1, column=1, padx=10, pady=10)

tk.Label(cua_so, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_email = tk.Entry(cua_so, width=25)
entry_email.grid(row=2, column=1, padx=10, pady=10)

# 4. Nút Submit
tk.Button(cua_so, text="Submit", command=xu_ly_submit).grid(row=3, column=0, columnspan=2, pady=15)

# 5. Vòng lặp giao diện
cua_so.mainloop()