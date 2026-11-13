# File: cau3.py
import matplotlib.pyplot as plt
import pandas as pd

# a) Đọc dữ liệu sản phẩm từ file sanpham.csv
df = pd.read_csv("Baithiso1/sanpham.csv")

# b) Tính và in ra màn hình các thông số thống kê
tong_so_sp = len(df)
gia_trung_binh = df["Gia"].mean()
# Tìm dòng có giá cao nhất để lấy Tên sản phẩm
sp_gia_cao_nhat = df.loc[df["Gia"].idxmax(), "TenSP"]

print(f"Tổng số sản phẩm: {tong_so_sp}")
print(f"Giá trung bình của các sản phẩm: {gia_trung_binh:,.0f}đ")
print(f"Sản phẩm có giá cao nhất: {sp_gia_cao_nhat}")

# c) Vẽ biểu đồ cột thể hiện SoLuong tồn kho và lưu thành bieudo.png (không dùng plt.show())
plt.figure(figsize=(8, 5))
plt.bar(df["TenSP"], df["SoLuong"], color="skyblue", width=0.5)
plt.title("Số lượng tồn kho của từng sản phẩm")
plt.xlabel("Tên sản phẩm")
plt.ylabel("Số lượng tồn kho")
plt.xticks(rotation=15)  # Xoay nhẹ nhãn trục X để tên không bị đè lên nhau
plt.tight_layout()
plt.savefig("bieudo.png")
plt.close()

# d) Lọc các sản phẩm có SoLuong < 10 và xuất ra file canh_bao_hang.csv
df_sap_het = df[df["SoLuong"] < 10]
df_sap_het.to_csv("canh_bao_hang.csv", index=False)
print(
    "\nĐã lưu biểu đồ 'bieudo.png' và xuất danh sách cảnh báo ra"
    " 'canh_bao_hang.csv'."
)