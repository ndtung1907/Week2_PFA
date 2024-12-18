"""
2. Người dùng nhập từ bàn phím chuỗi các số nhị phân viết liên
tiếp được nối nhau bởi dấu phẩy. Hãy nhập chuỗi đầu vào sau đó in ra những giá trị được nhập.
"""
def check(string):
    if string and all(char in "01" for char in string):
        return True
    return False

_input = list(map(str, input("Nhập các số nhị phân viết liên tiếp, nối với nhau bằng dấu phẩy: ").split(", ")))
result = []
for x in _input:
    if check(x):
        result.append(x)
print(",".join(result) if result else "Đầu vào không hợp lệ")