import sys
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMessageBox, QWidget


class CuaSoDangNhap(QWidget):

    def __init__(self):
        super().__init__()

        # 1. Nạp giao diện từ file form_dang_nhap.ui vào biến self.ui
        loader = QUiLoader()
        ui_file = QFile("Buoi 10/form_dang_nhap.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.setWindowTitle("Đăng nhập")

        # 2. BẮT BUỘC thêm self.ui trước tên widget (self.ui.nut_dang_nhap)
        self.ui.nut_dang_nhap.clicked.connect(self.xu_ly_dang_nhap)

    def xu_ly_dang_nhap(self):
        # Lấy văn bản từ các ô nhập thông qua self.ui
        tai_khoan = self.ui.o_nhap_tai_khoan.text().strip()
        mat_khau = self.ui.o_nhap_mat_khau.text().strip()

        if tai_khoan == "" or mat_khau == "":
            QMessageBox.critical(
                self, "Lỗi", "Vui lòng nhập đầy đủ tài khoản và mật khẩu."
            )
            return

        QMessageBox.information(
            self,
            "Thành công",
            f"Xin chào {tai_khoan}, đăng nhập thành công!",
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = CuaSoDangNhap()
    cua_so.show()
    sys.exit(app.exec())