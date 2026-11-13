# File: cau2.py
import sys
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class QuanLySanPhamApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản lý sản phẩm")
        self.resize(500, 450)

        # Danh sách lưu trữ dữ liệu sản phẩm trong chương trình
        self.danh_sach_sp = []

        self.thiet_lap_giao_dien()

    def thiet_lap_giao_dien(self):
        layout_chinh = QVBoxLayout(self)

        # --- a) Form nhập liệu (GridLayout căn chỉnh nhãn và ô nhập) ---
        grid_form = QGridLayout()

        self.o_nhap_ma = QLineEdit()
        self.o_nhap_ma.setPlaceholderText("Ví dụ: SP001")

        self.o_nhap_ten = QLineEdit()
        self.o_nhap_ten.setPlaceholderText("Ví dụ: Bút bi Thiên Long")

        self.o_nhap_gia = QLineEdit()
        self.o_nhap_gia.setPlaceholderText("Ví dụ: 3000")

        self.o_nhap_soluong = QLineEdit()
        self.o_nhap_soluong.setPlaceholderText("Ví dụ: 150")

        grid_form.addWidget(QLabel("Mã SP:"), 0, 0)
        grid_form.addWidget(self.o_nhap_ma, 0, 1)

        grid_form.addWidget(QLabel("Tên SP:"), 1, 0)
        grid_form.addWidget(self.o_nhap_ten, 1, 1)

        grid_form.addWidget(QLabel("Giá (vnđ):"), 2, 0)
        grid_form.addWidget(self.o_nhap_gia, 2, 1)

        grid_form.addWidget(QLabel("Số lượng:"), 3, 0)
        grid_form.addWidget(self.o_nhap_soluong, 3, 1)

        layout_chinh.addLayout(grid_form)

        # --- b) Nút Thêm sản phẩm ---
        self.nut_them = QPushButton("Thêm sản phẩm")
        self.nut_them.clicked.connect(self.xu_ly_them_san_pham)
        layout_chinh.addWidget(self.nut_them)

        # --- c) Khu vực tìm kiếm ---
        layout_tim_kiem = QHBoxLayout()
        self.o_tim_kiem = QLineEdit()
        self.o_tim_kiem.setPlaceholderText("Nhập tên sản phẩm cần tìm...")

        self.nut_tim_kiem = QPushButton("Tìm kiếm")
        self.nut_tim_kiem.clicked.connect(self.xu_ly_tim_kiem)

        layout_tim_kiem.addWidget(QLabel("Tìm kiếm:"))
        layout_tim_kiem.addWidget(self.o_tim_kiem)
        layout_tim_kiem.addWidget(self.nut_tim_kiem)
        layout_chinh.addLayout(layout_tim_kiem)

        # --- Vùng hiển thị danh sách sản phẩm ---
        layout_chinh.addWidget(QLabel("Danh sách sản phẩm:"))
        self.list_hien_thi = QListWidget()
        layout_chinh.addWidget(self.list_hien_thi)

    def cap_nhat_danh_sach_hien_thi(self, ds_can_hien_thi):
        # Xóa kết quả cũ trước khi hiển thị kết quả mới
        self.list_hien_thi.clear()
        for sp in ds_can_hien_thi:
            dong_text = (
                f"{sp['ma']} - {sp['ten']} - {sp['gia']:,.0f}vnđ - SL:"
                f" {sp['soluong']}"
            )
            self.list_hien_thi.addItem(dong_text)

    def xu_ly_them_san_pham(self):
        ma = self.o_nhap_ma.text().strip()
        ten = self.o_nhap_ten.text().strip()
        gia_str = self.o_nhap_gia.text().strip()
        soluong_str = self.o_nhap_soluong.text().strip()

        # --- d) Kiểm tra dữ liệu nhập ---
        if not ma or not ten:
            QMessageBox.critical(
                self, "Lỗi nhập liệu", "Mã SP và Tên SP không được để trống!"
            )
            return

        try:
            gia = float(gia_str)
            soluong = int(soluong_str)
            if gia < 0 or soluong < 0:
                raise ValueError
        except ValueError:
            QMessageBox.critical(
                self,
                "Lỗi nhập liệu",
                "Giá và Số lượng phải là số hợp lệ (không âm)!",
            )
            return

        # Lưu vào danh sách và cập nhật lên giao diện
        san_pham_moi = {"ma": ma, "ten": ten, "gia": gia, "soluong": soluong}
        self.danh_sach_sp.append(san_pham_moi)
        self.cap_nhat_danh_sach_hien_thi(self.danh_sach_sp)

        # Xóa trắng ô nhập sau khi thêm thành công
        self.o_nhap_ma.clear()
        self.o_nhap_ten.clear()
        self.o_nhap_gia.clear()
        self.o_nhap_soluong.clear()

    def xu_ly_tim_kiem(self):
        tu_khoa = self.o_tim_kiem.text().strip().lower()
        if not tu_khoa:
            # Nếu ô tìm kiếm trống thì hiển thị lại toàn bộ danh sách
            self.cap_nhat_danh_sach_hien_thi(self.danh_sach_sp)
            return

        ket_qua_loc = [
            sp for sp in self.danh_sach_sp if tu_khoa in sp["ten"].lower()
        ]
        self.cap_nhat_danh_sach_hien_thi(ket_qua_loc)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = QuanLySanPhamApp()
    cua_so.show()
    sys.exit(app.exec())