# ==========================================
# Hoạt động 6: Đệ quy – Giai thừa, Fibonacci
# ==========================================

# Bài tập 6.1 - Giai thừa bằng đệ quy và vòng lặp:
def giai_thua_de_quy(n):
    if n <= 1:
        return 1
    return n * giai_thua_de_quy(n - 1)

def giai_thua_lap(n):
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua

print("Giai thừa 5 (đệ quy vs lặp):", giai_thua_de_quy(5), "-", giai_thua_lap(5))


# Bài tập 6.2 - Số Fibonacci thứ n bằng đệ quy:
def fibonacci_de_quy(n):
    if n <= 1:
        return n
    return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)

print("10 số Fibonacci đầu tiên:")
for i in range(10):
    print(fibonacci_de_quy(i), end=" ")
print()

# Thử nghiệm tính fibonacci_de_quy(30)
print("Fibonacci thứ 30:", fibonacci_de_quy(30))