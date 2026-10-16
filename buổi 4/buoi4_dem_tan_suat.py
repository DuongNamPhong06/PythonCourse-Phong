# Hoạt động 6: Vận dụng - Đếm tần suất từ trong văn bản

doan_van = "python la ngon ngu lap trinh python de hoc python de dung"

danh_sach_tu = doan_van.split()
tan_suat = {}

for tu in danh_sach_tu:
    tan_suat[tu] = tan_suat.get(tu, 0) + 1

print("Tần suất xuất hiện các từ:")
for tu, so_lan in tan_suat.items():
    print(f"{tu}: {so_lan}")

"""
Giải thích cách hoạt động của tan_suat.get(tu, 0)+ 1 - vì sao chỉ một dòng này đã thay thế được việc
phải kiểm tra "từ đã xuất hiện hay chưa":
Lệnh tan_suat.get(tu, 0) + 1 lấy số lần xuất hiện hiện tại của 'tu' (nếu từ này chưa từng xuất hiện 
trong dictionary thì mặc định trả về 0), sau đó cộng thêm 1 rồi lưu lại vào tan_suat[tu].
Nhờ vậy, chỉ với một dòng ngắn gọn ta đã xử lý được cả 2 trường hợp: từ vừa xuất hiện lần đầu 
(0 + 1 = 1) và từ đã xuất hiện trước đó (số_cũ + 1) mà không cần phải dùng câu lệnh kiểm tra 
'if tu in tan_suat:'
"""