import tkinter as tk
from tkinter import messagebox


def bam_nut(val):
    entry_hien_thi.insert(tk.END, str(val))


def xoa_toan_bo():
    entry_hien_thi.delete(0, tk.END)


def xoa_mot_ky_tu():
    noi_dung = entry_hien_thi.get()
    if noi_dung:
        entry_hien_thi.delete(len(noi_dung) - 1, tk.END)


def tinh_ket_qua():
    try:
        bieu_thuc = entry_hien_thi.get()
        # Thay thế ký tự x và ÷ thành toán tử Python
        bieu_thuc_xu_ly = bieu_thuc.replace("x", "*").replace("÷", "/")
        ket_qua = eval(bieu_thuc_xu_ly)

        # Định dạng kết quả gọn gàng
        if isinstance(ket_qua, float) and ket_qua.is_integer():
            ket_qua = int(ket_qua)

        xoa_toan_bo()
        entry_hien_thi.insert(0, str(ket_qua))
    except ZeroDivisionError:
        messagebox.showerror("Lỗi", "Không thể chia cho số 0!")
        xoa_toan_bo()
    except Exception:
        messagebox.showerror("Lỗi", "Biểu thức không hợp lệ!")


# Khởi tạo cửa sổ ứng dụng
cua_so = tk.Tk()
cua_so.title("Máy Tính Bỏ Túi")
cua_so.geometry("340x450")
cua_so.resizable(False, False)
cua_so.config(bg="#f4f4f9")

# Ô hiển thị biểu thức/kết quả bằng Entry
entry_hien_thi = tk.Entry(
    cua_so,
    font=("Arial", 22),
    justify="right",
    bd=10,
    relief=tk.FLAT,
    bg="#ffffff",
)
entry_hien_thi.grid(
    row=0, column=0, columnspan=4, padx=15, pady=20, ipady=10, sticky="we"
)

# Danh sách các nút và vị trí tương ứng
cac_nut = [
    ("C", 1, 0),
    ("⌫", 1, 1),
    ("%", 1, 2),
    ("÷", 1, 3),
    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2),
    ("x", 2, 3),
    ("4", 3, 0),
    ("5", 3, 1),
    ("6", 3, 2),
    ("-", 3, 3),
    ("1", 4, 0),
    ("2", 4, 1),
    ("3", 4, 2),
    ("+", 4, 3),
    ("0", 5, 0),
    (".", 5, 1),
    ("=", 5, 2),
]

# Tạo các nút bấm
for text, row, col in cac_nut:
    if text == "C":
        cmd = xoa_toan_bo
        bg_color = "#ff5252"
        fg_color = "white"
    elif text == "⌫":
        cmd = xoa_mot_ky_tu
        bg_color = "#ffb74d"
        fg_color = "white"
    elif text == "=":
        cmd = tinh_ket_qua
        bg_color = "#4caf50"
        fg_color = "white"
    elif text in ["÷", "x", "-", "+", "%"]:
        cmd = lambda t=text: bam_nut(t)
        bg_color = "#2196f3"
        fg_color = "white"
    else:
        cmd = lambda t=text: bam_nut(t)
        bg_color = "#e0e0e0"
        fg_color = "black"

    # Xử lý riêng cho nút '=' chiếm 2 cột
    colspan = 2 if text == "=" else 1

    btn = tk.Button(
        cua_so,
        text=text,
        font=("Arial", 14, "bold"),
        bg=bg_color,
        fg=fg_color,
        bd=0,
        command=cmd,
        width=5,
        height=2,
    )
    btn.grid(
        row=row,
        column=col,
        columnspan=colspan,
        padx=5,
        pady=5,
        sticky="nsew",
    )

# Cấu hình tỉ lệ các hàng/cột
for i in range(4):
    cua_so.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    cua_so.grid_rowconfigure(i, weight=1)

if __name__ == "__main__":
    cua_so.mainloop()