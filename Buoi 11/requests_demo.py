# Hoạt động 5: Requests - gọi API công khai, xử lý JSON
# Bài tập 5.1 - Gọi API công khai và đọc dữ liệu JSON:

import requests
response = requests.get("https://api.github.com/repos/python/cpython")

if response.status_code == 200:
    du_lieu = response.json()
    print("Ten repository:", du_lieu["full_name"])
    print("So luot gan sao (stars):", du_lieu["stargazers_count"])
    print("Ngon ngu chinh:", du_lieu["language"])
else:
    print("Goi API that bai, ma loi:", response.status_code)

# Đoạn code trên đã được gọi thử thực tế và nhận đúng phản hồi: python/cpython, số lượt gắn sao hiện
# có hơn 74.000, ngôn ngữ chính là Python - xác nhận cơ chế gọi API và đọc JSON hoạt động đúng.
# Bài tập 5.2 - Vận dụng với API tỷ giá ngoại tệ (chạy trên máy có kết nối Internet đầy đủ):

import requests

response = requests.get("https://open.er-api.com/v6/latest/USD")

if response.status_code == 200:
    du_lieu = response.json()
    ty_gia_vnd = du_lieu["rates"]["VND"]
    print(f"1 USD = {ty_gia_vnd:,.0f} VND")
else:
    print("Khong lay duoc ty gia, ma loi:", response.status_code)

# Ghi chú: bài tập 5.1 đã kiểm thử thành công ngay trong môi trường chuẩn bị tài liệu. Bài tập 5.2 dùng
# một API tỷ giá công khai khác - sinh viên chạy trên máy cá nhân có kết nối Internet bình thường để lấy
# dữ liệu thời gian thực; cấu trúc xử lý JSON hoàn toàn tương tự Bài tập 5.1 đã được xác minh.